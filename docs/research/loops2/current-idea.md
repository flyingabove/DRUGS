# Current Idea — Track 2 Live State

**Read this plus [dead-ideas.md](dead-ideas.md) to reload track 2. Track 1 (GPX4/ferroptosis) lives
separately at [../loops/current-idea.md](../loops/current-idea.md) and is unaffected.**

Loop count: **72**. Status: **strong, not airtight.** See HOLES.

---

## THE IDEA — "Tip the Dimer"

**Don't kill the leukemia, and don't just differentiate it — control *which lineage it differentiates
into*, so it dies on its own schedule.**

The therapeutic entity: **a designed, C/EBPγ-selective dominant-negative bZIP miniprotein**, given
**with** an approved differentiation therapy, to redirect leukemic maturation from the long-lived
monocytic exit to the short-lived neutrophil exit.

Nothing is killed. No LSC-vs-HSC selectivity window is required. The agent chooses an **exit route.**

---

## THE LOGIC CHAIN

**1. Differentiation therapy already works — partially.** ATRA/ATO, IDH1/2 inhibitors, menin
inhibitors. Enasidenib: 40% response in R/R AML. Relapse is prevalent. Menin inhibitors do engage the
LSC: *"disruption of the menin–KMT2A interaction results in… loss of leukemic stem cell properties."*

**2. Why APL is the one cure.** *"Immortal, malignant promyelocytes are converted into mortal
neutrophils."* Neutrophils live ~1 day. **The cure mechanism is conversion to a lineage with an expiry
date**, not killing.

**3. Why the others fail — the escape lineage.**

| Therapy-induced lineage | Fate | Relapse contribution |
|---|---|---|
| Leukemia-derived **neutrophils** | *"Clear rapidly"* | **None** |
| Long-lived lineages (**eosinophil** in mouse, **monocytic** in human) | ***Persist during remission*** | **The reservoir** |

**4. The genetic proof.** *"Restricting therapy-induced leukemia maturation to the short-lived
neutrophil lineage markedly reduces relapse rates and **can yield cure**."* Achieved by blocking the
escape lineage — *"all AML cells matured into neutrophils."* **A cure claim in vivo, by lineage
control alone.** Strongest efficacy evidence in either track.

**5. Human relevance — and it is worse than "just relapse".** Patients on revumenib show
*"intermediate and **monocytic** cells enriched in post-treatment samples."* And monocytic AML
*"suppresses BCL2… relies on MCL1… rendering [it] inherently resistant to venetoclax plus
azacitidine"* — **genotype-independently**, per AML-derived iPSC work.

> **The original claim of this track:** menin/IDH differentiation therapy drives monocytic
> maturation; monocytic state confers venetoclax resistance; these agents are being **combined with
> venetoclax**. **Differentiation therapy may be manufacturing the resistance it is paired with.**
> Every link is published. The chain does not appear to be drawn anywhere.

**6. Lineage steering is already proven pharmacologically.** *"ATRA + **G-CSF** → **neutrophils**;
ATRA + **GM-CSF** → **eosinophils**."* Same leukemia, same driver, exit decided by the co-agent.
*Why not just use G-CSF? It signals through G-CSFR, which AML blasts express — a **proliferative**
signal, and its use in AML is "controversial due to a theoretically increased risk of relapse." We
want a cell-intrinsic, non-mitogenic steer.*

**7. The node: the C/EBPα:C/EBPγ dimer.**
- **C/EBPα drives granulocytic/neutrophil fate** — *"conditional expression of C/EBPα triggers
  neutrophilic differentiation."*
- **C/EBPγ is a dominant negative.** It retains the basic region and leucine zipper but **has no
  transactivation domain**, so heterodimerizing with C/EBPα produces a dead complex.
- *"Downregulation of Cebpg… **completely restored granulocytic differentiation**."*
- **The convergence:** C/EBPγ binds and represses the promoters of **CSF3R** (the G-CSF receptor) and
  **CEBPE**. Remove C/EBPγ → CSF3R rises → the cell becomes G-CSF-responsive. **The dimer switch and
  the lineage switch are the same switch** — which is why finding #6 and finding #7 are one mechanism.

---

## THE SELECTIVITY WINDOW — clean, and on the target itself

Every earlier target across both tracks was wounded by overlap with normal HSCs: CD123, CD33, CD44,
CD45, CXCR4, LSD1, HMG20B, MECOM/EVI1, GATA2, **and IRF8** (see the attack below).

> **"C/EBPγ is dispensable for steady-state and emergency granulopoiesis."** Conditional knockout,
> no defect. No difference in NK cells either — despite C/EBPγ being highly expressed across all
> hematopoietic cells.

**A dominant-negative regulator you can delete without harming normal blood production.** This is the
first target in this project whose *own* loss-of-function is clean in normal hematopoiesis.

Contrast IRF8, the node considered first: germline *Irf8*-null mice develop a **CML-like
myeloproliferative neoplasm at 10–16 weeks**, with blast crisis in ~⅓. The pivot is better than the
original on **both** efficacy and safety.

---

## THE MOLECULE — design spec

**A C/EBPγ-selective dominant-negative bZIP miniprotein** (or a small molecule blocking the
C/EBPα–C/EBPγ coiled-coil, if a pocket is findable).

**Clinically validated modality precedent:** **OMO-103** — a 91-aa designed dominant-negative
miniprotein from MYC's B-HLH-LZ domain with four substitutions, which *"can enter cells and reach its
target within the nucleus."* **Completed Phase 1** (*Nature Medicine* 2024, 22 patients): safe, mainly
grade-1 infusion reactions, one PR, one patient stable 26 months. The **first MYC inhibitor to
complete a Phase 1**. The exact modality, in humans, against an "undruggable" TF dimer.

**Mature design toolkit:**
- **A-ZIPs** = leucine zipper + acidic amphipathic N-terminal extension; new designs stabilize
  heterodimerization **up to 11 kcal/mol**; A-C/EBP regresses pre-formed papilloma in vivo
- **"The specificity of dominant-negative action is determined by the leucine zipper"** — specificity
  is a designable parameter, not a lucky property
- **Ubiquitin-tagged** dominant negatives can *degrade* the captured bZIP, not just sequester it
- Designed bZIP-binding peptides reach **nanomolar** IC50

**Design constraints:**
1. **Selective for C/EBPγ over C/EBPα, β, δ, ε.** This is the hard problem and the whole ballgame —
   a pan-C/EBP dominant negative would ablate C/EBPα too and abolish the very differentiation we want.
2. **No self-association** (the documented failure mode for designed bZIP inhibitors).
3. **Intracellular + nuclear delivery to marrow cells.** The acknowledged bottleneck. OMO-103 shows it
   is achievable; engineered peptide coacervates delivered Omomyc as further precedent.
4. **Transient/pulsed exposure.** C/EBPα-driven fate commitment is **hit-and-run** — a 4-day
   induction produced a stable macrophage fate persisting after inducer withdrawal. Fate changes may
   not need chronic dosing.

## WHY AI UNLOCKS IT

**bZIP coiled-coil specificity is one of the best-posed protein design problems in existence** and
squarely inside what current tooling does well:
- Published **data-driven prediction and design of bZIP coiled-coil interactions**, with designed
  peptides interacting specifically with **19 of 20 human bZIP families**
- The target is a **paralog-selectivity problem across a near-identical family** — the project's named
  AI-tractability criterion, verbatim
- It is a **flat PPI interface** with no natural small-molecule pocket — the other named criterion
- Positive *and* negative design simultaneously (bind C/EBPγ, avoid C/EBPα/β/δ/ε, avoid self-
  association): multi-parameter optimization that serial medicinal chemistry attacks badly

---

# ⚠️ THE ATTACK THAT KILLED THE FIRST VERSION (loop 53) — keep for context

The first version of this idea proposed **inhibiting IRF8** (which physically binds C/EBPα and blocks
it from chromatin) to steer monocyte→neutrophil. Hunting for the paper that kills it found one:

Hartung et al., *Blood* 2024: in *Irf8*-knockout AML cells, **ATRA IC50 rose 151-fold** (47 nM →
7.1 µM); LSD1-inhibitor IC50 rose 9.7-fold. **IRF8 loss makes AML far MORE resistant to
differentiation therapy** — IRF8 appears required for the differentiation *response*, not just the
fate *choice*. You cannot steer the car by removing the engine.

**The C/EBPγ pivot dodges this entirely** by tilting the same ratio from the other side: C/EBPα
activity is *raised* rather than IRF8 *removed*, so the differentiation response stays intact.
**Retain this as the cautionary case** — perturbing this network can backfire, and the same question
must be asked of C/EBPγ blockade directly (hole #1).

---

# HOLES — ordered by how badly a bad answer hurts

## 1. Does C/EBPγ blockade STEER lineage, or merely restore differentiation? — **CRITICAL, UNTESTED**
All the C/EBPγ evidence shows it restores **granulocytic differentiation in CEBPA-silenced cells**.
That is not the same claim as *"redirects the exit lineage from monocyte to neutrophil in
CEBPA-normal AML undergoing differentiation therapy."* **The central claim of this idea has never been
tested.** And the Hartung result proves perturbations here can invert.
**This is the gating experiment: menin inhibitor ± C/EBPγ knockdown, read out lineage.**

## 2. Does it work in CEBPA-NORMAL AML? — **CRITICAL, UNTESTED**
The C/EBPγ literature is about AML where **C/EBPα is silenced**. The broad use requires tipping the
dimer where C/EBPα is present and functional. Plausible (more free C/EBPα → more neutrophil) but
unestablished.

## 3. Population size — **A REAL PROBLEM for the narrow indication**
*CEBPG*-high is **8 of 526 AML cases (~1.5%)**; CEBPA-silenced is **1.4–2.1%**. Desperate patients
(silenced CEBPA: **5-year OS 25% vs 88%** for CEBPA-mutant) but orphan-sized.
**Two distinct uses, do not conflate:** (a) narrow — CEBPG-high/CEBPA-silenced AML, strong evidence,
tiny population; (b) broad — lineage-steering add-on to differentiation therapy in general AML, large
population, **no direct evidence yet**. The program's value rests on (b), which is hole #2.

## 4. Selective C/EBPγ inhibition may be undesignable — **OPEN**
The bZIP zipper is what confers specificity, and C/EBP family zippers are similar by construction.
A-C/EBP inhibits the **whole family**. Achieving γ-over-α selectivity is the core design risk.
*This is also exactly why the project's AI tooling is the right instrument — but it could still fail.*

## 5. Delivery to marrow LSCs — **OPEN**
*"Intracellular delivery is a bottleneck in the development of therapeutic peptides and proteins."*
OMO-103 proves nuclear delivery is achievable in solid tumors; marrow LSCs are not solid tumors.

## 6. CEBPA-mutant AML is excluded — **KNOWN CONSTRAINT**
In CEBPA-mutant AML (10–20% of normal-karyotype AML) *"in all cases at least one allele capable of
producing p30 is retained"* — p30 binds DNA but lacks the N-terminal transactivation domain. No
functional p42 to liberate. **Biomarker exclusion.**

## 7. Does differentiation therapy reach the dormant LSC? — **PARTIALLY CLOSED**
Menin inhibitors collapse stemness networks and cause *"loss of leukemic stem cell properties."*
But track-2 structural lesson 6 stands: quiescent cells are chromatin-locked (*"vast histone
deacetylation and chromatin compaction"*), so a chromatin-opening partner may be required.

---

# EFFICACY EVIDENCE (the primary gate)

| Tier | Status |
|---|---|
| **Cure / eradication of leukemia-initiating capacity** | **YES — genetically, in vivo, murine.** *"Markedly reduces relapse rates and can yield cure."* Genetic, not pharmacological; mouse, not human |
| **Human relevance of the escape** | **YES for the phenomenon** (monocytic enrichment in revumenib patients; monocytic venetoclax resistance genotype-independent). **NO for the fix** — no human lineage-steering data |
| **C/EBPγ as the lever** | **YES for restoring granulocytic differentiation** in CEBPA-silenced AML. **NO for lineage steering** (hole #1) |
| **Primary patient LSC killing** | **N/A** — this strategy does not kill. Endpoint is relapse prevention |

**Verdict: the mechanism yields cure in a mouse by lineage control, the failure mode it fixes is
confirmed in humans, and the proposed lever is clean in normal hematopoiesis. The specific claim that
C/EBPγ blockade steers the exit lineage is untested. That is the one experiment that makes or breaks
this.**

---

# FALLBACKS (track 2)

1. **Raise C/EBPα by other routes** — all have existing agents:
   - **MTL-CEBPA** — first-in-class saRNA upregulating CEBPA. Phase 1 in liver cancer, **no MTD
     reached**, acceptable safety. **Already applied to AML (2025):** boosts CEBPA, promotes a
     *"non-proliferative, mature state"* in FLT3-mutant AML, synergizes with gilteritinib in vivo.
     *Novelty hit on the repurposing angle — but framed as maturation, not lineage steering.*
   - **CDK1 inhibition** — CDK1 phosphorylates C/EBPα at Ser21 to inactivate it; inhibition relieves
     the block in primary patient samples
   - **CDK2 degraders** — CDK2→SKP2→C/EBPα degradation; a first-in-class selective CDK2 degrader
     *"induced remarkable differentiation of AML cell lines and primary patient cells"*
   - **TRIB2/COP1** — degrades C/EBPα p42; *"clinically untargeted vulnerability"*; afatinib
     (approved) degrades TRIB2 and synergizes with cytarabine
2. **IL5RA / benralizumab** — for the *eosinophil* escape if ever shown in humans. Retains the
   cleanest lineage-marker selectivity found (IL5RA absent from HSCs/MPPs) and 4+ years of human
   eosinophil-depletion safety with no immune compromise.
3. **ZMYND8** — upstream regulator of the IRF8–MEF2D circuit; ablation abrogates AML proliferation
   in vivo. Bromodomain-containing, so a better-precedented target class — but no selective chemical
   probe exists.
