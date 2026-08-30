---
name: judge-drug
description: Score the current drug candidate against the eight criteria that decide whether it becomes a real medicine, using explicit evidence-based standards anchored to actual FDA approval precedent. Use after any iteration of drug design work, or when asked for drug status. Produces a plain-language status table.
---

# Judge the drug

Scores the current candidate on the things that actually kill drug programmes. **Show this table after
every iteration of work.** The user has no biology background — every row must read in plain English.

## Symbols

| Symbol | Meaning |
|---|---|
| 🟢 | **Good.** Meets the standard below on real evidence |
| 🟡 | **Acceptable / open.** Meets a weaker form of the standard, or rests on inheritance or modelling |
| 🟠 | **Problem.** Falls short, with a known path to fixing it |
| 🔴 | **Blocker.** Would stop the programme |
| ⬛ | **Needs a lab or an animal.** Use only where no computation could settle it — never as a synonym for "I have not checked" |

**Every score cites its evidence class:** *measured* (this compound), *inherited* (a close analog, with
the property gap stated), *modelled*, or *asserted*. **Asserted is never above 🟡.**

---

## The eight criteria and their standards

### 1. Eliminates the target cells

| | Standard |
|---|---|
| 🟢 | **This compound** measurably kills primary patient LSCs, or irreversibly matures them with demonstrated loss of self-renewal/leukemia-initiating capacity |
| 🟡 | Activity is inherited from a close analog, the exact activity-critical features are preserved, and the property profile is compatible with reaching the target |
| 🟠 | Activity is inherited but a structural, reactivity, or intracellular-exposure gap makes retention doubtful |
| 🔴 | Evidence it leaves functional LSCs alive, or only changes maturation markers without abolishing leukemia initiation |

This is the programme's first gate. Never raise another property to distract from a non-green row 1.
Until row 1 is green, `Next thing that would move a score` must name the shortest decisive efficacy
experiment or exact-compound evidence search, not a solubility or safety optimization.

### 2. Doesn't kill the patient

| | Standard |
|---|---|
| 🟢 | No structural toxicity alerts beyond those inherited from a clinically-precedented class; predicted dose-limiting toxicity is monitorable and manageable |
| 🟡 | One manageable liability, or the dose-limiting toxicity is predicted but unverified |
| 🟠 | Several liabilities, or a predicted toxicity that cannot be routinely monitored |
| 🔴 | Structural alert for a severe toxicity with no mitigation |

*The therapeutic index itself is ⬛ — no computation gives a maximum tolerated dose.*

### 3. Extends life enough to matter — **anchored to real approval precedent**

**The only currency is overall survival — how long the patient lives.** Every other measurement is a
surrogate, and surrogates have failed here before.

#### The official language, verbatim

> "Overall survival is defined as the time from randomization until death from any cause. **Survival is
> considered the most reliable cancer endpoint**, and when trials can be conducted to adequately assess
> survival, it is the preferred endpoint."
> — FDA, *Clinical Trial Endpoints for the Approval of Cancer Drugs and Biologics* (2018)

> Accelerated approval may be granted where a drug has an effect on "a surrogate endpoint that is
> **reasonably likely to predict clinical benefit**", subject to a required confirmatory trial.
> — FDCA §506(c) / 21 CFR 314.510

**Note what is absent from both: any number.** No months, no hazard ratio, no percentage.

#### What the FDA actually requires — and what it does not

**The FDA publishes no numerical threshold.** There is no rule saying "X months of survival is enough".
Approval turns on a case-by-case judgement of *clinically meaningful benefit*. Anyone quoting a fixed
number is quoting a convention, not a regulation — **including the 2.5-month figure used earlier in this
skill, which is ASCO's yardstick, not the FDA's.**

What the FDA does provide:

| Source | What it says |
|---|---|
| **Guidance: Clinical Trial Endpoints for the Approval of Cancer Drugs and Biologics** (2005, rev. 2018) | Defines acceptable endpoints. **Overall survival is the gold standard** — unambiguous, not subject to assessment bias |
| **Accelerated approval pathway** | Permits approval on a surrogate **"reasonably likely to predict clinical benefit"**, with a confirmatory trial required afterwards |
| **Draft guidance: Approaches to Assessment of Overall Survival in Oncology Clinical Trials** | Pushes sponsors to collect and analyse survival data even when it is not the primary endpoint |
| **Recent direction** | A "one trial" design powered for **both** a surrogate and overall survival |

So there are two doors, and they demand different things:

- **Regular approval** — demonstrate clinical benefit. In practice, overall survival.
- **Accelerated approval** — a surrogate reasonably likely to predict benefit, then confirm it.

#### The three yardsticks, ranked by authority

| Yardstick | Status | Number |
|---|---|---|
| **Precedent in the same indication** | **strongest** — an actual decision by the actual regulator | QUAZAR: **+9.9 months** overall survival → approved for AML maintenance |
| **Empirical approval pattern** | observed, not mandated | hazard ratio **≤ 0.80** for overall survival ≈ 50% probability of approval |
| **ASCO clinically-meaningful threshold** | professional-society **recommendation**, not regulation | ≥2.5 months absolute **and** ≥25% relative |

**Score against precedent first.** A drug in AML maintenance is judged against what was actually approved
in AML maintenance, not against a generic number.

#### The decision procedure

Ask these in order and stop at the first that applies:

| Ask | Answer | Score |
|---|---|---|
| **1.** Does the disease stop coming back — patients die of something else? | yes | 🟢 **cure** |
| **2.** Does overall survival improve by an amount comparable to what was approved in this indication (AML maintenance: ~10 months; hazard ratio ≤0.80), statistically significant, in the primary analysis? | yes | 🟡 **approvable delay** |
| **3.** Does overall survival improve, but well short of that? | yes | 🟠 real but likely short of approval on its own |
| **4.** Does only a *surrogate* improve — remission rate, minimal residual disease, relapse-free survival — with no overall-survival gain? | yes | 🔴 **for regular approval.** Consider accelerated approval only if that surrogate is independently accepted as reasonably likely to predict survival in this disease |
| **5.** Nothing improves | — | 🔴 |

**Step 2 is the approval bar and a delay passes it.** Not curing is not failing.

#### The two precedents, with their real numbers

**QUAZAR AML-001 — oral azacitidine, approved September 2020.** Nobody was cured. Overall survival
**24.7 vs 14.8 months = +9.9 months** (67% relative). Relapse-free survival 10.2 vs 4.8. **Approved on
the survival gain.** This is what 🟡 looks like: a delay, reliably delivered, and it was enough.

**SIERRA — Iomab-B, refused filing.** Primary endpoint durable complete remission: **22% (13/76) vs 0%
(0/77), p<0.0001** — met overwhelmingly. **Overall survival hazard ratio 0.99 (95% CI 0.70–1.41,
p=0.96).**

**Iomab-B did not extend life a little. It extended life not at all.** A hazard ratio of 0.99 means the
two survival curves lie on top of each other. The FDA did not judge a small benefit insufficient — there
was no benefit to judge, and it required a head-to-head trial showing overall survival before it would
consider a filing.

#### How 22% durable remission produces zero survival benefit

**Because the treatment kills people too.** Iomab-B delivered targeted radiation before a bone-marrow
transplant. Some patients got a durable remission they would never otherwise have had. Others died of
the treatment. **Net effect on the population: zero.**

**This is the trap to internalise.** A drug can measurably cure some patients and still be worthless as
a medicine, because overall survival is a *net* figure and the treatment's own harm is subtracted from
it. Any score on this criterion that ignores the toxicity side is wrong.

#### Rules that follow

- **A surrogate endpoint scores nothing on its own.** Remission rate, minimal residual disease,
  leukaemia-stem-cell burden, relapse-free survival — all are 🔴 here unless a survival gain follows.
  QUAZAR's relapse-free gain counted *because* +9.9 months of survival came with it.
- **Post-hoc subgroups do not count.** Iomab-B showed a real-looking benefit in TP53-mutant patients
  (5.49 vs 1.66 months). It did not rescue the filing and must not rescue a score.
- **Score the primary analysis of the whole population**, not the best slice of it.
- **When scoring from a model, say so and state the discount.** A modelled relapse delay is not a
  measured survival benefit. QUAZAR's +5.4 months relapse-free became +9.9 months overall — an
  empirical relationship in one trial, not a conversion factor.

#### Scoring a compound that has never been in a patient

The procedure above interprets trial results. A preclinical compound has none, so score the **projection**
— and cap it, because a projection is not a result:

| Situation | Score |
|---|---|
| Modelled or inferred survival benefit clearing the bar, from a mechanism with a **surviving** precedent | 🟡 **maximum** |
| Projection rests only on a surrogate (tumour burden, stem-cell counts, remission depth) | 🟡 **and say so explicitly** — this is the Iomab-B failure mode |
| Projection needs optimistic assumptions to clear the bar | 🟠 |
| The mechanism has a precedent that failed on survival | 🟠 at best, and name the precedent |

**Never 🟢 before a survival readout exists.** Nothing preclinical can earn it.

**State the surrogate-to-survival gap every time.** If the whole case is "we reduce the cancer cell
count", that is precisely what Iomab-B proved at p<0.0001 while adding zero days of life. The gap
between killing measurable disease and extending life is where this criterion is won or lost, and it
cannot be closed by any amount of preclinical work.

### 4. Hits only what it should

| | Standard |
|---|---|
| 🟢 | Measured selectivity across a proteome-scale panel |
| 🟡 | Selectivity inherited from a compound with measured selectivity, **plus** a structural rationale for why it holds |
| 🟠 | Selectivity argued but a plausible off-target is unaddressed |
| 🔴 | Known off-target hit at comparable potency |

### 5. Can be made

| | Standard |
|---|---|
| 🟢 | Synthetic accessibility < 4, no unresolved stereocentres, ≤ 8 steps from catalogue materials |
| 🟡 | Accessibility 4–6, or stereocentres requiring resolution, or one step with real risk |
| 🟠 | Accessibility > 6, or a route with no precedent |
| 🔴 | No viable route |

### 6. Can be delivered

| | Standard |
|---|---|
| 🟢 | Soluble enough for the intended route **and** — for an intracellular target — inside the permeability range of drugs known to reach such targets |
| 🟡 | One of the two needs formulation work with clear precedent (salt, co-solvent, cyclodextrin) |
| 🟠 | A gap beyond routine formulation, or > 10× short on either axis |
| 🔴 | > 100× short with no salt handle and no formulation path |

**Both halves must be checked.** Solubility and permeability pull in opposite directions; a molecule
optimised for one silently fails the other.

### 7. Can be taken forever

| | Standard |
|---|---|
| 🟢 | No chronic-dosing liabilities: no cardiac pharmacophore, no accumulation risk, dose-response flat enough to use a low dose |
| 🟡 | One manageable chronic liability |
| 🟠 | Several, or requires monitoring that would limit real-world use |
| 🔴 | A liability incompatible with daily administration |

### 8. Is it new

| | Standard |
|---|---|
| 🟢 | Novel scaffold, or a novel target–mechanism combination; clear composition-of-matter space |
| 🟡 | Novel compound within a known scaffold, with a **defensible property advantage** over the disclosed art |
| 🟠 | Small edit to published art (≤ 2 changes); patentability doubtful |
| 🔴 | Already disclosed or claimed |

**Novelty of the *molecule* is what is scored here** — not novelty of the target, the combination, or
the biology, which are usually published. Say explicitly which parts are new and which are not.

---

## Removed criterion

**"Would a regulator approve it" was a scored row and has been removed.** It is the *output* of the
other eight, not an independent axis, and scoring it separately double-counted durability. The approval
bar now lives inside criterion 3, where it is testable. The overall read belongs in the closing lines,
not in a row of its own.

---

## Output format

```
### Drug status — <compound>, <date>

| # | Criterion | Status | Where it stands |
|---|---|---|---|
| 1 | Eliminates the target cells | 🟢 | <one line, with the number and the evidence class> |
...

**Biggest problem right now:** <one sentence>
**Next thing that would move a score:** <one sentence, naming which score>
**Changed since last time:** <what moved and why, or "nothing">
```

## Honesty requirements

- **Never average into a single number.** One 🔴 outranks seven 🟢. A drug that cannot be delivered does
  not become deliverable because it is easy to make.
- **No upward drift without new evidence.** If nothing changed, write "unchanged".
- **The "biggest problem" line must state the strongest argument against the drug**, even when the table
  looks healthy. This table exists to find what stops the programme, not to reassure.
- **Cite the evidence class in every row.** "Inherited from ML210" and "measured" are different claims
  and must not read the same.
