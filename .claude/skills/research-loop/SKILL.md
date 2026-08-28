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

## Efficacy First — Toxicity Is a Downstream Engineering Problem

**The single most important question about any candidate is whether it actually kills LSCs.**
Everything else is secondary at this stage.

- **Gate on efficacy, not safety.** If a mechanism demonstrably eradicates leukemic stem cells, it
  stays alive as a candidate **even if the current version would harm the patient.** Toxicity is a
  medicinal-chemistry and delivery problem — clearance route, warhead reactivity, dosing schedule,
  prodrug gating, targeted delivery. Those are solvable by engineering a better molecule around a
  validated mechanism.
- **You cannot engineer around a mechanism that does not kill the target.** No amount of delivery
  cleverness rescues a drug that leaves LSCs alive. That failure is terminal; toxicity usually is not.
- **Therefore: never retire an idea on toxicity alone.** Record the toxicity, mark it as an
  engineering problem, and keep hunting for whether the mechanism is lethal to LSCs. Retire an idea
  when the *efficacy* evidence fails.
- **Prioritize efficacy evidence in this order:** eradication of leukemia-initiating capacity on
  serial transplantation > primary patient LSC (CD34+CD38−) killing ex vivo > PDX in vivo efficacy >
  cell line data. Weight the top of that list heavily; discount the bottom.
- **When loops are limited, spend them on efficacy questions**, not on characterizing toxicities that
  a later chemistry program would address anyway.

## The Bar We Are Aiming At

**We do not need a miracle cure-all. We need a designable molecule that improves survival enough to
win FDA approval.**

Judge every idea against that bar, not against a cure:

- **A molecule must be designable.** If the idea cannot be reduced to a specific molecular entity
  someone could actually make (small molecule, peptide, antibody, conjugate, degrader), it is not a
  candidate no matter how elegant the biology.
- **Partial efficacy is a win.** An agent that helps a defined subgroup, or adds benefit on top of
  standard care, clears the bar. Universality is not required. Do not discard an idea because it only
  covers some patients.
- **The endpoint that matters is overall survival.** Iomab-B met its primary endpoint at p<0.0001 and
  the FDA still refused the filing for lack of an OS benefit. Killing more leukemia cells is not the
  goal; patients living longer is. Ask of every idea: what is the plausible path to an OS signal?
- **Prefer ideas with a realistic trial design.** A two-agent combination in a biomarker-selected
  population is approvable. A six-agent regimen requiring a novel combination pathway is not, however
  good the biology.
- **Existing safety data is an asset.** Repurposed compounds, known chemotypes, and validated target
  classes shorten the path to approval. Weigh that in the idea's favor.

## Prefer Ideas That AI Newly Unlocks

**The right idea is one that modern LLM, machine-learning, and large-scale simulation tooling makes
tractable — and that would have been very hard to pursue before it.** Score every candidate on this.

Favor ideas whose bottleneck is a **search, prediction, or design** problem:

- **Multi-parameter molecular optimization.** Satisfying several conflicting constraints at once
  (potency + isoform selectivity + deliberate barrier exclusion + preserved non-enzymatic function)
  was previously a slow medicinal-chemistry grind. Generative design plus property prediction now
  attacks all constraints simultaneously. This is the strongest signal an idea belongs here.
- **Paralog/isoform selectivity against near-identical active sites.** Structure prediction plus
  large-scale docking makes discriminating close homologs feasible where it once was not.
- **Protein-protein interaction and interface design.** Flat, undruggable interfaces are now
  approachable via structure prediction and de novo binder design.
- **Cross-field literature synthesis.** Connecting a mechanism published in one disease to an unmet
  need in another is something an LLM does at a scale no individual reviewer can match.
- **Virtual screening at billion-compound scale**, and in-silico triage before any synthesis.

Deprioritize ideas whose bottleneck is **wet-lab throughput, unknown biology, or clinical logistics** —
AI does not relieve those, so the idea is no better positioned now than it was a decade ago.

State explicitly, for each surviving idea: *what specifically does AI make possible here that was not
before?* If there is no good answer, the idea is probably not the right one for this project.

## Loop Budget — 150 Minimum, No Exceptions

**Run at least 150 loops. Do not stop early under any circumstances.**

The dead-end criteria below retire a **single idea**. They never end the run. When an idea dies, the
loop count keeps going — you move to the next idea, not to the summary.

**When every lead on the board is exhausted, do not stop. Broaden instead:**

1. Run a fresh comprehensive literature search on the disease area from a new angle — a different
   pathway family, a different modality, a different patient subgroup, an adjacent disease with
   transferable biology.
2. Attack the surviving idea rather than defending it. Go hunting for the paper that kills it. Every
   idea that died in this project died to one sentence someone went looking for.
3. Re-run the ladder on ideas previously marked dead, with the newer findings in hand — a dead idea
   plus a new fact is often a live one (senescence was dead until WNT explained the escape).
4. Follow the open threads already recorded in the research log (docs/research-log.md).

Report the loop count honestly. Never inflate it, and never pad with re-searches of covered ground —
if you are repeating yourself, that is the signal to broaden per the list above, not to stop and not
to fake progress.

## Stop Conditions (Retire an Idea — Never the Run)

Retire **one idea** and move to the next when **any** of these is true:

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
