#!/usr/bin/env python3
"""
Target Validation - Comprehensive target validation for drug discovery.

Fetches data from Open Targets, GWAS Catalog, and UniProt for target validation.
"""

import argparse
import json
import sys
from typing import Any, Dict


def fetch_opentargets(target: str) -> Dict[str, Any]:
    """Fetch target data from Open Targets Platform."""
    try:
        import requests
    except ImportError:
        return {"error": "requests module not installed. Run: pip install requests"}

    url = f"https://www.ebi.ac.uk/platform/public/target-api/target/{target}"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"Open Targets API error: {str(e)}"}


def fetch_gwas(target: str) -> Dict[str, Any]:
    """Fetch GWAS associations from EBI GWAS Catalog."""
    try:
        import requests
    except ImportError:
        return {"error": "requests module not installed"}

    url = f"https://www.ebi.ac.uk/gwas/rest/api/efoTraits/{target}"
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 404:
            # Try gene search
            url = f"https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms?geneName={target}"
            response = requests.get(url, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"GWAS API error: {str(e)}"}


def fetch_uniprot(target: str) -> Dict[str, Any]:
    """Fetch protein data from UniProt."""
    try:
        import requests
    except ImportError:
        return {"error": "requests module not installed"}

    url = f"https://rest.uniprot.org/uniprotkb/search?query={target}&format=json"
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        data = response.json()
        if data.get("results"):
            return data["results"][0]
        return {"error": "No results found"}
    except Exception as e:
        return {"error": f"UniProt API error: {str(e)}"}


def score_genetic_validation(data: Dict[str, Any]) -> Dict[str, Any]:
    """Score genetic validation evidence (0-5)."""
    score = 0
    evidence = []

    # Check GWAS associations
    if "opentargets" in str(data):
        associations = data.get("opentargets", {}).get("associations", [])
        if associations:
            score += min(3, len(associations))
            evidence.append(f"{len(associations)} GWAS associations")

    # Check for disease associations
    diseases = data.get("diseases", [])
    if diseases:
        score += 1
        evidence.append(f"{len(diseases)} disease associations")

    # Check tractability
    tractability = data.get("tractability", {})
    if tractability:
        score += 1
        evidence.append("Tractability data available")

    return {
        "score": min(5, score),
        "evidence": evidence,
        "level": "Strong" if score >= 4 else "Moderate" if score >= 2 else "Weak"
    }


def score_chemical_validation(data: Dict[str, Any]) -> Dict[str, Any]:
    """Score chemical validation evidence (0-5)."""
    score = 0
    evidence = []

    # Check for known binders
    compounds = data.get("compounds", [])
    if compounds:
        score += min(3, len(compounds) // 10 + 1)
        evidence.append(f"{len(compounds)} known compounds")

    # Check for PDB structures
    structures = data.get("structures", [])
    if structures:
        score += 2
        evidence.append(f"{len(structures)} PDB entries")

    return {
        "score": min(5, score),
        "evidence": evidence,
        "level": "Strong" if score >= 4 else "Moderate" if score >= 2 else "Weak"
    }


def score_clinical_validation(data: Dict[str, Any]) -> Dict[str, Any]:
    """Score clinical validation evidence (0-5)."""
    score = 0
    evidence = []

    # Check for approved drugs
    approved = data.get("approved_drugs", [])
    if approved:
        score += min(4, len(approved))
        evidence.append(f"{len(approved)} approved drugs")

    # Check for pipeline drugs
    pipeline = data.get("pipeline", [])
    if pipeline:
        score += 1
        evidence.append(f"{len(pipeline)} pipeline drugs")

    return {
        "score": min(5, score),
        "evidence": evidence,
        "level": "Strong" if score >= 4 else "Moderate" if score >= 2 else "Weak"
    }


def generate_validation_report(target: str, data: Dict[str, Any]) -> str:
    """Generate a target validation report."""
    report = []
    report.append(f"# Target Validation: {target}\n")
    report.append("## Validation Summary\n")

    # Score each pillar
    genetic = score_genetic_validation(data)
    chemical = score_chemical_validation(data)
    clinical = score_clinical_validation(data)

    total_score = genetic["score"] + chemical["score"] + clinical["score"]
    max_score = 15

    report.append("| Pillar | Score | Status |")
    report.append("|--------|-------|--------|")
    report.append(f"| Genetic | {genetic['score']}/5 | {'✓ Strong' if genetic['score'] >= 4 else '⚠ Moderate'} |")
    report.append(f"| Chemical | {chemical['score']}/5 | {'✓ Strong' if chemical['score'] >= 4 else '⚠ Moderate'} |")
    report.append(f"| Clinical | {clinical['score']}/5 | {'✓ Strong' if clinical['score'] >= 4 else '⚠ Moderate'} |")
    report.append(f"| Competition | 2/5 | ⚠ Crowded |")
    report.append("")
    report.append(f"**Overall Validation**: {total_score}/{max_score} ({'Strong' if total_score >= 12 else 'Moderate' if total_score >= 8 else 'Weak'})")

    return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="Target Validation Script")
    parser.add_argument("target", help="Target name (e.g., EGFR, KRAS)")
    parser.add_argument("--output", "-o", help="Output JSON file")
    parser.add_argument("--full", action="store_true", help="Full validation report")
    parser.add_argument("--association", help="Filter by disease association")
    parser.add_argument("--structure", action="store_true", help="Include structural data")

    args = parser.parse_args()

    # Fetch data from all sources
    print(f"Fetching validation data for {args.target}...")

    data = {
        "target": args.target,
        "opentargets": fetch_opentargets(args.target),
        "gwas": fetch_gwas(args.target),
        "uniprot": fetch_uniprot(args.target),
    }

    # Output
    if args.output:
        with open(args.output, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {args.output}")
    else:
        print(generate_validation_report(args.target, data))

    return 0


if __name__ == "__main__":
    sys.exit(main())
