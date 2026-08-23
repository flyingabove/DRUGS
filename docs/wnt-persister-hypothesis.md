# Wnt/Notch/Grip Hypothesis — Logic Chain and Plan

## Part 1: The Logic Chain — How Chemo Selects for the Strong Ones

**Step 1 — At diagnosis, the leukemia isn't one uniform enemy, it's a mixed crowd.** A patient's AML
at diagnosis contains many LSCs, and they're not identical clones. Some grip the marrow tighter than
others (via CXCR4 and CD44 — two separate "grappling hooks," covered below). Some have stronger
internal self-renewal machinery (Wnt) than others. Some have more thoroughly shut down their
"time to mature" switch (Notch) than others. It's a spectrum, not a single type.

**Step 2 — What each of these proteins actually does:**

- **CXCR4** — a dock on the LSC's surface that grabs a signal thrown by the marrow, physically
  anchoring the cell in its hiding spot and sending it a "stay quiet, don't divide" signal.
- **CD44** — a second, separate dock doing a similar anchoring job, independent of CXCR4. Two hooks,
  not one.
- **Wnt** — an internal switch that tells the cell "keep copying yourself, don't mature yet." The
  engine behind self-renewal.
- **Notch** — normally the opposite kind of switch, "okay, stop copying yourself and grow into a
  finished cell." In AML specifically, this switch has been silenced — so a cell that's better at
  keeping it silenced stays stuck in dangerous, immature, self-copying mode longer.

**Step 3 — Chemo doesn't kill cells randomly, it kills a specific type.** Most chemo drugs work by
damaging the machinery a cell uses to copy its DNA — which only matters while a cell is actively
dividing. A cell that's quiet (not dividing) or well-protected is much harder for chemo to reach or
kill.

**Step 4 — This turns chemo into a filter, not an eraser.** Cells that happen to grip the marrow
tighter (more CXCR4/CD44), lean harder on self-renewal (more Wnt), or have Notch more completely
shut off are, on average, better protected from this specific kind of attack. Chemo doesn't "choose"
these cells on purpose — it just kills the weaker-gripping, more exposed, more Notch-active cells
first, leaving the toughest ones standing. It's natural selection compressed into a few weeks instead
of generations.

**Step 5 — The result: the survivors aren't a smaller copy of the original leukemia, they're a
skewed sample.** The population left after treatment (what causes MRD and eventual relapse) is
disproportionately made up of the tightest-gripping, most Wnt-addicted, most Notch-silenced cells —
because those are exactly the traits that got them through.

**Step 6 — It might be worse than pure filtering — the survivors' own machinery may get cranked up
further.** Real evidence (found in related cancers) shows chemo stress itself can actively push Wnt
signaling higher in the cells that survive it — not just filtering for cells that already had high
Wnt, but turning the dial up further as a stress response. Two effects stacking: the weak ones die
(selection), and the ones that live come out even stronger on these exact traits (induction).

**Step 7 — Why this matters:** if the persister population really is disproportionately dependent on
tight CXCR4/CD44 grip, high Wnt, and silenced Notch — more so than the original diagnosis-time
population — then a therapy built to strip away exactly those traits should hit this specific
population harder than generic diagnosis-stage data would predict. We'd be targeting the precise
thing that made them survivors in the first place.

## Part 2: What We Propose

**Step 1 — Confirm the hypothesis first.** Test whether relapse/persister cells actually show
tighter CXCR4/CD44 grip, higher Wnt activity, and more silenced Notch than diagnosis-time cells from
the same patients — via a relapse-sample proxy comparison (relapse descends from the persister
population and is far easier to sample than true MRD-state cells) and a dish-based chemo-selection
experiment (expose cells to chemo, check whether the survivors were the high-scoring cells before
treatment).

**Step 2 — If confirmed, build a combination that attacks all three traits at once, not one at a
time:**

- **Cut both grappling hooks** — a CXCR4-blocking effect targeted specifically at LSCs (not free,
  systemic Plerixafor, which would also hit normal HSCs' CXCR4 grip) plus a Wnt inhibitor, which
  also weakens CD44 as a side effect. Together, the cell can't hang on either rope.
- **Kill the self-renewal engine** — the same Wnt inhibitor also removes the "keep copying yourself"
  signal directly.
- **Force the "grow up" switch back on** — a Notch-reactivating agent, pushing the cell toward
  finally maturing instead of staying stuck.

**Step 3 — Time it deliberately.** Give this as post-remission consolidation therapy (matching this
project's whole framing — cleaning up what's left after standard treatment), and separately consider
giving the Wnt component during the first round of chemo, to prevent the tough-survivor population
from ever being enriched in the first place.

**Step 4 — Use it as a biomarker-selected therapy, not universal.** Test a patient's residual disease
for how tightly-gripped and Wnt-dependent it actually is before committing to this specific
combination — consistent with the heterogeneity problem already flagged in
[challenges.md](challenges.md).

**Step 5 — Validate in the same staged order as the rest of the project's plan.** Dish experiments
first, then a mouse model that's treated with induction chemo first to actually create a real
persister population, then dosed with the combination — matching Phase 4/5 of the main plan doc
rather than skipping straight to testing on untreated disease.
