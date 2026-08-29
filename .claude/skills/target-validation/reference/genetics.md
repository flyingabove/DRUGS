# Genetic Validation Reference

Comprehensive reference for genetic evidence in target validation.

## Overview

Genetic validation uses human genetic data to establish causal relationships between targets and diseases. Human genetics is considered the **strongest predictor** of clinical success in drug development.

## Sources of Genetic Evidence

### 1. Mendelian Diseases

**Single gene disorders** provide definitive evidence:

| Evidence type | Strength | Example |
|---------------|----------|---------|
| Loss-of-function causes disease | High (inhibition) | PCSK9 → LDL lowering |
| Gain-of-function causes disease | High (activation) | EGFR → Lung cancer |
| Both LOF and GOF cause disease | Context-dependent | Not suitable |

**Interpretation rules**:
- LOF disease → **Inhibition** therapeutic strategy
- GOF disease → **Inhibition** therapeutic strategy
- Protective LOF → **Inhibition** therapeutic strategy
- Protective GOF → **Activation** therapeutic strategy

### 2. GWAS (Genome-Wide Association Studies)

**Population-level associations** identify disease-linked genes:

```
Study design: Case vs Control (or quantitative trait)
Output: Odds Ratio + P-value per SNP
```

| P-value | Significance |
|---------|--------------|
| < 5×10⁻⁸ | Genome-wide significant |
| < 1×10⁻⁵ | Suggestive |
| < 1×10⁻³ | Nominal |

**Key metrics**:
- **Odds Ratio (OR)**: Effect size
  - OR > 1: Risk allele
  - OR < 1: Protective allele
- **Allele Frequency**: Population relevance
- **Population**: Ancestry-specific effects
- **LD structure**: Causal gene identification

### 3. PheWAS (Phenome-Wide Association Studies)

**Reverse approach** - test genetic variant against all phenotypes:

| Application | Value |
|-------------|-------|
| Target repurposing | Same variant, different diseases |
| Safety assessment | Variant effects on other traits |
| Pleiotropy detection | Multiple phenotype effects |

### 4. eQTL (Expression QTL) Data

**Genetic regulation of gene expression**:

| Tissue | Resource |
|--------|----------|
| Multiple tissues | GTEx Project |
| Whole blood | eQTLGen, DICE (immune) |
| Disease-specific | TCGA, PsychENCODE |

**Interpretation**:
- **cis-eQTL**: Variant affects nearby gene (same locus)
- **trans-eQTL**: Variant affects distant gene (regulatory)

### 5. Somatic Mutations

**Cancer genetics** identifies oncogenic drivers:

| Evidence | Strength |
|----------|----------|
| Recurrent mutations | Strong selection |
| Hotspot mutations | Activating |
| Amplification | Overexpression |
| Fusion proteins | Novel targets |

## Functional Validation

### CRISPR Screens

**Genome-scale functional validation**:

| Screen type | Application |
|-------------|-------------|
| Whole-genome KO | Essential genes |
| Focused library | Pathway validation |
| CRISPRi/a | Gene dosage effects |
| Base editing | Point mutations |

**Hit criteria**:
- MAGeCK FDR < 0.05
- Multiple independent sgRNAs
- Replicate consistency
- Effect size (log2FC)

### Animal Models

**In vivo validation**:

| Model | Translatability |
|-------|-----------------|
| Mouse | High (mammalian) |
| Rat | High (physiology) |
| Zebrafish | Medium (vertebrate) |
| Drosophila | Low (invertebrate) |

**Validation criteria**:
- **Face validity**: Phenotype resembles disease
- **Construct validity**: Same mechanism
- **Predictive validity**: Same drug response

## Causal Inference Methods

### Mendelian Randomization

**Instrumental variable analysis** for causality:

```
Requirements:
1. Relevance: Variant strongly affects target
2. Independence: No confounder association
3. Exclusion: Only affects disease through target
```

| Method | Application |
|--------|-------------|
| Two-sample MR | Large GWAS datasets |
| Multivariable MR | Multiple targets |
| Bidirectional MR | Direction of causality |
| MR-Egger | Pleiotropy assessment |

### Colocalization Analysis

**Assess shared causal variant**:

| Method | Description |
|--------|-------------|
| COLOC | Bayesian colocalization |
| eCAVIAR | Credible set overlap |
| SMR/HEIDI | Test mediation |

**Posterior probability**:
- PP4 > 0.8: Likely shared variant
- PP4 < 0.5: Distinct signals

## Data Resources

### Primary Resources

| Resource | Content | URL |
|----------|---------|-----|
| GWAS Catalog | Published GWAS | ebi.ac.uk/gwas |
| GTEx | Tissue eQTLs | gtexportal.org |
| UK Biobank | Phenotype-genotype | ukbiobank.org |
| ClinVar | Clinical variants | ncbi.nlm.nih.gov/clinvar |
| dbGaP | Controlled access | dbgap.ncbi.nlm.nih.gov |
| Open Targets | Integrated platform | opentargets.org |

### Analysis Tools

| Tool | Purpose |
|------|---------|
| PLINK | GWAS analysis |
| FUMA | Functional mapping |
| MAGMA | Gene-set analysis |
| MR-Base | Mendelian randomization |
| Coloc | Colocalization |

## Interpretation Framework

### Evidence Integration

| Evidence type | Weight |
|---------------|--------|
| Mendelian | Highest |
| CRISPR + GWAS | High |
| GWAS only | Medium |
| eQTL only | Low |

### Confidence Levels

| Level | Criteria |
|-------|----------|
| Definitive | Mendelian + functional validation |
| Strong | GWAS significant + CRISPR validation |
| Moderate | GWAS suggest + expression correlation |
| Preliminary | GWAS nominal only |
| None | No genetic evidence |

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Population stratification | Adjust for PCs |
| Reverse causation | Use MR |
| Linkage disequilibrium | Fine-mapping |
| Winner's curse | Replication needed |
| Ancestry bias | Multi-ancestry studies |
