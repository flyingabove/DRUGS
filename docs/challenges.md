# Challenges

Dedicated doc for what's actually working against us — the general challenges to the whole problem,
challenges specific to our ideas, and a brainstorm on using **Plerixafor** (bone marrow niche
disruption) alongside the four Malone-inspired ideas. See
[problem-definition.md](problem-definition.md) for the core problem statement and
[brainstorm-topics.md](brainstorm-topics.md) for the full idea list this responds to.

## General Challenges to the Problem

Three tiers, from root cause to immediate blocker — each one causes the next:

1. **Root biological challenge:** LSCs mostly differ from normal HSCs *by degree, not by kind*. They
   hijack the same self-renewal, quiescence, and survival programs normal stem cells already run,
   rather than running something genuinely foreign (unlike, say, the BCR-ABL fusion protein in CML,
   a clean cancer-only target). There's no reliable on/off switch — only a dial that's turned up. This
   is compounded by **LSC heterogeneity**: different patients carry different driver mutations
   (FLT3, NPM1, IDH1/2, KMT2A-rearrangements, TP53), and a single patient can carry multiple
   genetically distinct LSC subclones — so no single target is likely to be universal.
2. **Recurring challenge across every idea we've generated:** selectivity — telling LSCs apart from
   normal HSCs — shows up in every single idea in a different costume (ADC toxicity, MCL-1 cardiac
   toxicity, Hedgehog's role in normal hematopoiesis, differentiation therapy risking normal HSC
   depletion, shared metabolic dependencies). See the per-idea breakdown below.
3. **Current concrete blocker:** we don't have paired diagnosis-vs-post-treatment-residual-disease
   data. Nearly every open question in the brainstorm doc — does CLL-1 hold up in the persister state,
   what genes are silenced specifically in persister LSCs, what's the persister cell-cycle timing —
   traces back to this one missing dataset (plan-doc Decision #3).

## Physical Access Challenge: The Bone Marrow Niche

A challenge distinct from selectivity: even a drug that *can* tell LSCs apart from normal cells still
has to physically reach them, and the bone marrow is a bad place to deliver drugs to.

- The marrow isn't uniform. LSCs preferentially sit in the **endosteal niche** (right against the
  inner bone surface), which is poorly vascularized and genuinely **hypoxic** (oxygen tension below
  10 mmHg) — and LSC proliferation actually expands this hypoxic zone further, growing their own
  hiding spot.
- LSCs physically anchor themselves there via **CXCR4 (on the LSC) binding CXCL12/SDF-1 (released by
  marrow stromal cells)** — a docking signal that both anchors the cell in the protected niche and
  actively sends it survival/dormancy signals.
- Net effect: a drug that works against LSCs in a lab dish may barely reach the cells that matter in
  a real patient, because they're sitting in the worst-perfused part of the marrow, gripped onto
  support cells that are actively protecting them.

**Existing drug strategy targeting this directly — Plerixafor:** an FDA-approved CXCR4-blocking drug
that breaks the LSC's grip on the niche and forces it out into the bloodstream, where it loses its
protective signaling and becomes exposed to circulating drugs like any other cell. A Phase I trial
combining plerixafor with decitabine (an epigenetic/DNMT-inhibitor drug) in AML patients showed a
**43% overall response rate**, successfully mobilized LSCs, and did so without triggering a dangerous
side effect (a sudden flood of leukemic cells causing vessel blockages) that researchers specifically
checked for.

## Per-Idea Challenge Recap

| Idea | Core challenge |
|---|---|
| 1: CLL-1 | No drug format proven to approval yet; ADC failed partly on normal-cell toxicity |
| 2: BCL-2/MCL-1 | MCL-1 = cardiac toxicity (selectivity failure); BCL-2 = high novelty bar vs. venetoclax |
| 3: Hedgehog-GLI2 [Malone-Inspired] | Normal hematopoiesis also uses Hedgehog signaling to some degree |
| 4: Wake and Kill [Malone-Inspired] | Timing window unknown; risk of waking normal HSCs too |
| 5: Differentiation Therapy [Malone-Inspired] | Normal HSCs are also dormant/epigenetically "silenced" — risk of depleting the normal stem cell reserve |
| 6: Metabolic Priming [Malone-Inspired] | Inherits the shared-metabolism toxicity problem seen in MCL-1/OXPHOS approaches |
| 7: Drug Repurposing [Malone-Inspired] | Doesn't solve selectivity itself — inherits whatever problem the underlying target has |
| (new) Niche access | Even a selective drug may not physically reach LSCs in the hypoxic endosteal niche |

---

## Brainstorm: Combining Plerixafor With the Four Malone-Inspired Ideas

### + Idea 4 (Wake and Kill)

Plerixafor may not just *complement* the wake-up step — it might **be** a better version of it.
CXCR4-CXCL12 signaling doesn't just anchor LSCs physically, it actively sends dormancy-maintaining
signals. Blocking it with plerixafor should evict LSCs from the niche *and* push them toward active
cycling in one move, rather than needing a separate dormancy-breaking drug. Proposed sequence:
**plerixafor (evict + wake) → killing agent (BCL-2 inhibitor or CLL-1 CAR-T), dosed while LSCs are
both exposed in circulation and out of quiescence.** This directly addresses Idea 4's open
question (unknown timing window) by giving the wake-up step a second, independent mechanism of
action instead of relying on Hedgehog blockade alone.

### + Idea 5 (Differentiation Therapy)

This pairing already has real clinical precedent: the plerixafor + decitabine trial cited above used
**exactly** the differentiation-therapy drug class from Idea 5 (decitabine is a DNMT inhibitor, same
family as the HDAC/DNMT inhibitors proposed to reactivate silenced stemness-suppressor genes).
Reasoning: differentiation-inducing epigenetic drugs need sustained exposure to reach effective
concentration in LSCs — much harder in a poorly-perfused hypoxic niche. Mobilizing LSCs into
circulation first should improve drug exposure/uptake for the differentiation agent, addressing Idea
5's core mechanism directly rather than just adding a second drug alongside it.

### + Idea 6 (Metabolic Priming)

The hypoxic niche itself is already a metabolic regulator — hypoxia drives its own adaptations in
LSC metabolism. Moving a cell from the hypoxic endosteal niche into normoxic peripheral blood is
itself a metabolic shock, potentially doing part of the "priming" work Idea 6 proposes to engineer
deliberately. Proposed angle: **use plerixafor-induced reoxygenation as the first-stage primer**,
then layer a smaller, more targeted metabolic agent on top to complete the shift toward a
BCL-2-dependent vulnerable state — potentially allowing a lower dose of the metabolic drug than would
be needed alone, which matters given Idea 6's toxicity-threshold concerns.

### + Idea 7 (Drug Repurposing)

Plerixafor is itself already a proof-of-concept for Idea 7's whole strategy: it's a drug originally
developed and approved for stem cell mobilization ahead of transplants, now being repurposed for AML
niche disruption. Two extensions worth exploring: (1) apply Idea 7's generative-analog approach *to
plerixafor itself* — design structural analogs optimized specifically for AML LSC mobilization rather
than inheriting the original transplant-mobilization profile; (2) more generally, treat "already an
approved mobilizer" as a search filter when repurposing-screening for niche-disruption agents, the
same way Idea 7 proposes filtering generative candidates toward analogs of approved compounds.

## Open Threads

- Confirm plerixafor's mobilization effect actually applies to the *post-treatment persister* LSC
  population specifically (same missing-dataset blocker as everywhere else in this project).
- Check for a hyperleukocytosis/vessel-blockage safety margin when combining plerixafor with a fast
  killing agent (e.g., CAR-T) rather than the slower decitabine it's been trialed with so far.
- Work out realistic timing/sequencing windows for plerixafor → wake → kill, and whether that's
  achievable with once-daily dosing or needs continuous infusion.
