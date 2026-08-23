# AML Post-Treatment LSC-Targeted Drug Discovery — Experimental Plan

Status: DRAFT — working document, decision points marked `[DECIDE]`

## 1. Problem Statement

Standard-of-care AML treatment (7+3 induction ± consolidation, venetoclax/azacitidine, allo-HSCT,
FLT3/IDH inhibitors where applicable) achieves morphologic complete remission (CR) in most patients,
but a rare, chemo-resistant leukemic stem cell (LSC) population survives as measurable residual
disease (MRD). These "persister" LSCs reconstitute the leukemia and drive relapse — the dominant
cause of AML treatment failure.

**Goal:** design a therapeutic that selectively eliminates post-treatment residual LSCs while
sparing normal hematopoietic stem cells (HSCs), using an AI/ML-driven discovery pipeline validated
through in vitro and in vivo preclinical models.

**Key distinction from "diagnosis LSC" targeting:** the LSC population that survives chemo is not
identical to the bulk LSC population at diagnosis — it is chemo-selected/enriched for a resistant,
often quiescent, "persister" phenotype. The target hypothesis should be built from post-treatment /
MRD-state biology, not just diagnosis-state LSC biology.

## 2. Biological Rationale — Why LSCs Survive Treatment

Mechanisms to build the target hypothesis around:

- **Quiescence** — G0 cell-cycle arrest evades S-phase-dependent cytotoxics (cytarabine, anthracyclines).
- **Niche protection** — bone marrow endosteal/perivascular niche adhesion (CXCR4/CXCL12, VLA-4/VCAM-1)
  shields LSCs and can be pharmacologically disrupted (e.g., plerixafor mobilization strategies).
- **Metabolic rewiring** — LSCs disproportionately depend on oxidative phosphorylation (OXPHOS) rather
  than glycolysis; this is the mechanistic basis for venetoclax (BCL-2i) + azacitidine efficacy.
- **Anti-apoptotic dependence** — BCL-2/MCL-1 overexpression raises the apoptotic threshold.
- **Efflux transporters** — ABCB1/ABCG2 pump out chemotherapeutics.
- **Epigenetic plasticity / dormancy programs** — reversible transcriptional states, not fixed mutations,
  can confer transient drug tolerance (the "persister cell" paradigm from solid-tumor drug resistance
  literature, increasingly applied to AML).
- **Immune evasion** — CD47 ("don't eat me") upregulation blocks macrophage clearance.

`[DECIDE]` Which mechanism(s) should the target hypothesis center on? Options and rationale below.

## 3. Candidate Target Classes

| Target | Biology | Clinical precedent | Selectivity concern |
|---|---|---|---|
| CD123 (IL3RA) | LSC-enriched surface marker, IL-3 signaling | Tagraxofusp, talacotuzumab, flotetuzumab, IMGN632 | Low-level normal HSC/progenitor expression |
| CLL-1 (CLEC12A) | LSC-specific, largely absent on normal HSC | CAR-T and ADC programs in trials | Better normal-HSC sparing profile than CD123 |
| CD47 | "Don't eat me" signal, innate immune evasion | Magrolimab | Pan-hematopoietic expression (RBC/platelet toxicity risk) |
| BCL-2 / MCL-1 | Anti-apoptotic, OXPHOS-linked survival | Venetoclax (approved) | Already targeted; differentiate via combination or MCL-1 |
| Menin–KMT2A interaction | Transcriptional dependency in KMT2A-r / NPM1-mut AML | Revumenib (approved 2024) | Genotype-restricted, not universal |
| DRD2 | Unexpectedly required for LSC self-renewal | Preclinical / early trials | Off-target CNS effects |
| GPR56 (ADGRG1) | LSC self-renewal regulator | Preclinical | Emerging, less validated |
| OXPHOS complex I (e.g., via IACS-010759-class) | Direct metabolic vulnerability | Preclinical, some toxicity issues | Narrow therapeutic index seen historically |

`[DECIDE]` Pick a primary target (or a dual-target/combination strategy) to scope Phase 0 data pulls
around. Recommendation: CLL-1 or a CD123×CLL-1 dual-targeting logic gate for surface-antigen selectivity,
paired with an OXPHOS/BCL-2-family vulnerability for the "persister-state" mechanism — but this should
be settled after Phase 0 differential analysis, not assumed up front.

## 4. Data Sources

- **Beat AML** (Tyner et al.) — ex vivo drug sensitivity + multi-omics across primary AML samples.
- **TCGA-LAML** — bulk genomic/transcriptomic AML cohort.
- **van Galen et al. 2019 (Cell)** — single-cell RNA-seq AML atlas defining malignant cell states
  and the **LSC17** prognostic gene signature.
- **Human Cell Atlas / normal BM scRNA-seq** — required as the normal-HSC comparator for selectivity
  filtering (this is the step that prevents designing another "CD123-but-still-toxic" molecule).
- **DepMap** — CRISPR essentiality screens to check target dependency and normal-tissue fitness cost.
- **Post-MRD paired samples** (diagnosis vs. post-induction residual disease, same patient) — the
  single most important dataset to source; needed to distinguish "persister LSC" biology from bulk
  diagnosis LSC biology. `[DECIDE/RESEARCH]` identify specific cohorts with paired pre/post-treatment
  scRNA-seq (e.g., MRD flow-sorted residual blast studies).

## 5. End-to-End Pipeline

### Phase 0 — Target Discovery & Prioritization (computational, data-only)
1. Differential expression: post-treatment residual LSC vs. diagnosis LSC vs. normal HSC (CD34+CD38-).
2. Rank candidates by: LSC-enrichment fold-change, normal-HSC low/absent expression, DepMap
   essentiality in AML lines, druggability (surface protein vs. enzyme vs. PPI).
3. Output: ranked target shortlist (3-5 candidates) with a written selectivity rationale each.
4. **Gate:** don't proceed to structure/generative work until a target is chosen and its selectivity
   window is quantified, not assumed.

### Phase 1 — Structural Biology
1. Pull experimental structures (PDB) where available; else predict with AlphaFold2/RoseTTAFold.
2. Pocket/interface detection (for small molecule: binding pocket; for biologic: epitope mapping).
3. Validate predicted structure confidence (pLDDT) in the relevant functional domain.

### Phase 2 — Generative Candidate Design
1. Choose modality first — small molecule vs. antibody/ADC vs. bispecific vs. CAR-T-adjacent —
   since target class (surface antigen vs. intracellular protein/PPI) constrains this.
2. Small-molecule route: generative model (VAE / diffusion / transformer-on-SMILES) proposes
   candidates conditioned on the target pocket; RL fine-tuning rewards predicted binding affinity,
   drug-likeness (QED), synthesizability (SA score).
3. Biologic route: structure-conditioned design (e.g., RFdiffusion/ProteinMPNN-style) for binder
   generation against the mapped epitope.
4. Output: ranked in-silico candidate library (thousands → hundreds after generation).

### Phase 3 — Virtual Screening & Triage
1. Docking / binding-affinity re-scoring on generated candidates.
2. ADMET prediction (absorption, distribution, metabolism, excretion, toxicity) to cut early failures.
3. Selectivity filter: predicted affinity for target vs. close paralogs/normal-tissue targets.
4. Output: 10-50 synthesizable candidates for wet-lab entry.

### Phase 4 — In Vitro Validation
1. Source primary AML patient samples (post-treatment MRD-state cells where possible) + normal
   CD34+ HSC controls (cord blood/BM).
2. Assays: colony-forming unit (CFU), long-term culture-initiating cell (LTC-IC) assay for
   self-renewal, flow cytometry for LSC marker/apoptosis readout (Annexin V), selectivity index
   (LSC kill vs. normal HSC kill).
3. Mechanism confirmation: does the candidate actually engage the intended target/pathway
   (e.g., target knockdown phenocopy, pathway biomarker readout)?
4. **Gate:** require a clear in vitro selectivity index before in vivo commitment.

### Phase 5 — In Vivo Validation
1. Patient-derived xenograft (PDX) model, ideally modeling the **post-treatment MRD state**
   specifically (e.g., treat engrafted mice with standard induction first, then dose the
   candidate against residual disease) — this mirrors the actual clinical use case rather than
   testing against bulk untreated leukemia.
2. Endpoints: residual leukemic burden, leukemia-initiating capacity on serial re-transplantation
   (the gold-standard functional LSC readout), survival, normal hematopoiesis toxicity.

### Phase 6 — Combination & Translational Positioning
1. Test candidate as a consolidation/maintenance therapy layered on top of standard induction,
   not as monotherapy replacement — consistent with how it would actually be used clinically.
2. Define the biomarker strategy for patient selection (does the target need to be confirmed
   present in a patient's residual MRD clone before treatment?).

## 6. Success Metrics

- Phase 0: selectivity ratio (LSC vs. normal HSC expression) ≥ some threshold `[DECIDE threshold]`.
- Phase 3: top candidates pass ADMET + synthesizability filters, docking score within target range.
- Phase 4: selectivity index (normal HSC IC50 / LSC IC50) — precedent therapies target >5-10x.
- Phase 5: reduction in serial-transplant leukemia-initiating capacity without HSC ablation.

## 7. Key Risks

- **LSC heterogeneity** — no single marker covers all patients/genotypes; may need biomarker-stratified
  approach or combination targeting.
- **Selectivity window** — LSCs and normal HSCs share substantial biology; this is the single biggest
  historical failure mode (e.g., OXPHOS inhibitors hitting normal HSC fitness).
- **In vitro→in vivo→clinic translation gap** — PDX models don't fully recapitulate human BM niche.
- **Data scarcity** — paired pre/post-treatment MRD-state single-cell data is limited; Phase 0 may need
  to proceed with proxy data (e.g., relapse-vs-diagnosis pairs) if true MRD-timepoint data isn't available.

## 8. Open Decisions Before Starting Phase 0

1. Primary target class (Section 3).
2. Modality (small molecule vs. biologic) — depends on #1.
3. Which post-treatment/MRD dataset to anchor "persister" biology on (Section 4).
4. Scope: single-target vs. dual-target/combination strategy from the outset.

---
*This is a research-planning document for a computational discovery exercise, not a clinical or
manufacturing protocol.*
