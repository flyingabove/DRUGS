# Dead Ideas — Do Not Re-Research

Compact graveyard. One line of what, one line of why it died. **Read this before proposing anything;
several of these were proposed twice.**

Format: `IDEA — KILLED BY: reason`

---

## Killed on selectivity (hits normal cells too)

- **HMG20B (LSD1-complex subunit)** — KILLED BY: *"HMG20B depletion was sufficient to block
  granulocytic differentiation of normal murine HSPCs."* Not leukemia-restricted. Was the most
  promising mid-run idea; the entire selectivity argument collapsed on one sentence.
- **LSD1 itself (as a selective target)** — KILLED BY: indispensable for normal hematopoiesis;
  knockout embryonically lethal, hematopoietic deletion kills mice of anemia. Direction reverses by
  context (AML: loss → differentiation; normal HSC: loss → blocked differentiation). Unavoidable
  hematologic toxicity. *Still useful as a differentiation mechanism, not as a clean target.*
- **Free/systemic plerixafor** — KILLED BY: mobilizes normal HSCs identically; also drives ROS/HSC
  exhaustion. Solves access, never selectivity.
- **CD123, CD33, CD45, CD44, CXCR4 (as standalone targets)** — KILLED BY: all shared with normal
  blood cells. Workable only with gating, epitope editing, or a graft.
- **MCL-1** — KILLED BY: cardiac toxicity. AMG 397 clinical hold, AMG 176 halted, AZD5991/ABBV-467
  troponin rises. Heart muscle needs MCL-1.

## Killed on mechanism (the premise was wrong)

- **Block niche re-entry between chemo rounds** — KILLED BY: LSCs never leave. Chemo hits
  proliferating blasts while LSCs "remain sheltered." No re-entry to block. The mobilization that
  does occur in recovery is disproportionately *normal* progenitors.
- **Hypoxia-activated prodrug (for kidney sparing)** — KILLED BY: renal medulla ~10 mmHg ≈ marrow
  niche <10 mmHg. No oxygen window. Worse, GPX4 vulnerability sits at the inner-cortex/outer-medulla
  interface, straddling it.
- **Iron-gated Fe(II) prodrug (for kidney sparing)** — KILLED BY: LSCs **overexpress ferritin
  (FTH/FTL)** vs normal HSCs and use ferritinophagy to *prevent* excess labile iron. They buffer
  iron; they do not run a large loose pool. Demoted to secondary pending direct LIP measurement.
- **Senescence one-two punch** — KILLED BY: post-senescent escapees retain stem features and become
  *more* invasive and tumorigenic; escape via polyploidization. Salvageable only with WNT blockade
  (SASP-induced WNT drives the stemness rebound).

## Killed on novelty (already exists)

- **LSD1 PROTAC** — EXISTS: MS9117, first-in-class, PNAS May 2025. Correctly predicted from
  mechanism, then found already done.
- **miR-146a restoration** — EXISTS: CpG-miR146a mimic conjugate, already internalized by myeloid
  cells. Also taken up by ~20% of long-term HSCs, so not selective either.
- **Anti-CXCR4 CAR-T** — EXISTS: preclinical in AML/ALL, positioned as transplant conditioning
  (the field concedes CXCR4 alone is too toxic standalone).
- **CD16-IL15-CLEC12A TriKE** — EXISTS: preclinical NK engager against CLL-1, kills AML cancer stem cells.
- **Iomab-B / anti-CD45 radioimmunotherapy** — EXISTS: Phase 3 SIERRA. See clinical failures below.
- **Chemical reprogramming cocktails (7C, DLC79)** — ABSORBED: the load-bearing component turned out
  to be LSD1; the cocktail was a lead, not a destination.

## Killed on clinical evidence (tried in humans, underdelivered)

- **Imetelstat as our lead** — KILLED BY: FDA-approved for lower-risk MDS but **"minimal efficacy in
  higher-risk MDS and AML."** Also mechanistically misattributed — telomere length did not predict
  response; its real AML activity is lipid ROS/ferroptosis. A poor witness either way.
- **Iomab-B** — KILLED BY: met primary endpoint (22% vs 0% durable CR, p<0.0001) but **FDA refused
  the filing** for lack of overall survival benefit. Mechanism works; OS did not follow.
- **CLL-1 ADC** — KILLED BY: terminated. Insufficient anti-leukemic activity plus significant
  hematologic toxicity.
- **CD123 ADC / earlier CD123 agents** — KILLED BY: on-target off-tumor toxicity from normal
  progenitor expression.
- **NAMPT inhibitors (FK866 etc.)** — KILLED BY: toxicity and resistance in trials, *because NAMPT
  is not compartmentalized* — inhibiting it drains NAD+ from all three cellular compartments.
- **RSL3 / ML162 as GPX4 tools** — KILLED BY: cell-free assays show they **fail to inhibit purified
  GPX4**; they hit TXNRD1 instead. NOTE: this is ML1**62**, not ML2**10**. ML210 (nitroisoxazole
  warhead) IS genuinely selective for GPX4 with low proteome-wide reactivity. Do not conflate them.

## Demoted, not dead (viable but superseded)

- **NMNAT1 (nuclear NAD+)** — Strong: LSC-specific, "dispensable for normal hematopoiesis," gatekeeper
  (NAD precursors bypass NAMPT but not NMNAT1), venetoclax synergy. **Superseded** by GPX4/FSP1 on
  indication sharpness (venetoclax-resistant AML) and AI-tractability. Retinal risk via NMNAT1's
  non-enzymatic chaperone function (Leber congenital amaurosis). *Best fallback if GPX4 fails.*
- **NCOA4 / ferritinophagy** — Strong: uniquely validated in **quiescent CD34+CD38−** LSCs, minimal
  normal toxicity, compound 9a exists. **Antagonistic with GPX4 approach** (starves iron vs exploits
  iron — cannot combine). The conservative alternative; less left to design.
- **SIN3A PAH2–SID inhibitor** — Genuine gap in AML (all published work is breast cancer), restores
  RARβ and retinoic-acid metabolism, most direct Malone lineage. Parked, not killed. Cheapest
  high-value experiment identified.
- **ELAVL1/HuR** — LSC-selective by in vivo CRISPR; MS-444 induces myeloid maturation in primary AML.
  Previously undruggable class = high AI leverage, high risk. Parked.
- **TXNRD1** — Overexpressed in AML, poor prognosis, auranofin (approved) works in AML. **Caution:**
  TXNRD1 inhibitors expand regulatory T cells — paradoxical immunosuppression limiting efficacy in
  immunocompetent models. Possible alternative or add-on.

## Structural lessons (apply to any new idea)

1. **Verify existence before claiming novelty.** Wrong at least four times here.
2. **Mechanism working ≠ patients living longer.** Iomab-B is the standing proof.
3. **Tool compounds may not hit their nominal target.** True for both RSL3/ML162 and imetelstat —
   found in the same run. Always check cell-free validation against purified protein.
4. **The niche resupplies whatever you deplete.** Stroma transfers mitochondria via tunneling
   nanotubes, and metabolic attack *induces* the transfer. Assume resupply for any metabolic target.
5. **Partial killing only delays relapse.** Killing is logarithmic; regrowth is exponential. Aim for
   containment or permanent loss of self-renewal, not deeper cytoreduction.
