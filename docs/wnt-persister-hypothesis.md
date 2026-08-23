# Did Surviving Chemo Make Persister Cells More Wnt-Dependent?

A dedicated brainstorm on one specific open question: whether the small population of LSCs that
survives chemotherapy is *more* dependent on Wnt signaling than LSCs were at diagnosis — and if so,
what to do about it. See [brainstorm-topics.md](brainstorm-topics.md) (Idea 9: Wnt/β-Catenin
Blockade) for background on the pathway itself, and
[problem-definition.md](problem-definition.md) for the core project problem.

## The Question, in Plain Terms

**Wnt signaling** is one of the body's "keep dividing, stay young, don't mature yet" switches — see
[brainstorm-topics.md](brainstorm-topics.md) for the full mechanism. LSCs lean on it to keep
self-renewing instead of maturing into harmless, finished blood cells.

Chemotherapy doesn't kill leukemia cells randomly. It disproportionately kills actively-dividing
cells and spares cells with strong internal survival/self-renewal machinery. **If having powerful
Wnt-driven self-renewal happens to be one of the traits that helps a cell weather chemo, then the
small population that survives treatment might not be a random, smaller-scale copy of the original
leukemia — it could be specifically enriched for cells that leaned hardest on Wnt to begin with.**

This is a **selection pressure / survivorship bias** effect, the same underlying logic as antibiotic
resistance: treatment doesn't create the trait, it filters for cells that already had it, so the
survivors look different from the starting population as a group — not because anything new evolved,
but because the vulnerable members of the group are gone.

**Why this hasn't already been answered:** every existing study measuring Wnt-dependence in LSCs was
done on cells *at diagnosis*, before any treatment — the full original population, not the specific
survivors. Nobody has directly compared Wnt-pathway activity between diagnosis-stage LSCs and the
post-treatment persister cells from the same patients.

## Why It Matters

If confirmed, this would be a meaningful upgrade to Idea 9 (Wnt/β-Catenin Blockade): a Wnt-blocking
drug could work *better* against the exact population this whole project cares about (post-remission
persisters) than existing diagnosis-stage data would predict, because that population would already
be pre-filtered toward cells that specifically need Wnt to survive. It would also strengthen the
project's overall target-prioritization case — Wnt already has the cleanest selectivity story found
so far (LSC-required, apparently not needed by normal adult HSCs); persister-specific enrichment
would make it stronger still.

## How to Test This

### Direct approach — needs data we don't have yet

Compare Wnt-pathway activity (Wnt target gene expression, beta-catenin protein levels) between
diagnosis-stage LSCs and true post-treatment/MRD-state persister LSCs, from the same patients. This
runs into the same missing-data problem flagged throughout this project (main plan-doc Decision #3):
true MRD-state cells are rare and hard to isolate in enough quantity for this kind of comparison.

### Practical proxy — achievable with more available data

Compare diagnosis-stage LSCs to **relapsed-disease** LSCs from the same patient. Relapsed disease
descends directly from the persister cells that survived treatment and regrew, and relapse samples
are far more available in existing biobanks than true low-abundance MRD-state samples (relapse
produces a full new tumor burden that's easy to biopsy; residual disease right after remission is a
handful of hard-to-find cells). If relapsed LSCs show higher Wnt-pathway activity than the original
diagnosis LSCs from the same patient, that's real, if indirect, supporting evidence.

### Controlled experimental approach — doesn't need rare human samples at all

Take LSCs in a lab dish (or a mouse model), expose them to chemotherapy to create an artificial
"surviving population," then directly measure whether the survivors show elevated Wnt-pathway
activity compared to the pre-treatment population. This tests the selection-pressure mechanism
directly and doesn't depend on sourcing scarce human MRD samples first.

A more precise version: use a live **Wnt-activity reporter** (a molecular tool that lights up or
signals in real time based on how active Wnt signaling is inside a given cell) combined with chemo
exposure in a dish, to directly watch whether high-Wnt cells are the ones preferentially surviving as
the population gets treated — turning the hypothesis into something observable in real time rather
than inferred after the fact.

## What to Do If Confirmed

- **Position a Wnt inhibitor specifically as post-remission/consolidation therapy** — matches this
  project's whole framing (a therapy given after standard treatment, aimed at what's left), rather
  than as a frontline drug competing with existing induction regimens.
- **Consider giving it *during* induction chemo, not only after** — if chemo itself is what enriches
  for Wnt-dependent survivors, adding a Wnt blocker alongside the first round of chemo could kill off
  the very cells that would otherwise become the resistant persister population, preventing the
  enrichment from happening in the first place rather than reacting to it afterward.
- **Use Wnt-pathway activity as a biomarker for patient/consolidation-therapy selection** — test a
  patient's residual disease for Wnt activity to decide whether this specific therapy is a good fit
  for them (see the heterogeneity challenge in [challenges.md](challenges.md) — this is the kind of
  biomarker-selection approach that challenge points toward).
- **Combine with other ideas** — e.g., Idea 8 (adhesion-axis disruption: Plerixafor + a Wnt inhibitor
  hitting both CXCR4 and CD44), since a Wnt inhibitor may already be doing double duty as both a
  self-renewal blocker and a niche-adhesion disruptor.

## What to Do If Not Confirmed

Wnt blockade still stands on its own as a reasonable strategy based on existing diagnosis-stage
data — the "LSCs need it, normal HSCs largely don't" selectivity story doesn't depend on the
persister-enrichment hypothesis being true. Without confirmation, though, we'd need to look
elsewhere for what specifically distinguishes persister cells from the general LSC population, since
the assumption that diagnosis-stage biology simply transfers to the persister state would need to be
checked pathway-by-pathway rather than assumed.

## Open Threads

- Identify which existing biobanks/datasets have matched diagnosis-vs-relapse samples suitable for
  the proxy comparison above.
- Design the chemo-selection dish experiment (agent, dose, timepoint) needed for the controlled
  approach.
- Check whether a validated Wnt-activity reporter system already exists for primary AML cells, or
  would need to be built.
