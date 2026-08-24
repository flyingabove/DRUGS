# Strategy 3: Provoke, Then Strike

**The strategy in one line:** don't lower the threshold to reach the cancer — **raise the cancer to
the threshold.** Deliberately provoke LSCs into displaying more target protein, then hit them with a
high-threshold drug during that window, keeping maximum separation from normal cells the whole time.

Sits alongside [Strategy 1: Nuke Everything and Replace](nuke-everything-and-replace.md) and
[Strategy 2: Identify, Profile, Counterattack](identify-profile-counterattack.md).

## The Core Insight

Target density is **not a fixed trait — it moves.** Every previous idea treated a cell's CXCR4/CD44
level as a static property to be measured. It isn't. It responds to stress, oxygen, and drug
exposure.

That changes the problem. A density-threshold drug (see the affinity-tuning section below) needs
cells to be above a line. There are two ways to get there:

- **Lower the line** → dangerous. It approaches normal-cell density, destroying the safety margin,
  and it selects for lower-density survivors — breeding the cancer to hide in the normal range.
- **Raise the cells** → keeps the line high and the margin intact. The cancer is pushed *toward*
  detection rather than away from it.

## Background: Why a High Threshold Works

Build the binder deliberately **weak** — micromolar Kd (~1–200 μM) rather than nanomolar. A strong
binder holds with a single bond, so it fires on any cell carrying any amount of target: no
discrimination. A weak binder's bonds keep falling off, so stable engagement requires *many
simultaneous* bonds — which only happens at high target density. That nonlinearity is the threshold.

Verified: affinity-tuned CARs kill antigen-rich tumor while sparing normal cells at physiologic
density; high-affinity versions hit everything, including cells whose antigen is undetectable by
flow.

## Provocation Lever 1: Hypoxia — the strong one

**This is the finding the strategy rests on.** Normal and leukemic cells respond to low oxygen in
*opposite directions*:

- **Normal cells DOWN-regulate CXCR4 under hypoxia**, via a post-transcriptional mechanism driven by
  miR-146a upregulation.
- **Primary AML blasts fail to do this** — the miR-146a/CXCR4 mechanism is dysregulated in them, so
  they keep CXCR4 high.

**Separation widens in both directions at once.** Cancer goes up (or holds), normal goes down. That's
better than a lever that simply raises both.

Mechanistic basis: the CXCR4 promoter carries four hypoxia-response elements (HREs) within 2.6 kb
upstream of the transcription start site, plus one intronic — CXCR4 is a genuinely
hypoxia-responsive gene. Separately confirmed: CXCR4 expression and biologic activity in AML are
directly dependent on oxygen partial pressure.

**Scope caveat:** the differential miR-146a finding is from monocytic cells and AML-M5 specifically,
partly in cell lines. Whether it generalizes across AML subtypes is the first thing to test.

### How to induce it without making the patient hypoxic

Use a **HIF-stabilizing drug** rather than actual low oxygen. Prolyl hydroxylase inhibitors
(roxadustat, daprodustat — already approved for anemia of chronic kidney disease) stabilize HIF-1α
pharmacologically, mimicking the hypoxic signal.

This is a drug-repurposing play in the same spirit as
[brainstorm-topics.md](../brainstorm-topics.md) Idea 7 — an approved compound with existing human
safety data, used for a new purpose.

## Provocation Lever 2: Chemotherapy — weaker, but real

Standard cytotoxic chemotherapy induces dynamic upregulation of surface CXCR4 on leukemia cells — a
documented mechanism of acquired resistance. Cells that upregulated were differentially protected
from chemo-induced apoptosis when co-cultured with stroma.

**Two limitations:**
1. Upregulation is **variable**, not universal — some lines do it, some don't.
2. The comparison against normal CD34+ cells isn't established in the literature found. Without that,
   we don't know whether chemo widens or merely shifts the separation.

Chemo is the weaker lever. Use it as a secondary/combination provocation, not the primary one.

**Note on dosing:** the goal at this step is **signal, not kill.** You need enough stress to trigger
the upregulation response, not enough to cause cytotoxic damage — a much lower dose than therapeutic
chemo. That makes HSC toxicity from the provocation step far more manageable than "give chemo"
implies.

## Will This Kill Too Many Normal HSCs?

### The provocation step is unusually favorable

Stacking the hypoxia findings gives a rare alignment. Under HIF stabilization:

- **Normal HSCs:** CXCR4 goes *down* (less visible to the drug) **and** they sit in their protected,
  low-ROS, quiescent state — hypoxia is protective for normal HSCs, not harmful (mice at 10% O₂ show
  *better* HSC function than at normal oxygen).
- **LSCs:** CXCR4 stays *up* — visible and targetable.

Both effects push the same direction. The lever that widens targeting separation is also the one
that shelters the cells we're trying to preserve.

**The risk that doesn't go away:** HIF-1α also drives pro-survival and stemness programs in cancer.
This could strengthen the leukemia while illuminating it. Still the single biggest unknown in this
strategy.

### The dual binder: separate the gating job from the killing job

Using **both hooks (CXCR4 + CD44) as the gate** is weaker than it looks.

An AND-gate's safety is multiplicative *only if the two signals are independent*. If each threshold
alone spares ~95% of normal HSCs, requiring both could spare ~99.75% — but that math assumes
independence.

**CXCR4 and CD44 aren't independent.** They're cross-linked: CXCL12 stimulates adhesion *via* CD44,
and blocking CD44 loosens CXCR4–SDF1 binding. A cell high in one tends to be high in the other. You'd
be partly measuring the same thing twice, and the multiplicative safety largely evaporates.

**The fix:**

- **Gate on independent axes** — CXCR4 (is it gripping hard?) AND CLL-1 (is it leukemic?). Different
  biology, genuinely uncorrelated, so the multiplicative safety is real.
- **Act on both hooks** — once the gate fires, sever CXCR4 *and* CD44 as the therapeutic effect.

Real independence in the decision, full coverage in the action.

### Reframing the bar

**The bar isn't zero HSC loss.** Patients tolerate substantial HSC depletion and recover — the
reserve regenerates. The failure mode is near-total ablation with nothing left to rebuild from.

Fallback: bank HSCs before treatment as insurance. That reintroduces the graft contamination problem
from [Strategy 1](nuke-everything-and-replace.md) and would need the purging step.

## Proposed Protocol

1. **Measure baseline.** Quantitative flow with calibration beads (ABC — antibodies bound per cell)
   to get real molecules-per-cell for the patient's LSCs *and* their normal CD34+ cells. Relative
   fluorescence is not sufficient; threshold design needs absolute counts.
2. **Provoke.** HIF-stabilizing agent (primary) ± chemotherapy (secondary).
3. **Confirm the shift.** Re-measure density. Verify LSC density rose and normal-cell density did
   not — this is the go/no-go gate. Without confirmed widening, don't proceed to the strike.
4. **Strike in the window.** High-threshold, affinity-tuned binder, gated on independent axes
   (CXCR4 AND CLL-1 — see above), timed to peak separation. Therapeutic action severs both hooks.
5. **Pair with a density-independent mechanism.** Ferroptosis via ferritinophagy, or synthetic
   lethality on a driver mutation — so cells escaping by shedding surface protein are still caught.

## Why This Composes Well With the Collateral-Sensitivity Trap

A cell facing a high-threshold drug has one escape route: shed target protein. But grip *depends* on
having lots of CXCR4/CD44 — shed them and the cell can't hold the niche, loses its dormancy brake,
and loses stromal chemoprotection. It becomes an ordinary dividing cell, which is exactly what
standard chemo kills.

That's a **collateral sensitivity** setup (resistance to one drug creating vulnerability to another),
deliberately engineered as an **evolutionary double bind**. Keep the hooks → threshold drug kills you.
Drop them → chemo kills you.

**Design consequence: the threshold drug must be given *with* chemo, not after it.** The trap needs
both jaws present. Post-remission consolidation, with the patient off chemo, leaves the second jaw
missing and escapers simply escape.

## Risks and Open Threads

- **HIF stabilization may help the cancer.** HIF-1α drives many pro-survival and stemness programs.
  Provoking it could strengthen LSCs in ways that outweigh the targeting benefit. This is the single
  biggest unknown and needs direct testing before anything else.
- **Does the miR-146a differential generalize** beyond monocytic/AML-M5 lineages?
- **Receptor internalization as a fake-out.** A cell can transiently pull the receptor inside itself
  to duck below threshold, then re-express it — hiding without paying the chemo-vulnerability price.
  Testable: does a cell that drops below threshold actually become chemo-sensitive, or just
  temporarily invisible?
- **Intrinsic dormancy leaks the trap.** Cells quiescent via p21/p27 rather than niche grip could
  shed the hooks *and* stay chemo-resistant, slipping both jaws.
- **Patient heterogeneity.** Primary AML spans ~557–11,726 CD123 molecules/cell. A fixed threshold
  can't fit everyone — this forces a companion diagnostic, and possibly a small panel of variants at
  different thresholds matched per patient.
- **Timing window unmeasured.** How long does provoked upregulation last? The strike has to land
  inside it.

## Sources

- [Differential hypoxic regulation of the miR-146a/CXCR4 pathway in normal and leukemic cells](https://haematologica.org/article/view/7491)
- [CXCR4 expression and biologic activity in AML are dependent on oxygen partial pressure](https://pmc.ncbi.nlm.nih.gov/articles/PMC2644078/)
- [Dynamic chemotherapy-induced upregulation of CXCR4: a mechanism of resistance in pediatric AML](https://aacrjournals.org/mcr/article/11/9/1004/89410/Dynamic-Chemotherapy-Induced-Upregulation-of-CXCR4)
- [Balance of anti-CD123 CAR binding affinity and density for targeting AML](https://pmc.ncbi.nlm.nih.gov/articles/PMC5542631/)
- [Affinity-tuned CARs spare normal cells](https://www.genengnews.com/topics/drug-discovery/affinity-tuned-car-t-cells-slay-tumor-cells-spare-normal-cells/)
- [T cell circuits that sense antigen density with an ultrasensitive threshold](https://limlab.ucsf.edu/pdfs/hernandez-lopez_2021.pdf)
