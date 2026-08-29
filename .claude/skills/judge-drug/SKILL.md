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

| | Standard |
|---|---|
| 🟢 | **Cure.** Durable remission; resistance does not emerge |
| 🟡 | **Reliable delay that clears the approval bar** — see below |
| 🟠 | Benefit clears the bar only under optimistic assumptions, or is unreliable |
| 🔴 | No survival benefit, or resistance emerges so fast the benefit is negligible |

**The bar, from actual precedent:**

- **ASCO clinically-meaningful threshold:** ≥ **2.5 months** absolute **and** ≥ **25%** relative
  improvement in overall survival
- **The direct AML-maintenance precedent — QUAZAR AML-001 (oral azacitidine, FDA approved Sept 2020):**
  overall survival **24.7 vs 14.8 months = +9.9 months**, relapse-free survival 10.2 vs 4.8. **Primary
  endpoint was overall survival, not a lab marker**
- **The cautionary precedent — Iomab-B:** hit its primary endpoint at p<0.0001 and was **refused filing
  for lack of survival benefit**

**So: a delay is not a failure.** A drug that reliably adds ~10 months of life is approvable and 🟡. A
drug that only improves a laboratory measurement is 🔴 regardless of how good that measurement looks.

**When scoring from a model, say so and state the discount.** A modelled relapse delay is not a measured
survival benefit — QUAZAR's +5.4 months relapse-free translated to +9.9 months overall survival, but
that relationship is empirical, not guaranteed.

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
