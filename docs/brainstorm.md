# Brainstorm / Exploratory Notes

Informal running notes from the planning conversation, organized as one idea per section. See
[aml-lsc-drug-discovery-plan.md](aml-lsc-drug-discovery-plan.md) for the structured plan this feeds into.

## Background: The Problem

Standard AML treatment gets most patients into remission, but a small population of chemo-resistant
**leukemic stem cells (LSCs)** survives as residual disease and drives relapse. LSCs closely resemble
normal healthy blood stem cells (HSCs) — a drug that can't tell them apart wipes out the patient's
normal blood-making system along with the cancer. So the core challenge is finding a real,
exploitable *difference* between LSCs and normal HSCs, then building a drug against it.

Targets generally come in two kinds, which constrains what *type* of drug can even be built:

- **Surface markers** — proteins poking through the outside of the cell, acting as docks (e.g.,
  CLL-1, CD123). To hit these you need something that recognizes the *outside* of the cell — a
  biologic (antibody-based drug).
- **Internal survival switches** — proteins inside the cell that block self-destruction (e.g., BCL-2,
  MCL-1). To hit these you need something small enough to get *inside* the cell and jam an internal
  pocket — a small molecule.

You can't easily fuse a membrane-recognizing biologic and a cell-penetrating small molecule into one
drug object, so each idea below implies a different kind of drug.

---

## Idea 1: CLL-1 (Surface Marker Target)

**What it is:** CLL-1 (also called CLEC12A) is a protein dock sitting on the outer surface of LSCs
that is largely absent on normal HSCs — making it a promising "identity marker" for telling cancer
stem cells apart from healthy ones. Because it's a surface marker, drugs against it have to be
biologics that recognize the outside of the cell. Three modalities have been tried; all rely on an
underlying building block called an **antibody**.

**What an antibody is:** a Y-shaped protein the immune system makes, with the tips of its two arms
custom-shaped to grab one specific target — like a key cut for one lock. Scientists can engineer
antibodies whose arms are shaped to grab CLL-1 specifically. An antibody alone doesn't kill
anything — it just sticks. The three drug types below are three different ideas for what to do once
it's stuck.

### 1a. Antibody-Drug Conjugate (ADC) — tried, failed

Glue a poison molecule onto the CLL-1-grabbing antibody, like strapping a small bomb to a homing
device. It's injected, the antibody arm sticks to CLL-1 on the LSC surface, the cell pulls the whole
thing inside itself (cells naturally absorb things attached to their surface docks), and the poison
releases and kills the cell from within.

**Status:** a CLL-1 ADC trial was **terminated** — not potent enough against the leukemia, and it
still caused significant toxicity to normal blood cells anyway.

### 1b. Bispecific antibody — preclinical only

Engineer an antibody with two *different* arms instead of two identical ones: one arm grabs CLL-1 on
the LSC, the other grabs CD3, a marker on the patient's own T cells (the immune system's dedicated
killer cells). The molecule physically staples a T cell next to the LSC, forcing contact, which
triggers the T cell to kill it. No modification of the patient is needed — it recruits whatever T
cells are already circulating in their blood.

**Status:** shown to work in preclinical (mouse/cell) studies; not yet in human trials for CLL-1
specifically.

### 1c. CAR-T — furthest along, strongest results

The most involved approach: draw the patient's own T cells from their blood, genetically engineer
them in the lab to grow an artificial receptor (a **C**himeric **A**ntigen **R**eceptor) built by
fusing the "grabbing" part of the CLL-1 antibody onto the "kill trigger" part of a normal T cell
receptor, grow millions of them, then infuse them back into the same patient. The patient now has an
army of their own immune cells permanently reprogrammed to recognize and kill anything displaying
CLL-1 — a long-term, self-renewing surveillance system rather than a one-time injected drug.

**Status:** five phase 1 trials (2020–2023, mostly pediatric AML, two adult) showed roughly **70%
response rate**. A newer IL-18-secreting version (CD371-targeted) showed 3 of 5 patients responding.
A dual-target CLL-1 + CD38 CAR-T trial is currently running (est. completion 2028).

**Takeaway:** CLL-1 looks like a legitimate target — the CAR-T data is the best evidence of that —
but no drug format has been fully proven out to approval yet. Of the three modalities, CAR-T has the
strongest signal, though it's also the most complex to build (cell engineering, not just molecule
design), which matters for how our "AI-driven generative design" phase would even apply here.

---

## Idea 2: BCL-2 / MCL-1 (Internal Survival-Switch Target)

**What it is:** BCL-2 and MCL-1 are internal proteins that act as a "survival switch" — they tell a
damaged or abnormal cell not to self-destruct. LSCs lean on this switch heavily to survive
chemotherapy. Because it's internal, drugs against it are small molecules, not biologics.

**BCL-2 — proven, precedented:** **venetoclax** (an approved BCL-2 inhibitor) is already standard of
care combined with azacitidine for AML patients who can't tolerate intensive chemo. This validates
the mechanism but raises the novelty bar for a new BCL-2 drug — it has to improve meaningfully on an
already-approved one.

**MCL-1 — mechanistically attractive, but blocked by cardiac toxicity:** MCL-1 inhibitors have
repeatedly hit a wall in clinical trials:
- **AMG 397** — FDA placed a **clinical hold** after a cardiac toxicity safety signal.
- **AMG 176** — halted voluntarily as a precaution, same concern.
- **AZD5991** and **ABBV-467** — both showed cardiac troponin increases (a blood marker of heart
  muscle damage) in patients.

**Why:** heart muscle cells depend heavily on MCL-1 to keep their mitochondria (energy-producing
structures) working. Blocking MCL-1 doesn't just stop cancer cells from resisting death — it also
disrupts how heart cells manage their own energy and stress. BCL-2 isn't nearly as load-bearing for
heart cells, which is a big part of why venetoclax succeeded where MCL-1 inhibitors keep struggling.

**Newer directions worth watching:** designing MCL-1 inhibitors with very short half-lives (hit the
cancer cell hard, then clear the body fast before sustained cardiac exposure), and "degrader"
molecules that mark MCL-1 for destruction rather than just blocking it — e.g., **CT-03p**, presented
as a "cardio-safe" MCL-1 degrader that also overcomes venetoclax resistance.

**Takeaway:** BCL-2 is the safer, precedented choice for this project; MCL-1 is a real, unresolved
research problem with the toxicity issue not yet solved, and would be a much higher-risk bet.

---

## Idea 3: Hedgehog–GLI2 Pathway (Dormancy/Self-Renewal Target)

**Where this came from:** prompted by looking into Marc Malone (see
[research/marc_malone.md](research/marc_malone.md)) and asking whether any of his ideas could help.
His specific protocol isn't credible (n=1, self-administered, no peer review — full assessment in
that file), but one of the pathway categories he references — Hedgehog-GLI2 signaling — is real,
independently-established AML biology with an actual approved drug behind it. This idea is grounded
in that independent evidence, not in his claims.

**What it is:** Hedgehog is a signaling pathway (GLI2 is one of its downstream effectors) that helps
keep LSCs in a dormant, self-renewing state — the exact "lingering, quiescent" behavior that lets
LSCs hide from chemo (see [problem-definition.md](problem-definition.md)). Blocking the pathway
pushes LSCs out of dormancy and can resensitize them to chemotherapy.

**Precedent — already approved:** **glasdegib** (Daurismo), an SMO inhibitor that blocks Hedgehog
signaling upstream of GLI2, was FDA-approved in 2018 in combination with low-dose cytarabine for AML
patients unfit for intensive chemo.

**Open question for our project:** glasdegib is currently used at diagnosis/induction, alongside
chemo — not specifically tested against the post-remission, already-quiescent MRD-state LSCs this
project is targeting. Whether Hedgehog blockade works the same way against *already-dormant*
persister LSCs (vs. LSCs at diagnosis) is an open question worth checking in Phase 0 data, and a
plausible third combination arm alongside CLL-1 + BCL-2.

---

## Combination Idea: CLL-1 + BCL-2 Together

Prompted by: "why don't people try CLL-1 and BCL-2/MCL-1 together?"

Because of the modality mismatch (biologic vs. small molecule), "combining" them in practice means
**two separate drugs given together as a regimen**, not one designed molecule doing both jobs.

This isn't a novel idea in the abstract — it's the same logic already validated by
**venetoclax + azacitidine**: attack the cancer's survival mechanism from two angles at once. Active
trials already combine venetoclax with CD123-targeted biologics; a CLL-1 equivalent doesn't exist yet
mainly because the CLL-1 side of the pairing (CAR-T/bispecific/ADC) is still earlier-stage than CD123.

**Tentative direction:** an **anti-CLL-1 CAR-T** (identifies/flags the LSC-specific population, per
Idea 1's strongest modality) **+ a BCL-2 inhibitor** (removes their survival crutch, per Idea 2),
mirroring the venetoclax+azacitidine precedent but with a more LSC-selective identity marker.

If confirmed, this resolves plan-doc Decision #4 (single vs. dual-target scope) as: **dual-target
combination regimen**, and Decisions #1/#2 (target class/modality) as: **both** — CAR-T against CLL-1
and a small molecule against BCL-2, developed/tested in parallel.

---

## Biology Primer (reference)

- **Protein** — a molecule made of a chain of amino acids that folds into a specific 3D shape; that
  shape determines its job (a machine doing chemistry, a structural beam, a switch, or a lock/dock on
  the cell surface).
- **Amino acid** — the individual building block ("bead") proteins are made of. 20 standard types.
  DNA → amino acid sequence (the recipe, read out in order) → folded protein (the built tool).
- **Cell composition** — not "basically all protein": membrane = lipids (with protein docks
  embedded); DNA = master blueprint (nucleotides, not amino acids); RNA = disposable working copies
  of DNA; proteins = the machines/workers/structural beams; carbs/fats = fuel + tags; water = the
  medium everything sits in. Proteins dominate the *active machinery*, which is why drug targets and
  cancer-driving mutations almost always trace back to a malfunctioning protein.
- **Antibody** — a Y-shaped protein with arms custom-shaped to grab one specific target; the building
  block behind ADCs, bispecifics, and CAR-T receptors (see Idea 1).

---

## Open Threads

- Confirm via Phase 0 data (main plan) that CLL-1 is differentially expressed in *post-treatment
  residual* LSCs specifically, not just diagnosis-stage LSCs.
- Decide whether to design a new BCL-2 inhibitor from scratch (harder novelty bar) vs. treat
  venetoclax as a given and focus generative-design effort on the CLL-1 CAR-T side.
- Work out what "AI-driven generative design" means for a CAR-T receptor specifically — it's a
  different design problem than the small-molecule/docking pipeline in the main plan.
- Still need Decision #3 from the main plan: which post-treatment/MRD dataset anchors the
  "persister" biology.
