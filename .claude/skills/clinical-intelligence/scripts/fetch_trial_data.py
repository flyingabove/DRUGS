#!/usr/bin/env python3
"""
Fetch clinical trial data from ClinicalTrials.gov.

Usage:
    python fetch_trial_data.py NCT03704547 --output trial.json
    python fetch_trial_data.py --condition "NSCLC" --phase 3
    python fetch_trial_data.py --intervention osimertinib --limit 50
"""

import argparse
import json
import sys

if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")
from datetime import datetime
from typing import Optional, Dict, Any, List
import requests


class ClinicalTrialsFetcher:
    """Fetch clinical trial data from ClinicalTrials.gov."""

    BASE_URL = "https://clinicaltrials.gov/api/query"

    def __init__(self):
        self.results = {
            "query_type": None,
            "data": {},
            "timestamp": datetime.now().isoformat()
        }

    def fetch_trial(self, nct_id: str) -> Dict[str, Any]:
        """Fetch detailed information for a specific trial."""
        try:
            # Get full study data
            url = f"{self.BASE_URL}/full_studies"
            params = {
                "expr": f"{nct_id}[NCTId]",
                "min_rnk": 1,
                "max_rnk": 1,
                "fmt": "json"
            }

            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            studies = data.get("FullStudiesResponse", {}).get("Studies", [])
            if not studies:
                print(f"✗ Trial {nct_id} not found")
                return {}

            study = studies[0].get("Study", {})
            protocol = study.get("ProtocolSection", {})

            # Extract key information
            result = {
                "nct_id": nct_id,
                "title": self._get_nested(protocol, "IdentificationModule.BriefTitle"),
                "status": self._get_nested(protocol, "StatusModule.OverallStatus"),
                "start_date": self._get_nested(protocol, "StatusModule.StartDateStruct.date"),
                "primary_completion": self._get_nested(protocol, "StatusModule.PrimaryCompletionDateStruct.date"),
                "phase": self._extract_phase(protocol),
                "study_type": self._get_nested(protocol, "DesignModule.StudyType"),
                "sponsor": self._get_nested(protocol, "SponsorCollaboratorsModule.LeadSponsor.Organization"),
                "interventions": self._extract_interventions(protocol),
                "conditions": self._extract_conditions(protocol),
                "eligibility": self._extract_eligibility(protocol),
                "locations": self._extract_locations(protocol),
                "contacts": self._extract_contacts(protocol)
            }

            # Get outcome measures if available
            outcomes = self._extract_outcomes(protocol)
            if outcomes:
                result["outcomes"] = outcomes

            # Get results if available
            results_section = study.get("ResultsSection", {})
            if results_section:
                result["has_results"] = True
                result["results"] = self._extract_results(results_section)

            print(f"✓ Fetched trial {nct_id}")
            return result

        except Exception as e:
            print(f"✗ Error fetching {nct_id}: {e}")
            return {}

    def search_trials(self, condition: Optional[str] = None,
                     intervention: Optional[str] = None,
                     phase: Optional[str] = None,
                     status: Optional[str] = None,
                     limit: int = 50) -> List[Dict[str, Any]]:
        """Search for clinical trials matching criteria."""
        try:
            # Build query
            query_parts = []

            if condition:
                query_parts.append(f'"{condition}"[Condition]')

            if intervention:
                query_parts.append(f'"{intervention}"[Intervention]')

            if phase:
                phase_map = {"1": "PHASE1", "2": "PHASE2", "3": "PHASE3", "4": "PHASE4"}
                phase_query = phase_map.get(phase, f"PHASE{phase}")
                query_parts.append(f"{phase_query}[Phase]")

            if status:
                query_parts.append(f'"{status}"[OverallStatus]')

            query = " AND ".join(query_parts) if query_parts else "cancer[Condition]"

            # Get study fields for faster response
            url = f"{self.BASE_URL}/study_fields"
            params = {
                "expr": query,
                "fields": "NCTId,BriefTitle,OverallStatus,Phase,StartDate,CompletionDate,Condition,InterventionName",
                "min_rnk": 1,
                "max_rnk": limit,
                "fmt": "json"
            }

            response = requests.get(url, params=params, timeout=60)
            response.raise_for_status()
            data = response.json()

            studies = data.get("FullStudiesResponse", {}).get("Studies", [])

            trials = []
            for item in studies:
                study = item.get("Study", {})
                protocol = study.get("ProtocolSection", {})
                id_module = protocol.get("IdentificationModule", {})
                status_module = protocol.get("StatusModule", {})
                design = protocol.get("DesignModule", {})

                trial = {
                    "nct_id": id_module.get("NCTId"),
                    "title": id_module.get("BriefTitle"),
                    "status": status_module.get("OverallStatus"),
                    "phase": self._extract_phase(protocol),
                    "start_date": self._get_nested(status_module, "StartDateStruct.date"),
                    "completion_date": self._get_nested(status_module, "PrimaryCompletionDateStruct.date"),
                    "conditions": self._extract_conditions(protocol),
                    "interventions": self._extract_interventions(protocol)
                }
                trials.append(trial)

            print(f"✓ Found {len(trials)} trials matching query")
            return trials

        except Exception as e:
            print(f"✗ Search error: {e}")
            return []

    def _get_nested(self, data: Dict, path: str) -> Any:
        """Get nested dictionary value using dot notation."""
        keys = path.split(".")
        for key in keys:
            if isinstance(data, dict):
                data = data.get(key)
            else:
                return None
        return data

    def _extract_phase(self, protocol: Dict) -> str:
        """Extract phase information."""
        phase_list = self._get_nested(protocol, "DesignModule.PhaseList.Phase")
        if phase_list:
            if isinstance(phase_list, list):
                return phase_list[0] if phase_list else "N/A"
            return phase_list
        return "N/A"

    def _extract_interventions(self, protocol: Dict) -> List[Dict]:
        """Extract intervention information."""
        arms = self._get_nested(protocol, "ArmsInterventionsModule.ArmList.Arm") or []
        interventions = []

        for arm in arms[:10]:  # Limit to first 10
            arm_name = arm.get("ArmName", "Unknown")
            for intv in arm.get("InterventionList", {}).get("Intervention", []):
                interventions.append({
                    "arm": arm_name,
                    "type": intv.get("InterventionType"),
                    "name": intv.get("Name") or intv.get("Description"),
                    "dose": intv.get("DosageText")
                })
        return interventions

    def _extract_conditions(self, protocol: Dict) -> List[str]:
        """Extract condition/disease information."""
        cond_module = protocol.get("ConditionsModule") or {}
        cond_list = cond_module.get("ConditionList", {}).get("Condition", [])

        if isinstance(cond_list, list):
            return [c.get("condition", "") for c in cond_list]
        elif isinstance(cond_list, dict):
            return [cond_list.get("condition", "")]
        return []

    def _extract_eligibility(self, protocol: Dict) -> Dict:
        """Extract eligibility criteria."""
        eligibility = protocol.get("EligibilityModule", {})

        return {
            "population": eligibility.get("EligibilityModule.Population"),
            "gender": eligibility.get("EligibilityModule.Gender"),
            "min_age": eligibility.get("EligibilityModule.MinimumAge"),
            "max_age": eligibility.get("EligibilityModule.MaximumAge"),
            "healthy_volunteers": eligibility.get("EligibilityModule.HealthyVolunteers"),
            "criteria_inclusion": eligibility.get("EligibilityModule.InclusionCriteria", "")[:500],
            "criteria_exclusion": eligibility.get("EligibilityModule.ExclusionCriteria", "")[:500]
        }

    def _extract_locations(self, protocol: Dict) -> List[Dict]:
        """Extract study locations."""
        locs = protocol.get("ContactsLocationsModule", {}).get("LocationList", {}).get("Location", [])

        locations = []
        for loc in locs[:20]:  # Limit to first 20
            locations.append({
                "facility": loc.get("LocationFacility"),
                "city": loc.get("LocationCity"),
                "state": loc.get("LocationState"),
                "country": loc.get("LocationCountry"),
                "status": loc.get("LocationStatus")
            })
        return locations

    def _extract_contacts(self, protocol: Dict) -> List[Dict]:
        """Extract contact information."""
        contacts = []

        central = protocol.get("CentralContactModule", {})
        contacts.append({
            "type": "Central Contact",
            "name": central.get("CentralContactName"),
            "email": central.get("CentralContactEmail"),
            "phone": central.get("CentralContactPhone"),
            "organization": central.get("CentralContactOrganization")
        })

        return contacts

    def _extract_outcomes(self, protocol: Dict) -> List[Dict]:
        """Extract primary and secondary outcomes."""
        outcomes = protocol.get("OutcomesModule", {})
        result = []

        primary = outcomes.get("PrimaryOutcomeList", {}).get("PrimaryOutcome", [])
        for p in primary[:3]:
            result.append({
                "type": "Primary",
                "measure": p.get("Measure"),
                "time_frame": p.get("TimeFrame"),
                "description": p.get("Description", "")[:200]
            })

        secondary = outcomes.get("SecondaryOutcomeList", {}).get("SecondaryOutcome", [])
        for s in secondary[:5]:
            result.append({
                "type": "Secondary",
                "measure": s.get("Measure"),
                "time_frame": s.get("TimeFrame"),
                "description": s.get("Description", "")[:200]
            })

        return result

    def _extract_results(self, results_section: Dict) -> Dict:
        """Extract study results."""
        outcome_stats = results_section.get("MoreInfoModule", {})

        return {
            "outcome_stats": outcome_stats.get("OutcomeStats", ""),
            "participant_flow": results_section.get("ParticipantFlowModule", {}),
            "baseline_data": results_section.get("BaselineCharacteristicsModule", {})
        }

    def save(self, output: str):
        """Save results to file."""
        with open(output, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"✓ Results saved to {output}")


def main():
    parser = argparse.ArgumentParser(description="Fetch clinical trial data")
    parser.add_argument("nct_id", nargs="?", help="ClinicalTrials.gov identifier (e.g., NCT03704547)")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("--condition", help="Search by condition")
    parser.add_argument("--intervention", help="Search by intervention")
    parser.add_argument("--phase", choices=["1", "2", "3", "4"], help="Filter by phase")
    parser.add_argument("--status", help="Filter by status")
    parser.add_argument("--limit", type=int, default=50, help="Max results for search")
    parser.add_argument("--format", choices=["json", "summary"], default="json", help="Output format")

    args = parser.parse_args()

    fetcher = ClinicalTrialsFetcher()

    if args.nct_id:
        # Fetch specific trial
        trial = fetcher.fetch_trial(args.nct_id)
        fetcher.results["trial"] = trial
        fetcher.results["query_type"] = "single"

        if args.format == "summary":
            print_trial_summary(trial)
        else:
            output = args.output or f"{args.nct_id}.json"
            fetcher.save(output)

    elif args.condition or args.intervention:
        # Search trials
        trials = fetcher.search_trials(
            condition=args.condition,
            intervention=args.intervention,
            phase=args.phase,
            status=args.status,
            limit=args.limit
        )
        fetcher.results["trials"] = trials
        fetcher.results["query_type"] = "search"
        fetcher.results["count"] = len(trials)

        if args.format == "summary":
            print_search_summary(trials)
        else:
            output = args.output or "trials_search.json"
            fetcher.save(output)
    else:
        parser.print_help()


def print_trial_summary(trial: Dict[str, Any]):
    """Print trial summary."""
    if not trial:
        print("No trial data found")
        return

    print("\n" + "="*60)
    print(f"CLINICAL TRIAL: {trial['nct_id']}")
    print("="*60 + "\n")

    print(f"**Title:** {trial.get('title')}")
    print(f"**Status:** {trial.get('status')}")
    print(f"**Phase:** {trial.get('phase')}")
    print(f"**Sponsor:** {trial.get('sponsor')}")

    print(f"\n**Dates:**")
    print(f"  Start: {trial.get('start_date', 'N/A')}")
    print(f"  Primary Completion: {trial.get('primary_completion', 'N/A')}")

    if trial.get('conditions'):
        print(f"\n**Conditions:**")
        for c in trial['conditions'][:3]:
            print(f"  - {c}")

    if trial.get('interventions'):
        print(f"\n**Interventions:**")
        for i in trial['interventions'][:5]:
            print(f"  - {i['name']} ({i['type']})")

    if trial.get('outcomes'):
        print(f"\n**Outcomes:**")
        for o in trial['outcomes'][:3]:
            print(f"  - [{o['type']}] {o['measure']}")

    print("\n" + "="*60 + "\n")


def print_search_summary(trials: List[Dict]):
    """Print search results summary."""
    print("\n" + "="*60)
    print(f"CLINICAL TRIALS SEARCH: {len(trials)} trials found")
    print("="*60 + "\n")

    phase_counts = {}
    status_counts = {}

    for trial in trials:
        phase = trial.get('phase', 'Unknown')
        status = trial.get('status', 'Unknown')
        phase_counts[phase] = phase_counts.get(phase, 0) + 1
        status_counts[status] = status_counts.get(status, 0) + 1

    print(f"**By Phase:**")
    for phase, count in sorted(phase_counts.items()):
        print(f"  {phase}: {count}")

    print(f"\n**By Status:**")
    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count}")

    print(f"\n**Recent Trials:**")
    for trial in trials[:10]:
        print(f"  {trial['nct_id']}: {trial['title'][:60]}...")
        print(f"    Phase: {trial['phase']}, Status: {trial['status']}")

    print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()
