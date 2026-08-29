# ChEMBL API Reference

ChEMBL database REST API for bioactive compound and drug discovery data.

## Base URL

```
https://www.ebi.ac.uk/chembl/api/data
```

## Key Endpoints

### 1. Target Search

Search for protein targets by name or gene symbol.

```
GET /target.json?search={query}
```

**Parameters:**
| Parameter | Description | Example |
|-----------|-------------|---------|
| search | Target name or gene symbol | `EGFR`, `kinase` |
| target_type | Filter by type | `SINGLE_PROTEIN` |
| organism | Filter by organism | `Homo sapiens` |

**Example:**
```bash
curl "https://www.ebi.ac.uk/chembl/api/data/target.json?search=EGFR"
```

**Response:**
```json
{
  "page_meta": {
    "total_count": 17803,
    "limit": 20
  },
  "targets": [
    {
      "target_chembl_id": "CHEMBL203",
      "pref_name": "Epidermal growth factor receptor",
      "target_type": "SINGLE_PROTEIN",
      "organism": "Homo sapiens",
      "synonyms": ["HER1", "ERBB1"]
    }
  ]
}
```

### 2. Target Details

Get detailed information about a specific target.

```
GET /target/{target_chembl_id}.json
```

**Example:**
```bash
curl "https://www.ebi.ac.uk/chembl/api/data/target/CHEMBL203.json"
```

### 3. Bioactivity Data

Get bioactivity measurements for a target.

```
GET /activity.json?target_chembl_id={target_id}
```

**Parameters:**
| Parameter | Description |
|-----------|-------------|
| target_chembl_id | ChEMBL target ID |
| pchembl_value__isnull | Filter for valid pChembl values (False) |
| standard_type | Bioactivity type (IC50, Ki, etc.) |
| limit | Number of results |

**Example:**
```bash
# Get bioactivities for EGFR
curl "https://www.ebi.ac.uk/chembl/api/data/activity.json?target_chembl_id=CHEMBL203&pchembl_value__isnull=False&limit=100"
```

**Response:**
```json
{
  "activities": [
    {
      "activity_id": 12345,
      "molecule_chembl_id": "CHEMBL123",
      "target_chembl_id": "CHEMBL203",
      "pref_name": "Erlotinib",
      "standard_type": "IC50",
      "standard_value": "0.5",
      "standard_units": "nM",
      "pchembl_value": 9.3,
      "assay_type": "B",
      "bao_format": "BAI_0000019"
    }
  ]
}
```

### 4. Drug Information

Get approved drugs and clinical candidates.

```
GET /drug.json?target_chembl_id={target_id}
```

**Parameters:**
| Parameter | Description |
|-----------|-------------|
| target_chembl_id | ChEMBL target ID |
| max_phase_for_indication__gte | Maximum development phase (4=approved) |
| first_approval | Filter by approval year |

**Example:**
```bash
# Get approved drugs for EGFR
curl "https://www.ebi.ac.uk/chembl/api/data/drug.json?target_chembl_id=CHEMBL203&max_phase_for_indication__gte=4"
```

**Response:**
```json
{
  "drugs": [
    {
      "drug_chembl_id": "CHEMBL880",
      "name": "Erlotinib",
      "synonyms": ["Tarceva", "CP-358774"],
      "max_phase_for_indication": 4,
      "first_approval": "2004",
      "indication_class": "Antineoplastic"
    }
  ]
}
```

### 5. Molecule Search

Search for compounds by name or properties.

```
GET /molecule.json?search={query}
```

**Parameters:**
| Parameter | Description |
|-----------|-------------|
| search | Compound name or identifier |
| molecule_properties | Property filters (e.g., `full_mwt<500`) |
| max_phase | Development phase filter |

**Example:**
```bash
# Search for erlotinib
curl "https://www.ebi.ac.uk/chembl/api/data/molecule.json?search=erlotinib"

# Find drug-like molecules
curl "https://www.ebi.ac.uk/chembl/api/data/molecule.json?molecule_properties__full_mwt__lte=500&molecule_properties__alogp__gte=0&max_phase=4"
```

### 6. Assay Information

Get experimental assay details.

```
GET /assay.json?target_chembl_id={target_id}
```

**Example:**
```bash
curl "https://www.ebi.ac.uk/chembl/api/data/assay.json?target_chembl_id=CHEMBL203"
```

## Python Example

```python
import requests

class ChEMBLClient:
    BASE_URL = "https://www.ebi.ac.uk/chembl/api/data"

    def search_target(self, query: str) -> dict:
        """Search for a target."""
        url = f"{self.BASE_URL}/target.json"
        params = {"search": query}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_bioactivities(self, target_id: str, limit: int = 100) -> list:
        """Get bioactivities for a target."""
        url = f"{self.BASE_URL}/activity.json"
        params = {
            "target_chembl_id": target_id,
            "pchembl_value__isnull": False,
            "limit": limit
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("activities", [])

    def get_approved_drugs(self, target_id: str) -> list:
        """Get approved drugs for a target."""
        url = f"{self.BASE_URL}/drug.json"
        params = {
            "target_chembl_id": target_id,
            "max_phase_for_indication__gte": 4
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("drugs", [])

# Usage
client = ChEMBLClient()

# Search for EGFR
targets = client.search_target("EGFR")
if targets["targets"]:
    target_id = targets["targets"][0]["target_chembl_id"]
    print(f"Found target: {target_id}")

    # Get bioactivities
    activities = client.get_bioactivities(target_id)
    print(f"Found {len(activities)} bioactivities")

    # Get approved drugs
    drugs = client.get_approved_drugs(target_id)
    print(f"Found {len(drugs)} approved drugs")
    for drug in drugs:
        print(f"  - {drug.get('name')}")
```

## Development Phase Codes

| Phase | Description |
|-------|-------------|
| 0 | Research |
| 1 | Phase I clinical |
| 2 | Phase II clinical |
| 3 | Phase III clinical |
| 4 | Approved |

## Standard Types

| Type | Description |
|------|-------------|
| IC50 | Half maximal inhibitory concentration |
| Ki | Inhibition constant |
| Kd | Dissociation constant |
| EC50 | Half maximal effective concentration |
| AC50 | Half maximal activity concentration |

## Best Practices

1. **Use pChembl values**: These are standardized (-log10 transformed) values
2. **Filter by assay type**: 'B' = binding, 'F' = functional
3. **Check molecule type**: 'Small molecule', 'Antibody', etc.
4. **Use limit parameter**: Avoid fetching too many records at once
5. **Cache results**: ChEMBL data doesn't change frequently

## Error Handling

| HTTP Code | Description |
|-----------|-------------|
| 200 | Success |
| 404 | Not found |
| 500 | Server error |

## Rate Limiting

No strict rate limit, but be respectful and implement delays between requests.
