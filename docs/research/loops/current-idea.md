# Current Idea — Live State

**Read this plus [dead-ideas.md](dead-ideas.md) to reload full context. Nothing else needed.**

Loop count: **40**. Full detail: [../../strategies/break-the-shield-gpx4.md](../../strategies/break-the-shield-gpx4.md)

---

## THE IDEA

**A selective covalent GPX4 inhibitor with FSP1 coverage, cleared hepatobiliarily, developed for
venetoclax-resistant AML.**

Force LSCs to die by ferroptosis — iron reacting with membrane fats until the membrane rusts apart.
This is a *different death pathway* from apoptosis, which is what venetoclax and most cancer drugs
trigger. That distinction is the entire clinical rationale.

## WHY IT WORKS (established)

| Claim | Evidence |
|---|---|
| Target is real | **GPX4 knockdown** (genetic, no compounds) induces ferroptosis in AML, anti-leukemic in vitro and in vivo |
| Selectivity window exists | GPX4 **high in most AML subtypes, lower in normal HSCs**; normal HSCs **tolerate GPX4 depletion** |
| Right patients | High GPX4 **and** high AIFM2/FSP1 both independently predict **adverse prognosis** in AML |
| Clinical rationale | ML210 + venetoclax **synergistic in primary AML patient cells including venetoclax-resistant ones** |
| Backbone sensitizes | Azacitidine independently sensitizes to ferroptosis (MAGEA6–AMPK–SLC7A11–GPX4) |
| Gap is real | GPX4 has a **shallow site with no drug-like pocket**; no validated selective inhibitor exists; crystal structures ARE solved |

## THE ESCAPE ROUTE (why FSP1 coverage is mandatory)

FSP1 suppresses ferroptosis **glutathione-independently** via CoQ10 regeneration, in parallel to GPX4.
Under pressure, **cells shift dependence from GPX4 to FSP1 by upregulating CoQ.** Block GPX4 alone
and you have built in the resistance mechanism.

**Our synthesis (not in any single source):** mitochondrial ETC is the primary CoQ recycling source,
*and* marrow stroma transfers mitochondria to AML via tunneling nanotubes — a transfer that metabolic
attack **induces**. So attacking GPX4 should provoke the niche to resupply the escape route.
Testable prediction.

Dual GPX4/TXNRD1 has been explored (2024 preprint). **Dual GPX4/FSP1 in AML has not.**

## THE MOLECULE — design spec

Architecture (b) recommended: best-in-class GPX4 inhibitor **co-developed with** an FSP1 inhibitor.
Architecture (a), a single dual-acting entity, is harder to design but simpler to register.

1. **Must inhibit purified GPX4 cell-free** — RSL3/ML210 fail this. Gating criterion.
2. **Selective vs TXNRD1** and selenoprotein machinery — the off-target that invalidated the tools.
3. **Hepatobiliary, not renal, clearance** — kidneys concentrate what they excrete.
4. **Reversible-covalent warhead** — differential recovery between doses.
5. **Tuned reactivity** — masked nitrile-oxide electrophiles are the reported starting point.
6. **FSP1 coverage** — dual pharmacology or partner agent.

## THE REGIMEN

Novel GPX4(+FSP1) agent **+ venetoclax + azacitidine**. Optional: HDAC inhibitor (raises labile iron,
enhances ferroptosis susceptibility; approved). One novel agent on an approved backbone in a
biomarker-selected population = approvable design.

**Patient selection:** published model integrating **TfR1, GPX4, FTH1** predicts LSC ferroptosis
susceptibility; GPX4-high/AIFM2-high adds a second axis.

## WHY AI UNLOCKS IT

Six coupled constraints optimized **simultaneously** on a structurally-solved but pocket-less target:
shallow-site binding, covalent reactivity tuning, selenoprotein-family selectivity, clearance-route
steering, reversibility kinetics, dual-target pharmacology. Human med-chem attacks these serially and
loses ground each round trip — which is why GPX4 resisted drugging for a decade despite solved
structures.

---

# STILL NEEDS VERIFICATION

Ordered by how badly a bad answer would hurt.

## 1. T-cell toxicity — **BIGGEST UNADDRESSED HOLE**
GPX4 is essential in T cells. Immunosuppression is a plausible dose-limiting toxicity and **no
proposed solution addresses it.** Unresolved. Next thing to research.

## 2. Kidney sparing is hypothesis, not result
Inducible GPX4 knockout causes acute renal failure via proximal tubule ferroptosis. Solutions
(hepatobiliary clearance, reversible-covalent + intermittent dosing) are design proposals with no
supporting data yet. **Run:** labile iron pool in LSCs vs proximal tubule cells.

## 3. Does the niche actually resupply CoQ?
The tunneling-nanotube → mitochondrial CoQ → FSP1 rescue chain is our inference. Untested.

## 4. Is TXNRD1 the better target?
The compounds that hit it *did* kill AML. Overexpressed, poor prognosis, approved drug (auranofin)
available. Counter: expands regulatory T cells, paradoxical immunosuppression.

## 5. FSP1 inhibitor status
iFSP1 exists as a tool. Need: is there a drug-like FSP1 inhibitor, and is dual pharmacology feasible?

## 6. Achievable selectivity vs the selenoprotein family
Assumed, not demonstrated. The whole design rests on beating the off-target that killed RSL3/ML210.

## 7. Does GPX4 inhibition reach *quiescent* LSCs?
NCOA4 has this evidence explicitly. GPX4 does not. Our target population is the dormant persister.

---

# FALLBACKS IF THIS DIES

1. **NMNAT1** — nuclear NAD+; LSC-specific, dispensable for normal hematopoiesis, gatekeeper property.
2. **SIN3A PAH2–SID** — genuine AML gap, direct Malone lineage, cheapest experiment.
3. **NCOA4** — best quiescent-LSC validation, but compound exists and antagonizes the GPX4 route.
