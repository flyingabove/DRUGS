# Strategy 3: Provoke, Then Strike

**One line:** don't lower the threshold to reach the cancer — **raise the cancer to the threshold.**
Deliberately force lingering leukemic stem cells (LSCs) to display more target protein, then hit them
with a threshold-gated drug during that window, keeping maximum separation from healthy cells the
whole time.

Sits alongside [Strategy 1: Nuke Everything and Replace](nuke-everything-and-replace.md) and
[Strategy 2: Identify, Profile, Counterattack](identify-profile-counterattack.md).

---

## The Core Insight

Target density is **not a fixed trait — it moves.** Every earlier idea treated a cell's CXCR4 level
as a static property to measure. It isn't. It responds to stress, oxygen tension, and drug exposure.

That reframes the problem. A density-threshold drug needs cells to sit above a line. Two ways to get
there:

- **Lower the line** → dangerous. It creeps toward normal-cell density, destroying the safety margin,
  and it selects for lower-density survivors — effectively breeding the leukemia to hide in the
  normal range.
- **Raise the cells** → keeps the line high and the margin intact. The cancer is pushed *toward*
  detection rather than away from it.

---

## Background: Why a Weak Binder Discriminates Better

Counterintuitive, so the mechanism matters.

**Affinity (Kd)** is the strength of a *single* bond. **Avidity** is the combined strength when many
bonds form at once.

A **high-affinity** binder holds on with one bond. One target molecule is enough, so it fires on any
cell carrying any amount — no discrimination. This is why high-affinity CARs attack normal tissue at
antigen levels undetectable by flow cytometry.

A **low-affinity** binder's bonds keep falling off. Stable engagement requires *many simultaneous*
bonds, and the probability of that scales nonlinearly with target density. That nonlinearity is the
threshold — you've converted a smooth "how much antigen" into a sharp "above or below the line."

Think weak Velcro: one industrial hook grabs any surface with a few loops; weak hooks only hold on a
surface densely covered in them.

**Working range:** micromolar Kd (~1–200 μM) discriminates. Nanomolar (~1–200 nM) does not.

---

## The Drug: A Tetraspecific NK-Cell Engager

An **engager** is a single manufactured protein — batch-produced, off-the-shelf, infused like any
biologic. It physically staples an immune killer cell to a cancer cell and forces the kill, without
engineering anyone's cells.

Four components:

| Arm | Plain terms | Purpose |
|---|---|---|
| **anti-CD16** | grabs NK cells | Recruits the killer |
| **anti-CLL-1 (CLEC12A)** | "is this leukemia?" | Identity gate |
| **anti-CXCR4, affinity-tuned** | "is it gripping hard?" | Density gate — only fires above threshold |
| **IL-15** | NK growth signal | Drives NK expansion and persistence |

### Why NK cells, not T cells

T-cell engagers were the obvious first choice, but **T cells are too slow.** Naive T cells need
activation and clonal expansion — days. Blinatumomab (a T-cell engager) takes weeks to show
responses. Our therapeutic window is measured in hours.

**NK (natural killer) cells are innate immune cells — pre-armed.** They circulate already loaded with
perforin and granzyme (the proteins that punch holes in target cells) and need no priming. Killing
happens within hours of engagement.

Complement is faster still, but complement is a passive plasma protein cascade — it can't migrate.
NK cells actively move into tissue, which matters for reaching the poorly-perfused endosteal niche.

### Why the two gates must be independent

Gating on both grip proteins (CXCR4 + CD44) looks appealing but is weaker than it seems. An AND-gate
is multiplicatively safe **only if the two signals are independent** — and CXCR4 and CD44 are
cross-linked (CXCL12 drives adhesion via CD44; blocking CD44 loosens CXCR4–SDF1 binding). A cell high
in one tends to be high in the other, so you'd be measuring the same thing twice.

**Gate on independent axes instead:** CXCR4 (grip strength) AND CLL-1 (leukemic identity). Different
biology, genuinely uncorrelated, so the multiplicative safety is real. Then act on both hooks once
the gate fires.

### Why this format also solves the half-life problem

Recruiting NK cells normally requires an **Fc domain** (the antibody tail that immune cells grab) —
but Fc also confers a weeks-long half-life via FcRn recycling, which would smear the drug far beyond
our window.

The TriKE-style format sidesteps this: it engages NK cells through a **direct anti-CD16 arm** rather
than through Fc, reportedly with higher affinity than natural Fc–CD16 binding. No Fc means no FcRn
recycling means short half-life comes free.

**Short half-life is a design goal here, not a compromise.** Precedent: blinatumomab has a ~2-hour
half-life and runs on a continuous infusion pump — the short half-life is what makes the pump an
on/off switch. Same logic drives newer MCL-1 inhibitors, engineered to hit hard then clear before
cardiac toxicity accumulates.

**Target half-life ≈ one-third to one-half the therapeutic window.** If the CXCR4 window turns out to
be 24–48 hours, that means roughly 4–12 hours — long enough to cover it without re-dosing gaps, short
enough to clear before it becomes pure off-target exposure. This spec cannot be fixed until the
window is measured.

---

## The Provocation

### Lever 1: Hypoxia signaling — the strong one

**This is the finding the strategy rests on.** Healthy and leukemic cells respond to low oxygen in
*opposite directions*:

- **Normal cells down-regulate CXCR4** under hypoxia, via a post-transcriptional mechanism driven by
  miR-146a.
- **Primary AML blasts fail to do this** — the miR-146a/CXCR4 mechanism is dysregulated in them, so
  they keep CXCR4 high.

**Separation widens in both directions at once.** Cancer holds or rises, healthy cells fall. That
beats a lever that merely raises both.

Mechanistic basis: the CXCR4 promoter carries four hypoxia-response elements (HREs) within 2.6 kb
upstream of the transcription start site, plus one intronic — CXCR4 is genuinely a hypoxia-responsive
gene. Independently confirmed: CXCR4 expression and biologic activity in AML depend directly on
oxygen partial pressure.

**Scope caveat:** the differential miR-146a finding comes from monocytic cells and AML-M5, partly in
cell lines. Whether it generalizes across AML subtypes is the first thing to test.

**How to induce it without making the patient hypoxic:** use a **prolyl hydroxylase (PHD) inhibitor**
— roxadustat or daprodustat, already approved for anemia of chronic kidney disease. These stabilize
HIF-1α pharmacologically, mimicking the hypoxic signal. A drug-repurposing play in the spirit of
[brainstorm-topics.md](../brainstorm-topics.md) Idea 7.

**A second benefit:** hypoxia is *protective* for normal HSCs — mice housed at 10% O₂ show better HSC
function than at room air. So the same lever that widens targeting separation also shelters the cells
we're trying to preserve. Both effects push the same way.

**The risk that doesn't go away:** HIF-1α also drives pro-survival and stemness programs in cancer.
This could strengthen the leukemia while illuminating it. Single biggest unknown in the strategy.

### Lever 2: Chemotherapy — weaker, but free

Standard cytotoxic chemotherapy induces dynamic upregulation of surface CXCR4 on leukemia cells — a
documented resistance mechanism. Cells that upregulated were differentially protected from apoptosis
when co-cultured with stroma.

**Limitations:** upregulation is *variable*, not universal, and the comparison against normal CD34+
cells isn't established. Without that, we don't know whether chemo widens the separation or just
shifts everything up together.

**Dosing note:** the goal here is **signal, not kill** — enough stress to trigger the upregulation
response, not enough to cause cytotoxic damage. A far lower dose than therapeutic chemo, which makes
marrow toxicity from the provocation step much more manageable than "give chemo" implies.

Chemo is the weaker lever but costs nothing extra, since patients are receiving it anyway.

---

## Timing: How We Know When to Strike

Striking blind is not an option — and provoking *without* striking actively harms the patient (see
Risks). Two layers:

### Layer 1 — ⁶⁸Ga-Pentixafor PET, to calibrate the protocol

**Pentixafor** is a PET imaging tracer that binds CXCR4, already used in AML patients. Tracer uptake
correlated with leukemia infiltration on MRI in 5 of 10 patients, and specificity is clean — signal
vanishes in CRISPR CXCR4-knockout xenografts.

That gives a **whole-body, quantitative, non-invasive readout of CXCR4 density** — no marrow biopsy,
no blood-sampling problem.

**Limitation:** PET images bulk disease. Our actual target — post-remission residual cells — is almost
certainly below detection.

**Workaround:** run PET in *active-disease* patients to map the kinetic curve (how fast CXCR4 rises,
when it peaks, how long it holds), then apply that fixed schedule in the residual-disease setting.
**PET calibrates the protocol; it doesn't guide each individual patient.**

**Bonus:** only 5 of 10 patients lit up. That's not a failure — that's patient selection. PET-positive
patients are the ones this strategy can work for. A companion diagnostic, already built.

### Layer 2 — Erythropoietin as the cheap real-time gate

**You don't have to measure CXCR4 directly in each patient.** If roxadustat is the provocateur,
erythropoietin (EPO) rises as a well-characterized pharmacodynamic marker of HIF stabilization,
peaking at ~6 hours.

EPO is a routine blood test. So you confirm "the provocation took" with a cheap, fast, repeatable
assay, and infer CXCR4 is climbing from the Layer 1 curve.

**Roxadustat kinetics:** peak PD response at ~6h; PHD inhibition sustained ≥24h; half-life 2–3 days;
reversible.

---

## Where This Fits in a Real Patient's Course

| When | What happens | Leukemic burden |
|---|---|---|
| **Day 0** | Diagnosis — marrow biopsy shows >20% blasts; genetic profiling assigns risk group | ~10¹² cells |
| **Days 1–7** | Induction ("7+3": cytarabine ×7 days, anthracycline ×3) | falling |
| **Days 8–28** | **Aplasia** — counts crash, neutropenic, transfusion-dependent, high infection risk | ↓ |
| **~Day 28** | Marrow biopsy; <5% blasts = **complete remission (CR)** | **~5×10⁹ remain** |
| **Months 1–6** | Consolidation — 2–4 cycles high-dose cytarabine (1 week on, ~3 weeks recovering), or transplant | ↓ |
| **Months 6–24** | Surveillance, or relapse. Most relapses occur in year one. | 0, or back to 10¹² |

**The number that matters: complete remission is only a ~200-fold reduction.** Start at a trillion
cells, divide by 200, and billions remain. "CR" means the leukemia is invisible on a slide — not that
it's gone. MRD testing goes deeper (flow ~1 in 10⁴; molecular ~1 in 10⁵–10⁶), but a significant
proportion of MRD-negative patients still relapse, because LSCs specifically are what the panels miss.

**What's happening to the hard grippers meanwhile:** induction kills dividing cells; the hard grippers
are dormant in the niche and mostly untouched — while chemo simultaneously upregulates their CXCR4.
Every consolidation cycle is another round of selection. By the time a patient is "in remission on
consolidation," the residual population isn't a smaller copy of the original leukemia — it's the
toughest slice of it, concentrated.

### Insertion point: after consolidation completes, as maintenance

Two reasons it belongs post-remission at all:

1. **Residual disease is at its minimum** — fewest cells to kill.
2. **Those cells are maximally enriched** for our target phenotype, so a hard-gripper-selective drug
   has its best hit rate.

And one hard constraint that pushes it later than expected:

3. **The engager borrows the patient's NK cells — they have to be functional.** The drug is a
   molecular clamp: it grabs an NK cell with one arm and a leukemia cell with another and forces
   contact. It kills nothing on its own. No working NK cells, no effect.

### NK reconstitution: why the window opens at ~6 weeks, not 3

| Timepoint | NK status |
|---|---|
| Days 8–28 (aplasia) | Effectively absent — therapy is unusable here |
| "A few weeks" post-chemo | Activating receptor expression partially restored |
| **~6 weeks post-chemo** | **Degranulation (the killing function) recovered; cytokine production still low** |

**That split is favorable.** The function we need — degranulation, releasing perforin and granzyme —
is the one that came back. The function driving **cytokine release syndrome**, our main
dose-limiting toxicity, is still suppressed. There may be a window where NK cells kill effectively
while being less prone to a runaway cytokine response.

**Baseline handicap:** AML actively suppresses NK cells. They're the most severely depleted
lymphocyte population at diagnosis, and leukemia-induced NK defects predict failure to achieve
remission. This is precisely why the TriKE format carries **IL-15** — that module exists to expand
and reactivate NK cells rather than assuming healthy ones are on hand.

**Scheduling conflict this creates:** consolidation cycles run roughly monthly; NK function needs
~6 weeks. Those don't fit — there may be no clean gap between cycles. **Hence maintenance rather than
inter-cycle:** after consolidation completes, no next cycle bearing down, NK function fully
recovered, residual disease still minimal.

### One treatment cycle

| Hour | Action |
|---|---|
| 0 | Provocation dose — oral roxadustat |
| ~6 | EPO blood test — confirm HIF stabilized. **Go/no-go gate.** |
| 12–24 | Begin infusion of the tetraspecific engager |
| 24–48 | NK-mediated killing — hours, not days |
| Days 3–5 | Washout (roxadustat half-life 2–3 days) |
| Then | Repeat on a maintenance schedule |

**Alternative insertion point worth considering:** run it *during* induction, when chemo is already
provoking CXCR4 for free — striking the hard grippers before they're selected and concentrated rather
than hunting them afterward.

**Why it doesn't work for this drug:** the patient is heading into aplasia, so NK cells vanish exactly
when the provocation window opens. The provocation and the striker cancel each other out. This is
the right idea for a mechanism that brings its *own* killing power and doesn't depend on the patient's
immune system — a radioligand (¹⁷⁷Lu-Pentixather), an antibody-drug conjugate, or a direct cytotoxic
payload. Worth pursuing as a separate arm.

---

## Does This Drug Already Exist?

**No — but it's one arm away from something that does.**

### What already exists

**The closest relative — CD16-IL15-CLEC12A TriKE.** A trispecific NK engager where CLEC12A *is*
CLL-1. Published work reports it drives NK expansion, activation, and "antigen-specific killing of
**cancer stem cells** in acute myeloid leukemia." Our antigen, our target population, preclinical
data in hand. This is the scaffold to build on.

**The engager format itself.** BiKE (bispecific killer engager) and TriKE platforms are established.
The CD16-IL15-CD33 TriKE showed *superior killing kinetics* versus the two-arm BiKE version, and the
anti-CD16 arm binds NK cells with higher affinity than natural Fc–CD16 binding. The IL-15 module was
added specifically to overcome cancer-induced immune suppression.

**The provocation drugs.** Roxadustat and daprodustat are FDA-approved PHD inhibitors for anemia of
chronic kidney disease — well-characterized kinetics, existing human safety data. Standard
chemotherapy is a second, free provocation lever (documented CXCR4 upregulation).

**The imaging.** ⁶⁸Ga-Pentixafor PET images CXCR4 density in AML patients, with clean specificity
(signal vanishes in CRISPR CXCR4-knockout xenografts). Its therapeutic partner ¹⁷⁷Lu/⁹⁰Y-Pentixather
has first-in-human data in multiple myeloma — a complete theranostic pair.

**The selectivity engineering.** Affinity-tuned binders that discriminate by antigen density are
demonstrated on CD123, mesothelin, and GPC2. AND-gate constructs for AML exist preclinically —
CD33+CLL-1 and CD13+TIM-3 pairs.

**CXCR4 as a target.** Anti-CXCR4 CAR-T shows potent anti-leukemic activity in AML and ALL
preclinically — but is positioned as *transplant conditioning*, meaning the field already concedes
CXCR4 alone is too toxic to use standalone. That's evidence the gate is necessary, not optional.

**Supporting finding.** Engineering CAR-T cells to co-express extra CXCR4 improves marrow homing,
drives memory over exhaustion, and enhances anti-leukemic activity — reinforcing that CXCR4-directed
homing into the niche works.

### Summary table

| Component | Status |
|---|---|
| CD16-IL15-CLEC12A TriKE (NK engager vs. CLL-1) | **Exists** — preclinical, kills AML cancer stem cells |
| NK engager format (TriKE/BiKE) | Established; better kinetics than two-arm |
| Roxadustat / daprodustat | FDA-approved (anemia of CKD) |
| Chemo-induced CXCR4 upregulation | Documented |
| ⁶⁸Ga-Pentixafor PET | Exists; used in AML patients |
| ¹⁷⁷Lu/⁹⁰Y-Pentixather | First-in-human (multiple myeloma) |
| Anti-CXCR4 CAR-T | Preclinical (AML/ALL), as transplant conditioning |
| Affinity-tuned density-threshold binders | Demonstrated (CD123, mesothelin, GPC2) |
| AND-gate constructs for AML | Preclinical (CD33+CLL-1, CD13+TIM-3) |
| **Tetraspecific: CD16 + CLL-1 + tuned CXCR4 + IL-15** | **Does not exist** |
| **HIF stabilization used deliberately to raise target density** | **Not found** |
| **A strike timed to a provoked density window** | **Not found** |
| **Any of this aimed at dormant persisters rather than bulk blasts** | **Not found** |

### What we'd actually build

1. **One molecule** — add an affinity-tuned CXCR4 arm to the existing CD16-IL15-CLEC12A TriKE. Every
   component is proven separately; nobody has assembled this one.
2. **The kinetics experiment** — how fast CXCR4 rises after provocation, when it peaks, how long it
   holds. The real unknown, and it determines the drug's core engineering spec (half-life).

Low technical risk on every component; the novelty is in the assembly and the timing.

---

## Why This Composes With the Collateral-Sensitivity Trap

A cell facing a threshold-gated drug has one escape route: shed target protein. But grip *depends* on
having lots of CXCR4/CD44 — shed them and the cell can't hold the niche, loses its dormancy brake,
and loses stromal chemoprotection. It becomes an ordinary dividing cell, which is exactly what
standard chemo kills.

That's **collateral sensitivity** (resistance to one drug creating vulnerability to another),
deliberately engineered as an **evolutionary double bind**. Keep the hooks → the engager kills you.
Drop them → chemo kills you.

**Design consequence: give the engager *with* chemo, not after it.** The trap needs both jaws present.

---

## Risks and Open Threads

- **HIF stabilization may help the cancer.** HIF-1α drives pro-survival and stemness programs.
  Biggest unknown; needs direct testing before anything else.
- **Roxadustat may suppress the killer cells.** It's been studied for *reducing* graft-versus-host
  disease — meaning HIF stabilization dampens immune-mediated killing. Could suppress our own NK
  response. May favor chemo as the provocation lever when pairing with an immune effector.
- **Provoking without striking makes things worse.** You'd have raised CXCR4 = tighter grip = more
  chemoresistance. If the strike misses the window, you've actively helped the leukemia. This is why
  the kinetics study is non-negotiable.
- **Cytokine release syndrome (CRS).** Engagers cause it, and it scales with how hard and fast you
  activate immune cells. Step-up dosing manages it but lengthens the ramp — directly fighting the
  narrow-window goal. Possible resolutions: step up in early cycles then hit hard once the patient's
  cytokine response is characterized, or pre-medicate with tocilizumab (IL-6 blocker).
- **Provocation deepens the hiding place.** More CXCR4 = tighter grip = further into the
  poorly-perfused endosteal niche. Partly mitigated because NK cells actively migrate rather than
  passively diffusing, but it's a real tension: the drug becomes more *visible* to the target and
  less *accessible* to it simultaneously.
- **Does the miR-146a differential generalize** beyond monocytic/AML-M5 lineages?
- **Receptor internalization as a fake-out.** A cell can transiently pull the receptor inside itself
  to duck below threshold, then re-express it — hiding without paying the chemo-vulnerability price.
  Testable: does a cell that drops below threshold actually become chemo-sensitive, or just
  temporarily invisible?
- **Intrinsic dormancy leaks the trap.** Cells quiescent via p21/p27 rather than niche grip could
  shed the hooks *and* stay chemo-resistant, slipping both jaws.
- **Patient heterogeneity.** Primary AML spans ~557–11,726 CD123 molecules/cell; CXCR4 likely varies
  similarly. A fixed threshold can't fit everyone — forces a companion diagnostic and possibly a
  small panel of variants at different thresholds.
- **Low affinity narrows the escape margin.** Because the drug needs high density, modest antigen
  downregulation drops cells below threshold. Selectivity bought at the cost of a thinner margin.

---

## Sources

- [Differential hypoxic regulation of the miR-146a/CXCR4 pathway in normal and leukemic cells](https://haematologica.org/article/view/7491)
- [CXCR4 expression and biologic activity in AML are dependent on oxygen partial pressure](https://pmc.ncbi.nlm.nih.gov/articles/PMC2644078/)
- [Dynamic chemotherapy-induced upregulation of CXCR4: a resistance mechanism in pediatric AML](https://aacrjournals.org/mcr/article/11/9/1004/89410/Dynamic-Chemotherapy-Induced-Upregulation-of-CXCR4)
- [CD16-IL15-CLEC12A TriKE drives NK killing of AML cancer stem cells](https://ashpublications.org/blood/article/132/Supplement%201/1454/272874/CD16-IL15-CLEC12A-Trispecific-Killer-Engager-TriKE)
- [CD16-IL15-CD33 TriKE — enhanced killing kinetics in MDS and AML](https://www.sciencedirect.com/science/article/pii/S0006497119342922)
- [Targeted PET imaging of CXCR4 expression in patients with AML](https://pmc.ncbi.nlm.nih.gov/articles/PMC4967572/)
- [Balance of anti-CD123 CAR binding affinity and density for targeting AML](https://pmc.ncbi.nlm.nih.gov/articles/PMC5542631/)
- [Affinity-tuned CARs spare normal cells](https://www.genengnews.com/topics/drug-discovery/affinity-tuned-car-t-cells-slay-tumor-cells-spare-normal-cells/)
- [T cell circuits that sense antigen density with an ultrasensitive threshold](https://limlab.ucsf.edu/pdfs/hernandez-lopez_2021.pdf)
- [Logic-gated CAR T cells against AML — current status](https://doi.org/10.3390/lymphatics4020031)
- [CXCR4 induces memory formation over exhaustion in CAR-T cells](https://www.nature.com/articles/s41467-025-67745-x)
- [Eradication of measurable residual disease in AML: a challenging clinical goal](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8268140/)
- [Kinetics of cytotoxic lymphocyte reconstitution after induction chemotherapy in AML](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5288405/)
- [Leukemia-induced NK cell defects predict failure to achieve remission in AML](https://pubmed.ncbi.nlm.nih.gov/24488563/)
- [NK cell defects: implication in acute myeloid leukemia](https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2023.1112059/full)
