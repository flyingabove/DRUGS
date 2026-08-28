# Strategy 5: The Armor Is the Target — A GPX4 Program for Venetoclax-Resistant AML

**Thesis in one line:** leukemic stem cells survive their own iron load by armoring up with GPX4.
That armor is not incidental — it is a dependency. Strip it and they die of a mechanism their
apoptosis-resistance cannot touch.

**The drug:** a drug-like, kidney-sparing, selective covalent **GPX4 inhibitor**, paired with an
**FSP1 inhibitor**, on a venetoclax/azacitidine backbone, for **venetoclax-resistant AML**.

*Supersedes `break-the-shield-gpx4.md`. Derived from 51 research loops; see
[../research/loops/current-idea.md](../research/loops/current-idea.md) and
[../research/loops/dead-ideas.md](../research/loops/dead-ideas.md).*

---

# PART 1 — THE CENTRAL INSIGHT

## LSCs are ferroptosis-resistant, and that is exactly why this works

The naive version of this strategy — "LSCs are iron-rich, so push them into ferroptosis" — is wrong,
and the literature says so plainly.

> In CD34⁺CD38⁻ primitive-like leukemic stem cells, iron-homeostatic and anti-peroxidation networks
> including **SLC7A11–GPX4** collectively shape a **relatively ferroptosis-resistant state**. LSCs
> evade lipid-peroxidation-induced cell death by **upregulating antioxidant defense systems,
> including GPX4 and ferritin heavy chain 1 (FTH1)**. [1]

LSCs are not sitting ducks. They have already solved the ferroptosis problem.

**But look at *how* they solved it.** They did not eliminate the threat — they built armor against it,
and the armor is GPX4. That has a consequence:

**Their resistance runs through GPX4, which makes GPX4 a dependency rather than merely a marker.**

This produces the single most important design conclusion in the program:

| Approach | Outcome |
|---|---|
| Attack **upstream** — SLC7A11 inhibition, iron loading, generic oxidative stress | Their elevated GPX4 mops up the damage. **This is why upstream ferroptosis induction underperforms against LSCs.** |
| Attack **GPX4 directly** | Removes the exact protein they rely on to survive an iron load they cannot switch off |

**Hit the armor, not the sword.** Every alternative node in this pathway — SLC7A11, NCOA4, iron
loading — is upstream of the defense they have already reinforced.

## The resistance is surmountable

> **Ferroptosis-inducing nanoparticles eliminate 97% of CD34⁺/CD38⁻ LSCs** through ferroptosis-immune
> synergy. [2]

That is the LSC-enriched fraction specifically — not bulk blasts, not CD34⁺ progenitors. Baseline
resistance does not mean invulnerability.

## Why a *different* death pathway matters clinically

Ferroptosis is iron-dependent death by lipid peroxidation — the cell membrane oxidizes until it
fails. It is mechanistically distinct from apoptosis, the pathway venetoclax and most cytotoxics
engage. **Cells that have become resistant to apoptosis have not thereby become resistant to
ferroptosis.** That distinction is the entire clinical rationale for the chosen indication.

---

# PART 2 — THE BIOLOGY

## The three-arm defense

| Arm | Mechanism | Status in AML |
|---|---|---|
| **GPX4** | Uses glutathione to reduce lipid hydroperoxides before damage propagates | High expression = adverse prognosis; **highest in relapsed/refractory AML** [3] |
| **FSP1 / AIFM2** | Regenerates CoQ10 using NAD(P)H; ubiquinol traps lipid peroxyl radicals — **glutathione-independent** [4][5] | High AIFM2 independently predicts adverse prognosis [3] |
| **TXNRD1** | Thioredoxin system | Overexpressed, correlates with poor prognosis [6] |

Upstream: **SLC7A11** (system xc⁻) imports cystine for glutathione synthesis [7][8]; **NRF2** is the
master transcriptional regulator of the whole program.

## Why LSCs are on this tightrope in the first place

They are metabolically committed to a state that generates the threat:

> Persister cells preferentially depend on **oxidative phosphorylation, a major source of ROS**, and
> this dependence generates oxidative stress which **sensitizes to ferroptosis**. [9]

This is the same OxPhos dependence established earlier in this project as the basis for venetoclax
activity in AML LSCs. The metabolic choice that makes LSCs chemoresistant is the same choice that
creates their ferroptotic liability — and forces them to over-express GPX4 to survive it.

## Four independent lines converged here

Found in four separate research loops before the connection was made:

| Line | Finding | Population |
|---|---|---|
| NCOA4 / ferritinophagy | Controls iron release from ferritin stores | Quiescent CD34⁺CD38⁻ LSCs [10] |
| Imetelstat | Its actual AML mechanism is lipid ROS / ferroptosis, **not telomerase** | AML PDX [11] |
| Cysteine / SLC7A11 | Depletion impairs energy metabolism in **ROS-low LSCs but not normal HSPCs** | Quiescent LSCs [7] |
| GPX4 expression | Terminal enzyme of the glutathione arm | See Part 3 |

---

# PART 3 — THE SELECTIVITY WINDOW

Every earlier target in this project (CXCR4, CD44, CD45, CD33, CD123, LSD1, HMG20B) was shared with
normal blood cells in a way that cut against us. This one is not.

- **GPX4 is highly expressed across most AML subtypes and lower in normal hematopoietic stem cells**,
  varying by myeloid differentiation stage [3].
- **Acquired GPX4 depletion has no significant effect on hematopoietic stem cells**, indicating
  tolerability for normal hematopoiesis [3].
- **A therapeutic window has been measured, not assumed:** GPX4 inhibitors HA344 and #231 kill CD34⁺
  cells from AML patients, with **blast cells showing statistically significant increased sensitivity
  compared with non-blast cells in the same bone marrow sample** [12].
- **Indication alignment:** relapsed/refractory AML shows the highest GPX4 levels and enzyme
  activities [3] — the patients with the most target are precisely the intended population.

---

# PART 4 — EFFICACY EVIDENCE (the primary gate)

Ranked by evidentiary tier. Efficacy is the gate; toxicity is downstream engineering.

| Tier | Status | Source |
|---|---|---|
| **Eradicates leukemia-initiating capacity (serial transplant / limiting dilution)** | **NOT DEMONSTRATED.** Searched directly and genuinely absent for any ferroptosis inducer in AML. Existing limiting-dilution work is on GADD45A; existing secondary-transplant work is DOT1L. **The single most important experiment remaining.** | — |
| **True LSC fraction (CD34⁺CD38⁻) killing** | **YES.** 97% elimination by ferroptosis-inducing nanoparticles | [2] |
| **Primary patient cells, with internal selectivity** | **YES.** HA344/#231 kill AML patient CD34⁺ cells; blasts significantly more sensitive than non-blasts | [12] |
| **Dormant / persister cells** | **YES.** Persisters across tumor types are vulnerable to ferroptosis specifically **via GPX4 inhibitors**; dormant cells highly sensitive while **normal cells are largely spared** | [9][13] |
| **Venetoclax-resistant primary patient cells** | **YES.** ML210 + venetoclax synergistic in primary AML cells **including venetoclax-resistant** | [14] |
| **In vivo** | **YES.** GPX4 knockdown induces ferroptosis with mitochondrial lipid peroxidation and anti-AML effects in vitro and in vivo | [14] |
| **Target validity independent of tool compounds** | **YES.** Genetic knockdown — no compounds involved | [14] |

**Verdict: the mechanism kills LSCs.** The evidence spans genetic knockdown, multiple independent
compounds, primary patient cells, the CD34⁺CD38⁻ fraction, dormant persisters, and
venetoclax-resistant disease. **What remains unproven is durability** — whether self-renewal is
eliminated, not merely whether cells die.

---

# PART 5 — THE TOOL-COMPOUND CORRECTION

This program was nearly built on a false premise. Recording it because the error is instructive.

> **The ferroptosis-inducing compounds RSL3 and ML162 are not direct inhibitors of GPX4 but of
> TXNRD1.** [15]

| Compound | Warhead | Actual target |
|---|---|---|
| **RSL3, ML162** | Chloroacetamide | **TXNRD1** — misattributed |
| **ML210** | Nitroisoxazole / masked nitrile-oxide | **Genuinely selective for GPX4**, low proteome-wide reactivity [16] |

**Note carefully: ML1*62*, not ML2*10*.** An earlier draft of this program conflated them.

**Two consequences:**

1. **The venetoclax-resistant synergy data is more credible, not less** — it was generated with ML210
   [14], the selective compound.
2. **The gap narrows and de-risks.** Selective GPX4 chemistry exists. What does not exist is a
   compound with clinical-grade pharmacokinetics and a kidney-sparing clearance route. The design
   problem is *optimize a validated chemotype*, not *solve selectivity from scratch*.

**Selectivity is achievable and there is an established method to prove it:** counter-screens against
TXNRD1 and glutathione reductase are described as "imperative" for identifying specific GPX
inhibitors; of compounds inhibiting GPX4 in primary screens, **26% also inhibited TXNRD1 — meaning
74% did not** [17]. Selectivity traces to the nitroisoxazole warhead; replacing that group yields
less selective analogs [16].

---

# PART 6 — THE ESCAPE ROUTE

## Blocking GPX4 alone pre-installs the resistance mechanism

**FSP1 suppresses ferroptosis glutathione-independently**, regenerating CoQ10 whose reduced form traps
lipid peroxyl radicals; it acts in parallel to GPX4 and rescues cells from GPX4 deletion [4][5].

**Under therapeutic pressure, cells do not die — they switch arms:**

> **Upregulation of CoQ shifts ferroptosis dependence from GPX4 to FSP1** in acquired
> radioresistance. [18]

**Pharmacological FSP1 targeting strongly synergizes with GPX4 inhibitors** across multiple cancer
types [19].

## Independent validation of two design choices in a single title

> **"FSP1 and histone deacetylases suppress cancer persister cell ferroptosis."** [13]

That confirms, from one source, both (a) FSP1 is the persister ferroptosis defense — so FSP1 coverage
is mandatory — and (b) HDAC inhibition removes a second persister defense, justifying the HDAC
component of the regimen. Both had been reasoned to independently.

## The niche supplies the escape route — a synthesis not present in any single source

- Mitochondrial electron transport chains are a **primary source of CoQ recycling**, and
  **mitochondria-specific CoQ potently inhibits GPX4-inhibition-mediated ferroptosis in AML** [14].
- Separately, **marrow stroma transfers functional mitochondria to AML cells** via tunneling
  nanotubes, and **metabolic attack induces that transfer** [20].

**Therefore: attacking GPX4 should provoke the niche to hand LSCs fresh mitochondria, more CoQ, and a
reinforced FSP1 arm.** The resistance is not merely intrinsic — it is resupplied from outside.

**Testable prediction, currently untested. It is also the strongest argument that FSP1 coverage is not
optional.**

## Prior art status

Dual **GPX4/TXNRD1** targeting in AML has been explored [21]. Dual **GPX4/FSP1** in AML has not, and
**no FSP1 inhibitor has been tested in AML at all**.

---

# PART 7 — THE PARTNER AGENT ALREADY EXISTS

We design the GPX4 agent — the real gap — and pair it with an existing FSP1 compound rather than
inventing both.

| Compound | Mechanism | Status |
|---|---|---|
| **icFSP1** | Non-competitive; triggers FSP1 relocalization from membrane and **condensation** before ferroptosis | **Best drug-likeness.** Significantly improved microsomal stability and maximum tolerated dose over iFSP1; **impairs tumour growth in vivo**; **explicit synergy with GPX4 inhibition** [22] |
| **viFSP1** | Binds the NAD(P)H pocket; **species-independent** (mouse models viable) | EC50 170 nM [19] |
| **iFSP1** | Binds the quinone pocket; human-selective | First-generation; cannot be tested in mouse models [19] |

---

# PART 8 — THE KIDNEY PROBLEM, REFRAMED

## What the evidence actually says

> Inducible Gpx4⁻/⁻ mice die after approximately two weeks, with mean survival **13.5 days**.
> Histology shows **widespread tubular cell death, interstitial edema, and proteinaceous casts**;
> electron micrographs confirm severe destruction of renal tubule cells. [23]

Serious — but note what that experiment is: **complete, permanent, whole-body ablation of the protein
in every cell.**

## Knockout is not a drug

A drug produces partial target occupancy, reversibly, at a controlled dose, intermittently. Many
proteins are lethal as genetic knockouts and entirely viable as drug targets — the proteasome is the
canonical example, and bortezomib is approved.

**No pharmacological therapeutic window has ever been measured for GPX4**, because every compound
failed on pharmacokinetics before such a study could run [24]. **The window is unmeasured, not proven
absent.**

## Three favorable facts

1. **A window has been measured in marrow** — blasts significantly more sensitive than non-blasts
   within the same patient sample [12].
2. **Normal HSCs tolerate GPX4 depletion** [3].
3. **An antidote exists.** **Liproxstatin-1**, a spiroquinoxalinamine, suppresses ferroptosis in
   Gpx4-null mice [23] — a candidate rescue agent or protective co-therapy if renal toxicity emerges.

## Design levers

| Lever | Rationale |
|---|---|
| **Hepatobiliary, not renal, clearance** | Kidneys concentrate what they excrete; a renally-cleared drug is delivered to the tissue we must protect. Tune MW, charge, transporter-substrate profile. **Primary defense.** |
| **Reversible-covalent warhead + intermittent dosing** | Tubular epithelium regenerates; LSCs under continuous oxidative load with no defense reserve do not tolerate transient loss. **Addresses kidney and T-cell toxicity with one feature.** |
| **Liproxstatin-1 as rescue** | Established renal ferroptosis protection [23] |

## Rejected: hypoxia-activated prodrug

The intuitive move given this project's long thread on the hypoxic marrow niche. The oxygen numbers
kill it:

| Tissue | Oxygen tension |
|---|---|
| Marrow endosteal niche | **< 10 mmHg** |
| **Renal medulla** | **~10 mmHg** [25] |
| Renal cortex | ~30 mmHg [25] |

The renal medulla is as hypoxic as the marrow niche, and the GPX4-dependent vulnerability sits at the
**inner-cortex/outer-medulla interface**, straddling the boundary. No usable window. Recorded because
it is the obvious proposal.

## Rejected: iron-gated Fe(II) prodrug

Proposed making the compound inert until it met high labile ferrous iron, so the property making LSCs
vulnerable would be the trigger arming the drug. **The premise fails:** LSCs **overexpress ferritin
(FTH/FTL) relative to normal HSCs** and use ferritinophagy to *prevent* excess labile iron [1]. They
buffer iron rather than running a large loose pool. Demoted pending direct labile-iron-pool
measurement in LSCs versus proximal tubule cells.

---

# PART 9 — T-CELL TOXICITY

Effects are **subset-dependent and directionally opposite** [26]:

- GPX4 inhibition in **Tregs → augments** antitumor immunity *(helpful)*
- GPX4 inhibition in **CD8⁺ and TFH cells → impairs** antitumor immunity *(harmful)*
- T-cell stimulation itself **decreases GPX4 expression**, raising ROS and labile iron and making
  activated T cells ferroptosis-sensitive

**Specific contraindication: do not combine with CAR-T.** CAR-T cells are susceptible to
GPX4-inhibition-induced ferroptosis, which reduces their antitumor potential [26].

Our regimen is chemotherapy-based rather than immunotherapy-based, limiting exposure. Intermittent
dosing should permit recovery. **Net effect unknown; this remains the largest unresolved safety
question.**

---

# PART 10 — THE MOLECULE

**A selective, reversible-covalent GPX4 inhibitor with hepatobiliary clearance, paired with an
icFSP1-class agent.**

Design constraints, each traceable to a documented failure:

1. **Build on the nitroisoxazole / masked nitrile-oxide warhead** (the ML210 chemotype) — the group
   conferring selectivity [16]. **Do not use chloroacetamide chemistry**, which produced the
   TXNRD1-hitting compounds [15].
2. **Cell-free validation against purified GPX4.** A gating criterion, not a confirmatory
   afterthought — RSL3 and ML162 failed exactly this [15].
3. **Counter-screen against TXNRD1 and glutathione reductase** — established, described as
   imperative [17].
4. **Hepatobiliary, not renal, clearance.**
5. **Reversible-covalent warhead** for differential recovery.
6. **FSP1 coverage** via icFSP1-class partner (architecture (b), recommended) or a single dual-acting
   entity (architecture (a), harder to design, simpler to register).

**Structural resources available:** crystal structures of GPX4 in apo form and covalently bound to
ML162 [27]; the target has a shallow active site with no drug-like pocket [24], making it a covalent
problem by necessity.

**Delivery prior art to be aware of:** GCFN, a glutathione-responsive cysteine-polymer nanocarrier
that depletes intracellular GSH and inhibits GPX4 in AML [28]. The nanomedicine route to this axis is
already occupied.

---

# PART 11 — THE REGIMEN

| Component | Role | Status |
|---|---|---|
| **GPX4 inhibitor** | Remove the armor LSCs depend on | **The molecule we design** |
| **icFSP1-class agent** | Close the CoQ/FSP1 escape route | Exists; never tested in AML |
| **Venetoclax** | Apoptotic arm; synergy demonstrated in primary venetoclax-*resistant* cells [14] | Approved |
| **Azacitidine** | Backbone; independently sensitizes to ferroptosis via MAGEA6–AMPK–SLC7A11–GPX4 [29] | Approved |
| *HDAC inhibitor (optional)* | *Removes a second persister ferroptosis defense [13]; upregulates iron metabolism genes, raising labile iron and ferroptosis susceptibility [30]* | *Approved* |
| **DO NOT ADD: NCOA4 inhibitor** | **Antagonizes.** NCOA4 depletion *inhibits* ferroptosis by eliminating intracellular free iron accumulation [31] | — |

**Patient selection:** a published model integrating **TfR1, GPX4, and FTH1** predicts LSC ferroptosis
susceptibility [2]. GPX4-high / AIFM2-high status provides a second axis [3].

**Regulatory shape:** one novel agent added to an approved backbone, in a biomarker-selected
population, in an indication with clear unmet need. That is an approvable design.

---

# PART 12 — WHY AI MAKES THIS TRACTABLE NOW

Six coupled constraints optimized **simultaneously** on a structurally-solved but pocket-less target:

1. Shallow active-site binding with no conventional pocket
2. Covalent warhead reactivity tuning
3. Selectivity across a near-identical selenoprotein family
4. Clearance-route steering toward hepatobiliary elimination
5. Reversibility kinetics matched to tubular recovery
6. Optional dual-target pharmacology

Conventional medicinal chemistry attacks these serially and loses ground on each round trip — which
is why GPX4 has resisted drugging for over a decade **despite solved crystal structures**. Generative
chemistry, structure prediction, and multi-parameter property models attack all six at once.

**This is the strongest AI-tractability case in the project:** the biology is settled, the structures
exist, and the sole obstacle is a multi-parameter molecular design problem.

---

# PART 13 — WHAT MUST BE PROVEN

Ordered by decisiveness.

1. **Serial transplantation.** Does GPX4 inhibition eliminate leukemia-initiating capacity, or merely
   kill cells? Treat a PDX, then serially transplant. **The single most important experiment; nothing
   else substitutes for it.**
2. **Pharmacological therapeutic index.** Never measured. Requires a compound with adequate PK — which
   is the program's first deliverable.
3. **Niche CoQ resupply.** Does stromal mitochondrial transfer rescue LSCs from GPX4 inhibition, as
   Part 6 predicts?
4. **Labile iron pool**, LSC versus proximal tubule — decides whether iron-gating is recoverable.
5. **FSP1 inhibition in AML.** Never tested. Confirm the GPX4/FSP1 synergy holds in AML specifically.
6. **Is TXNRD1 the better target?** RSL3/ML162 killed AML cells *through* TXNRD1 [15]; auranofin is
   approved and active in AML [6]. Counter: TXNRD1 inhibitors expand regulatory T cells, a
   paradoxical immunosuppressive effect.

**Known resistance mechanism to screen for:** **GADD45A loss** increases LSC self-renewal *and*
ferroptosis resistance, reduces ROS, decreases response to ferroptosis inducers, and yields an
increasingly aggressive phenotype on serial transplantation [32].

**Residual caution:** quiescent cells possess ferroptosis-protective membrane lipid domains [33].

---

# PART 14 — THE FORK

**Iron starvation and ferroptosis induction are opposite strategies and cannot be combined.**

- **NCOA4 inhibition** (compound 9a exists) kills by *starving* cells of iron [10].
- **GPX4/FSP1 inhibition** kills by *exploiting* iron.

A contradictory source claimed NCOA4 inhibition causes iron overload and sensitizes to ferroptosis.
Checked: the consensus mechanism is the opposite — **NCOA4 depletion inhibits ferroptosis by
eliminating accumulation of intracellular free iron** [31]. The fork stands.

**The flip side is a genuine unexploited idea:** if NCOA4 *activity* promotes ferroptosis, an **NCOA4
agonist** — forcing ferritinophagy to dump stored iron — would synergize with GPX4 inhibition. No
such agonist exists. **The HDAC inhibitor is the practical proxy**, raising labile iron with an
approved drug [30].

NCOA4 inhibition remains the more conservative alternative — better validated in quiescent LSCs, with
a compound in hand — but it forecloses this program rather than complementing it.

---

# REFERENCES

1. [Regulating Ferroptosis in Leukemic Stem Cells: From Stemness Preservation to Targeted Differentiation Strategies — *Stem Cell Reviews and Reports* (2025)](https://link.springer.com/article/10.1007/s12015-025-11016-1)
2. [Ferroptosis in AML: nanoparticles, biomarkers, and immune rewiring for therapeutic breakthroughs — *Discover Oncology* (2025)](https://link.springer.com/article/10.1007/s12672-025-03777-5)
3. [The ferroptosis landscape in acute myeloid leukemia — *Aging*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10713399/)
4. [FSP1 is a glutathione-independent ferroptosis suppressor — *Nature* (2019)](https://www.nature.com/articles/s41586-019-1707-0)
5. [The CoQ oxidoreductase FSP1 acts parallel to GPX4 to inhibit ferroptosis — *Nature* (2019)](https://www.nature.com/articles/s41586-019-1705-2)
6. [Thioredoxin reductase is a major regulator of metabolism in leukemia cells](https://www.researchgate.net/publication/353077930_Thioredoxin_reductase_is_a_major_regulator_of_metabolism_in_leukemia_cells)
7. [Cysteine depletion targets leukemia stem cells through inhibition of electron transport complex II — *Blood* (2019)](https://ashpublications.org/blood/article/134/4/389/260692/Cysteine-depletion-targets-leukemia-stem-cells)
8. [Cystine uptake inhibition potentiates front-line therapies in acute myeloid leukemia](https://pubmed.ncbi.nlm.nih.gov/35474100/)
9. [Targeting dormant cancer cells: ferroptosis as a precision therapeutic strategy — *Cellular & Molecular Biology Letters*](https://link.springer.com/article/10.1186/s11658-026-00895-y)
10. [Ferritinophagy is a druggable vulnerability of quiescent leukemic stem cells](https://www.biorxiv.org/content/10.1101/2023.12.18.572101.full.pdf)
11. [Telomerase inhibitor imetelstat kills AML cells via lipid ROS and ferroptosis — *Nature Cancer*](https://www.nature.com/articles/s43018-020-00126-z)
12. [Dual targeting of GPX4 and TXNRD1 triggers eradication of AML cells through induction of apoptosis and ferroptosis (HA344, #231)](https://www.biorxiv.org/content/10.1101/2024.04.03.584800.full.pdf)
13. [FSP1 and histone deacetylases suppress cancer persister cell ferroptosis — *Science Advances* (2025)](https://www.science.org/doi/10.1126/sciadv.aea8771)
14. [Mitochondrial regulation of GPX4 inhibition–mediated ferroptosis in acute myeloid leukemia — *Leukemia*](https://www.nature.com/articles/s41375-023-02117-2)
15. [The ferroptosis inducing compounds RSL3 and ML162 are not direct inhibitors of GPX4 but of TXNRD1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10149367/)
16. [Selective covalent targeting of GPX4 using masked nitrile-oxide electrophiles](https://pubmed.ncbi.nlm.nih.gov/32231343/)
17. [Development of an assay pipeline for the discovery of novel small molecule inhibitors of human glutathione peroxidases GPX1 and GPX4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10220285/)
18. [Upregulation of CoQ shifts ferroptosis dependence from GPX4 to FSP1 in acquired radioresistance](https://www.sciencedirect.com/science/article/pii/S1368764623001152)
19. [Inhibition of FSP1: A new strategy for the treatment of tumors (Review)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11228423/)
20. [Bone marrow niche-mediated survival of leukemia stem cells in AML](https://pmc.ncbi.nlm.nih.gov/articles/PMC4944541/)
21. [Dual targeting of GPX4 and TXNRD1 in AML — preprint (2024)](https://www.biorxiv.org/content/10.1101/2024.04.03.584800.full.pdf)
22. [Phase separation of FSP1 promotes ferroptosis (icFSP1) — *Nature* (2023)](https://www.nature.com/articles/s41586-023-06255-6)
23. [Inactivation of the ferroptosis regulator Gpx4 triggers acute renal failure in mice — *Nature Cell Biology* (2014)](https://www.nature.com/articles/ncb3064)
24. [Targeting GPX4 in ferroptosis and cancer: chemical strategies and challenges](https://www.sciencedirect.com/science/article/abs/pii/S0165614724000981)
25. [What Makes the Kidney Susceptible to Hypoxia? — *The Anatomical Record*](https://anatomypubs.onlinelibrary.wiley.com/doi/10.1002/ar.24260)
26. [GPX4 is a key ferroptosis regulator orchestrating T cells and CAR-T-cells sensitivity to ferroptosis](https://pmc.ncbi.nlm.nih.gov/articles/PMC12321709/)
27. [Crystal structures of the selenoprotein glutathione peroxidase 4 in apo form and in complex with covalently bound ML162](https://pubmed.ncbi.nlm.nih.gov/33559612/)
28. [A Ferroptosis-Inducing and Leukemic Cell-Targeting Drug Nanocarrier Formed by Redox-Responsive Cysteine Polymer for AML Therapy — *ACS Nano*](https://pubs.acs.org/doi/10.1021/acsnano.2c06313)
29. [Low-dose hypomethylating agents cooperate with ferroptosis inducers via the MAGEA6-AMPK-SLC7A11-GPX4 pathway in AML — *Experimental Hematology & Oncology*](https://link.springer.com/article/10.1186/s40164-024-00489-4)
30. [HDAC inhibitor enhances ferroptosis susceptibility of AML cells by stimulating iron metabolism](https://pubmed.ncbi.nlm.nih.gov/39756501/)
31. [The Role of NCOA4-Mediated Ferritinophagy in Ferroptosis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6316710/)
32. [Loss of the stress sensor GADD45A promotes stem cell activity and ferroptosis resistance in LGR4/HOXA9-dependent AML — *Blood* (2024)](https://ashpublications.org/blood/article/144/1/84/515642/Loss-of-the-stress-sensor-GADD45A-promotes-stem)
33. [Ferroptosis-protective membrane domains in quiescence — *Cell Reports*](https://www.cell.com/cell-reports/fulltext/S2211-1247(23)01573-5)
