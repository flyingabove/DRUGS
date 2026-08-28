# Current Idea — Live State

**Read this plus [dead-ideas.md](dead-ideas.md) to reload full context. Nothing else needed.**

Loop count: **44**. Full detail: [../../strategies/break-the-shield-gpx4.md](../../strategies/break-the-shield-gpx4.md)

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

## 4. Kidney sparing — **DESIGN HYPOTHESIS, NO DATA**
Inducible GPX4 knockout causes acute renal failure via proximal tubule ferroptosis. Hepatobiliary
clearance and reversible-covalent dosing are proposals, unvalidated.

## 5. Does the niche resupply CoQ? — **UNTESTED**
Tunneling-nanotube → mitochondrial CoQ → FSP1 rescue is our inference.

## 6. Is TXNRD1 the better target? — **OPEN**
Overexpressed in AML, poor prognosis, approved drug (auranofin) works in AML. And RSL3/ML162 killed
AML cells *through* TXNRD1. Counter: TXNRD1 inhibitors expand Tregs (paradoxical immunosuppression).

---

# FALLBACKS

1. **NMNAT1** — nuclear NAD+; LSC-specific, dispensable for normal hematopoiesis, gatekeeper property.
2. **SIN3A PAH2–SID** — genuine AML gap, direct Malone lineage, cheapest experiment.
3. **NCOA4** — best quiescent-LSC validation; antagonizes the GPX4 route, cannot combine.
