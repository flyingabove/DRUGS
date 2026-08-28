# Current Idea — Track 2 Live State

**Read this plus [dead-ideas.md](dead-ideas.md) to reload track 2. Track 1 (GPX4/ferroptosis) lives
separately at [../loops/current-idea.md](../loops/current-idea.md) and is unaffected by this track.**

Loop count: **28**.

---

## THE IDEA — "Close the Escape Hatch"

**Don't kill the leukemia and don't just differentiate it — control *which lineage it differentiates
into*, so it dies on its own schedule.**

The one-sentence version: **existing differentiation therapy already works; it fails because the
leukemia escapes down a long-lived lineage. Shut that exit and the same drugs become curative.**

This is a fundamentally different therapeutic logic from everything else in this project. Nothing is
being killed. No selectivity window between LSC and HSC is required. The agent chooses an *exit
route*.

---

## THE LOGIC CHAIN

**Step 1 — Differentiation therapy already exists and already works, partially.** ATRA/ATO, IDH1/2
inhibitors, menin inhibitors. Responses are real (enasidenib: 40% response in R/R AML) but relapse is
prevalent.

**Step 2 — Why APL is the one cure.** APL promyelocytes are forced into **neutrophils** — *"immortal,
malignant promyelocytes are converted into mortal neutrophils."* Neutrophils live ~1 day. The cure
mechanism is not killing; it is **conversion to a lineage with a built-in expiry date**.

**Step 3 — Why every other differentiation therapy fails.** Differentiation therapy produces **two**
mature lineages, and only one of them expires:

| Therapy-induced lineage | Fate | Contribution to relapse |
|---|---|---|
| Leukemia-derived **neutrophils** | *"Clear rapidly"* | **None** |
| Leukemia-derived **eosinophil-like cells** | ***Persist during remission, often in extramedullary organs*** | **This is the relapse reservoir** |

**Step 4 — The genetic proof.** *"Restricting therapy-induced leukemia maturation to the short-lived
neutrophil lineage markedly reduces relapse rates and **can yield cure**."* Achieved by selectively
blocking eosinophil differentiation — *"all AML cells matured into neutrophils."*

**That is a cure claim in vivo, achieved by lineage control alone.** It is the strongest efficacy
evidence found anywhere in this project, across both tracks.

**Step 5 — Nobody has drugged it.** The Nature Communications authors state the implication in their
own discussion — *"differentiation therapy combined with targeted eradication of mature
leukemia-derived lineages may improve disease outcome"* — and stop there. The genetic tool exists.
**The drug does not.**

---

## THE SELECTIVITY WINDOW — the first clean one in this project

Every prior target across both tracks was wounded or killed by overlap with normal HSCs: CD123, CD33,
CD44, CD45, CXCR4, LSD1, HMG20B, MECOM/EVI1, GATA2.

**IL5RA (CD125) is different, by developmental logic rather than luck:**

> *"IL5RA gene expression was detectable in the first identifiable eosinophil progenitors, but not
> earlier"* — **absent from normal HSCs and multipotent progenitors.** Expression begins only *after*
> the divergence point of the basophil/mast-cell and eosinophil lineages, **only in cells committed
> to the eosinophil fate.**

And the target population expresses it: *"IL5RA transcript and CD125 surface protein were found in
both immature and eosinophil-like leukemic cells"* — so it covers the reservoir **and** immature
leukemic cells, while sparing HSCs.

**Human safety of depleting this lineage is already established.** Benralizumab (anti-IL-5Rα,
approved) produces near-complete eosinophil depletion for **4+ years** with *"no evidence of increased
infection risk or immunologic compromise"*, no malignancy signal, no autoimmune signal. Eosinophils
are, in practice, dispensable.

---

## TWO IMPLEMENTATIONS — near-term and designed

### (A) Fast path — repurposing, low design risk
**Approved differentiation agent + anti-IL-5Rα (benralizumab)** in a biomarker-selected population.
Adds one approved agent to an approved backbone. Cheapest possible test of the whole thesis.
*Weakness: this is repurposing, not design — it scores poorly on the project's AI-tractability
criterion. Also an IgG1, and the reservoir sits in **extramedullary organs**, where antibody
penetration is poor.*

### (B) Designed path — the molecule this project would actually build
**A small-molecule lineage-steering agent that acts at the fate decision point**, so the persistent
cell is never made rather than chased into tissue sanctuaries.

The molecular switch is transcription-factor stoichiometry, not a receptor:
- **GFI1 + C/EBPα high → neutrophil** (the exit we want)
- **PU.1 + IRF8 high → monocyte/DC**; **GATA2 high → eosinophil** (the exits we want closed)
- **IRF8 physically binds C/EBPα and prevents its chromatin binding**, blocking neutrophil
  differentiation — a documented, structurally-defined PPI

**No small-molecule inhibitor of the IRF8–C/EBPα interaction exists** (loop 22, tentative).

*Why a small molecule beats the antibody here:* tissue penetration into the extramedullary sanctuary
sites where the reservoir actually lives.

---

## WHY AI UNLOCKS IT

**A transcription-factor–transcription-factor protein–protein interface.** Flat, no natural small-
molecule pocket, historically the definition of undruggable — and precisely the class the project's
AI-tractability criterion names as newly approachable via structure prediction plus de novo binder
and interface design.

Additional AI leverage: the target is a **ratio**, not an on/off switch. Steering a fate decision means
tuning relative TF activity without abolishing either factor — a multi-parameter optimization problem
of exactly the shape generative design plus property prediction attacks well, and that serial
medicinal chemistry attacks badly.

---

# HOLES — STATUS, ordered by how badly a bad answer hurts

## 1. Does the eosinophil-persister phenomenon occur in HUMAN AML? — **CRITICAL, UNVERIFIED**
The entire thesis rests on a **mouse model**. If therapy-induced eosinophil-like persisters are a
mouse artifact, the idea is dead. Must find human evidence: patients on IDH or menin inhibitors
showing eosinophilic differentiation or persistent mature leukemic cells.
**This is the next search, and it is the make-or-break question.**

## 2. Has the follow-up combination already been published? — **UNVERIFIED**
The authors proposed it in their discussion; the Mark Foundation funds *"Preventing Relapse Following
AML Differentiation Therapy."* High risk that the originating lab has already executed this.
**Novelty is not yet established. Do not claim it.**

## 3. Is there already a selective TRIM28 inhibitor driving neutrophil differentiation? — **UNVERIFIED**
One search summary claimed *"a selective small-molecule TRIM28 inhibitor induces neutrophil
differentiation with anti-leukemia activity."* A follow-up search did **not** confirm it. If it
exists, it is either a competitor or the ideal partner agent. **Claim came from a search summary, not
a read paper — treat as unverified.**

## 4. Does this reach the dormant LSC at all? — **OPEN, AND POSSIBLY MISFRAMED**
This strategy targets the *differentiated progeny*, not the dormant LSC. That may be a feature
(it closes the relapse route) or a fatal gap (the dormant LSC is untouched and reseeds anyway).
Track-2 structural lesson 6 applies: quiescent cells are chromatin-locked against reprogramming.
**Unresolved: does differentiation therapy engage the dormant compartment in the first place?**

## 5. Which node is druggable — IRF8–C/EBPα, or the GATA2 axis? — **OPEN**
IRF8–C/EBPα governs *monocyte* vs neutrophil. The persister lineage is *eosinophil*, which is
GATA2-driven. These may be different switches, and GATA2 is essential in normal HSCs
(haploinsufficiency causes marrow failure — MonoMAC/Emberger). **The exact druggable node is not yet
identified.**

## 6. Extramedullary penetration — **OPEN**
The reservoir is in extramedullary organs. Any agent must get there. Favors small molecule over
antibody; unquantified either way.

---

# EFFICACY EVIDENCE (the primary gate)

| Tier | Status |
|---|---|
| **Eradicates leukemia-initiating capacity / cure** | **YES, genetically, in vivo (mouse).** *"Markedly reduces relapse rates and can yield cure."* Strongest efficacy claim in either track — but genetic, not pharmacological, and murine |
| **Primary patient LSC killing ex vivo** | **NOT APPLICABLE / NOT SOUGHT** — this strategy does not kill LSCs. Efficacy is measured as relapse prevention, not cytotoxicity |
| **Human relevance** | **UNVERIFIED — hole #1** |

**Verdict: the mechanism prevents relapse and yields cure in a mouse model, by lineage control alone.
Human relevance is unestablished and is the gating question.**

---

# FALLBACKS (track 2)

1. **PU.1 restoration** — *"Restoring endogenous PU.1 activity in established AML is sufficient to
   trigger robust differentiation into polymorphonuclear neutrophil-like cells, with sustained
   disease clearance."* Note it produces the *right* (neutrophil) lineage. No PU.1 **agonist** small
   molecule exists — only inhibitors (DB1976, DB2115, DB2313). Real gap, hard modality.
2. **C/EBPα hit-and-run reprogramming** — 4-day induction produces a **stable** macrophage fate that
   persists after the inducer is withdrawn. Permanent fate change from transient dosing. Mostly
   B-lineage data so far; the *hit-and-run* property is the valuable part and transfers.
3. **In vivo DC transdifferentiation** — Kit-M (GM-CSF + PGE1) converts AML blasts to DCleu *without
   inducing blast proliferation*; DC vaccines show most benefit *in the MRD setting* — our exact
   population. Currently ex vivo manufacturing; in vivo small-molecule version is open.
