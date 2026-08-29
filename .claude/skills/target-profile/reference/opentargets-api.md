# Open Targets API Reference

Open Targets Platform REST API for target validation and disease associations.

## Base URL

```
https://api.opentargets.org/v3/platform/public
```

## API Rate Limits

- **Public**: 10 requests per second
- **Registered**: Higher limits available
- **Authentication**: Not required for public endpoints

## Key Endpoints

### 1. Search

Search for targets, diseases, or drugs.

```
GET /search?q={query}&size={size}&filter={filter}
```

**Parameters:**
- `q` (required): Search query
- `size` (optional): Number of results (default: 10)
- `filter` (optional): Filter by type (target, disease, drug)

**Example:**
```bash
curl "https://api.opentargets.org/v3/platform/public/search?q=EGFR&size=1"
```

**Response:**
```json
{
  "data": [
    {
      "id": "ENSG00000146648",
      "symbol": "EGFR",
      "name": "epidermal growth factor receptor",
      "biotype": "protein_coding",
      "tractability": [...]
    }
  ]
}
```

### 2. Target Details

Get detailed information about a specific target.

```
GET /targets/{target_id}
```

**Parameters:**
- `target_id` (required): ENSG ID or target symbol

**Example:**
```bash
curl "https://api.opentargets.org/v3/platform/public/targets/ENSG00000146648"
```

**Response Fields:**
| Field | Description |
|-------|-------------|
| `id` | ENSG identifier |
| `symbol` | Gene symbol |
| `name` | Protein name |
| `biotype` | Gene biotype |
| `tractability` | Tractability assessment |
| `protein_annotations` | Protein structure info |

### 3. Disease Associations

Get disease associations for a target.

```
GET /associations?target={target_id}&size={size}
```

**Parameters:**
- `target` (required): Target ID
- `size` (optional): Number of results (default: 100)
- `sort` (optional): Sort by field (e.g., `-association_score.overall`)

**Response:**
```json
{
  "data": [
    {
      "id": "association_id",
      "disease": {
        "id": "EFO_0001075",
        "name": "lung carcinoma"
      },
      "association_score": {
        "overall": 0.95
      },
      "evidence_count": 234
    }
  ]
}
```

### 4. Tractability Assessment

Tractability indicates how "druggable" a target is.

**Tractability Classes:**
| Modality | Description |
|----------|-------------|
| Small molecule | Small molecule drugs |
| Antibody | Monoclonal antibodies |
| PROTAC | Proteolysis targeting chimeras |
| Other | Other modalities |

**Tractability Levels:**
| Score | Description |
|-------|-------------|
| 1-3 | Challenging |
| 4-6 | Moderate |
| 7-10 | High tractability |

**Response Structure:**
```json
{
  "tractability": [
    {
      "modality": "Small molecule",
      "summary": "High tractability",
      "properties": [...]
    }
  ]
}
```

## Target Development Levels (TDL)

| TDL | Description |
|-----|-------------|
| Tclin | Approved drugs |
| Tchem | Bioactive compounds |
| Tbio | Biological target (no small molecules) |
| Tdark | Limited knowledge |
| Tbio | Characterized biology |

## Python Example

```python
import requests

class OpenTargetsClient:
    BASE_URL = "https://api.opentargets.org/v3/platform/public"

    def search_target(self, query: str) -> dict:
        url = f"{self.BASE_URL}/search"
        params = {"q": query, "size": 1}
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        if data.get("data"):
            return data["data"][0]
        return None

    def get_target_details(self, target_id: str) -> dict:
        url = f"{self.BASE_URL}/targets/{target_id}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["data"]

    def get_associations(self, target_id: str, limit: int = 20) -> list:
        url = f"{self.BASE_URL}/associations"
        params = {
            "target": target_id,
            "size": limit,
            "sort": "-association_score.overall"
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("data", [])

# Usage
client = OpenTargetsClient()
target = client.search_target("EGFR")
print(target["name"])  # "epidermal growth factor receptor"

details = client.get_target_details(target["id"])
associations = client.get_associations(target["id"])
```

## Data Fields Reference

### Association Score Breakdown

| Score Component | Description |
|-----------------|-------------|
| `overall` | Combined association score |
| `genetic_association` | Genetic evidence score |
| `somatic_mutation` | Somatic mutation evidence |
| `known_drug` | Known drug evidence |
| `affected_pathway` | Pathway evidence |
| `rna_expression` | RNA expression evidence |
| `literature` | Literature mining evidence |

## Error Handling

| HTTP Code | Description |
|-----------|-------------|
| 200 | Success |
| 404 | Resource not found |
| 429 | Rate limit exceeded |
| 500 | Server error |

## Best Practices

1. **Cache responses**: Target data doesn't change frequently
2. **Use ENSG IDs**: More reliable than symbols for lookups
3. **Batch requests**: Use /associations with appropriate limits
4. **Handle pagination**: Use `next` cursor for large result sets
