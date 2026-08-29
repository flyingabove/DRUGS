# Target Profile Data Schema

Schema definitions for target profile data structures.

## Root Schema

```json
{
  "target": "string",           // Gene symbol (e.g., "EGFR")
  "data": {                     // Data from various sources
    "opentargets": {...},
    "uniprot": {...},
    "chembl": {...}
  },
  "sources_queried": [          // List of successfully queried sources
    "opentargets",
    "uniprot",
    "chembl"
  ],
  "timestamp": "ISO-8601"       // When data was fetched
}
```

## Open Targets Schema

```json
{
  "id": "ENSG00000146648",      // Ensembl Gene ID
  "symbol": "EGFR",             // HGNC gene symbol
  "name": "epidermal growth factor receptor",
  "biotype": "protein_coding",

  "tractability": {             // Druggability assessment
    "tractability": [
      {
        "modality": "Small molecule",
        "summary": "High tractability",
        "properties": [
          {
            "property": "Small molecule - Clinical precedence",
            "value": "Clinical precedence with 9 approved drugs"
          }
        ]
      },
      {
        "modality": "Antibody",
        "summary": "High tractability",
        "properties": [...]
      }
    ],
    "target_class": [
      {
        "id": "kinase",
        "label": "Protein kinase"
      }
    ]
  },

  "associations": [             // Disease associations
    {
      "disease_id": "EFO_0001075",
      "disease_name": "lung carcinoma",
      "association_score": 0.95,
      "evidence_count": 234
    }
  ]
}
```

## UniProt Schema

```json
{
  "accession": "P00533",        // UniProt primary accession
  "name": "Epidermal growth factor receptor",
  "gene_name": "EGFR",
  "function": "Receptor tyrosine kinase...",

  "length": 1210,               // Amino acid count
  "mass": 134305,               // Molecular weight in Da
  "subcellular_location": "Cell membrane; Single-pass type I membrane protein",

  "pathways": [                 // KEGG pathways
    {
      "id": "hsa04012",
      "name": "ErbB signaling pathway"
    },
    {
      "id": "hsa04010",
      "name": "MAPK signaling pathway"
    }
  ]
}
```

## ChEMBL Schema

```json
{
  "chembl_id": "CHEMBL240",     // ChEMBL target ID
  "target_components": [...],

  "bioactivity_count": 15234,   // Total bioactivity records

  "top_compounds": [            // Highest affinity compounds
    {
      "molecule_chembl_id": "CHEMBL123",
      "pref_name": "Erlotinib",
      "pchembl_value": 8.2,
      "standard_type": "IC50"
    }
  ],

  "approved_drugs": [           // Approved drugs targeting this protein
    {
      "name": "Erlotinib",
      "chembl_id": "CHEMBL880",
      "max_phase": 4,
      "first_approval": "2004"
    }
  ]
}
```

## Clinical Trials Schema

```json
{
  "total_studies": 234,
  "studies": [
    {
      "nct_id": "NCT03704547",
      "title": "Study of osimertinib in EGFR-mutated NSCLC",
      "status": "Recruiting",
      "phase": "Phase 3",
      "start_date": "2018-11-01",
      "interventions": [
        "Osimertinib",
        "Chemotherapy"
      ]
    }
  ],
  "phase_distribution": {
    "phase_1": 45,
    "phase_2": 89,
    "phase_3": 67,
    "other": 33
  }
}
```

## Combined Target Profile Schema

```json
{
  "target": {
    "symbol": "EGFR",
    "name": "Epidermal growth factor receptor",
    "uniprot_id": "P00533",
    "ensembl_id": "ENSG00000146648",
    "chembl_id": "CHEMBL240"
  },

  "overview": {
    "class": "Receptor tyrosine kinase",
    "location": "Cell membrane",
    "length": 1210,
    "mass_kda": 134.3
  },

  "druggability": {
    "small_molecule_score": 8.2,
    "antibody_score": 7.8,
    "tdl": "Tclin",              // Target Development Level
    "summary": "High tractability with clinical precedence"
  },

  "diseases": [
    {
      "name": "Lung adenocarcinoma",
      "id": "EFO_0005568",
      "association_score": 0.95,
      "evidence": "Genetic association"
    }
  ],

  "pathways": [
    {
      "id": "hsa04012",
      "name": "ErbB signaling pathway",
      "database": "KEGG"
    }
  ],

  "competition": {
    "approved_drugs": 9,
    "pipeline_count": 34,
    "leading_companies": ["AstraZeneca", "Roche", "Boehringer"]
  },

  "safety": {
    "tier": 2,
    "known_toxicities": [
      "Skin rash",
      "Diarrhea"
    ],
    "summary": "Moderate safety risk"
  }
}
```

## Field Value Enums

### Target Development Level (TDL)
- `Tclin` - Clinical precedence (approved drugs)
- `Tchem` - Chemical precedence (bioactive compounds)
- `Tbio` - Biological target (characterized biology)
- `Tdark` - Limited knowledge

### Safety Tier
- `1` - Low risk (well characterized)
- `2` - Moderate risk (some concerns)
- `3` - High risk (significant safety issues)
- `4` - Critical risk (serious safety concerns)

### Tractability Score Ranges
| Score Range | Description |
|-------------|-------------|
| 8.0-10.0 | High tractability |
| 5.0-7.9 | Moderate tractability |
| 1.0-4.9 | Challenging |
| 0.0-0.9 | Not tractable |

## Validation Rules

1. **Gene symbol**: Must be valid HGNC symbol (2-10 uppercase letters/numbers)
2. **Ensembl ID**: Must match pattern `ENSG\d{11}`
3. **UniProt ID**: Must match pattern `[A-Z0-9]{6}` or `[A-Z0-9]{10}`
4. **ChEMBL ID**: Must match pattern `CHEMBL\d+`
5. **Association score**: Must be between 0 and 1

## Error Response Schema

```json
{
  "error": {
    "code": "TARGET_NOT_FOUND",
    "message": "Target 'INVALID' not found in Open Targets",
    "details": {
      "query": "INVALID",
      "suggestions": ["EGFR", "ERBB1", "HER2"]
    }
  }
}
```

## Common Error Codes

| Code | Description |
|------|-------------|
| `TARGET_NOT_FOUND` | Target not found in database |
| `INVALID_SYMBOL` | Invalid gene symbol format |
| `API_ERROR` | External API error |
| `RATE_LIMITED` | Rate limit exceeded |
| `TIMEOUT` | Request timeout |
