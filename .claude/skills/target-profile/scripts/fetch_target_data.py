#!/usr/bin/env python3
"""
Fetch target data from Open Targets, UniProt, and other sources.

Usage:
    python fetch_target_data.py EGFR --output data.json
    python fetch_target_data.py KRAS --uniprot --chembl --pathways -o full.json
"""

import argparse
import json
import sys
from typing import Optional, Dict, Any
import requests


class TargetDataFetcher:
    """Fetch comprehensive target data from multiple sources."""

    def __init__(self, target: str):
        self.target = target.upper()
        self.results = {
            "target": target,
            "data": {},
            "sources": []
        }

    def fetch_opentargets(self) -> Dict[str, Any]:
        """Fetch target data from Open Targets Platform."""
        # Try multiple API endpoints
        base_urls = [
            "https://api.opentargets.io/v2/platform/public",
            "https://platform.opentargets.org/v1/platform/public"
        ]

        for base_url in base_urls:
            try:
                # Search for target
                search_url = f"{base_url}/search"
                params = {"q": self.target, "size": 1}
                headers = {"Accept": "application/json"}
                response = requests.get(search_url, params=params, headers=headers, timeout=30)
                response.raise_for_status()
                search_data = response.json()

                if not search_data.get("data"):
                    continue  # Try next URL

                target_id = search_data["data"][0]["id"]
                target_info = search_data["data"][0]

                # Get detailed target info
                info_url = f"{base_url}/targets/{target_id}"
                info_response = requests.get(info_url, timeout=30)
                info_response.raise_for_status()
                target_data = info_response.json()["data"]

                result = {
                    "id": target_id,
                    "name": target_info.get("name"),
                    "symbol": target_info.get("symbol"),
                    "biotype": target_info.get("biotype"),
                    "tractability": target_data.get("tractability", {}),
                    "associations": self._fetch_disease_associations(base_url, target_id)
                }

                self.results["data"]["opentargets"] = result
                self.results["sources"].append("opentargets")
                print(f"✓ Fetched Open Targets data for {self.target}")
                return result

            except Exception as e:
                continue  # Try next URL

        print(f"✗ Open Targets error: Could not fetch data for {self.target}")
        return {}

    def _fetch_disease_associations(self, base_url: str, target_id: str, limit: int = 20) -> list:
        """Fetch disease associations from Open Targets."""
        try:
            url = f"{base_url}/associations"
            params = {
                "target": target_id,
                "size": limit,
                "sort": "-association_score.overall"
            }
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            associations = []
            for assoc in data.get("data", []):
                disease = assoc.get("disease", {})
                associations.append({
                    "disease_id": disease.get("id"),
                    "disease_name": disease.get("name"),
                    "association_score": assoc.get("association_score", {}).get("overall", 0),
                    "evidence_count": assoc.get("evidence_count", 0)
                })

            return associations

        except Exception as e:
            print(f"  Warning: Could not fetch disease associations: {e}")
            return []

    def fetch_uniprot(self) -> Dict[str, Any]:
        """Fetch protein data from UniProt."""
        try:
            base_url = "https://rest.uniprot.org"

            # Use simpler query format
            search_url = f"{base_url}/uniprotkb/search"
            params = {
                "query": f"gene:{self.target} AND organism_id:9606",
                "format": "json",
                "size": 1
            }
            response = requests.get(search_url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            if not data.get("results"):
                print(f"Warning: No UniProt entry found for {self.target}")
                return {}

            protein = data["results"][0]
            uni_id = protein.get("primaryAccession")

            # Extract protein name safely
            protein_desc = protein.get("proteinDescription", {})
            recommended_name = protein_desc.get("recommendedName", {})
            protein_name = recommended_name.get("fullName", {}).get("value", "N/A") if recommended_name else "N/A"

            # Extract gene name
            genes = protein.get("genes", [])
            gene_name = genes[0].get("geneName", {}).get("value", self.target) if genes else self.target

            # Extract length and mass
            seq_info = protein.get("sequence", {})
            length = seq_info.get("length", "N/A")
            mass = seq_info.get("molWeight", {}).get("value", "N/A") if seq_info.get("molWeight") else "N/A"

            # Extract subcellular location
            location = "Unknown"
            for comment in protein.get("comments", []):
                if comment.get("commentType") == "SUBCELLULAR_LOCATION":
                    sub_locs = comment.get("subcellularLocations", [])
                    if sub_locs:
                        location = sub_locs[0].get("location", {}).get("value", "Unknown")
                        break

            # Get KEGG pathway info
            pathways = self._fetch_kegg_pathways(uni_id)

            result = {
                "accession": uni_id,
                "name": protein_name,
                "gene_name": gene_name,
                "function": "N/A",
                "length": length,
                "mass": mass,
                "subcellular_location": location,
                "pathways": pathways
            }

            self.results["data"]["uniprot"] = result
            self.results["sources"].append("uniprot")
            print(f"✓ Fetched UniProt data for {self.target}")
            return result

        except Exception as e:
            print(f"✗ UniProt error: {e}")
            return {}

    def _extract_location(self, protein: Dict) -> str:
        """Extract subcellular location from UniProt data."""
        try:
            for comment in protein.get("comments", []):
                if comment.get("commentType") == "SUBCELLULAR_LOCATION":
                    locations = comment.get("subcellularLocations", [])
                    if locations:
                        return locations[0].get("location", {}).get("value", "Unknown")
            return "Unknown"
        except:
            return "Unknown"

    def _fetch_kegg_pathways(self, uniprot_id: str) -> list:
        """Fetch KEGG pathways for a protein."""
        try:
            url = f"https://rest.kegg.jp/link/pathway/{uniprot_id}"
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                pathways = []
                for line in response.text.strip().split("\n"):
                    if line:
                        parts = line.split("\t")
                        if len(parts) == 2:
                            pathway_id = parts[1].replace("path:", "")
                            pathways.append({
                                "id": pathway_id,
                                "name": self._get_pathway_name(pathway_id)
                            })
                return pathways[:5]  # Limit to top 5
            return []
        except:
            return []

    def _get_pathway_name(self, pathway_id: str) -> str:
        """Get pathway name from KEGG."""
        try:
            url = f"https://rest.kegg.jp/get/{pathway_id}"
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                for line in response.text.split("\n"):
                    if line.startswith("NAME"):
                        return line.replace("NAME", "").strip().split()[0]
            return pathway_id
        except:
            return pathway_id

    def fetch_chembl(self) -> Dict[str, Any]:
        """Fetch compound/bioactivity data from ChEMBL."""
        try:
            # Use the new ChEMBL v2 API
            base_url = "https://www.ebi.ac.uk/chembl/api/data"

            # Search for target by gene name
            target_url = f"{base_url}/target.json?search={self.target}"
            response = requests.get(target_url, timeout=30)
            response.raise_for_status()

            targets_data = response.json()
            if not targets_data.get("page_meta", {}).get("total_count", 0):
                print(f"Warning: No ChEMBL target found for {self.target}")
                return {}

            target_chembl_id = targets_data["targets"][0]["target_chembl_id"]

            # Get bioactivities
            bio_url = f"{base_url}/activity.json?target_chembl_id={target_chembl_id}&pchembl_value__isnull=False&limit=100"
            response = requests.get(bio_url, timeout=30)
            response.raise_for_status()
            activities = response.json()

            # Get approved drugs
            drugs = self._get_approved_drugs(base_url, target_chembl_id)

            result = {
                "chembl_id": target_chembl_id,
                "bioactivity_count": activities.get("page_meta", {}).get("total_count", 0),
                "top_compounds": [
                    {
                        "molecule_chembl_id": a.get("molecule_chembl_id"),
                        "pref_name": a.get("pref_name"),
                        "pchembl_value": a.get("pchembl_value"),
                        "standard_type": a.get("standard_type")
                    }
                    for a in activities.get("activities", [])[:10]
                    if a.get("molecule_chembl_id") and a.get("pchembl_value")
                ],
                "approved_drugs": drugs
            }

            self.results["data"]["chembl"] = result
            self.results["sources"].append("chembl")
            print(f"✓ Fetched ChEMBL data for {self.target}")
            return result

        except Exception as e:
            print(f"✗ ChEMBL error: {e}")
            import traceback
            traceback.print_exc()
            return {}

    def _get_approved_drugs(self, base_url: str, target_id: str) -> list:
        """Get approved drugs for a target."""
        try:
            # Use query parameter format instead of JSON encoding
            url = f"{base_url}/drug.json?target_chembl_id={target_id}&max_phase_for_indication__gte=4"
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            data = response.json()

            drugs = []
            for drug in data.get("drugs", [])[:10]:
                drugs.append({
                    "name": drug.get("synonyms", [drug.get("name")])[0] if drug.get("synonyms") else drug.get("name"),
                    "chembl_id": drug.get("molecule_chembl_id"),
                    "max_phase": drug.get("max_phase_for_indication"),
                    "first_approval": drug.get("first_approval")
                })
            return drugs

        except:
            return []

    def fetch_all(self, include_uniprot: bool = True, include_chembl: bool = True, include_pathways: bool = True) -> Dict[str, Any]:
        """Fetch data from all enabled sources."""
        print(f"\nFetching data for target: {self.target}\n")

        self.fetch_opentargets()

        if include_uniprot:
            self.fetch_uniprot()

        if include_chembl:
            self.fetch_chembl()

        self.results["sources_queried"] = self.results["sources"]
        return self.results

    def save(self, output: str):
        """Save results to file."""
        with open(output, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\n✓ Results saved to {output}")


def main():
    parser = argparse.ArgumentParser(description="Fetch drug target data")
    parser.add_argument("target", help="Target gene symbol or name (e.g., EGFR, KRAS)")
    parser.add_argument("-o", "--output", default="target_data.json", help="Output file path")
    parser.add_argument("--no-uniprot", action="store_true", help="Skip UniProt fetch")
    parser.add_argument("--no-chembl", action="store_true", help="Skip ChEMBL fetch")
    parser.add_argument("--diseases-only", action="store_true", help="Only fetch disease associations")
    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format")

    args = parser.parse_args()

    fetcher = TargetDataFetcher(args.target)

    if args.diseases_only:
        # Only fetch disease associations
        data = fetcher.fetch_opentargets()
        if args.format == "summary":
            print_summary(data)
    else:
        data = fetcher.fetch_all(
            include_uniprot=not args.no_uniprot,
            include_chembl=not args.no_chembl
        )

        if args.format == "summary":
            print_summary(data)
        else:
            fetcher.save(args.output)


def print_summary(data: Dict[str, Any]):
    """Print a summary of fetched data."""
    print("\n" + "="*60)
    print(f"TARGET PROFILE: {data['target'].upper()}")
    print("="*60 + "\n")

    # Open Targets
    if "opentargets" in data.get("data", {}):
        ot = data["data"]["opentargets"]
        print(f"Open Targets:")
        print(f"  Name: {ot.get('name', 'N/A')}")
        print(f"  Symbol: {ot.get('symbol', 'N/A')}")
        print(f"  ID: {ot.get('id', 'N/A')}")

        # Tractability
        tract = ot.get("tractability", {})
        if tract:
            print(f"\n  Tractability:")
            for t in tract.get("tractability", []):
                modality = t.get("modality", "Unknown")
                score = t.get("summary", "N/A")
                print(f"    {modality}: {score}")

        # Top disease associations
        if ot.get("associations"):
            print(f"\n  Top Disease Associations:")
            for assoc in ot["associations"][:5]:
                print(f"    {assoc['disease_name']}: {assoc['association_score']:.2f}")

    # UniProt
    if "uniprot" in data.get("data", {}):
        up = data["data"]["uniprot"]
        print(f"\nUniProt:")
        print(f"  Accession: {up.get('accession', 'N/A')}")
        print(f"  Name: {up.get('name', 'N/A')}")
        print(f"  Length: {up.get('length', 'N/A')} aa")
        print(f"  Location: {up.get('subcellular_location', 'N/A')}")
        if up.get("pathways"):
            print(f"  Pathways:")
            for p in up["pathways"][:3]:
                print(f"    {p['name']} ({p['id']})")

    # ChEMBL
    if "chembl" in data.get("data", {}):
        ch = data["data"]["chembl"]
        print(f"\nChEMBL:")
        print(f"  Bioactivities: {ch.get('bioactivity_count', 0)}")
        if ch.get("approved_drugs"):
            print(f"  Approved Drugs:")
            for drug in ch["approved_drugs"][:5]:
                print(f"    {drug.get('name', 'N/A')} (approval: {drug.get('first_approval', 'N/A')})")

    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
