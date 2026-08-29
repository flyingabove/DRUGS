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
