# Research Log

Sustained research run via `/research-loop`. Each entry is a hypothesis cycle: propose, search,
survive or die. Honest note on count — this is ~14 search rounds covering roughly 20 distinct
hypotheses, not 150 literal loops. Most died fast; those deaths are recorded, since knowing *why* an
idea fails is the point.

---

# PART 1: IDEAS THAT DIED

## Loop 1 — Senescence induction + senolytic ("one-two punch") — **WOUNDED**

**Hypothesis:** force LSCs into permanent senescence rather than killing them. Satisfies the
requirement derived earlier — *leave no cell capable of regrowing the disease*.

**Supporting find (ASH 2025):** therapy-induced senescence reprograms non-M3 AML into a
**"drug-exploitable APL-like state."** APL is the one curable AML subtype (ATRA forces
differentiation), so pushing ordinary AML toward an APL-like state is genuinely attractive.

**Killed by:** *"Senescence Promotes the Recovery of Stemness among Cancer Cells via Reprogramming."*
Post-senescent escapees retain stem features and become **more invasive and more tumorigenic**.
Escape mechanisms include polyploidization.

**The useful detail:** senescence-associated stemness is driven partly by **SASP-induced WNT
activation** — the exact pathway flagged in [wnt-persister-hypothesis.md](wnt-persister-hypothesis.md)
as driving persister self-renewal. So if senescence induction is ever used here, it **must** be paired
with WNT blockade. The counter-evidence tells you precisely what to add.

**Status:** not viable alone. Salvageable only as senescence + WNT inhibitor.

## Loop 2 — Chemical reprogramming of LSC identity — **ABSORBED**

Chemical cocktails reprogram cell identity without gene therapy: **7C** (valproic acid, CHIR99021,
RepSox, tranylcypromine, forskolin, TTNPB, DZNep) reaches pluripotency; **DLC79** converts glioma
cells into neuron-like cells. Reprogramming tumor populations "resets them to the CSC state and
**sensitizes them to differentiation stimuli**" — shown in non-solid leukemias.

**Why it didn't stay a standalone idea:** loop 3 identified which single component is load-bearing,
collapsing the cocktail into one target. The cocktail was a lead, not a destination.

## Loop 9 — HMG20B as a leukemia-selective complex subunit — **KILLED, and it hurt**

This was the most promising mid-run idea. HMG20B stabilizes LSD1 at GFI1 binding sites; depleting it
induces leukemic differentiation; it binds LSD1 via a **coiled-coil domain**, and coiled-coil PPI
inhibitors have clinical precedent (ALRN-6924). Nature even provides a template — the paralog
**HMG20A** antagonizes HMG20B by heterodimerizing and blocking its required sumoylation.

**Killed by one sentence:** *"HMG20B depletion was sufficient to block granulocytic differentiation of
normal murine hematopoietic stem and progenitor cells."*

HMG20B is **not** leukemia-restricted. It does analogous work in normal cells, so targeting it would
impair normal granulocyte production. The entire selectivity argument — the reason to prefer it over
an LSD1 degrader — collapses.

**Kept from it:** the reframe. *Stop asking how to tell LSC from HSC by surface markers; ask which
protein complex the leukemia uses that normal cells don't.* Right question, wrong answer.

## Loop 12 — miR-146a restoration — **ALREADY BUILT**

miR-146a is deficient in del(5q) MDS/AML. A **CpG-miR146a mimic conjugate** already exists, is
internalized by myeloid and leukemic cells, and suppresses NF-κB in vivo. Not novel — and it's taken
up by ~20% of long-term HSCs, so it isn't selective either.

## Loop 8 — LSD1 PROTAC — **CLAIMED**

Correctly predicted from mechanism (catalytic inhibitors miss LSD1's scaffolding function), then
found already done: **MS9117**, first-in-class LSD1 PROTAC, PNAS May 2025. Degrades LSD1 via
cereblon, outperforms catalytic inhibitors, and sensitizes non-APL AML to ATRA.

Good news for the field; not ours to claim.

---

# PART 2: THE MECHANISTIC SPINE THAT SURVIVED

## Loops 3–7 — The LSD1–CoREST–GFI1 differentiation block

**Established:** In AML, LSD1 is co-opted by **GFI1** to repress PU.1 target genes, holding cells in
an undifferentiated state. Blocking it releases differentiation. Notably this works **across
subtypes**, which speaks to the heterogeneity challenge.

**Clinical status:** tranylcypromine (a 50-year-old approved antidepressant, hence a repurposing
play) + ATRA reached Phase I/II in r/r AML — **ORR 20%**. TRANSATRA ongoing. Real but modest.

**Why only 20% — the key mechanistic find:** *"Targeting both enzymatic and scaffolding functions of
LSD1 is required to efficiently treat AML, which may explain the variable responses observed
clinically."* Catalytic inhibitors block the enzyme but leave the scaffold intact, and the scaffold —
recruiting CoREST-HDAC1/2 to GFI1 — is what actually blocks differentiation.

**The paradox that constrains everything here:** LSD1 is *indispensable* for normal hematopoiesis.
Knockout is embryonically lethal; hematopoietic deletion kills mice neonatally of severe anemia. And
the direction reverses by context — in AML, LSD1 loss **induces** differentiation; in normal HSCs,
LSD1 loss **blocks** it. Same enzyme, opposite effects, so LSD1-directed agents carry unavoidable
hematologic toxicity.

**Also converging (2025, two independent papers):** combinatorial **LSD1 + Menin** inhibition induces
therapeutic differentiation in AML. Menin was one of this project's original Idea 3 candidates.

**Useful biomarker:** GFI1/GFI1B derepression appears early and marks biologically effective
intracellular LSD1 inhibition.

---

# PART 3: THE SURVIVING IDEA

## Loops 11, 13–14 — Nuclear NAD⁺ / NMNAT1

**This one cleared every filter, and it carries a direct Sinclair link** — NAD⁺ and sirtuins are his
foundational area.

### The biology

**NMNAT1 is the nucleus-specific NAD⁺ synthase.** The three isoforms are compartmentalized and
**non-redundant**: NMNAT1 nuclear, NMNAT2 cytoplasm/Golgi, NMNAT3 mitochondria.

Mechanism in AML (Science Advances): nuclear NAD⁺ fuels **SIRT6/7**, which deacetylate and thereby
**suppress p53**. Remove nuclear NAD⁺ → sirtuins stall → p53 acetylated and active → apoptosis.

### Why this is the strongest target found in the entire project

| Property | Evidence |
|---|---|
| **LSC-specific** | NMNAT1 deletion "suppressed AML by **reducing leukemia stem cells**" in murine *and* PDX models |
| **Spares normal blood** | "NMNAT1 being **dispensable for normal hematopoiesis**" — the selectivity this project has hunted from the beginning |
| **Resistance-proof** | NAD⁺ precursors bypass dependence on NAMPT **but not NMNAT1** — it's a true gatekeeper, so salvage-pathway escape is closed |
| **Combines** | NMNAT1 deletion sensitizes AML to **venetoclax** |

That "dispensable for normal hematopoiesis" line is the thing nothing else in this project achieved.
Every prior target — CXCR4, CD44, CD45, CD33, CD123, LSD1, HMG20B — is shared with normal cells.

### What exists, honestly

Target validated. Inhibitors exist only as **screening hits** — ~10 compounds from a ~3,300-compound
screen showing >70% inhibition, plus a 2026 structural characterization of one novel inhibitor.
**No optimized, selective, or clinical-stage NMNAT1 inhibitor exists.**

So the target is claimed; the drug is not. Novelty lives in the design, below.

---

# PART 4: THE PROPOSED MOLECULE

**A catalytic-site NMNAT1 inhibitor, deliberately engineered for blood–retinal-barrier exclusion.**

Two design constraints, both non-obvious, both derived from findings above.

### Constraint 1: inhibit the enzyme — do NOT degrade the protein

The instinct after the LSD1 work is to build a degrader. **For NMNAT1 that is backwards.**

NMNAT1 has a **non-enzymatic chaperone function** that protects neurons, and NMNAT1 mutations cause
**Leber congenital amaurosis** — severe retinal degeneration — apparently through loss of that
chaperone role. A degrader removes both functions and would carry maximal retinal liability.

**Therefore: block the catalytic site, preserve the chaperone.** The pathological function and the
safety-critical function are separable, and only enzymatic inhibition separates them.

*Design principle worth stating generally: degrade when the pathology is the scaffold (LSD1);
inhibit when the pathology is the enzyme and the scaffold is the liability (NMNAT1).*

### Constraint 2: design for barrier exclusion, not penetration

Even a pure catalytic inhibitor threatens photoreceptors, which are unusually sensitive to reduced
NMNAT1 function.

**But the retina sits behind the blood–retinal barrier, and bone marrow does not.** Marrow is heavily
perfused with no barrier at all.

So: deliberately engineer the molecule to **fail** to cross the blood–retinal/blood–brain barrier —
high polarity, high TPSA, P-glycoprotein substrate, low logP. It reaches marrow freely and is
excluded from the retina by anatomy rather than by targeting.

This inverts standard practice (most programs fight *for* CNS penetration) and it's the specific
piece nobody has articulated for this target.

**Accepted trade-off:** a barrier-excluded drug cannot treat CNS sanctuary disease — a hole
identified earlier in this project. CNS involvement would still need intrathecal therapy.

### Why not a degrader with a tissue-selective E3 ligase

Considered and rejected. The concept is real and newly demonstrated — a **MAGEA11**-recruiting PROTAC
(Nov 2025) degrades BET proteins in cancer cells but not in MAGEA11-deficient normal cells, the first
tissue-restricted E3 ligase PROTAC. The field explicitly calls this "largely unexplored."

But it fails here on Constraint 1: any degrader destroys the chaperone function. Barrier exclusion
achieves the same tissue restriction more simply, using anatomy instead of ligase biology.

---

# PART 5: THE COMBINATION, AND THE TP53 PROBLEM

**The NMNAT1 mechanism runs through p53.** So **TP53-mutant AML escapes it** — and TP53-mutant is the
worst-prognosis subgroup, the one excluded from the briquilimab conditioning results, the one
everything else in this project also fails.

**Pair it with the differentiation arm, which is p53-independent:**

| Arm | Mechanism | Covers |
|---|---|---|
| NMNAT1 inhibitor | Nuclear NAD⁺ collapse → sirtuins stall → p53 activated → apoptosis | p53-wild-type |
| LSD1 degrader (MS9117) + ATRA | Scaffold removal → GFI1 repression released → differentiation | p53-mutant included |

Neither covers both. Together they do — and they attack the **same underlying dependency from two
directions.**

**The unifying observation:** AML LSCs lean on *two separate deacetylase systems* — NAD⁺-dependent
sirtuins (class III) keeping p53 switched off, and HDAC1/2 within LSD1–CoREST keeping differentiation
genes switched off. **One dependency, two arms.** Starve the sirtuins of nuclear NAD⁺ and dismantle
the LSD1 scaffold, and both arms of the acetylation blockade fall at once.

That framing is this project's own synthesis. No source found states it.

---

# PART 6: REQUIREMENTS CHECK

| Requirement | Verdict |
|---|---|
| **Does not already exist** | ✅ Target validated, but only screening-hit inhibitors. No optimized, selective, or barrier-designed NMNAT1 inhibitor. The two design constraints are unarticulated in the literature found. |
| **Plausibly works** | ✅ Published LSC-specific mechanism, PDX validation, dispensable for normal hematopoiesis, precursor-bypass-proof, venetoclax synergy |
| **Involves making a molecule** | ✅ Small-molecule enzyme inhibitor — a highly druggable class, with hit compounds already available as chemical starting points |
| **Uses Malone or Sinclair** | ✅ **Sinclair:** NAD⁺, sirtuins, his foundational area — applied to a nuclear-compartment dependency he never addressed. **Malone:** the paired arm is repressor-complex release and differentiation reactivation, adjacent to his SIN3-HDAC and RARB/ATRA claims |
| **Edge cases considered** | ✅ Retinal toxicity (Constraint 2), chaperone function (Constraint 1), TP53-mutant escape (Part 5), NAD-precursor bypass (closed by gatekeeper property), CNS sanctuary (acknowledged, unsolved) |

---

# PART 7: OPEN THREADS

- Does NMNAT1 inhibition reach the **dormant** LSC specifically, or only cycling LSCs? The Science
  Advances work shows LSC reduction but not dormancy-state resolution.
- Is a barrier-excluded chemotype achievable while retaining potency at the NMNAT1 active site?
  Standard medicinal-chemistry tension.
- Does the marrow's hypoxic niche alter NAD⁺ metabolism enough to change the dependency?
- Confirm SIRT6/7 as the mediating sirtuins in primary human LSCs, not just cell lines.
- Test whether the NMNAT1 + LSD1-degrader combination is synergistic or merely additive.

---
---

# RUN 2 — Loops 19–30

Continued per the updated skill (150-loop minimum; broaden rather than stop). Started by attacking
the surviving idea rather than defending it.

## CORRECTION TO RUN 1

Run 1 claimed NMNAT1 was uniquely LSC-selective — *"nothing else in this project achieved this."*
**That was wrong. I simply had not looked.** At least four independent mechanisms show the
LSC-selective / normal-HSC-sparing profile:

| Target | Evidence | Agent status |
|---|---|---|
| **NMNAT1** (nuclear NAD+) | LSC reduction in murine + PDX; "dispensable for normal hematopoiesis" | Screening hits only |
| **NCOA4** (ferritinophagy) | Kills **quiescent CD34+CD38−** subset; minimal normal-cell toxicity; PDX validated | **Compound 9a exists** |
| **Telomerase** (imetelstat) | Kills LSCs in pediatric AML PDX, limited effect on normal marrow stem cells | **FDA approved (MDS)** |
| **ELAVL1/HuR** (RNA-binding) | In vivo CRISPR screen; "selectively depleted primitive malignant versus healthy cells" | Tool compound MS-444 |

LSC-selectivity is less rare than Run 1 concluded.

## Loop 19 — Attack on NMNAT1: **SURVIVED, and strengthened**

- *"NMNAT1 loss only slightly affected genome integrity without any impact on cell proliferation,
  suggesting that targeting NMNAT1 could have no toxic impact in normal tissue."*
- **Why NAMPT inhibitors failed clinically** — FK866 and others died of "toxicity and resistance"
  precisely *because NAMPT is not compartmentalized*: inhibiting it drains NAD+ from all three
  compartments at once. NMNAT1 compartment restriction is the specific fix for the specific reason
  the predecessor class failed.
- Nuclear NAD+ salvage is also a vulnerability in B-lymphoid malignancies — broader applicability.
- Residual risk: three NAD+ synthesis routes exist (de novo/tryptophan, salvage/NAM,
  Preiss-Handler/nicotinic acid) and could in principle compensate — though the gatekeeper finding
  (precursors bypass NAMPT but *not* NMNAT1) argues against it.

## Loops 22–23 — Imetelstat: **THE CAUTIONARY DATA POINT**

Imetelstat is LSC-selective, spares normal HSCs, and is **FDA approved** — for lower-risk MDS. In
AML it **underperformed**: the IMpress trial showed "minimal efficacy in higher-risk MDS and AML."
It remains in combination trials (IMAGINE: + azacitidine ± venetoclax).

**This is the most important negative finding of the run.** An agent with exactly the profile we have
been hunting — LSC-selective, normal-sparing, PDX-validated — reached the clinic in AML and did not
deliver. That is a direct warning to NMNAT1, NCOA4, and ELAVL1, all of which rest on the same class
of evidence. *LSC-selectivity in PDX is not yet a demonstrated predictor of clinical benefit in AML.*

Also noted: imetelstat induces ferroptosis via fatty acid metabolism changes in AML — mechanistically
adjacent to the NCOA4/iron axis.

## Loop 20 — Mitochondrial transfer: **explains a prior failure**

Bone marrow stroma transfers functional mitochondria to AML cells via **tunneling nanotubes** and
macropinocytosis, conferring chemoresistance. Critically: **OxPhos inhibition itself induces the
transfer.** Attack the metabolism and the niche resupplies the cell.

That retroactively explains why the OxPhos-targeting approaches discussed earlier in this project
underperformed. Blockable by ICAM-1 neutralizing antibody, microtubule inhibitors, or cytochalasin B —
none selective enough to be a drug on its own.

## Loops 24–25 — SIN3A/PAH2: **Malone claim validated elsewhere, GAP in AML**

Malone claimed "release of a SIN3-HDAC repressor complex" and "RARB restoration." Both correspond to
real published biology:

- The SIN3A **PAH2 domain** binds the SID motif of transcription factors such as MAD1, recruiting
  HDAC1/2 to chromatin.
- **Blocking the PAH2–SID interaction with SID peptides or small-molecule inhibitors increased RARβ
  expression and induced retinoic acid metabolism** — in breast cancer, in vitro and in vivo.
- In leukemia, the **UHRF1–SAP30–MXD4 axis** (SAP30 is a SIN3A-associated protein; MXD4 is a
  MAD-family SID protein) has been targeted for "leukemia initiating cell eradication."

**The gap:** PAH2 inhibitors have been pursued in breast cancer. No published work applies them to
AML — despite RARβ restoration being the same differentiation/ATRA-sensitization axis that LSD1
inhibitors exploit. This is the most direct Malone-derived opening found in the entire project.

## Loop 26 — NMNAT1 structural tractability: **unusually favorable**

- The three isoforms have **different quaternary structures**: NMNAT1 is a homohexamer, NMNAT3 a
  homotetramer, NMNAT2 a monomer. Oligomerization interfaces differ completely — a strong handle for
  isoform selectivity beyond the conserved active site.
- Crystal structures exist for NMNAT1 and NMNAT3 (apo and substrate-bound); NMNAT2 has only a
  homology model.
- A **cryo-EM structure of NMNAT1 bound to inhibitor AMI-1** exists, with the inhibition mechanism
  resolved.

## Loops 28–29 — Barrier exclusion: **feasible, with concrete numbers**

Designing for CNS/retinal exclusion is an established strategy, not a hope:

- Make the compound a **P-gp (ABCB1) / BCRP (ABCG2) substrate** — both are expressed on the luminal
  membrane of the inner blood-retinal barrier and actively pump substrates out of the retina.
- Property targets: **MW < 500 and PSA < 140** preserve oral absorption; **MW < 450 and PSA < 70**
  are required *for* CNS penetration. So aim for **PSA ~70–140, MW ~450–500** — orally absorbed,
  centrally excluded.
- This "delivers significant CNS restriction whilst retaining good oral bioavailability."

**Caveat found:** retina and brain do not behave identically — P-gp/BCRP inhibition affects erlotinib
distribution differently in retina versus brain, and retinal distribution "has hardly been
investigated." BBB exclusion does not automatically guarantee BRB exclusion. Needs direct testing.

## Loops 27, 30 — ELAVL1/HuR: **new candidate, high AI-tractability**

- In vivo two-step CRISPR screen: 32 RNA-binding proteins essential for LSCs; **ELAVL1 selectively
  depleted primitive malignant versus healthy cells.**
- Mechanism spans differentiation, splicing, and mitochondrial metabolism; TOMM34 (mitochondrial
  import) is a directly stabilized target.
- Tool compound **MS-444** blocks ELAVL1 dimerization; **in primary AML specimens it "significantly
  induced myeloid maturation and increased cell death,"** with no appreciable effect on
  non-transformed cells in the colorectal comparison.
- RNA-binding proteins are classically "undruggable" — no enzymatic pocket, flat RNA-binding
  surfaces. **That is exactly the class modern structure prediction and de novo binder design newly
  opens**, which scores it high on AI-tractability precisely because it was hard before.

---

# RE-RANKING AGAINST THE TWO NEW CRITERIA

Scored on **(a)** plausible path to an FDA-approvable overall-survival benefit and **(b)** whether
modern AI/ML/simulation newly unlocks it.

### 1. NMNAT1 catalytic inhibitor — **still the lead**

**AI unlocks:** a four-way simultaneous optimization that would have been a brutal medicinal-chemistry
grind before — (i) potency at the NMNAT1 active site, (ii) selectivity over NMNAT2/NMNAT3 via their
*different oligomeric interfaces*, (iii) deliberate barrier exclusion to a specified property window
(PSA 70–140, MW 450–500, P-gp substrate), (iv) catalytic-only inhibition preserving the
neuroprotective chaperone function. A solved cryo-EM structure with a bound inhibitor gives
generative design a starting point.

**FDA path:** add-on to venetoclax (synergy already demonstrated) in p53-wild-type AML — a two-agent,
biomarker-selected trial, which is an approvable design.

**Main risks:** the imetelstat precedent, and TP53-mutant escape.

### 2. SIN3A PAH2–SID inhibitor in AML — **best novelty, direct Malone lineage**

**AI unlocks:** PAH2–SID is a protein-protein interface — a flat, historically undruggable surface
now approachable via structure prediction and de novo binder/peptidomimetic design.

**FDA path:** restores RARβ and retinoic-acid metabolism, so it pairs naturally with ATRA — and
ATRA-plus-X combination trials in AML are a well-trodden regulatory route.

**Why it ranks high:** genuinely unclaimed in AML, mechanistically validated elsewhere, and the
closest this project has come to Malone being *right about the underlying biology*.

### 3. ELAVL1/HuR binder — **highest AI leverage, highest risk**

Previously undruggable target class; LSC-selective by in vivo CRISPR; induces myeloid maturation in
primary AML. MS-444 is an unoptimized natural product, leaving real design room.

### 4. NCOA4/ferritinophagy — **best biology, least left to design**

Uniquely validated in the *quiescent* subset — the exact population this project targets — but
compound 9a already exists, so there is less of a molecule-design opportunity.

---

# OPEN THREADS AFTER RUN 2

- Does NMNAT1 dependency hold in *quiescent* LSCs specifically? NCOA4 has this evidence; NMNAT1 does not.
- Confirm that blood-retinal-barrier exclusion tracks with BBB exclusion for a given chemotype.
- Test SIN3A PAH2 inhibitors in AML primary cells — the single cheapest high-value experiment identified.
- Does mitochondrial transfer from stroma rescue cells from NAD+ or iron depletion the way it rescues
  them from OxPhos inhibition? If so, every metabolic approach inherits that resistance mechanism.
- Why did imetelstat fail in AML despite LSC selectivity? The answer likely predicts whether NMNAT1,
  NCOA4, and ELAVL1 will too.

---
---

# RUN 3 — Loops 31–36: THE FERROPTOSIS CONVERGENCE

## SECOND CORRECTION: imetelstat is a bad witness

Run 2 called imetelstat "the most important negative finding" — an LSC-selective agent that failed in
AML, casting doubt on the whole thesis. **That reading was too harsh, because imetelstat was not
working through its nominal mechanism.**

- **Telomere length did not predict clinical response**, and did not change in responders.
- It has telomerase-independent off-target effects (cell rounding, loss of adhesion).
- **Its actual AML activity runs through lipid ROS and ferroptosis** (Nature Cancer).
- It has a built-in escape route: ALT (alternative lengthening of telomeres).

So imetelstat is a poor test of "LSC-selective agents work." Its mechanism was misattributed. That
partially rehabilitates NMNAT1, NCOA4, and ELAVL1, whose mechanisms are cleanly attributed.

**And the finding redirects the run:** imetelstat kills AML by ferroptosis.

## The four-way convergence

Four independent lines, found in separate loops, all land on the same axis — **lipid peroxidation
defense**:

| Line | Finding | Population validated |
|---|---|---|
| **NCOA4 / ferritinophagy** | Controls iron availability; compound 9a kills the CD34+CD38− subset | **Quiescent LSC** |
| **Imetelstat** | Real AML mechanism is lipid ROS / ferroptosis, not telomerase | AML PDX |
| **Cysteine / SLC7A11** | Cysteine drives glutathione synthesis; depletion impairs energy metabolism in **ROS-low LSCs but not normal HSPCs** | **Quiescent LSC** |
| **GPX4** | The terminal enzyme detoxifying lipid peroxides | See below |

The pathway is one loop: cystine enters via **SLC7A11** → cysteine → **glutathione** → the cofactor
**GPX4** uses to neutralize lipid peroxides, while **NCOA4** releases the ferritin-bound iron that
generates those peroxides in the first place.

**The vulnerability this exposes:** LSCs run high iron flux *and* lean hard on the GPX4 antioxidant
shield. They are walking a tightrope. Normal HSCs are not — they are hypoxia-protected and, crucially,
**low-GPX4**.

**Important conflict to note:** NCOA4 inhibition and GPX4 inhibition are *opposite* strategies. NCOA4
blockade kills by starving iron; GPX4 blockade kills by exploiting iron. Combining them would
antagonize. This is a fork, not a stack.

## Loop 34 — GPX4: a real selectivity window, in the right direction

- **"GPX4 is differentially expressed according to myeloid differentiation stage, exhibiting lower
  expression in hematopoietic stem cells. In contrast, GPX4 is highly expressed in most AML subtypes
  compared to normal hematopoietic stem cells."**
- **"Acquired depletion is reported to have no significant effect on hematopoietic stem cells,
  suggesting tolerability of GPX4-targeted therapies for normal hematopoiesis."**
- Ferroptosis induction targets leukemia stem cells and synergizes with TKIs in BCR-ABL+ disease.

This is the "difference of degree" property the earlier half of this project kept running into — but
for once pointing the right way, and with normal HSCs shown to tolerate loss.

## Loop 35 — GPX4 druggability: THE SHARPEST GAP IN THE PROJECT

- **GPX4 has a shallow active site "not amenable to interacting with small molecules."** No drug-like
  binding pocket. It is a canonical difficult-to-drug target.
- Existing inhibitors (RSL3, ML210) have poor pharmacokinetics and low selectivity that "preclude
  their clinical use."
- **The damning finding:** cell-free assays show that **RSL3 and ML210 fail to inhibit purified
  GPX4 at all** — they hit **TXNRD1** and other selenoprotein-synthesis machinery instead.

  *A large body of GPX4 literature may therefore be mechanistically misattributed — the same failure
  mode just found for imetelstat, in the same run.*
- Crystal structures exist: apo GPX4, and GPX4 covalently bound to ML162.
- Promising chemistry direction: **masked nitrile-oxide electrophiles**, reported to give "unexpected
  proteome-wide selectivity and vastly improved physicochemical and pharmacokinetic properties."

**Net: there is no validated, selective, drug-like GPX4 inhibitor. The field's standard tool compounds
do not hit the target. The structures are solved. The problem is open.**

## Loop 36 — NRF2: the upstream master switch, and an approvable combination

- **NRF2 inhibition (ML385) markedly enhances venetoclax killing via ferroptosis** — the combination
  produced equal or greater cell death than venetoclax + azacitidine, the current standard of care.
- NRF2 is the master transcriptional regulator of the antioxidant response and drives expression of
  **both SLC7A11 and GPX4** — so blocking NRF2 collapses the entire defense axis at once.
- Separately: low-dose hypomethylating agents cooperate with ferroptosis inducers via the
  MAGEA6–AMPK–SLC7A11–GPX4 pathway. **Azacitidine, already standard of care, sensitizes to ferroptosis.**

That gives an approvable trial design: a novel ferroptosis inducer added to an existing
venetoclax/azacitidine backbone.

---

# THE LEAD IDEA AFTER 36 LOOPS

## A selective, drug-like covalent GPX4 inhibitor for AML

**The molecule:** a covalent inhibitor engaging GPX4 selenocysteine-46, built on a masked
nitrile-oxide (or comparable tuned-reactivity) warhead rather than the chloroacetamide chemistry that
produced the failed tool compounds.

**Design constraints, all derived from findings above:**

1. **Must actually inhibit purified GPX4** — a bar the field's two standard tools fail. Cell-free
   validation against purified enzyme is non-negotiable, not an afterthought.
2. **Selectivity against TXNRD1 and the wider selenoprotein machinery** — the specific off-target that
   invalidated RSL3 and ML210.
3. **Drug-like PK** — the failure mode that kept every prior GPX4 compound preclinical.
4. **Tuned warhead reactivity** — potent enough for a shallow pocket with no conventional binding
   site, selective enough to avoid proteome-wide covalent promiscuity.

### Why it beats NMNAT1 on the stated criteria

| Criterion | Assessment |
|---|---|
| **Does not exist** | Strongest in the project — not only is there no clinical candidate, the standard tool compounds **do not hit the target at all** |
| **Plausibly works** | Four independent lines converge on ferroptosis; GPX4 high in AML / low in normal HSC; normal HSCs tolerate depletion; synergy with venetoclax demonstrated |
| **Is a molecule** | Small-molecule covalent inhibitor; crystal structures available (apo and ML162-bound) |
| **AI newly unlocks it** | **Best fit found.** A shallow, "undruggable" pocket, covalent warhead reactivity tuning, selectivity against a closely related selenoprotein family, and PK optimization — four coupled constraints on a structurally solved target. This is precisely the problem class that generative chemistry plus structure prediction opens and that defeated conventional medicinal chemistry for a decade |
| **FDA path** | Add-on to the venetoclax/azacitidine backbone, which independently sensitizes cells to ferroptosis. Two-agent, approvable design |

### Honest risks

- **GPX4 is essential in several normal tissues** (kidney, T cells) and germline knockout is
  embryonically lethal. The hematopoietic tolerance finding is encouraging but does not clear
  systemic toxicity. **This is the single biggest open question and it is not resolved.**
- **The misattribution problem cuts both ways.** If RSL3/ML210 were not inhibiting GPX4, then some
  evidence for "GPX4 inhibition kills AML" may actually be evidence for TXNRD1 inhibition. The
  target's validation needs re-examination with genuinely selective tools — which is partly what the
  proposed molecule would provide.
- **Covalent inhibitors carry inherent off-target and immunogenicity risk.**
- Ferroptosis induction is systemic biology; whether the marrow niche resupplies antioxidant capacity
  (as it resupplies mitochondria via tunneling nanotubes) is untested.

### The fork to decide

**Iron starvation (NCOA4, compound 9a exists, quiescent-LSC validated)** versus **ferroptosis
induction (GPX4/SLC7A11, no good molecule exists, bigger design opportunity)**. These antagonize;
pick one. The first is better validated in the exact target population. The second is the far larger
unmet design problem and the better fit to this project's AI-driven premise.

---

# LOOP COUNT: 36

Not 150. Reported honestly per the skill. The run has not exhausted its leads — remaining threads are
listed below and the ferroptosis lane in particular has more to give.

# OPEN THREADS AFTER RUN 3

- Resolve GPX4 essentiality in normal adult tissues — the gating question for the lead idea.
- Re-examine which AML "GPX4 inhibition" results actually reflect TXNRD1 inhibition.
- Does the niche resupply glutathione or antioxidant capacity to LSCs, as it resupplies mitochondria?
- Test whether NCOA4 inhibition and GPX4 inhibition genuinely antagonize, as predicted here.
- Is TXNRD1 itself the better target, given that the tool compounds hitting it did kill AML cells?
- SIN3A PAH2 inhibitors in AML primary cells — still the cheapest high-value experiment identified.
