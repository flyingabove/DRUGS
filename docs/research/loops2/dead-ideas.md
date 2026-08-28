# Dead Ideas — Track 2 (Differentiation / Maturation)

Graveyard for the **differentiation-based** idea track. One line of what, one line of why it died.
**Read this before proposing anything.**

Track 1 (ferroptosis/GPX4) has its own graveyard at [../loops/dead-ideas.md](../loops/dead-ideas.md)
— **read that too**; several ideas were already killed there and must not be re-proposed here.

Format: `IDEA — KILLED BY: reason`

---

## Killed on novelty (already exists)

- **MECOM/EVI1–CTBP2 interaction inhibitor** (loop 12) — EXISTS: *"Oncogene EVI1 drives acute myeloid
  leukemia via a targetable interaction with CTBP2"* (bioRxiv 2023 → published 2024). The exact
  synthesis I was converging on. Caught at loop 12, not loop 40.
- **EVI1 targeting generally** — CROWDED FIELD: pyrrole-imidazole polyamide vs the N-terminal zinc
  finger; **NICE-01** (AP1867-PEG2-JQ1) bifunctional BRD4-recruiting EVI1 degrader; BET inhibitors
  suppress EVI1; **tegavivint** disrupts EVI1–TBL1; PA2G4–MYC axis in 3q26 AML. Multiple independent
  programs. No room.

## Killed on selectivity (hits normal cells too)

- **MECOM/EVI1 depletion or degradation** (loop 9) — KILLED BY: *"Evi1 is essential for hematopoietic
  stem cell self-renewal."* **Heterozygosity alone** markedly impairs LT-HSC self-renewal, and EVI1 is
  expressed predominantly *in* LT-HSCs. Same failure class as LSD1/HMG20B in track 1. A dose window
  may exist (leukemia has out-of-context enhancer-driven overexpression vs. normal baseline) but it
  is narrow and unquantified.

## Killed on mechanism (the premise was wrong / inverted)

- **IRF8 blockade to steer monocyte→neutrophil** (loop 53) — KILLED BY: Hartung et al., *Blood* 2024.
  In *Irf8*-KO AML cells the **ATRA IC50 rose 151-fold** (47 nM → 7.1 µM) and LSD1-inhibitor IC50 rose
  9.7-fold. **IRF8 loss makes AML more resistant to differentiation therapy**, not better steered —
  IRF8 is required for the differentiation *response*, not only the fate *choice*. You cannot steer
  the car by removing the engine.
  - Secondary strike: germline *Irf8*-null mice develop a **CML-like MPN at 10–16 weeks** with blast
    crisis in ~⅓. Chronic deep IRF8 loss is oncogenic.
  - *Survives as: the cautionary case. The C/EBPγ pivot tilts the same ratio from the opposite side
    and dodges both problems.*
- **Pan-C/EBP dominant negative (A-C/EBP class)** — KILLED BY: inhibits the **whole C/EBP family**,
  including C/EBPα — which would ablate the very differentiation the strategy depends on. Only a
  **γ-selective** version is viable; that selectivity is the core design risk.

## Demoted, not dead

- **Eosinophil escape / IL5RA / benralizumab** (loops 21–28, demoted loop 31) — The eosinophil
  persister lineage is a **mouse** finding; human patients on revumenib show **monocytic** enrichment
  instead. Retains the **cleanest lineage-marker selectivity in the project** (*"IL5RA… absent from
  normal HSCs and multipotent progenitors,"* expressed only after eosinophil commitment) and 4+ years
  of human eosinophil-depletion safety with *"no evidence of increased infection risk or immunologic
  compromise."* **Revive if human eosinophilic escape is ever demonstrated.**
  - Partial novelty hit: *"Preliminary Effects of Benralizumab in an AML Cell Model with Promyelocytic
    Features Expressing IL-5R"* exists — but HL-60 only, exploratory, and about direct anti-leukemic
    signalling, **not** about clearing therapy-induced persisters.
- **MTL-CEBPA (saRNA raising CEBPA)** — EXISTS AND ALREADY IN AML: *"RNA activation of CEBPA improves
  leukemia treatment"* (2025) — boosts CEBPA, promotes a *"non-proliferative, mature state"* in
  FLT3-mutant AML, synergizes with gilteritinib in vivo. **Novelty hit on the repurposing route**, but
  framed as maturation, not lineage steering. Best *fast* fallback and a possible combination partner.
- **ZMYND8** — upstream regulator of the IRF8–MEF2D circuit; ablation abrogates AML proliferation
  in vivo and improves xenograft survival. Bromodomain-containing (well-precedented target class) but
  **no selective chemical probe exists**.
- **G-CSF as the lineage steer** — works (*ATRA+G-CSF → neutrophils*) but signals through G-CSFR,
  which AML blasts express; a **proliferative** signal whose AML use is *"controversial due to a
  theoretically increased risk of relapse."* The obvious move, and the reason a cell-intrinsic
  non-mitogenic steer is worth designing.

## Killed on tool-compound validity

- **MSI2 / Musashi-2 via Ro 08-2750** (loop 6) — KILLED BY: *"Small-molecule Ro-08-2750 interacts with
  many RNA-binding proteins and elicits MUSASHI2-independent phenotypes"* (RNA, Oct 2023). Ro is a
  **promiscuous RBP binder**; its viability phenotypes are MSI2-independent, and it induces stress
  granules — wholesale RBP disruption. **Third instance of tool-compound misattribution in this
  project** (after RSL3/ML162 and imetelstat). The MSI2 *target* is not disproven; the *tool* is
  worthless, so nothing built on Ro-08-2750 data can be trusted.
  - Secondary strike: *"MSI2 protein levels are higher in dividing and recently divided leukemic
    cells"* — wrong population. Our target is dormant.

## Structural lessons — track 2 additions

*(Track 1's five lessons still apply and are not repeated here.)*

6. **Quiescence is a chromatin lock, not just a cell-cycle state.** A hallmark of quiescence is *vast
   histone deacetylation and chromatin compaction*, with global narrowing of nucleosome-depleted
   regions and a repressive chromatin environment. **Any reprogramming or differentiation agent must
   first get the chromatin open** — pioneer factors need accessible enhancers. This is the central
   structural obstacle for the entire differentiation strategy, and it predicts that a
   chromatin-opening partner agent is mandatory, not optional.
7. **Differentiation therapy is a crowded graveyard above the LSC line.** ATRA/ATO (APL only), IDH1/2
   inhibitors, menin inhibitors, DHODH inhibitors, LSD1 inhibitors have all been tried. Any new entry
   must explain why it reaches the *dormant* compartment specifically — that is where the field's
   failures concentrate, and it is our stated target population.
