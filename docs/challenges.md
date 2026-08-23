# Challenges

This doc is a checklist, not just a description. The point isn't to list problems for their own
sake — it's that **a real therapy has to solve every challenge below at the same time.** Solving
selectivity but not access doesn't work. Solving access but not selectivity doesn't work either
(see the cross-cutting caveat below — this is the mistake it's easy to make). No single idea in
[brainstorm-topics.md](brainstorm-topics.md) solves all of them on its own, which is exactly why the
project keeps landing on *combinations* rather than a single silver-bullet drug. See
[problem-definition.md](problem-definition.md) for the core problem statement.

## The Challenges We Need to Solve

### 1. Selectivity — telling LSCs apart from normal stem cells

- **In plain terms:** LSCs look and behave a lot like the patient's own healthy blood stem cells
  (HSCs). A drug that can't tell them apart wipes out the patient's normal blood supply along with
  the cancer.
- **Why it's this hard:** LSCs mostly differ from normal HSCs *by degree, not by kind* — they overuse
  the same self-renewal, survival, and quiescence machinery normal stem cells already have, rather
  than running something genuinely foreign. There's no clean on/off switch, only a dial turned up.
- **Status:** open. Every idea we've generated runs into this in some form — see the coverage check
  below.

### 2. Physical access — actually reaching LSCs in the bone marrow

- **In plain terms:** even a drug that *could* tell LSCs apart from normal cells still has to
  physically get to them, and LSCs hide in one of the hardest parts of the body to deliver a drug to.
- **Why it's this hard:** LSCs preferentially sit in the **endosteal niche** — the region right
  against the bone surface — which is poorly supplied with blood and genuinely **hypoxic** (low
  oxygen). LSCs also physically grip onto marrow support cells there (via a docking signal called
  CXCR4–CXCL12), which anchors them in the worst-supplied spot in the marrow.
- **Status:** partially addressed. **Plerixafor**, an FDA-approved drug, blocks that docking signal
  and forces LSCs out of the niche into the bloodstream, where they're easier to reach. A real trial
  combining plerixafor with an epigenetic drug (decitabine) showed a 43% response rate. But see the
  cross-cutting caveat below — this doesn't finish the job by itself.

### 3. Dormancy — LSCs that aren't actively dividing

- **In plain terms:** most cancer drugs (chemo especially) work by disrupting cell division. A cell
  that isn't dividing is largely invisible to that kind of attack.
- **Why it's this hard:** the same CXCR4–CXCL12 docking signal that physically anchors LSCs in the
  niche also acts as a direct brake on their proliferation — so LSCs sitting in the niche are both
  hidden *and* switched into a low-activity state that most drugs can't touch.
- **Status:** partially addressed. Plerixafor may address this too, not just physical access — see
  Idea 4 in [plerixafor-combination-brainstorm.md](plerixafor-combination-brainstorm.md).

### 4. Heterogeneity — no single target covers every patient

- **In plain terms:** AML isn't one disease. Different patients carry different driver mutations, and
  even one patient can carry multiple genetically distinct LSC subclones at once.
- **Why it's this hard:** a target we validate in one patient's data (e.g., CLL-1 expression, a
  specific silenced gene) may simply not be present, or not be the dominant driver, in another
  patient's leukemia.
- **Status:** open. Not directly addressed by any current idea — likely means the eventual therapy
  needs a companion biomarker test to select which patients it applies to, rather than being
  universal.

### 5. The missing data gap — we haven't confirmed any of this in the actual population we care about

- **In plain terms:** this whole project is about *post-treatment, lingering* LSCs — the ones that
  survive remission and cause relapse. Almost everything we know about LSC biology (CLL-1 expression,
  which genes are silenced, Hedgehog dependence) comes from studies of LSCs *at diagnosis*, not from
  the specific persister cells left behind after treatment.
- **Why it's this hard:** paired diagnosis-vs-post-treatment-residual-disease data, from the same
  patients, is scarce. Without it we're assuming diagnosis-stage LSC biology transfers to the
  persister state — a reasonable starting assumption, but an unconfirmed one.
- **Status:** open, and blocking. This is plan-doc Decision #3, and nearly every other open question
  in this project traces back to it.

## Cross-Cutting Caveat: Solving Access Doesn't Solve Selectivity

This is easy to miss, so it gets its own section: **Plerixafor mobilizes normal HSCs exactly as
readily as it mobilizes LSCs.** They share the same CXCR4–CXCL12 machinery, so plerixafor can't tell
them apart any more than anything else can.

That means plerixafor is a real, working answer to Challenge #2 (access) and possibly Challenge #3
(dormancy) — but it does **nothing** for Challenge #1 (selectivity). Pairing plerixafor with a killing
or differentiation agent only works if *that second agent* brings its own selectivity — plerixafor
just gets both LSCs and normal HSCs equally exposed to whatever comes next. Pair it with something
non-selective (like a broad metabolic hit) and you've made the normal-cell toxicity problem *easier*
to trigger, not harder, because you've pushed normal HSCs into an exposed, actively-cycling state too.

**Practical rule this implies:** plerixafor (or any niche-disruption strategy) should only ever be
paired with a partner that independently solves Challenge #1. Of our ideas, that points toward Idea 1
(CLL-1, which has a real selectivity story) or Idea 5 (differentiation therapy, which sidesteps
selectivity by not trying to kill anything) as the safer pairings — not Idea 6 (metabolic priming),
which inherits the same shared-toxicity risk that already broke MCL-1 inhibitors on its own.

## Do Our Ideas Solve These Challenges? A Coverage Check

✓ = solves it directly · ~ = partially / conditionally · ✗ = does not solve it (open or inherited)

| Idea | 1. Selectivity | 2. Access | 3. Dormancy | 4. Heterogeneity | 5. Confirmed in persister state |
|---|---|---|---|---|---|
| 1: CLL-1 | ~ | ~ (CAR-T can actively migrate to the niche) | ~ (immune killing doesn't require the cell to be dividing) | ~ (only patients with CLL-1+ LSCs) | ✗ |
| 2: BCL-2/MCL-1 | ~ (BCL-2 safer than MCL-1, still imperfect) | ✗ | ~ (BCL-2 blockade doesn't require active division either) | ~ | ✗ |
| 3: Hedgehog-GLI2 | ✗ (shared with normal hematopoiesis) | ✗ | ✓ (this is its whole mechanism) | ✗ | ✗ |
| 4: Wake and Kill | ✗ (inherited from whichever killer is paired) | ~ | ✓ | ✗ | ✗ |
| 5: Differentiation Therapy | ~ (sidesteps the need to kill at all, but risks normal dormant HSCs too) | ✗ | ~ | ✗ | ✗ |
| 6: Metabolic Priming | ✗ (most exposed idea — see caveat above) | ✗ | ~ | ✗ | ✗ |
| 7: Drug Repurposing | ✗ (inherits whatever the underlying target has) | ✗ | ✗ | ✗ | ✗ |
| Plerixafor / niche disruption | ✗ (see caveat above) | ✓ | ~ | ✗ | ✗ |

**Reading this table honestly: nothing solves everything, and nothing except the missing-data gap
(#5) is fully unaddressed by every single idea.** That last column being all ✗ is the clearest
argument for why sourcing the post-treatment/MRD dataset is the most urgent next step — every other
gap in this table has at least one idea partially covering it; that one doesn't.

## Per-Idea Challenge Recap (short form)

- **Idea 1 (CLL-1):** no drug format proven to full approval yet; the ADC attempt failed partly on
  normal-cell toxicity.
- **Idea 2 (BCL-2/MCL-1):** MCL-1 has a real cardiac toxicity problem; BCL-2 is safer but has to beat
  an already-approved drug (venetoclax) to be worth it.
- **Idea 3 (Hedgehog-GLI2):** normal blood stem cells use this pathway too, to some degree.
- **Idea 4 (Wake and Kill):** the timing window between "wake" and "kill" isn't established yet.
- **Idea 5 (Differentiation Therapy):** normal HSCs are also dormant/epigenetically quiet — reactivate
  the wrong gene and you risk depleting the normal stem cell reserve, not just the cancer.
- **Idea 6 (Metabolic Priming):** inherits the same shared-metabolism toxicity problem that already
  broke MCL-1/OXPHOS approaches on their own.
- **Idea 7 (Drug Repurposing):** a delivery/discovery strategy, not a target — it doesn't solve
  selectivity itself, it just inherits whatever problem the underlying target already has.

## Where the Plerixafor Combinations Fit

The full brainstorm on pairing plerixafor with each of the four Malone-inspired ideas — including the
mechanism detail on why it may solve dormancy as well as access — now lives in its own doc:
[plerixafor-combination-brainstorm.md](plerixafor-combination-brainstorm.md).

## Open Threads

- Source the post-treatment/MRD-state dataset — the one gap with no partial coverage from any idea
  (see the coverage check above).
- Confirm the CXCR4 proliferation-brake mechanism specifically in LSCs (currently shown only in
  normal primitive hematopoietic cells).
- Decide whether Challenge #4 (heterogeneity) needs to be solved directly, or whether the plan should
  explicitly scope down to a biomarker-selected patient subgroup instead.
- Check hyperleukocytosis/vessel-blockage safety margins if plerixafor is paired with a fast-acting
  killing agent (e.g., CAR-T) instead of the slower decitabine it's been trialed with so far.
