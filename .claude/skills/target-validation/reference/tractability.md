# Target Tractability Assessment

Comprehensive reference for assessing target tractability.

## Overview

**Tractability** assesses the feasibility of developing a therapeutic modality against a target. Not all targets are equally druggable.

## Tractability Classes

### Open Targets Classification

| Class | Description | Examples |
|-------|-------------|----------|
| **Class A** | Highly tractable, small molecule | Kinases, GPCRs, Ion channels |
| **Class B** | Tractable with challenges | Protein-protein interactions |
| **Class C** | Emerging approaches | Transcription factors, RNA |
| **Class D** | Challenging, novel modalities | Scaffolding proteins, non-enzymatic |

## Tractability Dimensions

### 1. Structural Tractability

**Binding site characteristics**:

| Feature | Tractable | Challenging |
|---------|-----------|-------------|
| Pocket depth | Deep, buried | Shallow, surface |
| Pocket volume | 300-800 Å³ | <100 or >1500 Å³ |
| Hydrophobicity | Mixed polar/apolar | Highly polar or hydrophobic |
| Flexibility | Rigid | Highly flexible |

**Assessment methods**:
- X-ray crystallography
- Cryo-EM
- NMR
- Computational pocket detection (FTMap, SiteMap)

### 2. Cellular Location

**Subcellular accessibility**:

| Location | Small Molecule | Biologic | RNA |
|----------|----------------|----------|-----|
| Cell surface | ✓ | ✓ | ✓ |
| Cytoplasm | ✓ | ✗ | ✓ |
| Nucleus | ✓ | ✗ | ✓ |
| Extracellular | ✓ | ✓ | ✓ |
| Mitochondria | △ | ✗ | ✓ |
| ER lumen | △ | ✗ | ✗ |

### 3. Ligandability

**Historical success rates**:

| Target class | Success rate | Tractability |
|--------------|--------------|--------------|
| Kinases | 25% | High |
| GPCRs | 30% | High |
| Ion channels | 20% | High |
| Proteases | 15% | Medium |
| Nuclear receptors | 35% | High |
| Transporters | 10% | Medium |
| PPIs | 5% | Low |
| Transcription factors | <2% | Very Low |

### 4. Assayability

**Developability of screening assays**:

| Assay type | Feasibility | Readout |
|------------|-------------|---------|
| Biochemical | High | Enzyme activity |
| Binding | High | SPR, ITC, NMR |
| Cellular | Medium | Reporter, viability |
| Phenotypic | Low | Complex readouts |
| In vivo | Low | Animal models |

## Modality-Specific Tractability

### Small Molecules

**Requirements**:
- Well-defined binding pocket
- Drug-like physicochemical properties
- Synthetic accessibility

| Assessment metric | Threshold |
|-------------------|-----------|
| Pocket depth | >8 Å |
| Pocket volume | >200 Å³ |
| Druggability score (Dscore) | >0.8 |

### Biologics (Antibodies)

**Requirements**:
- Extracellular or cell surface location
- Accessible epitope
- Immunogenic surface

| Assessment metric | Threshold |
|-------------------|-----------|
| Surface accessibility | >30% |
| Epitope size | >15 Å |
| Membrane proximity | <20 Å |

### PROTACs

**Requirements**:
- Ligand for target
- Ligand for E3 ligase
- Suitable linker geometry

| Assessment metric | Threshold |
|-------------------|-----------|
| Ternary complex formation | Observable |
| Degradation potency | DC50 < 100 nM |
| Hook effect | Minimal |

### RNA Therapeutics

**Requirements**:
- Accessible RNA sequence
- Minimal secondary structure
- Tissue-specific delivery

| Assessment metric | Threshold |
|-------------------|-----------|
| Sequence accessibility | High |
| Conservation | Species-specific |
| Off-target potential | Low |

### Gene Therapy

**Requirements**:
- Genetic causality established
- Tissue-specific delivery
- Acceptable safety profile

| Assessment metric | Threshold |
|-------------------|-----------|
| Genetic validation | Definitive |
| Tissue tropism | Defined |
| Immune response | Manageable |

## Computational Assessment

### Pocket Detection

**Tools and algorithms**:

| Tool | Algorithm | Output |
|------|-----------|--------|
| FTMap | Fragment mapping | Hot spots |
| SiteMap | Grid-based | Druggability score |
| DoGSiteScorer | Pocket detection | Volume, depth |
| PockDrug | ML-based | Druggability probability |

**Key metrics**:
- **Dscore**: >0.8 (druggable), 0.5-0.8 (borderline), <0.5 (undruggable)
- **Volume**: 200-800 Å³ (optimal)
- **Hydrophobicity**: Mixed (not too polar, not too hydrophobic)

### Molecular Dynamics

**Assess flexibility and binding**:

| Application | Method |
|-------------|--------|
| Pocket stability | RMSD analysis |
| Cryptic pockets | MD with enhanced sampling |
| Water networks | WaterMap, GIST |

## Family-Based Assessment

### Kinases

**Tractability**: **Very High**

| Feature | Assessment |
|---------|------------|
| ATP pocket | Conserved, druggable |
| Allosteric sites | Variable |
| Selectivity | Challenging (kinome-wide) |
| Structures | >10,000 PDB entries |

### GPCRs

**Tractability**: **Very High**

| Feature | Assessment |
|---------|------------|
| Orthosteric site | Druggable |
| Allosteric sites | Emerging |
| Structures | 500+ PDB entries |
| Subtype selectivity | Feasible |

### Ion Channels

**Tractability**: **High**

| Feature | Assessment |
|---------|------------|
| Pore block | Tractable |
| State dependence | Feasible |
| Structures | Improving (Cryo-EM) |
| Selectivity | Challenging |

### Protein-Protein Interactions

**Tractability**: **Variable**

| PPI type | Tractability |
|----------|--------------|
| Helix-helix | Medium (stapled peptides) |
| Small domain | Low (mimetics) |
| Large interface | Very Low |
| Transient | Low |

## Tractability Reporting Template

```markdown
## Tractability Assessment

| Dimension | Score | Details |
|-----------|-------|---------|
| Class | A | Kinase, well-characterized |
| Binding site | A | ATP pocket, drug-like |
| Location | A | Cell surface (TKI) |
| Assayability | A | Biochemical, cellular |
| Selectivity | B | Kinome-wide selectivity needed |

**Overall Tractability**: Highly tractable (Class A)
```

## References

1. Frankson LA, et al. *Nat Rev Drug Discov* 2023 - "Druggable genome"
2. Hu Y, et al. *Nat Rev Drug Discov* 2020 - "Open Targets platform"
3. Arrowsmith CH, *Nat Rev Drug Discov* 2015 - "Druggable genome"
4. Vollers S, et al. *Nat Rev Drug Discov* 2021 - "Ligandability assessment"
