# Tier 1 and Tier 4 Results — One Hard Stop, One Clean Win

---

# TIER 1 — Reaction chemistry: **UNBLOCKED at DFT, and my earlier conclusion was wrong**

psi4 1.11 has a win-64 conda build. My earlier statement that "no DFT engine is available on Windows"
was wrong — I had tried only `pip install pyscf`, which fails to compile, and stopped there.
`conda install -c conda-forge psi4` works. **The blocker was mine, not the platform's.**

## The correction that matters: my control was mis-specified

I had declared GFN2-xTB "sign-inverted" for selenium based on this control:

> **CH₃Br + Nu⁻ → CH₃Nu + Br⁻**, "where selenolate is experimentally the better nucleophile"

**That reasoning was invalid.** "Better nucleophile" is a statement about the **reaction barrier** —
a kinetic quantity. What I computed was **ΔE of reaction** — a thermodynamic quantity fixed largely by
bond strengths. **C–S (~272 kJ/mol) is stronger than C–Se (~234 kJ/mol)**, so thiolate methylation
*should* be more exothermic. I was testing a kinetic claim with a thermodynamic number and calling the
disagreement a method failure.

### DFT reference — ωB97X-D/def2-TZVPPD // def2-SVPD, IEFPCM water

| | ΔE (kcal/mol) |
|---|---|
| CH₃Br + CH₃Se⁻ | −34.02 |
| CH₃Br + CH₃S⁻ | −39.74 |
| **Se − S** | **+5.72** |

**Positive, and correct** — thiolate methylation is more exothermic, exactly as bond strengths predict.

### What that does to the semiempirical verdicts

| Method | Se − S | Error vs DFT | Revised verdict |
|---|---|---|---|
| **DFT (reference)** | **+5.72** | — | — |
| GFN2 + ALPB water | +38.77 | **+33.05** | **right sign, magnitude inflated ~7×** |
| GFN2 gas | +31.13 | +25.41 | right sign, inflated |
| GFN1 + ALPB water | −6.73 | −12.45 | **WRONG SIGN** |
| GFN1 gas | −5.71 | −11.43 | **WRONG SIGN** |

**Both of my earlier verdicts were backwards.** GFN2 was not sign-inverted — it has the right direction
with a badly inflated magnitude. GFN1, which I endorsed as "passing the control," is the one that gets
the sign wrong.

**GFN2 remains unusable for this comparison** — a 33 kcal/mol error is not salvageable — but the reason
is magnitude, not direction, and **GFN1 is worse, not better.**

## What still has to be computed

**Reaction energies do not answer the selectivity question.** Selectivity is kinetic: whether the
masked warhead reacts with Sec46 faster than with the cysteine proteome. That needs **barriers**,
and the control for a barrier calculation must itself be kinetic — computed ΔE‡ for the SN2, checked
against the documented faster reaction of selenolate with alkyl halides.

**Status: barrier calculations are the remaining Tier 1 work, now tractable.** The thermodynamics
above are a method calibration, not the answer.

## What is solid without QM — the protonation argument (Tier 1.4)

| Species | pKa | % anionic at pH 7.4 | Count in a cell | Reactive sites |
|---|---|---|---|---|
| Sec46 selenocysteine | 5.2 | **99.4%** | 1 | 0.99 |
| Generic cysteine | 8.3 | 11.2% | ~200,000 | **~22,000** |

**Population does not deliver selectivity — it argues against it.** 11% of 200,000 cysteines still
swamps a single selenolate by four orders of magnitude. Selectivity must come from the masking
kinetics.

## The strongest current basis: selectivity by inheritance

**ML210 is experimentally selective for GPX4 and does not hit TXNRD1** — unlike ML162 and RSL3, whose
chloroacetamide warheads do. GPX4-M3 carries ML210's warhead atom for atom.

**Limit:** inheritance covers *warhead-driven* selectivity, not off-targets reached because our
modifications changed shape. We changed only solvent-facing positions, which makes that risk small but
not zero.

---

# TIER 4 — ADMET: **GPX4-M3 sweeps the panel**

| Compound | cLogP | logS | TPSA | basic N | **hERG risk** | PPB (est.) |
|---|---|---|---|---|---|---|
| GPX4-M1 (piperazine) | 2.16 | −4.30 | 150.9 | 1 | **MODERATE-HIGH** | 79% |
| **GPX4-M3 (2-oxopiperazine)** | **1.68** | **−4.08** | 168.0 | **0** | **low** | **70%** |
| GPX4-M4 (piperidine) | 3.29 | −5.01 | 147.7 | 0 | low | 99% |
| ML210 (reference) | 4.75 | −5.84 | 92.7 | 1 | **HIGH** | ~100% |

**One linker change fixed three liabilities at once.** Removing the basic nitrogen:

1. **Kidney** — removes the OCT2 proximal-tubule trap (the cisplatin/metformin mechanism)
2. **Heart** — hERG blockade needs a protonatable basic nitrogen plus lipophilic aromatics. **No basic
   N drops hERG risk from MODERATE-HIGH to low.** This was not the reason for the change; it came free
3. **Exposure** — lowest plasma protein binding of the set (70%), so **highest free fraction** — and
   free drug is the only drug that works

**Against ML210, M3 is better on every ADMET axis**: 3 log units less lipophilic, ~1.8 log more
soluble, no hERG pharmacophore, far lower protein binding.

## CYP soft spots

All compounds share the **benzhydryl CH** (oxidation to benzhydrol) and **N-methyl amides**
(N-dealkylation). ML210 additionally carries **two aryl-Cl** dehalogenation sites — which our amide
replacement removes. **M3 has one fewer α-amino CH₂ than M1**, marginally fewer soft spots.

## Reactive-metabolite alerts

**The nitroaromatic alert fires on all four compounds including ML210 — because it *is* the warhead.**
Per Rule 9, an alert on the shared scaffold of a validated chemotype is not a differentiator.

**But it is a genuine class liability**: nitroreduction yields an arylamine, a recognised idiosyncratic
tox route. It is **inherited, not introduced by us**, and it is the strongest argument for eventually
exploring a non-nitro masked warhead — which the Tier 1 DFT work would also inform.

---

# Consolidated ranking

| | M1 | **M3** | M4 |
|---|---|---|---|
| Basic N / OCT2 kidney risk | 1 ✗ | **0 ✓** | 0 ✓ |
| hERG | MOD-HIGH ✗ | **low ✓** | low ✓ |
| Solubility (injectable) | −4.30 | **−4.08 ✓** | −5.01 ✗ |
| Free fraction | 79% | **70% ✓** | 99% ✗ |
| Stereocentres | 0 ✓ | **0 ✓** | 0 ✓ |
| Warhead intact | ✓ | **✓** | ✓ |

**GPX4-M3 is the lead on the ADMET panel above.** It wins or ties on every axis *measured here*, and
it removes two liabilities (kidney, heart) that M1 carried.

**This ranking is qualified later in this document.** The solubility work (Tier 4.3) found that removing
the basic nitrogen also removes the option of salt formation — the standard route to an injectable — so
M1 retains a formulation advantage the panel above does not capture. **Both compounds are carried
forward.**

**Outstanding on M3:** the anchored covalent fit (§16) has been run for M1, not M3. The lactam changes
the benzhydryl nitrogen's geometry, so that test must be repeated before M3 is confirmed.

---

# Anchored covalent fit, recalibrated — M3 confirmed

Rebuilt the §16 protocol (it had been run inline and never saved) and re-ran it with a stronger
calibration: **the crystal ligand scored in its own deposited pose**, which is the empirical definition
of a tolerable fit.

Two bugs were found and fixed on the way, both silent:

1. **Ring-closure digits.** The adduct-construction regex assumed digit `1`; M1/M3 use `3` and ML210
   writes its carbonyl as `O=C(...)`. Result: no Se was attached and three of four compounds were
   silently skipped. Fixed by hardcoding the four adducts explicitly.
2. **Wrong catalytic residue.** Matching `residue in (SEC,CYS,CSE) and atom in (SE,SG)` selected
   **Cys10**, the first such atom in the file — not Sec46. The tell was the crystal ligand sitting
   **34.28 Å** from the "catalytic" site. Fixed by asserting `SEC/SE` explicitly, plus a hard assertion
   that the crystal ligand is within 2.5 Å of the identified site.

## Result

| | Max overlap | What it is |
|---|---|---|
| **Crystal ligand G9N, deposited pose** | **−0.23 Å** | **ground truth — no overlap at all** |
| G9N re-derived by conformer search | 0.35 Å | **protocol control** |
| ML210 | 0.31 Å | known selective binder |
| GPX4-M1 | 0.29 Å | previous lead |
| **GPX4-M3** | **0.29 Å** | **new lead** |

**The steric question is answered for M3.** It sits at the same overlap as ML210 and as the
reconstructed crystal ligand.

**Stated honestly: the protocol control (0.35 Å) scores *worse* than every compound (0.29–0.31 Å).**
That means ~0.58 Å is this method's own error against the crystal pose, and **differences between
compounds of 0.02–0.06 Å are far below its resolution.** This test can show *"no steric problem"*. It
cannot rank compounds, and the §16 reading that GPX4-M1 "fits better than the positive control" was
over-interpretation of noise.

**These numbers supersede §16's (0.55 / 0.39 / 0.42)**, which were computed in the QM-cluster
coordinate frame with a different receptor subset and without the deposited-pose benchmark.

---

# Per-atom burial of M3 in its own anchored pose

The design premise — that the N-methylamide arms, the only thing changed from ML210, sit in solvent —
had only ever been checked on ML210's pose. Recomputed in **M3's own** best anchored pose.

**Correction to a first version of this section.** The adduct SMILES used
`C(=[N+][O-])`, which puts three bonds on a positively charged nitrogen and therefore carries **one
radical electron**. RDKit accepts it silently. The corrected structure is the **oximate**,
`C(=N[O-])`. Rerun with the correct valence:

| | Max overlap | Mean burial | Atoms >50% buried |
|---|---|---|---|
| ML210 | 0.34 Å | 0.27 | 8 / 28 |
| GPX4-M3 | 0.34 Å | 0.31 | 9 / 35 |

**The earlier claim that M3 is *less* buried than ML210 (0.22 vs 0.36) was an artifact of the radical
structure and is withdrawn.** With correct valences the two are comparable, M3 marginally more buried —
and given that conformer search is stochastic, a 0.04 difference is not meaningful either way.

**What survives, and it is the claim that matters:** the modified arms sit at **burial 0.00 — fully
solvent-exposed** — while the buried set in both compounds is the warhead region (Se and the adjacent
N/O/C). **Anchor buried, payload in water**, exactly as designed.

**Scope of the radical defect.** It affected the adduct structures in the fit and burial scripts. It did
**not** affect the DFT run: psi4 is given explicit coordinates and a charge, never SMILES bond orders,
and it re-optimises the geometry — so it computed the correct closed-shell anion regardless. The
nitrile-oxide electrophile itself was always correct.

---

# Tier 4.3 — Solubility: a real problem, and a trade-off I missed

Three empirical models (ESOL, Ali, GSE with an estimated melting point), anchored against two compounds
with known measured solubility.

| Compound | mean logS | **mg/mL** |
|---|---|---|
| *ref: caffeine* (measured ~21 mg/mL) | −0.45 | *69* |
| *ref: griseofulvin* (measured ~0.009 mg/mL) | −4.61 | *0.009* |
| **GPX4-M3** | −4.27 | **0.029** |
| GPX4-M1 | −4.65 | 0.012 |
| GPX4-M4 | −5.65 | 0.001 |
| ML210 | −6.81 | 0.0004 |

**The anchors validate the method at the low end:** griseofulvin comes out at 0.009 mg/mL against a
measured 0.009. Caffeine is overestimated ~3× but lands correctly as freely soluble.

## The finding

**GPX4-M3 at ~0.03 mg/mL sits in griseofulvin territory — a textbook poorly-soluble drug.** A daily
injectable needs roughly **>1 mg/mL** in a formulable vehicle. **We are 30–100× short.**

M3 is the best of the series — 2.4× better than M1, 30× better than M4, 70× better than ML210 — but
"best of a poorly-soluble set" is not solved. This is a genuine formulation problem, not a rounding
error, and it is the most concrete liability the campaign has produced.

## The trade-off I missed

Earlier I wrote that **M3 dominates M1 on every axis.** That was wrong in one important respect.

**These models predict *intrinsic* (neutral-form) solubility. A basic amine can be formulated as a
salt**, which routinely improves apparent solubility by orders of magnitude and is the standard route to
an injectable. M1's piperazine (est. pKa ~6–7) would form a stable HCl salt. **M3 has no basic nitrogen
at all — that was the point of the change — so salt formation is not available to it.**

| | GPX4-M1 | GPX4-M3 |
|---|---|---|
| OCT2 kidney risk | basic N — **present** | none |
| hERG pharmacophore | **moderate-high** | low |
| Intrinsic solubility | 0.012 mg/mL | **0.029 mg/mL** |
| **Salt formation for injection** | **available** | **not available** |

**So the ranking is a genuine trade-off, not a clean win.** M3 removes two safety liabilities and gives
up the most common formulation lever. Which matters more is an empirical question — measured solubility
and a rat PK study decide it, not these models.

**Both should be carried forward.** Dropping M1 on the strength of my earlier "dominates on every axis"
claim would have discarded the only salt-formable candidate.

## What computation cannot settle here

The melting-point term drives the GSE estimate and is the weakest input. **Symmetric, rigid molecules
pack efficiently and melt high, which suppresses solubility** — and symmetry is precisely what we chose
for the no-stereocentre advantage. That benefit may have a solubility cost.

**A measured melting point and a measured intrinsic solubility resolve this, and nothing else does.**
Both are cheap, early experiments and belong in the first wet-lab batch alongside the enzyme assay.
