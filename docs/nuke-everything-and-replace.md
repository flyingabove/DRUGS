# Nuke Everything and Replace

Two fundamentally different strategies for eliminating lingering LSCs:

1. **Cure in place** — kill/weaken/mature LSCs inside the patient while sparing normal HSCs. Requires
   a selectivity window. Everything in [brainstorm-topics.md](brainstorm-topics.md),
   [challenges.md](challenges.md), and [wnt-persister-hypothesis.md](wnt-persister-hypothesis.md)
   is this strategy.
2. **Nuke everything and replace** — stop trying to be selective. Wipe out all stem cells, then
   rebuild the blood system from a clean, engineered graft. This doc.

## The Core Idea: Epitope Editing

Instead of making the drug selective, **make the healthy cells invisible to it.**

Base-edit or prime-edit the donor graft so a target protein has 1–2 amino acids changed — the drug
can no longer bind it, but the protein still works normally. Transplant those edited cells. Now the
drug can be completely non-selective: it kills every unedited cell carrying the target (including
all LSCs), and the edited graft survives untouched.

**Two flavors:**

- **Deletion** — remove the antigen entirely. Only works if the protein is dispensable (CD33 is).
- **Epitope edit** — change 1–2 amino acids, preserving function. Required when the protein is
  essential. Demonstrated for **CD123, FLT3, KIT (CD117), CD45**.

## Why This Doesn't Accidentally Shield the LSCs

It doesn't shield selectively — **it never touches the LSCs at all.**

1. Take a clean graft, edit it **in a dish** (ex vivo).
2. Transplant the edited cells.
3. Attack with a non-selective drug.

The LSCs are inside the patient. They were never in the dish. There's no targeting step to get
wrong — it's physical separation, not molecular discrimination.

**This makes graft purity the entire ballgame:**

- **Allogeneic (donor cells)** — structurally guaranteed clean. A donor has no patient LSCs. This is
  why the trem-cel trial is allogeneic.
- **Autologous (patient's own cells)** — dangerous. If LSCs contaminate the harvest (see the graft
  contamination problem in [plerixafor-combination-brainstorm.md](plerixafor-combination-brainstorm.md)),
  **you edit and shield the cancer too** — permanently immunizing the leukemia against your own
  therapy. Worse than not treating.
- **In vivo editing (lipid nanoparticle-delivered)** — being explored, but editing inside the patient
  means LSCs are present and could be edited. Loses the physical-separation guarantee entirely.

## Status: Already in Humans

- **trem-cel** — CRISPR CD33-deleted allogeneic transplant + gemtuzumab ozogamicin maintenance.
  Phase 1/2 first-in-human results published in Nature Medicine (2026).
- Prime editing efficiency in HSPCs improved from 5.9% → 78.9% in recent work.
- A Nature (2026) paper on **non-genotoxic conditioning** via epitope editing suggests the harsh
  pre-transplant chemo may become avoidable.

## Hard Constraint: Biologics Only

**Epitope editing defeats biologics (antibodies, CAR-T) — not small molecules.** Small molecules bind
functional pockets; edit the pocket and you break the protein.

Direct consequence for this project: our targeted-CXCR4 idea can't use a plerixafor conjugate here.
Plerixafor is a competitive antagonist sitting in CXCL12's binding site — edit that and normal HSCs
lose homing too. It would have to become **antibody-based** (anti-CXCR4 antibodies like ulocuplumab
or LY2624587 bind surface epitopes away from the ligand pocket, which are editable). Same logic for
CD44.

## What This Unlocks

- **CD123 comes back as a target.** Rejected in Idea 1 for overlapping with normal HSCs — that's
  exactly the problem this solves, and CD123 is already a demonstrated epitope-editing target.
- **CD117/KIT** becomes viable for the same reason.
- **Multiplex editing solves heterogeneity (Challenge #4).** Shield against several antigens at once
  (CD123 + CD33 + CD117), then attack all of them simultaneously. If a patient's LSCs escape one
  antigen, the other two still cover it. **This is the only approach in the project that addresses
  Challenge #4** — every "cure in place" idea is at best partial there.

## Trade-offs vs. Cure in Place

| | Cure in place | Nuke and replace |
|---|---|---|
| Selectivity needed | Yes — the hard problem | No — sidestepped entirely |
| Requires transplant | No | Yes |
| Solves heterogeneity | No | Yes (multiplex) |
| Failure mode | Kills normal HSCs | Shields the cancer (if graft contaminated) |
| Patient burden | Lower | Transplant + conditioning |

## Open Threads

- Does the patient's *own* residual normal HSC population matter? They're unedited and would be
  killed by the therapy — presumably acceptable since the graft replaces them, but worth confirming.
- Which antigen combination to multiplex for AML persisters specifically.
- Whether an anti-CXCR4/CD44 antibody with an editable epitope away from the functional site actually
  exists, or would need to be developed.

## Sources

- [Epitope editing enables targeted immunotherapy of AML (Nature)](https://www.nature.com/articles/s41586-023-06496-5)
- [CD33-deleted allo-HCT with gemtuzumab maintenance, phase 1/2 (Nature Medicine 2026)](https://www.nature.com/articles/s41591-026-04362-1)
- [Epitope prime editing shields hematopoietic cells from CD123 immunotherapy (Cell Stem Cell)](https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(24)00317-5)
- [Epitope base editing CD45 enables universal blood cancer immune therapy (Sci Transl Med)](https://www.science.org/doi/10.1126/scitranslmed.adi1145)
- [Non-genotoxic transplantation and in vivo selection through epitope editing (Nature 2026)](https://www.nature.com/articles/s41586-026-10737-8)
- [CD33 epitope editing unlocks UM171-expanded cord blood grafts (Molecular Therapy)](https://www.cell.com/molecular-therapy-family/molecular-therapy/abstract/S1525-0016(25)00950-5)
