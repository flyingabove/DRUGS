#!/usr/bin/env python3
"""
Fetch competitive landscape data from ChEMBL and other sources.

Usage:
    python fetch_competitor_data.py "EGFR inhibitors" --output competitors.json
    python fetch_competitor_data.py KRAS --clinical-trials -o full.json
"""

import argparse
import json
import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
from typing import Optional, Dict, Any, List
import requests


class CompetitorDataFetcher:
    """Fetch competitive intelligence data."""

    def __init__(self, query: str):
        self.query = query
        self.results = {
            "query": query,
            "data": {},
            "sources": []
        }

    def fetch_chembl_compounds(self, target: Optional[str] = None) -> Dict[str, Any]:
        """Fetch compound data from ChEMBL."""
        try:
            base_url = "https://www.ebi.ac.uk/chembl/api/data"

            # Try to find target first
            target_id = None
            if target:
                target_url = f"{base_url}/target_list.json?json={json.dumps({'target_synonym': target})}"
                response = requests.get(target_url, timeout=30)
                if response.status_code == 200:
                    targets_data = response.json()
                    if targets_data.get("page_meta", {}).get("total_count", 0) > 0:
                        target_id = targets_data["targets"][0]["target_chembl_id"]

            # Get molecules with activity data
            if target_id:
                activity_url = f"{base_url}/activity.json?json={json.dumps({'target_chembl_id': target_id, 'pchembl_value__isnull': False})}&limit=100"
            else:
                # Search by molecule name
                molecule_url = f"{base_url}/molecule/search.json?q={self.query}&limit=50"
                activity_url = None

            compounds = []
            approved_drugs = []
            pipeline = {"phase_i": [], "phase_ii": [], "phase_iii": [], "approved": []}

            if target_id and activity_url:
                response = requests.get(activity_url, timeout=30)
                response.raise_for_status()
                activities = response.json()

                # Get unique molecules
                seen = set()
                for act in activities.get("activities", []):
                    mol_id = act.get("molecule_chembl_id")
                    if mol_id and mol_id not in seen:
                        seen.add(mol_id)
                        compounds.append({
                            "chembl_id": mol_id,
                            "name": act.get("pref_name", mol_id),
                            "pchembl_value": act.get("pchembl_value"),
                            "standard_type": act.get("standard_type"),
                            "target_chembl_id": target_id
                        })

                # Get drug info for these molecules
                for mol in compounds[:20]:
                    mol_data = self._get_molecule_details(base_url, mol["chembl_id"])
                    if mol_data:
                        mol.update(mol_data)
                        phase = mol_data.get("max_phase", 0)
                        if phase >= 4:
                            pipeline["approved"].append(mol)
                        elif phase == 3:
                            pipeline["phase_iii"].append(mol)
                        elif phase == 2:
                            pipeline["phase_ii"].append(mol)
                        elif phase == 1:
                            pipeline["phase_i"].append(mol)

            result = {
                "total_compounds": len(compounds),
                "compounds": compounds[:20],  # Top 20
                "pipeline": pipeline
            }

            self.results["data"]["chembl"] = result
            self.results["sources"].append("chembl")
            print(f"✓ Fetched ChEMBL data ({len(compounds)} compounds)")
            return result

        except Exception as e:
            print(f"✗ ChEMBL error: {e}")
            return {}

    def _get_molecule_details(self, base_url: str, mol_id: str) -> Dict[str, Any]:
        """Get detailed molecule information."""
        try:
            url = f"{base_url}/molecule/{mol_id}.json"
            response = requests.get(url, timeout=15)
            if response.status_code == 200:
                data = response.json()
                return {
                    "max_phase": data.get("max_phase", 0),
                    "first_approval": data.get("first_approval"),
                    "therapeutic_flag": data.get("therapeutic_flag"),
                    "synonyms": data.get("molecule_synonyms", [])[:5]
                }
        except:
            pass
        return {}

    def fetch_clinical_trials(self, limit: int = 50) -> Dict[str, Any]:
        """Fetch clinical trial data from ClinicalTrials.gov."""
        try:
            base_url = "https://clinicaltrials.gov/api/query"

            # Build query fields
            query_fields = {
                "expr": self.query,
                "min_rnk": 1,
                "max_rnk": limit,
                "fmt": "json"
            }

            response = requests.get(base_url, params=query_fields, timeout=30)
            response.raise_for_status()
            data = response.json()

            studies = []
            if data.get("protocolSection"):
                for study in data["protocolSection"].values():
                    try:
                        identity = study.get("identificationModule", {})
                        status = study.get("statusModule", {})
                        design = study.get("designModule", {})
                        arms = design.get("armsInterventionsModule", {}).get("arms", [])

                        studies.append({
                            "nct_id": identity.get("nctId"),
                            "title": identity.get("briefTitle"),
                            "status": status.get("overallStatus"),
                            "phase": self._extract_phase(design),
                            "start_date": status.get("startDateStruct", {}).get("date"),
                            "interventions": [arm.get("name") for arm in arms[:3]] if arms else []
                        })
                    except:
                        continue

            # Group by phase
            phase_distribution = {"phase_1": 0, "phase_2": 0, "phase_3": 0, "other": 0}
            for s in studies:
                phase = s.get("phase", "other").lower().replace(" ", "_")
                if phase in phase_distribution:
                    phase_distribution[phase] += 1
                else:
                    phase_distribution["other"] += 1

            result = {
                "total_studies": len(studies),
                "studies": studies[:20],
                "phase_distribution": phase_distribution
            }

            self.results["data"]["clinical_trials"] = result
            self.results["sources"].append("clinicaltrials")
            print(f"✓ Fetched ClinicalTrials.gov data ({len(studies)} studies)")
            return result

        except Exception as e:
            print(f"✗ ClinicalTrials.gov error: {e}")
            return {}

    def _extract_phase(self, design: Dict) -> str:
        """Extract phase from design module."""
        phase = design.get("phaseModule", {}).get("phase", "N/A")
        if isinstance(phase, dict):
            return phase.get("value", "N/A")
        return str(phase)

    def fetch_company_portfolio(self, company: str) -> Dict[str, Any]:
        """Fetch company portfolio information (public data only)."""
        try:
            # Use ChEMBL to find drugs associated with a company
            base_url = "https://www.ebi.ac.uk/chembl/api/data"

            # Search for drugs by company name in synonyms
            # Note: This is limited as ChEMBL doesn't have comprehensive company data
            result = {
                "company": company,
                "note": "Limited public data available",
                "data_sources": ["ChEMBL (limited)"]
            }

            self.results["data"]["company_portfolio"] = result
            self.results["sources"].append("company_portfolio")
            print(f"✓ Company portfolio data (limited)")
            return result

        except Exception as e:
            print(f"✗ Company portfolio error: {e}")
            return {}

    def fetch_all(self, include_clinical: bool = True, target: Optional[str] = None) -> Dict[str, Any]:
        """Fetch data from all enabled sources."""
        print(f"\nFetching competitive data for: {self.query}\n")

        self.fetch_chembl_compounds(target=target)

        if include_clinical:
            self.fetch_clinical_trials()

        self.results["sources_queried"] = self.results["sources"]
        return self.results

    def save(self, output: str):
        """Save results to file."""
        with open(output, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\n✓ Results saved to {output}")


def main():
    parser = argparse.ArgumentParser(description="Fetch competitive landscape data")
    parser.add_argument("query", help="Search query (e.g., 'EGFR inhibitors', 'KRAS G12C')")
    parser.add_argument("-o", "--output", default="competitor_data.json", help="Output file path")
    parser.add_argument("--target", help="Target gene symbol for ChEMBL lookup")
    parser.add_argument("--clinical-trials", action="store_true", help="Include clinical trials data")
    parser.add_argument("--company", help="Company name for portfolio analysis")
    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format")

    args = parser.parse_args()

    fetcher = CompetitorDataFetcher(args.query)

    if args.company:
        fetcher.fetch_company_portfolio(args.company)
    else:
        fetcher.fetch_all(
            include_clinical=args.clinical_trials,
            target=args.target
        )

    if args.format == "summary":
        print_summary(fetcher.results)
    else:
        fetcher.save(args.output)


def print_summary(data: Dict[str, Any]):
    """Print a summary of fetched data."""
    print("\n" + "="*60)
    print(f"COMPETITIVE LANDSCAPE: {data['query'].upper()}")
    print("="*60 + "\n")

    # ChEMBL data
    if "chembl" in data.get("data", {}):
        ch = data["data"]["chembl"]
        print(f"ChEMBL Data:")
        print(f"  Total Compounds: {ch.get('total_compounds', 0)}")

        pipeline = ch.get("pipeline", {})
        print(f"\n  Pipeline Distribution:")
        print(f"    Approved: {len(pipeline.get('approved', []))}")
        print(f"    Phase III: {len(pipeline.get('phase_iii', []))}")
        print(f"    Phase II: {len(pipeline.get('phase_ii', []))}")
        print(f"    Phase I: {len(pipeline.get('phase_i', []))}")

        if pipeline.get("approved"):
            print(f"\n  Approved Drugs:")
            for drug in pipeline["approved"][:10]:
                print(f"    {drug.get('name', 'N/A')} ({drug.get('chembl_id', 'N/A')})")

    # Clinical trials
    if "clinical_trials" in data.get("data", {}):
        ct = data["data"]["clinical_trials"]
        print(f"\nClinical Trials:")
        print(f"  Total Studies: {ct.get('total_studies', 0)}")

        phases = ct.get("phase_distribution", {})
        print(f"\n  Phase Distribution:")
        for phase, count in phases.items():
            if count > 0:
                print(f"    {phase.replace('_', ' ').title()}: {count}")

        if ct.get("studies"):
            print(f"\n  Recent Studies:")
            for study in ct["studies"][:5]:
                print(f"    {study.get('nct_id', 'N/A')}: {study.get('title', 'N/A')[:60]}...")

    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
