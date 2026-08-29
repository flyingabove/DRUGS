# PubChem PUG REST API Reference

PubChem is a public database of chemical molecules and their activities against biological assays.

## Base URL

```
https://pubchem.ncbi.nlm.nih.gov/rest/pug
```

## Key Concepts

### Compound (CID) vs Substance (SID) vs Assay (AID)

| ID Type | Prefix | Description |
|---------|--------|-------------|
| CID | CID | Compound identifier (canonicalized structure) |
| SID | SID | Substance identifier (submitted sample) |
| AID | AID | Assay identifier (bioactivity experiment) |

## Input Types

| Input | Description | Example |
|-------|-------------|---------|
| CID | Compound ID | CID=2244 |
| Name | Compound name | Name=aspirin |
| SMILES | SMILES string | SMILES=CC(=O)OC1=CC=CC=C1C(=O)O |
| InChI | InChI string | InChI=InChI=1S/C9H8O4/c1-6(10)13-8-5-3-2-4-7(8)9(11)12/h2-5H,1H3 |
| InChIKey | InChIKey | InChIKey=BSYNRYMUTXBXSQ-UHFFFAOYSA-N |
| Formula | Molecular formula | Formula=C9H8O4 |

## Compound Endpoints

### Get Compound Properties

```
GET /compound/{input_type}/{input}/property/{property_list}/JSON
```

**Available properties**:
| Property | Description |
|----------|-------------|
| MolecularFormula | Molecular formula |
| MolecularWeight | Molecular weight |
| CanonicalSMILES | Canonical SMILES |
| IsomericSMILES | Isomeric SMILES |
| InChI | InChI string |
| InChIKey | InChIKey |
| IUPACName | IUPAC name |
| XLogP | LogP (octanol/water) |
| ExactMass | Exact mass |
| MonoisotopicMass | Monoisotopic mass |
| Complexity | Complexity score |
| Charge | Formal charge |
| HBondDonorCount | Hydrogen bond donors |
| HBondAcceptorCount | Hydrogen bond acceptors |
| RotatableBondCount | Rotatable bonds |
| TPSA | Topological polar surface area |
| Volume | 3D volume |
| HeavyAtomCount | Heavy atoms |
| IsotopeAtomCount | Isotope atoms |
| AtomStereoCount | Stereogenic atoms |
| DefinedAtomStereoCount | Defined stereogenic atoms |
| UndefinedAtomStereoCount | Undefined stereogenic atoms |
| BondStereoCount | Stereogenic bonds |
| DefinedBondStereoCount | Defined stereogenic bonds |
| UndefinedBondStereoCount | Undefined stereogenic bonds |
| CovalentUnitCount | Covalent units |
| Fingerprint2D | 2D fingerprint (not in JSON) |

**Examples**:
```bash
# Get properties by CID
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/property/MolecularFormula,MolecularWeight,XLogP/JSON"

# Get properties by name
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/aspirin/property/CanonicalSMILES,InChIKey/JSON"
```

### Get Compound Description

```
GET /compound/{input_type}/{input}/description/JSON
```

**Example**:
```bash
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/description/JSON"
```

### Get Compound Synonyms

```
GET /compound/{input_type}/{input}/synonyms/JSON
```

**Example**:
```bash
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/synonyms/TXT"
```

### Get Compound Classification

```
GET /compound/{input_type}/{input}/classification/{format}
```

**Classifications available**:
- Classyfire
- LIPID MAPS

**Example**:
```bash
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/classification/JSON"
```

### Similarity Search

```
GET /compound/fastidentity/{input_type}/{input}/cids/{format}
```

**Parameters**:
- `Threshold`: 0-100 (default 90)
- `MaxRecords`: Max results

**Example**:
```bash
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/fastidentity/cid/2244/cids/JSON?Threshold=70&MaxRecords=10"
```

### Substructure Search

```
POST /compound/fastsimilarity_{input_type}/cids/{format}
```

## Assay Endpoints

### Get Assay Summary

```
GET /assay/{aid}/description/JSON
```

**Example**:
```bash
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/assay/aid/1/description/JSON"
```

### Get Assay Results

```
GET /assay/{aid}/JSON
```

### Get Assay CID List

```
GET /assay/aid/{aid}/cids/JSON
```

## Bioactivity Endpoints

### Bioactivity by Target (Gene)

```
GET /protein/gene/{gene_id}/cids/JSON
```

**Parameters**:
- `activity`: Active, inactive, both (default)
- `response_type`: gene, organism, protein, accession

**Example**:
```bash
# Get active compounds for EGFR
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/gene/1956/cids/JSON?activity=active"
```

### Bioactivity by Target Accession

```
GET /protein/accession/{accession}/cids/JSON
```

**Example**:
```bash
# Get active compounds by UniProt accession
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/accession/P00533/cids/JSON"
```

## Structure Endpoints

### Get 2D Coordinates (PNG)

```
GET /compound/{input_type}/{input}/PNG
```

**Parameters**:
- `image_size`: Small, medium, large
- `PNGrecord`: CID number

**Example**:
```bash
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/PNG?image_size=large" -o aspirin.png
```

### Get 3D Coordinates (SDF)

```
GET /compound/{input_type}/{input}/SDF
```

**Example**:
```bash
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/SDF?record_type=3d" -o aspirin.sdf
```

## Response Formats

| Format | Extension | Description |
|--------|-----------|-------------|
| JSON | JSON | Machine-readable |
| XML | XML | Machine-readable |
| TXT | TXT | Plain text |
| PNG | PNG | Image |
| SDF | SDF | Structure data file |
| CSV | CSV | Comma-separated |

## List Operations

### Get List of CIDs

```
GET /compound/list_id/{list_key}/cids/JSON
```

### Create List Key

```
GET /compound/{input_type}/{input}/cids/{list_key}
```

**Example**:
```bash
# Create list from SMILES
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/CC1=CC=C(C=C1)CNC/cids/TXT"
```

## Rate Limiting

- **Default**: 5 requests/second
- **IP-based**: Limited by IP address
- **Wait time**: If busy, includes `Wait-Time` header

## Error Handling

| Status | Description |
|--------|-------------|
| 200 | Success |
| 400 | Bad request (invalid input) |
| 404 | Not found |
| 405 | Method not allowed |
| 500 | Server error |
| 503 | Rate limited (check `Wait-Time` header) |

## REST vs PUG SOAP

- **PUG REST**: Simple URL-based queries
- **PUG SOAP**: Complex queries, batch operations

## Python Integration

```python
import requests

BASE = "https://pubchem.ncbi.nlm.nih.gov/rest/pug"

def get_properties(name, properties):
    """Get compound properties by name."""
    url = f"{BASE}/compound/name/{name}/property/{','.join(properties)}/JSON"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    data = response.json()
    return data["PropertyTable"]["Properties"][0]

def get_cid(name):
    """Get CID for compound name."""
    url = f"{BASE}/compound/name/{name}/cids/JSON"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()["IdentifierList"]["CID"][0]

def get_similar_compounds(cid, threshold=90, limit=10):
    """Get similar compounds by CID."""
    url = f"{BASE}/compound/fastidentity/cid/{cid}/cids/JSON"
    params = {"Threshold": threshold, "MaxRecords": limit}
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()["IdentifierList"]["CID"]
```

## Common Use Cases

### Drug-Likeness Filter

```python
def is_drug_like(properties):
    """Lipinski's Rule of 5."""
    return (
        properties["MolecularWeight"] < 500 and
        properties["XLogP"] < 5 and
        properties["HBondDonorCount"] <= 5 and
        properties["HBondAcceptorCount"] <= 10
    )
```

### Bioactivity Lookup

```bash
# Get active compounds for EGFR gene
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/protein/gene/1956/cids/JSON?activity=active"

# Get bioactivity summary for compound
curl "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/2244/assaysummary/JSON"
```

## Additional Resources

- **PubChem Home**: https://pubchem.ncbi.nlm.nih.gov/
- **PUG REST Documentation**: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest.html
- **Power User Gateway**: https://pubchem.ncbi.nlm.nih.gov/pug_rest/PUG_REST.html
