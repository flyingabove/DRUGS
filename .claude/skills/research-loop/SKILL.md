---
name: research-loop
description: Research one idea (or sweep all ideas) in docs/ to exhaustion — verify it exists, find whether it's been tried, find why it failed, isolate what's genuinely novel — then write findings back to the doc. Use when the user says "research X", "loop on X", "dig into the ideas", or wants existing claims verified/updated.
---

# Research Loop

Take an idea, research it until you hit a dead end, write findings back to its doc, move on.

## Arguments

- `research-loop <idea>` — loop on one idea (e.g. "provoke-then-strike", "ferroptosis", "CLL-1")
- `research-loop all` — sweep every idea in `docs/` and `docs/strategies/`
- `research-loop verify` — re-check existing claims in the docs for accuracy; correct what's wrong

## The Question Ladder

For each idea, work down this ladder. **Each answer determines the next search.** Do not skip
levels — the value is almost always at levels 3–5, not level 1.

1. **Does the mechanism exist?** Is the underlying biology real and independently established?
2. **Has anyone built a drug/tool for it?** Name it. Get the specific compound, not the concept.
3. **What's its clinical status?** Preclinical / Phase 1 / Phase 3 / approved / **discontinued**.
4. **If discontinued or rejected — why?** ← *The highest-value question in this ladder.* The reason
   reveals the field's own diagnosis of the bottleneck, which is usually more informative than any
   positive result. (This is how we learned GTB-3550 was replaced for **potency**, not safety — which
   directly challenged our density-gate design.)
5. **What endpoint did it actually hit, and which did it miss?** Distinguish "the mechanism works"
   from "patients lived longer." A trial can meet its primary endpoint and still fail. (Iomab-B: met
   durable-remission endpoint with p<0.0001, FDA still refused the filing for lack of overall
   survival benefit.)
6. **What's the failure mode?** Every approach has one. Find it before claiming the idea works.
7. **Does this contradict anything already in our docs?** If yes, resolve it explicitly — don't
   leave both claims standing.
8. **What's left that's genuinely novel?** State it as a specific gap, not a vague "combination."

## Stop Conditions (Dead Ends)

Stop looping on an idea when **any** of these is true:

- **Repetition** — three consecutive searches return sources you've already seen.
- **Needs an experiment** — the remaining question can't be answered from literature (e.g. "how fast
  does CXCR4 rise after provocation" — nobody has measured it). Record it as an open experiment.
- **Gap isolated** — you can state precisely what exists and what doesn't, in one sentence.
- **Refuted** — the premise is wrong. Record why; do not quietly drop it.

## Rules

**Verify before claiming novelty.** Never write "this doesn't exist" without searching for it
specifically. This project has been wrong about that more than once (anti-CXCR4 CAR-T existed;
CD16-IL15-CLEC12A TriKE existed; Iomab-B was already in Phase 3).

**Hunt the negative result.** Search terms like "discontinued", "why replaced", "did not meet",
"FDA", "terminated", "toxicity". Positive results are press-released; negative ones must be dug for
and are worth more.

**Correct prior overclaims.** If new evidence contradicts something already written in the docs, fix
the doc in the same pass. Say what changed and why. Don't leave a favorable half-truth standing.

**Separate mechanism from benefit.** "It killed the target cells" and "patients lived longer" are
different claims requiring different evidence.

**Note the population.** An agent tested in relapsed/refractory disease tells you little about how it
would perform in minimal residual disease. Record which population was studied — mismatch between
tested population and intended population is a recurring finding in this project.

## Output

For each idea researched, append or update a section in its doc:

```markdown
### Research status: <idea> (<date>)

**Mechanism:** established / contested / speculative
**Existing agents:** <names, or "none found">
**Clinical status:** <phase / approved / discontinued — and why>
**Endpoints hit / missed:** <what was proven vs not>
**Failure mode:** <the specific way it breaks>
**Contradicts:** <any prior claim in our docs, and how resolved>
**Genuine gap:** <one sentence — what specifically does not exist>
**Dead end reason:** repetition / needs-experiment / gap-isolated / refuted
```

Then commit with a message naming the idea and the key finding.

## Sweep Order for `all`

Work through in this order, since later ideas depend on earlier findings:

1. `docs/brainstorm-topics.md` — Ideas 1–9
2. `docs/wnt-persister-hypothesis.md` — the grip/dormancy hypothesis and Grip Score
3. `docs/strategies/` — each strategy doc
4. `docs/challenges.md` — re-check whether any challenge has been solved by findings above

After the sweep, report: which ideas survived, which were refuted, and which single gap is most
worth pursuing.
