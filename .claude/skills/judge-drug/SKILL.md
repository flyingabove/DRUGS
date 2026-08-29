---
name: judge-drug
description: Score the current drug candidate against the criteria that decide whether it becomes a real medicine. Use after any iteration of drug design work, or when asked for drug status. Produces a plain-language status table.
---

# Judge the drug

Scores the current candidate on the things that actually kill drug programmes. **Show this table after
every iteration of work.** The user has no biology background — every row must read in plain English.

## Scoring

Each criterion gets a **status** and a **one-line reason with the number behind it**.

| Symbol | Meaning |
|---|---|
| ✅ | **Settled.** Measured or established. Would survive challenge from an expert |
| 🟢 | **Good, with a caveat.** Evidence is real but indirect, modelled, or inherited from a parent compound |
| 🟡 | **Unknown.** Not yet answered. Neither good nor bad news — just open |
| 🟠 | **Problem.** Real liability with a known path to fixing it |
| 🔴 | **Blocker.** Would stop the programme if not solved |
| ⬛ | **Unanswerable by computation.** Needs a lab or an animal. Say so; never fake it |

**Rules:**
- **Never score from an assumption.** If the evidence is a model, say "modelled". If it is inherited
  from the parent compound, say "inherited". If it is a guess, it is 🟡.
- **A criterion that no computation can settle is ⬛, not 🟡.** Distinguish "we don't know yet" from
  "this can only be answered by an experiment."
- Include the actual number wherever one exists. "Poorly soluble" is useless; "0.03 mg/mL, need >1" is
  a decision.
- When a score changes, say **what changed it**.

## The criteria

| # | Criterion | The question in plain terms |
|---|---|---|
| 1 | **Kills the target cells** | Does it actually kill the cancer stem cells that cause relapse? |
| 2 | **Doesn't kill the patient** | Is there a dose that hurts the cancer more than the person? |
| 3 | **Stays killed** | Does the cancer come back resistant, and how fast? |
| 4 | **Hits only what it should** | Does it attack the intended target, or everything similar to it? |
| 5 | **Can be made** | Can a chemist actually synthesise it, at reasonable cost and purity? |
| 6 | **Can be delivered** | Can it be dissolved, injected or swallowed, and reach the bone marrow? |
| 7 | **Can be taken forever** | Is it tolerable daily for months — the whole point of a maintenance drug? |
| 8 | **Is it new** | Does it already exist? Is there something to own and defend? |
| 9 | **Would a regulator approve it** | Does it extend survival, not just improve a lab number? |

**Criterion 9 is the one that kills approved-looking drugs.** Iomab-B hit its primary endpoint at
p<0.0001 and was refused filing because it did not extend survival. Any status table that looks good on
1–8 and ignores 9 is misleading.

## Output format

Always this shape:

```
### Drug status — <compound name>, <date>

| # | Criterion | Status | Where it stands |
|---|---|---|---|
| 1 | Kills the target cells | 🟢 | <one line, with the number> |
...

**Biggest problem right now:** <one sentence>
**Next thing that would move a score:** <one sentence, and which score it moves>
**Changed since last time:** <what moved, or "nothing">
```

Close with those three lines every time. They are what makes the table actionable rather than
decorative.

## Honesty requirements

- **Do not average the scores into a single number.** One 🔴 outranks eight ✅. A drug that cannot be
  delivered does not become deliverable because it is easy to synthesise.
- **Do not let a good score drift upward without new evidence.** If nothing changed, say "unchanged".
- **State the strongest argument against the drug** in the "biggest problem" line, even when the rest of
  the table looks healthy. The purpose of this table is to find the thing that stops the programme, not
  to reassure.
