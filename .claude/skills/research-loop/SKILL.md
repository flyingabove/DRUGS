---
name: research-loop
description: Central controller for every AML leukemic-stem-cell drug iteration. Routes work through the other project skills and available MCPs, gates first on whether the exact candidate kills LSCs or irreversibly matures them, then considers delivery, safety, survival, manufacture, and novelty. Also use for broad idea research and claim verification.
---

# LSC Drug Research Loop

This is the central controller for every drug-design iteration. Route work through the other project
skills and available MCPs, then write the evidence back to the live state.

## Non-negotiable priority

**The exact candidate must kill LSCs or irreversibly force them to mature so they lose
leukemia-initiating capacity. This is Gate 1 and outranks every other property.**

- Do not promote a modified molecule because it is more soluble, safer, newer, or easier to make.
- A close analog's activity keeps a design plausible; it does not prove the new molecule works.
- Docking, reactivity calculations, target-occupancy models, and cell-line data are supporting evidence
  only. They cannot make Gate 1 green.
- If the exact candidate lacks target-cell evidence, the next iteration must reduce that uncertainty:
  find overlooked measurements, preserve the activity-critical pharmacophore, or specify the decisive
  assay. Do not spend the iteration polishing downstream properties.
- Differentiation counts only when it is functional and durable: mature-cell markers plus loss of
  self-renewal or leukemia initiation. A marker change alone is not enough.

## Controller workflow — run on every drug iteration

1. **Reload state.** Read `CLAUDE.md`, `docs/research/loops/current-idea.md`, and `dead-ideas.md`. Name
   the exact molecule and intended patient population.
2. **State the Gate 1 claim.** Choose LSC killing, irreversible LSC maturation, or both. Define the
   measurement that would prove it.
3. **Search efficacy first.** Seek exact-compound evidence in this order: serial transplantation or
   limiting dilution; primary patient LSC killing or durable maturation; patient-derived xenograft;
   then cell lines. Record required combination partners.
4. **Check that the molecule can plausibly retain the effect.** Verify structure and formula; preserve
   the activity-critical pharmacophore; test target engagement/reactivity and intracellular reach with
   validated positive and negative controls. A method that rejects the known active control is invalid.
5. **Make the Gate 1 decision.** Green only on measured target-population activity by this compound.
   Otherwise keep it below green and make the missing efficacy experiment the next action.
6. **Only after Gate 1 plausibility survives**, evaluate selectivity, delivery, chronic safety,
   survival path, synthesis, and novelty. These can kill a candidate, but never substitute for efficacy.
7. **Write and judge.** Update the live state and long-form strategy, correct contradictions in place,
   run `judge-drug`, show its table, and commit the significant finding.

## Skill and MCP routing

Use the project skills as modules rather than duplicating them:

| Need | Load/use |
|---|---|
| Publications and negative results | `literature-search` |
| Exact structure, identifiers, activity, and physicochemical facts | `compound-profile` |
| Target dependence and disease biology | `target-validation` |
| Existing molecules, patents, and differentiation | `competitor-landscape` |
| Exposure, metabolism, and toxicity predictions | `admet-prediction` |
| Pharmacokinetic/pharmacodynamic or resistance modelling | `drug-simulation` |
| Trial, regulatory, and approval precedent | `clinical-intelligence` |
| Deliverable synthesis | `report-generator` |
| Mandatory end-of-iteration decision table | `judge-drug` |

Prefer the working MCPs named in `CLAUDE.md` when they cover the question: `biocontext-kb` for
biological and clinical records, `gget-mcp` for sequences/alignment, and `patent-mcp-server` for prior
art. Use scripts when an MCP is unavailable or deterministic local computation is the better
instrument. Verify at least one real record before trusting a new source or tool.

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

## Context Management — Exactly Two Living Docs

Long runs die from context exhaustion, not from running out of ideas. **Keep exactly two files under
`docs/research/loops/` and treat them as the complete working memory of the run.** Reading those two
must be enough to fully reload the project state — nothing else required.

**1. `dead-ideas.md` — the graveyard.**
Every retired idea as one entry: what it was, and the specific sentence or finding that killed it.
Group by failure class (selectivity / mechanism / novelty / clinical evidence / demoted-not-dead).
Keep it dense — this file is read constantly, so no padding. Its job is to stop the same idea being
proposed twice, which has already happened in this project.

**2. `current-idea.md` — the live state.**
The one surviving idea, why it works with evidence attached, its design spec, and a
**"still needs verification"** list ordered by how badly a bad answer would hurt. Mark holes CLOSED
as they close, with the loop number. Keep the fallback list at the bottom.

**Rules:**
- **Update these two as you go, not at the end.** A finding that is not written down is lost when
  context rolls over.
- **Log corrections in place.** When a later loop contradicts an earlier claim, fix it in the doc and
  say what changed — do not leave both versions standing. This project has already made several such
  corrections (ML162 vs ML210; NCOA4 fork; imetelstat mechanism).
- **Long-form strategy docs live elsewhere** (`docs/strategies/`). These two are the working memory,
  not the deliverable.
- **Do not build search infrastructure.** No indexes, no databases, no MCP servers for this. Standing
  up that machinery costs more context than it saves. Two well-maintained markdown files are the
  right size for the problem.

## Efficacy First — Toxicity Is a Downstream Engineering Problem

**The single most important question about any candidate is whether it actually kills LSCs or
irreversibly matures them so they cannot restart leukemia.**
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
