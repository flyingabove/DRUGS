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
