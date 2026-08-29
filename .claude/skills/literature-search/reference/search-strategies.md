# PubMed Search Strategies for Drug Discovery

Effective search strategies for literature review in pharmaceutical research.

## Building Effective Queries

### 1. Start with Core Concepts

Identify 2-4 key concepts for your search:

**Example:** EGFR resistance mechanisms
- Concept 1: EGFR (target)
- Concept 2: resistance (phenomenon)
- Concept 3: NSCLC (disease - optional)

```bash
# Core query
EGFR AND resistance
```

### 2. Add Specificity with Field Tags

```bash
# Focus on title/abstract
EGFR[Title/Abstract] AND resistance[Title/Abstract]

# Include disease context
EGFR[Title/Abstract] AND resistance[Title/Abstract] AND NSCLC[Title/Abstract]
```

### 3. Use MeSH Terms

```bash
# Combine free text with MeSH
("Epidermal Growth Factor Receptor"[MeSH] OR EGFR[Title/Abstract]) AND
("Drug Resistance"[MeSH] OR resistance[Title/Abstract])
```

### 4. Include Synonyms

```bash
# Comprehensive query
(EGFR OR "epidermal growth factor receptor" OR "ERBB1" OR HER1) AND
(resistance OR "refractory" OR "relapse" OR "progression")
```

## Disease-Specific Strategies

### Oncology

| Goal | Query Template |
|------|----------------|
| Target validation | `{TARGET}[Title/Abstract] AND ({CANCER_TYPE}[MeSH] OR {CANCER_TYPE}[Title/Abstract])` |
| Drug efficacy | `{DRUG}[Title/Abstract] AND {CANCER_TYPE}[Title/Abstract] AND (response OR efficacy OR survival)` |
| Resistance | `{TARGET}[Title/Abstract] AND (resistance[Title/Abstract] OR refractory[Title/Abstract])` |
| Biomarker | `{BIOMARKER}[Title/Abstract] AND (predictive[Title/Abstract] OR biomarker[Title/Abstract])` |

### Neurology

| Goal | Query Template |
|------|----------------|
| Disease mechanism | `{DISEASE}[MeSH] AND (pathogenesis[Title/Abstract] OR mechanism[Title/Abstract])` |
| Treatment | `{DISEASE}[MeSH] AND (therapy[MeSH] OR treatment[Title/Abstract])` |
| Clinical trials | `{DISEASE}[MeSH] AND clinical trial[Publication Type]` |

### Immunology

| Goal | Query Template |
|------|----------------|
| Immunotherapy | `{TARGET}[Title/Abstract] AND (immunotherapy[Title/Abstract] OR "checkpoint inhibitor"[Title/Abstract])` |
| Cytokines | `{CYTOKINE}[Title/Abstract] AND (inflammation[Title/Abstract] OR immune[Title/Abstract])` |

## Drug-Specific Strategies

### Small Molecules

```bash
# Generic name + brand
(generic_name[Title/Abstract] OR brand_name[Title/Abstract])

# Add mechanism
({DRUG}[Title/Abstract] AND inhibitor[Title/Abstract])

# Add class
({DRUG}[Title/Abstract] AND "kinase inhibitor"[Title/Abstract])
```

### Biologics

```bash
# Antibodies
({DRUG}[Title/Abstract] AND (antibody[Title/Abstract] OR mAb[Title/Abstract]))

# Specific format
({DRUG}[Title/Abstract] AND monoclonal[Title/Abstract])
```

### Novel Modalities

| Modality | Query Example |
|----------|---------------|
| PROTAC | `PROTAC[Title/Abstract] AND {TARGET}[Title/Abstract]` |
| ADC | `("antibody-drug conjugate"[Title/Abstract] OR ADC[Title/Abstract]) AND {TARGET}[Title/Abstract]` |
| CAR-T | `"CAR-T"[Title/Abstract] AND {TARGET}[Title/Abstract]` |
| Bispecific | `bispecific[Title/Abstract] AND {TARGET}[Title/Abstract]` |
| RNAi | `(siRNA[Title/Abstract] OR RNAi[Title/Abstract]) AND {TARGET}[Title/Abstract]` |

## Time-Based Strategies

### Recent Literature (1-2 years)

```bash
# Last 12 months
{QUERY} AND ("2023/01/01"[PDAT]:"2024/12/31"[PDAT])

# Last 2 years (using reldate)
{QUERY} AND reldate=730
```

### Historical Context

```bash
# Landmark papers
{QUERY} AND ("2010"[PDAT]:"2020"[PDAT])

# First reports
{QUERY} AND ("2000"[PDAT]:"2010"[PDAT])
```

## Publication Type Filters

### Clinical Focus

```bash
# Only clinical trials
{QUERY} AND clinical trial[Publication Type]

# Phase III only
{QUERY} AND ("Phase III"[Title/Abstract] OR "phase 3"[Title/Abstract])

# Randomized controlled trials
{QUERY} AND randomized[Title/Abstract]
```

### Review Articles

```bash
# All review types
{QUERY} AND review[Publication Type]

# Systematic reviews
{QUERY} AND ("systematic review"[Title/Abstract] OR meta-analysis[Title/Abstract])
```

### Preclinical

```bash
# Animal studies
{QUERY} AND (animal[Title/Abstract] OR mouse[Title/Abstract] OR murine[Title/Abstract])

# In vitro
{QUERY} AND ("in vitro"[Title/Abstract] OR cell[Title/Abstract])
```

## Combination Search Strategies

### Drug Combinations

```bash
# Two drugs together
({DRUG1}[Title/Abstract] AND {DRUG2}[Title/Abstract])

# Combination therapy
({DRUG}[Title/Abstract] AND combination[Title/Abstract])

# Specific combination format
({DRUG1}[Title/Abstract] AND {DRUG2}[Title/Abstract] AND (combo* OR combination))
```

### Target + Disease

```bash
# Direct association
({TARGET}[Title/Abstract] AND {DISEASE}[Title/Abstract])

# With outcome
({TARGET}[Title/Abstract] AND {DISEASE}[Title/Abstract] AND (survival[Title/Abstract] OR outcome[Title/Abstract]))
```

## Exclusion Strategies

### Remove Unwanted Topics

```bash
# Exclude specific cancer types
{QUERY} NOT (prostate[Title/Abstract] OR breast[Title/Abstract])

# Exclude animal studies
{QUERY} NOT animal[Title/Abstract]

# Exclude reviews (for primary research)
{QUERY} NOT review[Publication Type]
```

### Focus on Human Studies

```bash
# Humans only
{QUERY} AND human[Title/Abstract]

# Explicitly exclude animals
{QUERY} AND human[Title/Abstract] NOT animal[Title/Abstract]
```

## Query Templates by Use Case

### Competitive Intelligence

```bash
# Pipeline scanning
({TARGET}[Title/Abstract] AND (clinical[Title/Abstract] OR trial[Title/Abstract]))

# Recent developments
({TARGET}[Title/Abstract] AND ("2023"[PDAT]:3000[PDAT]))
```

### Target Validation

```bash
# Genetic evidence
({TARGET}[Title/Abstract] AND (mutation[Title/Abstract] OR variant[Title/Abstract] OR polymorphism[Title/Abstract]))

# Disease association
({TARGET}[Title/Abstract] AND {DISEASE}[Title/Abstract] AND (association[Title/Abstract] OR correlation[Title/Abstract]))
```

### Safety Assessment

```bash
# Toxicity
({DRUG}[Title/Abstract] AND (toxicity[Title/Abstract] OR adverse[Title/Abstract] OR safety[Title/Abstract]))

# Side effects
({DRUG}[Title/Abstract] AND ("side effect"[Title/Abstract] OR toxicity[Title/Abstract]))
```

### Mechanism of Action

```bash
# Pathway analysis
({TARGET}[Title/Abstract] AND (pathway[Title/Abstract] OR signaling[Title/Abstract]))

# Binding studies
({DRUG}[Title/Abstract] AND (binding[Title/Abstract] OR affinity[Title/Abstract]))
```

## Search Optimization Tips

1. **Iterate**: Start broad, then refine
2. **Check counts**: Too many (>1000) = narrow; too few (<20) = broaden
3. **Use filters**: Apply after initial search
4. **Review terms**: Check MeSH for relevant terms
5. **Save strategies**: Document successful queries
6. **Set alerts**: Use for ongoing monitoring

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Too broad | Add specific terms or date limits |
| Too narrow | Remove filters or add synonyms |
| Missing recent papers | Check date range, use `reldate` |
| Wrong nomenclature | Check for gene/protein name synonyms |
| Mixed species | Explicitly add `human[Title/Abstract]` |
