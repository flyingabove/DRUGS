# Strategy 4: Tag Then Burrow

**One line:** stop trying to tell leukemic stem cells from healthy ones. **Tag every stem cell in the
marrow for extermination** — LSC and HSC alike — using a payload that kills on its own schedule
regardless of where the cell hides. Then rebuild the entire blood system from a graft.

**Graft only.** There is no version of this that works without a transplant.

Related: [Strategy 1: Nuke Everything and Replace](nuke-everything-and-replace.md) shares the
graft-dependency logic but solves it by shielding the graft genetically. This one solves it by
choosing when and how to tag.

---

## The Core Logic

Every "cure in place" strategy in this project runs into the same wall: LSCs and normal HSCs are too
similar to reliably tell apart. We spent enormous effort on density thresholds, AND-gates, and
affinity tuning — all of it machinery to protect healthy stem cells.

**If a graft is coming, that machinery is unnecessary.** Kill everything in the stem compartment.
The graft replaces it.

That single decision dissolves the hardest problem in the project — and unlocks a much harder-hitting
approach than anything selectivity-constrained.

---

## Why the Payload Must Be Autonomous

The critical design requirement: **binding is not killing.** If the payload acts by itself once
attached, it doesn't matter where the cell goes afterward. You don't need to reach into the niche —
you need to have already been there when the tag went on.

| Payload | Autonomous? | Why it matters |
|---|---|---|
| **Radioconjugate** | ✅ | Decays on its own schedule wherever the cell ends up |
| **Antibody-drug conjugate (ADC)** | ✅ | The cell internalizes it and releases the toxin inside itself |
| **Engager (TriKE / BiTE)** | ❌ | Requires an NK or T cell to physically arrive later — the niche access problem stays fully intact |

**This rules out the engager design** developed in [Strategy 3](provoke-then-strike.md). It's the one
format that cannot do "tag early, kill later."

### Crossfire: the reason radioconjugates beat ADCs here

A beta-emitting isotope kills cells within a **radius**, not just the one it's attached to:

| Isotope | Mean range | Max range |
|---|---|---|
| **Lu-177** | ~0.2 mm | ~1.8 mm |
| **Y-90** | ~2.5 mm | ~11 mm |
| **Ac-225** (alpha) | ~0.05–0.1 mm | very short, far more lethal per hit |
| **I-131** | ~0.4 mm | ~2 mm |

**You don't have to bind every cell — you have to get near them.** A radioconjugate attached to
accessible cells irradiates the surrounding niche, killing cells that were never tagged and could
never have been reached by any drug.

This is the direct answer to the niche penetration problem that blocked every other strategy. For
marrow, I-131 or Lu-177 gives enough range to cover a niche pocket without irradiating the whole body.

---

## The Timing Insight: Tag Before They Burrow

**Before chemotherapy, CXCR4 is at baseline.** Chemo is what drives it up — that's a documented
resistance mechanism. Lower CXCR4 means:

- Weaker grip on the marrow
- Shallower burrowing
- **Better physical access**

So pre-treatment cells are genuinely easier to reach than post-treatment survivors. Tag them while
they're still shallow; let them burrow afterward, tagged and already dying.

### This directly contradicts Strategy 3, and that's fine

| Approach | Wants CXCR4 | Because |
|---|---|---|
| [Provoke-then-strike](provoke-then-strike.md) | **High** | A threshold-gated binder needs density to fire selectively |
| **Tag-then-burrow** | **Low** | Better physical access before the cell grips down |

They're incompatible, and which is correct depends entirely on the agent:

- **Threshold-gated agent** (needs density to discriminate) → provoke first, accept worse access.
- **High-affinity autonomous agent** (binds at any density, kills by itself) → **strike early, when
  access is best.**

Because this strategy has a graft covering the marrow, selectivity is not a constraint — so there is
no reason to provoke, and every reason to tag while cells are still shallow.

---

## This Already Exists — the Mechanism Works, the Clinical Benefit Is Unproven

**Iomab-B (¹³¹I-apamistamab)** is an anti-CD45 antibody carrying iodine-131. CD45 is pan-hematopoietic
— present on essentially all blood cells, healthy and leukemic. It is precisely "tag everything for
extermination, graft only."

### SIERRA trial (randomized Phase 3)

Population: relapsed/refractory AML, median age 65, **median 3 prior lines of therapy** — about the
hardest population that exists.

**What worked:**

| Outcome | Iomab-B arm | Conventional care |
|---|---|---|
| **Durable complete remission** (primary endpoint) | **22% (13/76)** | **0% (0/77)**, p<0.0001 |
| Reached transplant and engrafted | 100% (31/31) | 18% (7/38) |
| Event-free survival | **HR 0.22**, p<0.0001 | — |
| 100-day non-relapse mortality | 6% | — |
| Treatment-related deaths | None | — |

Conventional care produced **zero** durable remissions in that population. Iomab-B also uses
**personalized dosimetry** — measuring actual radiation dose delivered per patient before the
therapeutic dose — which is the quantitative per-patient targeting this project kept speculating
about, already in clinical practice.

**What didn't work:**

- **The FDA determined the SIERRA data are not adequate to support a BLA filing.** They advised
  demonstrating an **overall survival** benefit in a randomized head-to-head trial first.
- **Iomab-B is not approved.**

### Why the gap, and what it means for this project

Likely contributors: the trial permitted crossover (control-arm failures could receive Iomab-B),
which dilutes any survival signal; a population with a median of three prior therapies has overall
survival dominated by everything else going wrong; and 13 patients achieving durable remission is a
thin base on which to move a survival curve.

**The uncomfortable implication.** Every strategy in this project rests on an implicit chain:

> kill lingering LSCs → prevent relapse → patient lives longer

Iomab-B is a partial real-world test of that chain, and **the last link did not demonstrate.** It
cleared the target population effectively and produced remissions that otherwise did not occur, and
overall survival still did not move enough to satisfy the FDA.

That is not proof the premise is wrong — a heavily pretreated relapsed/refractory cohort is close to
the worst possible setting in which to detect a survival benefit, which reinforces this project's
recurring observation that these agents keep being tested in the wrong patients. But it does mean
**"we killed more LSCs" is not automatically a win**, and any design produced here must be honest
about the distance between that and a patient living longer.

---

## What's Actually New in Our Version

Honest accounting: the strategy itself is precedented and validated. Three narrower additions:

**1. Timing — tag at diagnosis, not at conditioning.** Iomab-B is given to relapsed/refractory
patients as conditioning immediately before transplant, after cells have already been driven deep by
prior therapy. Tagging *before* the first chemotherapy — while CXCR4 is at baseline and cells are
shallow — has not been tried. This is the core "tag then burrow" claim.

**2. Repeatability via an epitope-edited graft.** Iomab-B is one-shot conditioning. Combine it with a
graft base-edited at the target epitope ([Strategy 1](nuke-everything-and-replace.md)) and the agent
can be **re-dosed indefinitely after transplant** as long-term surveillance — killing any residual
LSC that surfaces without touching the graft. Converts a one-shot procedure into an ongoing therapy.
This is the trem-cel model (CD33-deleted graft + gemtuzumab maintenance) applied to a radioconjugate.

**3. Target choice.** CD45 is pan-hematopoietic, which is appropriate for "tag everything." But a
second, LSC-enriched radioconjugate (CLL-1, or CXCR4 via Pentixather) layered on top would
concentrate additional dose specifically where LSCs sit — using crossfire to cover the niche pocket
around them.

---

## Risks and Open Threads

- **Radiation is radiation.** This strategy explicitly reintroduces what
  [Strategy 3's](provoke-then-strike.md) conditioning discussion argued for removing — secondary
  cancers, infertility, late organ effects. The counterargument is that it's *targeted* radiation
  concentrated on the blood compartment rather than whole-body, and the SIERRA safety data (no
  treatment-related deaths, 6% non-relapse mortality) supports that. But it's a real tension between
  strategies.
- **Requires a transplant** — so it addresses ~21% of AML patients, though targeted conditioning may
  expand that number by making more patients eligible.
- **Tagging at diagnosis means committing to transplant at diagnosis.** You'd be destroying the
  marrow of a patient who might have achieved remission and never needed a transplant. That's a
  serious ethical and clinical problem with the timing innovation, and possibly disqualifying —
  it would need to be restricted to patients already identified as high-risk and transplant-bound.
- **Isotope supply and handling.** Radiopharmaceuticals require specialized facilities, licensing,
  and short-shelf-life logistics — the same access constraint that argued against total-body
  irradiation.
- **Epitope editing only defeats biologics** — but here the *targeting* is a biologic (the antibody),
  so editing the epitope does shield the graft. The radiation crossfire, however, is indiscriminate
  and would still hit an edited graft within range. **Post-transplant re-dosing may not be as clean
  as the ADC/engager version of this idea.** Needs modeling.

---

## Sources

- [Randomized Phase III SIERRA Trial of ¹³¹I-Apamistamab before allogeneic HCT vs conventional care (JCO)](https://ascopubs.org/doi/10.1200/JCO.23.02018)
- [SIERRA results do not support BLA filing for ¹³¹I-apamistamab in R/R AML](https://www.cancernetwork.com/view/sierra-results-do-not-support-bla-filing-for-131i-apamistamab-in-r-r-aml)
- [Targeted conditioning with Iomab-B leads to high rates of transplantation and engraftment](https://www.sciencedirect.com/science/article/abs/pii/S1083879119315046)
- [Personalized dosimetry using ¹³¹I-anti-CD45-apamistamab prior to myeloablative radioimmunotherapy](https://jnm.snmjournals.org/content/60/supplement_1/434)
- [SIERRA clinical experience — engraftment and safety in R/R AML](https://www.sciencedirect.com/science/article/pii/S0006497121037551)
- [Targeted PET imaging of CXCR4 expression in AML (Pentixafor)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4967572/)
- [Dynamic chemotherapy-induced upregulation of CXCR4 in pediatric AML](https://aacrjournals.org/mcr/article/11/9/1004/89410/Dynamic-Chemotherapy-Induced-Upregulation-of-CXCR4)
- [CD33-deleted allo-HCT with gemtuzumab maintenance, phase 1/2 (Nature Medicine 2026)](https://www.nature.com/articles/s41591-026-04362-1)
