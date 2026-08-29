# ClinicalTrials.gov API Reference

ClinicalTrials.gov REST API for clinical trial information.

## Base URL

```
https://clinicaltrials.gov/api/query
```

## API Status

- **Authentication**: Not required
- **Rate Limits**: None specified, be respectful
- **Data Format**: JSON or XML

## Key Endpoints

### 1. Full Studies

Get complete study information.

```
GET /full_studies?expr={query}&min_rnk={start}&max_rnk={end}
```

**Parameters:**
| Parameter | Description | Default |
|-----------|-------------|---------|
| expr | Search expression | Required |
| min_rnk | Starting rank | 1 |
| max_rnk | Ending rank | 100 |
| fmt | Format (json, xml) | json |

**Example:**
```bash
# Search for EGFR trials
curl "https://clinicaltrials.gov/api/query/full_studies?expr=EGFR&min_rnk=1&max_rnk=10&fmt=json"
```

**Response Structure:**
```json
{
  "FullStudiesResponse": {
    "APIVrs": "v2",
    "DataVrs": "2024.01.01",
    "NStudiesAvail": 1500,
    "NStudiesReturned": 10,
    "Studies": [
      {
        "Rank": 1,
        "Study": {
          "ProtocolSection": {
            "IdentificationModule": {
              "NCTId": "NCT03704547",
              "BriefTitle": "Study of osimertinib in EGFR-mutated NSCLC"
            },
            "StatusModule": {
              "OverallStatus": "Recruiting",
              "StartDateStruct": {
                "date": "2018-11-01"
              }
            },
            "DesignModule": {
              "PhaseList": {"Phase": ["Phase 3"]},
              "ArmsInterventionsModule": {
                "ArmList": {"Arm": [...]}
              }
            }
          }
        }
      }
    ]
  }
}
```

### 2. Field Search

Search specific fields only.

```
GET /study_fields?expr={query}&fields={field_list}
```

**Common Fields:**
| Field | Description |
|-------|-------------|
| NCTId | ClinicalTrials.gov identifier |
| BriefTitle | Study title |
| Condition | Medical condition |
| Intervention | Treatment/intervention |
| Phase | Study phase |
| OverallStatus | Recruitment status |
| StartDate | Study start date |
| PrimaryCompletionDate | Primary completion date |
| SponsorCollaborators | Sponsor information |

**Example:**
```bash
# Get NCT IDs and titles only
curl "https://clinicaltrials.gov/api/query/study_fields?expr=EGFR&fields=NCTId,BriefTitle&min_rnk=1&max_rnk=20"
```

### 3. Study Statistics

Get study count information.

```
GET /study_statistics?expr={query}
```

**Example:**
```bash
curl "https://clinicaltrials.gov/api/query/study_statistics?expr=EGFR+NSCLC"
```

## Search Expression Syntax

### Basic Operators

| Operator | Description | Example |
|----------|-------------|---------|
| AND | Both terms | `EGFR AND NSCLC` |
| OR | Either term | `lung OR pulmonary` |
| NOT | Exclude term | `cancer NOT lung` |
| `()` | Grouping | `(EGFR OR HER2) AND NSCLC` |

### Field Restrictions

| Field | Syntax | Example |
|-------|--------|---------|
| Condition | `AREA[Condition]` | `cancer[Condition]` |
| Intervention | `TERM[Intervention]` | `erlotinib[Intervention]` |
| Phase | `PHASE[Phase]` | `PHASE3[Phase]` |
| Status | `STATUS[OverallStatus]` | `Recruiting[OverallStatus]` |

### Advanced Search

**Example Queries:**
```bash
# EGFR inhibitors in NSCLC
"EGFR" AND ("inhibitor" OR "TKI") AND "lung cancer"[Condition]

# Recruiting Phase III trials
Recruiting[OverallStatus] AND PHASE3[Phase]

# Specific drug studies
osimertinib[Intervention] AND NSCLC[Condition]

# Recently started trials
2023[StartDate] AND "cancer"[Condition]
```

## Python Example

```python
import requests
import time

class ClinicalTrialsClient:
    BASE_URL = "https://clinicaltrials.gov/api/query"

    def __init__(self):
        self.last_request = 0

    def _rate_limit(self, min_interval=0.34):
        """Basic rate limiting."""
        elapsed = time.time() - self.last_request
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)
        self.last_request = time.time()

    def search_studies(self, query: str, max_results: int = 50) -> list:
        """Search for clinical trials."""
        self._rate_limit()

        url = f"{self.BASE_URL}/full_studies"
        params = {
            "expr": query,
            "min_rnk": 1,
            "max_rnk": max_results,
            "fmt": "json"
        }

        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        studies = []
        for item in data.get("FullStudiesResponse", {}).get("Studies", []):
            study = item.get("Study", {})
            studies.append(self._parse_study(study))

        return studies

    def _parse_study(self, study: dict) -> dict:
        """Extract key study information."""
        proto = study.get("ProtocolSection", {})
        id_module = proto.get("IdentificationModule", {})
        status = proto.get("StatusModule", {})
        design = proto.get("DesignModule", {})
        contacts = proto.get("ContactsLocationsModule", {})
        arms = design.get("ArmsInterventionsModule", {}).get("ArmList", {}).get("Arm", [])

        # Extract phase
        phase_list = design.get("PhaseList", {}).get("Phase", [])
        phase = phase_list[0] if phase_list else "N/A"

        # Extract interventions
        interventions = []
        for arm in arms[:3]:  # Limit to first 3 arms
            for intv in arm.get("InterventionList", {}).get("Intervention", []):
                interventions.append(intv.get("name", ""))

        return {
            "nct_id": id_module.get("NCTId"),
            "title": id_module.get("BriefTitle"),
            "status": status.get("OverallStatus"),
            "phase": phase,
            "start_date": status.get("StartDateStruct", {}).get("date"),
            "completion_date": status.get("PrimaryCompletionDateStruct", {}).get("date"),
            "interventions": interventions,
            "conditions": proto.get("ConditionsModule", {}).get("ConditionList", {}).get("Condition", []),
            "sponsor": contacts.get("CentralContact", {}).get("Organization", "N/A")
        }

    def get_study_count(self, query: str) -> int:
        """Get total number of studies matching query."""
        self._rate_limit()

        url = f"{self.BASE_URL}/study_statistics"
        params = {"expr": query}

        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        return data.get("StudyStatisticsResponse", {}).get("NStudiesFound", 0)

# Usage
client = ClinicalTrialsClient()

# Get study count
count = client.get_study_count("EGFR AND NSCLC")
print(f"Found {count} studies")

# Get studies
studies = client.search_studies("EGFR AND osimertinib", max_results=20)
for study in studies:
    print(f"{study['nct_id']}: {study['title']}")
    print(f"  Status: {study['status']}, Phase: {study['phase']}")
```

## Status Values

| Status | Description |
|--------|-------------|
| Recruiting | Currently enrolling |
| Not yet recruiting | Not yet open for enrollment |
| Active, not recruiting | Ongoing but not enrolling |
| Completed | Finished study |
| Suspended | Temporarily halted |
| Terminated | Stopped early |
| Withdrawn | Withdrawn before enrollment |

## Phase Values

| Phase | Description |
|-------|-------------|
| N/A | Not applicable |
| Phase 1 | Safety and dosage |
| Phase 2 | Efficacy and side effects |
| Phase 3 | Large scale comparison |
| Phase 4 | Post-marketing studies |

## Best Practices

1. **Use specific queries**: Combine condition and intervention
2. **Check status**: Filter by recruitment status for active trials
3. **Limit results**: Use max_rnk to avoid large responses
4. **Rate limiting**: Add delays between requests
5. **Handle pagination**: Process results in batches

## Common Search Patterns

```python
# Drug + Disease
"{drug}[Intervention] AND {disease}[Condition]"

# Specific phase
"Recruiting[OverallStatus] AND PHASE2[Phase] AND {disease}[Condition]"

# Recent trials
"{disease}[Condition] AND 2023[StartDate]"

# Combination therapy
"{drug1}[Intervention] AND {drug2}[Intervention]"

# Biomarker-driven
"{biomarker}[Biomarker] AND {disease}[Condition]"
```

## Data Access

- **Public Domain**: All data is publicly available
- **Citation**: ClinicalTrials.gov identifier (NCT number)
- **Updates**: Daily
