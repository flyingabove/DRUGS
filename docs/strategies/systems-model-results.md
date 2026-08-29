# Tier 5 Results — Systems Modelling Overturns the Combination Strategy

**Status: complete. Three findings, one of which contradicts §6 of the main strategy doc.**

These are ODE/regime models, not predictions. Parameters are stated and scanned; the output is which
*qualitative regime* wins, not a number of cells or months to trust literally. The structural
conclusions survive across the whole parameter range tested, which is what makes them usable.

---

## 1. The first run failed, and the failure was the finding

Every dosing schedule — continuous, and pulsed at 7/14/28-day cycles, all dose-matched — left LSC
counts **higher** than baseline at 2 years, 100% dominated by the resistant clone.

The cause is a single inequality:

```
LSC net growth rate        r  = 0.0231 /day   (30-day doubling)
kill rate, resistant clone kG = 0.0030 /day
                                kG < r  ->  the clone outgrows the drug
```

**No schedule, no fractionation, and no dose increase can fix that** — it is a property of the
resistant cell, not of the dosing.

**This did not mean the drug was bad. It meant the endpoint was wrong.** Real maintenance therapy does
not produce indefinite control either: QUAZAR AML-001 (oral azacitidine) delivered median OS 24.7 vs
14.8 months — **a ~10-month delay, not a cure — and was FDA approved in 2020.** Re-run against
time-to-relapse, the correct endpoint:

| Schedule (dose-matched) | Time to relapse | Delay vs control |
|---|---|---|
| No drug | 3.1 mo | — |
| **Continuous low** | **25.4 mo** | **+22.3 mo** |
| Pulse 7 d (2 on/5 off) | 23.5 mo | +20.3 mo |
| Pulse 28 d (5 on/23 off) | 23.2 mo | +20.0 mo |
| Continuous, 2× dose | 26.5 mo | +23.4 mo |
| Continuous, 4× dose | 27.4 mo | +24.3 mo |

**Continuous gentle dosing beats every pulsed schedule.** The maintenance framing is vindicated on its
own terms, not just on tolerability grounds.

---

## 2. Potency barely matters. This is the uncomfortable one.

Sensitivity scan, spread in time-to-relapse across each parameter's plausible range:

| Parameter | Spread (months) | Interpretation |
|---|---|---|
| **kG — residual kill on the resistant clone** | **172.9** | **dominates everything** |
| r — LSC growth rate | 76.9 | biology, not druggable by us |
| μ — resistance emergence rate | 7.0 | modest |
| **kS — potency against sensitive cells** | **3.2** | **nearly irrelevant** |
| β — adaptive reversion | 0.5 | negligible |
| α — adaptive induction | 0.3 | negligible |

**A 10× improvement in potency buys 3.2 months.** Every medicinal-chemistry cycle we ran was optimising
kS — the parameter that matters least. That does not make the chemistry wasted (the molecule still has
to work at all), but **potency optimisation past "good enough" has almost no strategic value here.**

Dose escalation agrees: 4× the dose buys +1.9 months over 1×. **There is no reason to push toxicity.**

---

## 3. The phase transition — the one number the program lives on

| kG /day | kG / r | Time to relapse |
|---|---|---|
| 0.000 | 0.00 | 23.7 mo |
| 0.010 | 0.43 | 30.7 mo |
| 0.020 | 0.87 | 45.0 mo |
| **0.0231** | **1.00** | **69.0 mo** |
| 0.025 | 1.08 | **>390 mo** |
| 0.050 | 2.16 | **>390 mo** |

**Sharp threshold at kG/r = 1.** Below it, relapse is arithmetically inevitable. Above it, the disease
is controlled past any clinical horizon.

*(">390 months" means control beyond the simulated horizon, not mathematical eradication.)*

**The entire program reduces to one question: does anything in the regimen still kill the escaping
clone faster than it divides?**

---

## 4. The FSP1 combination does nothing. §6 was wrong.

| Regimen | Time to relapse |
|---|---|
| GPX4i alone | 25.4 mo |
| **+ FSP1i (second ferroptosis arm)** | **25.3 mo — no benefit** |
| + azacitidine (lowers emergence rate) | 28.9 mo |
| + orthogonal-mechanism partner, weak (0.005/day) | 33.8 mo |
| **+ orthogonal-mechanism partner, modest (0.015/day)** | **>390 mo — control** |

**Why FSP1 inhibition fails:** the escaping clone is *ferroptosis-incompetent* — the plausible genetic
routes (ACSL4 loss, LPCAT3 loss, MUFA lipid remodelling) make the cell unable to execute ferroptosis at
all. **Once that happens, every ferroptosis defence arm is irrelevant to it.** Closing a second arm
closes a door the cell already stopped using.

**This directly contradicts the §6 recommendation to pair GPX4-M3 with an FSP1 inhibitor, and that
recommendation is withdrawn.** It was reasoning about redundancy in the *pathway* when the relevant
redundancy is in the *death mechanism*.

### The corrected combination strategy

**The partner drug must kill through a mechanism that does not require ferroptosis.** And it does not
need to be strong — a *weak* orthogonal agent clears the kG/r threshold, because it only has to
out-pace a 30-day doubling time.

That is a far easier medicinal-chemistry brief than "find a potent second ferroptosis inhibitor," and
it points at agents that already exist: venetoclax (apoptosis), azacitidine (already additive here),
or a differentiation agent that removes self-renewal rather than killing.

---

## 5. Deeper initial remission is worth more than a better drug

| LSC burden at start of maintenance | Time to relapse |
|---|---|
| 10⁶ | 0.0 mo |
| 10⁵ | 25.4 mo |
| 10⁴ | 28.9 mo |
| 10³ | 32.4 mo |
| 10² | 35.9 mo |

Three logs of deeper cytoreduction buys +10.5 months — **more than a 10× potency gain (+3.2 mo).**
Argues for deploying this in *deepest remission*, not in relapsed/refractory disease.

---

## 6. What this changes

| Before | After |
|---|---|
| Pair with an FSP1 inhibitor | **Pair with an orthogonal death mechanism; FSP1i withdrawn** |
| Optimise potency | **Potency is nearly irrelevant past adequacy; optimise retained activity on resistant cells** |
| Pulsed dosing to allow resistance reversion | **Continuous gentle dosing wins** |
| Push dose for efficacy | **4× dose buys 1.9 months — do not push toxicity** |
| Target measurable residual disease broadly | **Deploy in deepest remission** |

**New experiment required, added to the plan:** measure whether GPX4-M3 retains *any* activity against
ferroptosis-incompetent cells (ACSL4-knockout lines). **That single number — kG — matters more than the
IC₅₀ we have been chasing.**

---

# Tier 5.1 — Covalent PK/PD: the dosing question answered

For an **irreversible** inhibitor the duration of effect is set by **target resynthesis**, not by drug
half-life. The drug can clear completely while GPX4 stays inactivated until the cell rebuilds it.
Modelled with GPX4 protein half-life ≈ 24 h.

## How long does the drug need to last?

| Drug t½ | Mean occupancy | Trough | Verdict |
|---|---|---|---|
| 0.5 h | 34.4% | 24.4% | inadequate |
| 1 h | 49.9% | 36.1% | oscillating |
| 2 h | 65.3% | 48.9% | oscillating |
| **4 h** | **78.4%** | **64.2%** | **sustained** |
| 8 h | 88.2% | 80.7% | sustained |
| 24 h | 96.0% | 94.8% | sustained |

**A ~4-hour half-life is sufficient.** That is a low bar — a non-covalent daily drug would need
something closer to 12–24 h. **We do not have to fight the CYP soft spots hard**, which is fortunate
given the benzhydryl CH and N-methyl amides flagged in Tier 4.

*(A 30-minute half-life is not enough — trough falls to 24%.)*

## How potent does it need to be?

| kinact/K_I | Mean occupancy | Requirement |
|---|---|---|
| 0.10 | 45.1% | insufficient |
| **0.25** | **66.5%** | **adequate** |
| 0.50 | 78.4% | adequate |
| 1.00 | 85.8% | adequate |
| 2.00 | 90.6% | **saturating — excess potency wasted** |

**Occupancy saturates above kinact/K_I ≈ 0.5.** Extra potency past that point buys nothing.

**This independently reproduces the resistance model's conclusion** — which found a 10× potency gain
worth only 3.2 months — by a completely different route. **Two unrelated models, same answer: potency
is not the lever.**

## What schedule?

| Interval | Mean occupancy | Trough |
|---|---|---|
| 8 h | 92.5% | 90.3% |
| 12 h | 88.9% | 84.2% |
| **24 h (daily)** | **78.4%** | **64.2%** |
| 48 h | 59.4% | 32.8% |
| 168 h (weekly) | 16.7% | 1.0% |

**Daily dosing sits on the plateau.** Twice-daily adds little; every-other-day degrades; weekly fails
outright.

**And it is schedule-robust** — a missed dose costs little, because the target stays inactivated while
the patient is between doses. For a therapy meant to be taken indefinitely, that tolerance to imperfect
adherence matters as much as the pharmacology.

## Combined design brief, from all three models

| Property | Requirement | Status for GPX4-M3 |
|---|---|---|
| Half-life | **≥ 4 h** (not 24 h) | plausible; CYP soft spots tolerable |
| kinact/K_I | **≥ 0.25**, saturates ~0.5 | inherited from ML210 — likely adequate |
| Schedule | **daily injection** | matches the stated goal |
| Potency beyond adequacy | **worthless** | stop optimising it |
| **Retained kill on resistant clone (kG)** | **the actual lever** | **unmeasured — the key experiment** |

---

# kG has literature support, and the news is bad

The systems model identified **kG** — residual kill on the ferroptosis-incompetent escaping clone — as
the parameter the whole programme lives on, with a sharp phase transition at kG/r = 1. It was flagged
as unmeasured. Published data constrains it, and constrains it in the unfavourable direction.

## What the literature says

- **ACSL4 is required for ferroptosis sensitivity**, by enriching membranes with the long
  polyunsaturated ω6 fatty acids that are the substrate for lethal lipid peroxidation
  ([Nat Chem Biol](https://www.nature.com/articles/nchembio.2239)).
- **GPX4-ACSL4 double-knockout cells are markedly resistant to ferroptosis.**
- Critically: **ACSL4 matters far more for ferroptosis induced by GPX4 inhibitors (RSL3-type) than for
  ferroptosis induced by SLC7A11 inhibitors (erastin) or cystine starvation**
  ([ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2451945622002781)).
- GPX4-knockout cells that survive show **compensatory upregulation of FSP1 and PRDX1**
  ([PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10747702/)).

## What this means for GPX4-M3

**kG is likely near zero for GPX4 monotherapy.** ACSL4 loss is not a partial shield against a GPX4
inhibitor — it is close to a complete one, and it is *specifically* protective against this mechanism.
With kG ≈ 0 the model gives kG/r ≈ 0, which is the regime where **relapse is arithmetically inevitable**
and monotherapy delivers delay only.

**This is confirmation of the model's central prediction, not a new problem** — but it removes the
optimistic end of the parameter range. The maintenance thesis survives as *delay* (the QUAZAR
precedent, ~10 months, FDA-approved) and does not survive as *control*.

## The actionable asymmetry

**Erastin-type killing is less ACSL4-dependent than RSL3-type killing.** That is a specific, published
asymmetry and it matters: an SLC7A11 inhibitor retains more activity in exactly the cells that escape a
GPX4 inhibitor.

That does **not** contradict the earlier finding that a second ferroptosis arm adds nothing. The
withdrawn recommendation was **FSP1i**, which acts on the same GPX4-type lipid-peroxidation axis the
escaping clone has already disabled. **SLC7A11 inhibition is a different dependency** — it kills through
cystine/glutathione starvation, which reaches cells whose ACSL4-dependent peroxidation machinery is
gone.

**Revised partner ranking for durability:**

| Partner | Acts on | Expected effect on kG |
|---|---|---|
| FSP1 inhibitor | same lipid-peroxidation axis | **none** — clone already ferroptosis-incompetent |
| **SLC7A11 / cystine-starvation agent** | **partially ACSL4-independent** | **plausible, published basis** |
| Venetoclax (apoptosis) | fully orthogonal | plausible, mechanism-independent |
| Azacitidine | lowers emergence rate μ | modest, additive |

## The experiment this sharpens

The proposed kG measurement stands and is now better specified: **GPX4-M3 against ACSL4-knockout AML
lines, with an erastin-type agent and venetoclax as comparator arms.** The prediction is that M3 alone
shows near-zero activity, and that the comparators retain measurable killing. **If M3 retains
nothing and no partner rescues it, the durability thesis fails and the programme is a delay strategy
only — which is still approvable, but it is a different clinical claim.**
