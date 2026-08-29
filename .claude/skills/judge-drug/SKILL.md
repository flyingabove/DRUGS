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

### 1. Kills the target cells

| | Standard |
|---|---|
| 🟢 | Measured killing of the actual target population by **this** compound |
| 🟡 | Inherited from a close analog with measured activity, **and** the property profile is compatible with reaching the target |
| 🟠 | Inherited, but a property gap makes reaching the target doubtful |
| 🔴 | Evidence it does not kill them |

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

#### The decision procedure

Ask these in order and stop at the first that applies:

| Ask | Answer | Score |
|---|---|---|
| **1.** Does the disease stop coming back — patients die of something else? | yes | 🟢 **cure** |
| **2.** Does overall survival improve by **≥2.5 months absolute AND ≥25% relative**, statistically significant, in the primary analysis? | yes | 🟡 **approvable delay** |
| **3.** Does overall survival improve, but below that threshold? | yes | 🟠 real but probably not approvable alone |
| **4.** Does only a *surrogate* improve — remission rate, minimal residual disease, relapse-free survival — with no overall-survival gain? | yes | 🔴 |
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
| 1 | Kills the target cells | 🟢 | <one line, with the number and the evidence class> |
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
