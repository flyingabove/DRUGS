# Current Idea — Live State

**Read this plus [dead-ideas.md](dead-ideas.md) to reload full context. Nothing else needed.**

Loop count: **51**. Full detail: [../../strategies/lsc-ferroptosis-hypothesis.md](../../strategies/lsc-ferroptosis-hypothesis.md)

---

## THE IDEA

**A drug-like, kidney-sparing GPX4 inhibitor, paired with an FSP1 inhibitor, for venetoclax-resistant
AML.**

Force LSCs to die by ferroptosis — iron reacting with membrane fats until the membrane rusts apart.
This is a *different death pathway* from apoptosis, which is what venetoclax and most cancer drugs
trigger. That distinction is the entire clinical rationale.

## CORRECTION LOGGED (loop 44)

Earlier drafts said *"RSL3 and ML210 fail to inhibit purified GPX4."* **Wrong compound.** The paper
is *"The ferroptosis inducing compounds RSL3 and **ML162** are not direct inhibitors of GPX4 but of
TXNRD1."*

- **RSL3, ML162** — chloroacetamide warheads → actually hit **TXNRD1**. Misattributed.
- **ML210** — nitroisoxazole / masked nitrile-oxide warhead → **genuinely selective for GPX4**, low
  proteome-wide reactivity. Selectivity traced to the nitroisoxazole group; replacing it gives less
  selective analogs.

**Two consequences, both important:**
1. **The venetoclax-resistant synergy data is more credible, not less** — it was generated with
   ML210, the selective compound.
2. **The gap narrows and de-risks.** Selective GPX4 chemistry *does* exist. What does not exist is a
   compound with clinical-grade **pharmacokinetics and a kidney-sparing clearance route.** The design
   problem is now *optimize a validated chemotype*, not *solve selectivity from scratch* — lower risk,
   slightly less novel.

## WHY IT WORKS (established)

| Claim | Evidence |
|---|---|
| Target is real | **GPX4 knockdown** (genetic, no compounds) induces ferroptosis in AML; anti-leukemic in vitro and in vivo |
| Selectivity window | GPX4 **high in most AML subtypes, lower in normal HSCs**; normal HSCs **tolerate GPX4 depletion** |
| Right patients | High GPX4 **and** high AIFM2/FSP1 each independently predict **adverse prognosis** in AML |
| Clinical rationale | **ML210 + venetoclax synergistic in primary AML patient cells including venetoclax-resistant ones** |
| **Hits our actual target population** | **"Persister cells from multiple tumor types and treatments are vulnerable to ferroptosis, which can be induced with inhibitors of GPX4."** Dormant cancer cells are highly ferroptosis-sensitive **while normal cells are largely spared** |
| Mechanistic throughline | Persisters preferentially depend on **OxPhos** → generates ROS → sensitizes to ferroptosis. The same OxPhos dependence this project established for AML LSCs early on |
| Backbone sensitizes | Azacitidine independently sensitizes to ferroptosis (MAGEA6–AMPK–SLC7A11–GPX4) |
| Selective chemistry is achievable | Counter-screens vs GR and TXNRD1 are established practice; 74% of GPX4 hits were **not** dual-inhibitors |

## THE ESCAPE ROUTE — why FSP1 coverage is mandatory

FSP1 suppresses ferroptosis **glutathione-independently** via CoQ10 regeneration, parallel to GPX4.
Under pressure **cells shift dependence from GPX4 to FSP1 by upregulating CoQ.** Block GPX4 alone and
the resistance mechanism is pre-installed.

**Independent validation of two of our design choices in one paper title:** *"FSP1 and histone
deacetylases suppress cancer persister cell ferroptosis"* (Science Advances, 2025). That confirms
(a) FSP1 is the persister ferroptosis defense, and (b) HDAC inhibition removes a second persister
defense — both of which we had reasoned to separately.

**Our synthesis (not in any single source):** mitochondrial ETC is the primary CoQ recycling source,
*and* marrow stroma transfers mitochondria to AML via tunneling nanotubes — a transfer that metabolic
attack **induces**. So attacking GPX4 should provoke the niche to resupply the escape route.
Testable, untested.

Dual GPX4/TXNRD1 in AML has been explored (2024 preprint). **Dual GPX4/FSP1 in AML has not.**

## THE PARTNER AGENT EXISTS

FSP1 inhibitors, in order of drug-likeness:
- **icFSP1** — best. Non-competitive; triggers FSP1 relocalization and condensation. **Significantly
  improved microsomal stability and maximum tolerated dose** over iFSP1; **impairs tumour growth
  in vivo**; **explicit synergy with GPX4 inhibition**.
- **viFSP1** — species-independent (so mouse models work), EC50 170 nM, binds the NAD(P)H pocket.
- **iFSP1** — first-generation, human-selective, cannot be tested in mouse models.

**No FSP1 inhibitor has been tested in AML.** So we design the GPX4 agent (the real gap) and pair it
with an existing FSP1 tool compound rather than inventing both.

## THE MOLECULE — design spec

1. **Build on the nitroisoxazole / masked nitrile-oxide warhead** (the ML210 chemotype) — the group
   that confers selectivity. Do not use chloroacetamide chemistry.
2. **Counter-screen against TXNRD1 and glutathione reductase** — established, "imperative" practice.
3. **Cell-free validation against purified GPX4** — gating criterion.
4. **Hepatobiliary, not renal, clearance** — kidneys concentrate what they excrete. *Primary kidney
   defense.*
5. **Reversible-covalent warhead + intermittent dosing** — differential recovery. *Addresses kidney
   AND T-cell toxicity with one design feature.*
6. **FSP1 coverage** — via icFSP1-class partner agent.

## THE REGIMEN

Novel GPX4 agent **+ icFSP1-class partner + venetoclax + azacitidine**. Optional HDAC inhibitor
(removes a second persister ferroptosis defense; approved).

**Patient selection:** published model integrating **TfR1, GPX4, FTH1** predicts LSC ferroptosis
susceptibility; GPX4-high/AIFM2-high adds a second axis.

## WHY AI UNLOCKS IT

Coupled constraints optimized **simultaneously** on a structurally-solved but pocket-less target:
shallow-site binding, covalent reactivity tuning, selenoprotein-family selectivity, clearance-route
steering, reversibility kinetics. Human med-chem attacks these serially and loses ground each round
trip — which is why GPX4 has resisted drugging for a decade despite solved crystal structures.

---

# HOLES — STATUS

## ~~1. Does it reach quiescent/dormant LSCs?~~ **CLOSED, FAVORABLY (loop 43)**
Persister cells across tumor types are vulnerable to ferroptosis specifically via GPX4 inhibition.
Dormant cells are highly sensitive; normal cells largely spared. Mechanism: persister OxPhos
dependence generates the ROS that sensitizes them.
*Residual caution:* quiescent cells have some ferroptosis-protective membrane lipid domains.

## ~~2. Selenoprotein selectivity achievable?~~ **CLOSED (loop 44)**
ML210's nitroisoxazole warhead achieves it. Counter-screen methodology (GR + TXNRD1) is established.
74% of GPX4 hits were not dual inhibitors.

## 3. T-cell toxicity — **CHARACTERIZED, NOT ELIMINATED (loop 41)**
Effects are **subset-dependent and opposite**:
- GPX4 inhibition in **Tregs → augments** antitumor immunity (helpful)
- GPX4 inhibition in **CD8+ and TFH → impairs** antitumor immunity (harmful)
- Activated T cells downregulate GPX4 and become ferroptosis-sensitive

**Specific contraindication: do not combine with CAR-T** — CAR-T cells are susceptible to
GPX4-inhibition ferroptosis, reducing their antitumor potential. Our regimen is chemo-based, not
immunotherapy-based, which limits exposure. Intermittent dosing should allow recovery.
*Net effect unknown. Still the largest unresolved safety question.*

## 4. Kidney sparing — **REFRAMED, LESS ALARMING THAN ASSUMED (loop 50)**

**All the kidney evidence is genetic knockout.** Induced Gpx4-/- mice die in ~13.5 days with
widespread tubular death, interstitial edema, and proteinaceous casts. But that is **complete,
permanent, whole-body ablation in every cell** — not what a drug does. A drug gives partial
occupancy, reversibly, dose-controlled, intermittently. Many targets are lethal as knockouts and
fine as drugs (proteasome / bortezomib being the obvious case).

**No pharmacological therapeutic window has ever been measured**, because every GPX4 compound failed
on PK before the study could be run. The window is **unmeasured, not proven absent.**

Three favorable points:
1. A window HAS been measured in marrow — **blasts significantly more sensitive than non-blasts in
   the same patient sample** (HA344/#231).
2. GPX4 is higher in AML than normal HSCs; normal HSCs tolerate depletion.
3. **An antidote exists** — **liproxstatin-1** suppresses ferroptosis in Gpx4-null mice. Potential
   rescue agent or protective co-therapy if renal toxicity emerges.

Levers unchanged: hepatobiliary clearance, reversible-covalent warhead, intermittent dosing.

## 5. Does the niche resupply CoQ? — **UNTESTED**
Tunneling-nanotube → mitochondrial CoQ → FSP1 rescue is our inference.

## 6. Is TXNRD1 the better target? — **OPEN**
Overexpressed in AML, poor prognosis, approved drug (auranofin) works in AML. And RSL3/ML162 killed
AML cells *through* TXNRD1. Counter: TXNRD1 inhibitors expand Tregs (paradoxical immunosuppression).

---

# LOOP 51 — THE CD34+CD38- QUESTION, ANSWERED (and it sharpens the design)

**The complication:** in CD34+CD38- primitive LSCs, the iron-homeostatic and anti-peroxidation
networks — **SLC7A11-GPX4 together with FTH1** — "collectively shape a relatively
**ferroptosis-RESISTANT** state." LSCs evade lipid-peroxidation death by **upregulating GPX4 and
ferritin.**

So the actual LSC fraction is ferroptosis-*resistant* at baseline, not sensitive. That looked like it
might sink the idea.

**It does the opposite, and this is the key strategic insight of the run:**

**LSC resistance runs *through* GPX4 upregulation. That makes GPX4 their dependency, not merely a
marker.** High expression = high reliance.

- Attack **upstream** (SLC7A11 inhibition, iron loading, generic oxidative stress) → their elevated
  GPX4 mops up the damage. **This is why upstream ferroptosis induction underperforms against LSCs.**
- Attack **GPX4 directly** → you remove the exact thing they are relying on to survive their own iron
  load.

**Design conclusion: hit GPX4 itself. Do not rely on upstream ferroptosis inducers.** This validates
the target choice over the alternatives considered.

**And the resistance is surmountable — direct evidence at the exact precision tier previously flagged
as missing:**

> **Ferroptosis-inducing nanoparticles eliminate 97% of CD34+/CD38- LSCs** through
> ferroptosis-immune synergy.

**Indication alignment:** "AML cells, **especially relapsed and refractory AML**, present high GPX4
levels and enzyme activities." The patients with the most GPX4 are exactly the population this drug
targets.

**Backbone confirmed again:** low-dose decitabine + RSL3 synergistically drive ferroptosis by
inhibiting the AMPK-SLC7A11-GPX4 axis — independent support for the hypomethylating-agent component.

---

# EFFICACY EVIDENCE (the primary gate)

Ranked by the hierarchy in the skill: serial transplant > primary patient LSC > PDX > cell line.

| Tier | Status |
|---|---|
| **Eradicates leukemia-initiating capacity (serial transplant)** | **NOT DEMONSTRATED — searched directly, loop 49, genuinely absent.** No ferroptosis inducer has been shown to eliminate LIC by serial transplant or limiting-dilution assay in AML. Existing limiting-dilution work is on GADD45A (a resistance gene); existing secondary-transplant work is DOT1L. **This is the single most important experiment to run.** |
| **Primary patient LSC killing ex vivo** | **YES — gap closed loop 51.** Ferroptosis-inducing nanoparticles **eliminate 97% of CD34+/CD38- LSCs**. Separately, GPX4 inhibitors HA344/#231 kill AML patient CD34+ cells with **blasts significantly more sensitive than non-blasts** in the same marrow. |
| **Persister/dormant cell killing** | **YES.** Persisters across tumor types are vulnerable to ferroptosis specifically via GPX4 inhibition; dormant cells highly sensitive, normal cells largely spared |
| **Venetoclax-resistant primary cells** | **YES.** ML210 + venetoclax synergistic in primary AML patient cells including venetoclax-resistant |
| **In vivo / PDX** | **YES.** GPX4 knockdown anti-leukemic in vivo |

**Verdict on the primary gate: the mechanism kills LSCs.** Evidence spans genetic knockdown, multiple
independent compounds, primary patient CD34+ cells, dormant persisters, and venetoclax-resistant
disease. The one missing tier is serial transplantation.

---

# NCOA4 FORK — CONTRADICTION FOUND AND RESOLVED (loops 46–47)

One source claimed *"inhibition of NCOA4 leads to iron overload and increased susceptibility to
ferroptosis in LSCs"* — which would have meant NCOA4 inhibition **synergizes** with our GPX4 approach
rather than antagonizing it, turning the fork into a combination.

**Checked. That source was loosely worded. The consensus mechanism is the opposite:**

> NCOA4 depletion **inhibits ferroptosis** by eliminating the accumulation of intracellular free iron.

NCOA4-mediated ferritinophagy *releases* iron from ferritin and thereby **promotes** ferroptosis.
Blocking NCOA4 traps iron in ferritin → less labile iron → **less** ferroptosis.

**The fork stands. Do not combine an NCOA4 inhibitor with a GPX4 inhibitor.**

**But the flip side is a real design idea:** if NCOA4 *activity* promotes ferroptosis, then an **NCOA4
agonist** — forcing ferritinophagy to dump stored iron — would **synergize** with GPX4 inhibition.
NCOA4 agonists do not appear to exist (agonists are harder than inhibitors).

**Practical proxy: the HDAC inhibitor.** It upregulates iron metabolism genes and raises the labile
iron pool, achieving "raise the iron" with an approved drug and no new agonist required. This
reinforces the HDAC component of the regimen.

**Mechanistically consistent regimen:**
- Raise labile iron → HDAC inhibitor *(approved)*
- Remove defense arm 1 → GPX4 inhibitor *(the molecule we design)*
- Remove defense arm 2 → FSP1 inhibitor, icFSP1 class *(exists)*
- Apoptotic backbone → venetoclax + azacitidine *(approved; azacitidine also sensitizes to ferroptosis)*
- **Do NOT add** an NCOA4 inhibitor — antagonizes

---

# DELIVERY PRIOR ART

**GCFN** — a glutathione-responsive cysteine-polymer nanocarrier that depletes intracellular GSH
*and* inhibits GPX4, causing lipid peroxidation in AML cells. Relevant as prior art on delivery:
someone has already attacked this axis with a nanomedicine rather than a small molecule. Worth
knowing before claiming the delivery approach is open.

# NEW RESISTANCE MECHANISM LOGGED

**GADD45A loss** increases LSC self-renewal *and* ferroptosis resistance, reduces ROS, decreases
response to ferroptosis inducers, and produces an increasingly aggressive phenotype on serial
transplantation. A stemness/ferroptosis-resistance axis to screen for.

---

# FALLBACKS

1. **NMNAT1** — nuclear NAD+; LSC-specific, dispensable for normal hematopoiesis, gatekeeper property.
2. **SIN3A PAH2–SID** — genuine AML gap, direct Malone lineage, cheapest experiment.
3. **NCOA4** — best quiescent-LSC validation; antagonizes the GPX4 route, cannot combine.
