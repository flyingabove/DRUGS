# ChEMBL API Reference

ChEMBL is a database of bioactive drug-like molecules with drug-like properties.

## Base URL

```
https://www.ebi.ac.uk/chembl/api/data
```

## Key Endpoints

### Molecule Endpoints

#### Get Molecule by ChEMBL ID

```
GET /molecule/{chembl_id}.json
```

**Response fields**:
| Field | Description |
|-------|-------------|
| molecule_chembl_id | Unique ChEMBL identifier |
| pref_name | Preferred compound name |
| molecule_type | Small molecule, antibody, etc. |
| molecule_structures | SMILES, InChI, InChIKey |
| max_phase | Highest clinical phase (0-4) |
| first_approval | First approval date |
| therapeutic_flag | Is therapeutic |
| ro5_compliant | Lipinski's Rule of 5 compliance |

**Example**:
```bash
curl "https://www.ebi.ac.uk/chembl/api/data/molecule/CHEMBL880.json"
```

#### Search Molecules

```
GET /molecule.json?search={query}
```

**Parameters**:
- `search`: Query string (name, synonym, SMILES)
- `limit`: Max results (default 20)
- `offset`: Pagination offset

**Example**:
```bash
curl "https://www.ebi.ac.uk/chembl/api/data/molecule.json?search=erlotinib&limit=1"
```

#### Similarity Search

```
GET /molecule.json?smiles={smiles}&similarity={threshold}
```

**Parameters**:
- `smiles`: Query SMILES
- `similarity`: Threshold (0-100)
- `molecule_type`: Filter by type

**Example**:
```bash
curl "https://www.ebi.ac.uk/chembl/api/data/molecule.json?smiles=CC1=CC=C(C=C1)CNC&similarity=70"
```

### Activity Endpoints

#### Get Activities for Molecule

```
GET /activity.json?molecule_chembl_id={chembl_id}
```

**Response fields**:
| Field | Description |
|-------|-------------|
| activity_id | Unique activity identifier |
| assay_chembl_id | Source assay |
| target_chembl_id | Target protein |
| standard_type | IC50, EC50, Ki, Kd, etc. |
| standard_value | Numerical value |
| standard_units | Units (nM, uM, etc.) |
| pchembl_value | -log10(activity value) |
| assay_type | Binding, Functional, Cell-based |

**Example**:
```bash
curl "https://www.ebi.ac.uk/chembl/api/data/activity.json?molecule_chembl_id=CHEMBL880&limit=10"
```

#### Get Activities for Target

```
GET /activity.json?target_chembl_id={target_id}
```

**Example**:
```bash
curl "https://www.ebi.ac.uk/chembl/api/data/activity.json?target_chembl_id=CHEMBL203&limit=50"
```

### Target Endpoints

#### Get Target by ID

```
GET /target/{target_id}.json
```

**Response fields**:
| Field | Description |
|-------|-------------|
| target_chembl_id | Unique target identifier |
| pref_name | Target name |
| target_type | Single protein, Protein family, etc. |
| organism | Species |
| tax_id | NCBI Taxonomy ID |
| uniprot_id | UniProt accession |
| drugcomDB | Drugable genome classification |

**Example**:
```bash
curl "https://www.ebi.ac.uk/chembl/api/data/target/CHEMBL203.json"
```

#### Search Targets

```
GET /target.json?search={query}
```

### Drug Endpoints

#### Get Drug Indications

```
GET /drug.json?molecule_chembl_id={chembl_id}
```

**Response fields**:
| Field | Description |
|-------|-------------|
| name | Drug name |
| synonyms | Alternative names |
| administration_route | Oral, IV, etc. |
| indication_class | Therapeutic class |
| max_phase_for_indication | Phase for this indication |
| withdrawn_flag | Is withdrawn |
| withdrawn_year | Year of withdrawal |
| withdrawn_reason | Reason for withdrawal |
| withdrawn_country | Country of withdrawal |

### Assay Endpoints

#### Get Assay by ID

```
GET /assay/{assay_id}.json
```

**Response fields**:
| Field | Description |
|-------|-------------|
| assay_chembl_id | Unique assay identifier |
| assay_type | B, F, P (Binding, Functional, Phenotypic) |
| assay_description | Full description |
| assay_organism | Species used |
| target_chembl_id | Associated target |

## Data Structures

### Molecule Properties

```
molecule_properties: {
    "mw_freebase": 393.4,           # Molecular weight
    "alogp": 3.2,                   # LogP (calculated)
    "hbd": 2,                       # Hydrogen bond donors
    "hba": 5,                       # Hydrogen bond acceptors
    "psa": 73.5,                    # Polar surface area
    "rtb": 6,                       # Rotatable bonds
    "aromatic_rings": 3,            # Aromatic ring count
    "heavy_atoms": 28,              # Heavy atom count
    "qed_weighted": 0.67,           # QED score
    "full_mw": 393.4                # Full molecular weight
}
```

### Bioactivity Summary

```
activities: [{
    "molecule_chembl_id": "CHEMBL880",
    "target_chembl_id": "CHEMBL203",
    "target_pref_name": "Epidermal growth factor receptor",
    "standard_type": "IC50",
    "standard_value": "0.8",
    "standard_units": "nM",
    "pchembl_value": 9.1,
    "assay_type": "B"
}]
```

## Common Queries

### Most Potent Compounds for Target

```
GET /activity.json?target_chembl_id={target_id}&order=pchembl_value.desc&limit=10
```

### Selective Compounds (Single Target)

```
GET /molecule.json?target_chembl_id={target_id}&molecule_type=Small molecule
```

### Clinical Candidates

```
GET /molecule.json?max_phase=4&molecule_type=Small molecule&limit=100
```

### Rule of 5 Compliant

```
GET /molecule.json?ro5_compliant=true&limit=100
```

## Activity Types

| Type | Description | Typical Units |
|------|-------------|---------------|
| IC50 | Half maximal inhibitory concentration | nM, uM |
| EC50 | Half maximal effective concentration | nM, uM |
| Ki | Inhibition constant | nM, uM |
| Kd | Dissociation constant | nM, uM |
| %Inhibition | Percent inhibition | % |
| %Activity | Percent activity | % |
| Selectivity | Selectivity ratio | ratio |

## Response Limits

- **Default limit**: 20 results
- **Maximum limit**: 1000 results per request
- **Pagination**: Use `offset` parameter

## Rate Limiting

- **No strict rate limit**
- **Recommended**: < 1 request/second
- **Bulk downloads**: Available via FTP

## Error Handling

| Status | Description |
|--------|-------------|
| 200 | Success |
| 404 | Resource not found |
| 500 | Server error |

## Authentication

No authentication required for public API.

## Python Integration

```python
import requests

BASE = "https://www.ebi.ac.uk/chembl/api/data"

# Get molecule
def get_molecule(chembl_id):
    url = f"{BASE}/molecule/{chembl_id}.json"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()

# Get activities
def get_activities(chembl_id, limit=20):
    url = f"{BASE}/activity.json"
    params = {"molecule_chembl_id": chembl_id, "limit": limit}
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()["activities"]
```

## Additional Resources

- **ChEMBL Web Interface**: https://www.ebi.ac.uk/chembl/
- **ChEMBL Blog**: https://www.ebi.ac.uk/chembl/blog/
- **Schema Documentation**: https://www.ebi.ac.uk/chembl/ws_schema
- **FTP Download**: ftp://ftp.ebi.ac.uk/pub/databases/chembl/
