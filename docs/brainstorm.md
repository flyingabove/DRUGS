# Brainstorm / Exploratory Notes

Informal running notes from the planning conversation — biology fundamentals covered so far,
and reasoning threads that aren't formal decisions yet. See
[aml-lsc-drug-discovery-plan.md](aml-lsc-drug-discovery-plan.md) for the structured plan this feeds into.

## Biology Primer (fundamentals covered)

- **Protein** — a molecule made of a chain of amino acids that folds into a specific 3D shape;
  that shape determines its job (a machine doing chemistry, a structural beam, a switch, or a
  lock/dock on the cell surface).
- **Amino acid** — the individual building block ("bead") proteins are made of. 20 standard types,
  each with a different variable chemical group, which is why sequence determines fold shape.
  DNA → amino acid sequence (the recipe, read out in order) → folded protein (the built tool).
- **Cell composition** — a cell is not "basically all protein." Rough breakdown:
  - Membrane (outer wall) = lipids (fats), with protein "gates/docks" embedded in it.
  - DNA = master blueprint, locked in the nucleus, made of a different molecule (nucleotides,
    not amino acids).
  - RNA = disposable working copies of DNA pages, sent out to be read.
  - Proteins = the machines/workers/structural beams built from those RNA instructions.
  - Carbohydrates/fats = fuel + surface tags; water = the medium everything sits in.
  - Takeaway: proteins dominate the *machinery and structure doing active work*, which is why
    drug targets and cancer-driving mutations almost always come down to a malfunctioning protein
    — but they're not the whole cell.

## Why target selection is the hard part for LSCs specifically

Leukemic stem cells (LSCs) closely resemble normal hematopoietic stem cells (HSCs). A drug that
can't distinguish them wipes out the patient's normal blood-making system along with the cancer.
The entire target-picking exercise (plan doc, Section 3) is about finding a real, exploitable
*difference* between LSC and normal HSC biology — not just something LSCs have, but something
they have that normal HSCs largely don't.

## Two target "kinds," and why that constrains the drug type

- **Surface markers (CLL-1, CD123)** — proteins poking through the outer cell membrane, acting as
  docks. To hit these you need something that recognizes the *outside* of the cell — a biologic
  (antibody, antibody-drug conjugate, bispecific, CAR-T).
- **Internal survival switches (BCL-2, MCL-1)** — proteins inside the cell that block
  self-destruction. To hit these you need something small enough to get *inside* the cell and jam
  an internal pocket — a small molecule.
- These require fundamentally different drug-building technology. You can't easily fuse a
  membrane-recognizing biologic and a cell-penetrating small molecule into one drug object.

## The CLL-1 + BCL-2/MCL-1 combination idea

Prompted by: "why don't people try CLL-1 and BCL-2/MCL-1 together?"

- Because of the modality mismatch above, "combining" them in practice means **two separate drugs
  given together as a regimen**, not one designed molecule doing both jobs.
- This is not a novel idea in the abstract — it's the same logic already validated by
  **venetoclax (BCL-2 inhibitor) + azacitidine**, current standard of care for AML patients who
  can't tolerate intensive chemo. Attack the survival mechanism from two angles at once.
- There are active trials combining venetoclax with CD123-targeted biologics (ADCs, bispecifics,
  CAR-T); CLL-1-targeted equivalents exist but are earlier-stage / less mature than CD123 ones,
  which is part of why this exact pairing (CLL-1 + BCL-2) isn't yet a standard combo — the CLL-1
  side of it just hasn't caught up clinically.
- **MCL-1 caution:** MCL-1 inhibitors (e.g., AMG 176, AZD5991) have hit cardiac toxicity signals
  in clinical trials — MCL-1 is also needed for normal heart muscle cell survival, not just cancer
  cell survival. This is a real, still-unresolved obstacle and leans the project toward **BCL-2**
  over MCL-1 as the survival-switch target, at least as the starting point.

## Tentative direction (not yet locked into the formal plan)

A combination-regimen framing: an **anti-CLL-1 biologic** (identifies/flags the LSC-specific
population) **+ a BCL-2 inhibitor** (removes their survival crutch), mirroring the
venetoclax+azacitidine precedent but with a more LSC-selective identity marker than azacitidine's
broad epigenetic mechanism.

If this direction is confirmed, it resolves plan-doc Decision #4 (single-target vs.
dual-target/combination scope) as: **dual-target combination regimen**, and partially resolves
Decision #1/#2 (target class / modality) as: **both** — a biologic against CLL-1 and a small
molecule against BCL-2, developed/tested in parallel rather than choosing one.

## Open threads

- Confirm via Phase 0 data (see main plan) that CLL-1 is actually differentially expressed in
  *post-treatment residual* LSCs specifically, not just diagnosis-stage LSCs.
- Decide whether to design a new BCL-2 inhibitor from scratch (harder novelty bar, venetoclax
  already exists) vs. treat venetoclax as a given and focus all generative-design effort on the
  CLL-1 biologic side.
- Still need Decision #3 from the main plan: which post-treatment/MRD dataset anchors the
  "persister" biology.
