# Tier 1 and Tier 4 Results — One Hard Stop, One Clean Win

---

# TIER 1 — Reaction chemistry: **BLOCKED, and this is the compute barrier**

I called ΔΔG‡(Cys − Se) the single most important calculation remaining. **It cannot be done on this
hardware, and the way that was established matters more than the failure.**

## The first answer was wrong, and the control caught it

Relaxed distance scans (GFN2-xTB / ALPB water) of selenolate and thiolate attacking the unmasked
nitrile oxide returned:

| Nucleophile | Barrier | Endpoint |
|---|---|---|
| Selenolate (Sec46) | **+17.4 kcal/mol** | uphill throughout |
| Thiolate (generic Cys) | **0.0 — barrierless** | −16.0 kcal/mol |

Read literally: **thiolate reacts freely, selenolate not at all.** That is backwards from textbook
chemistry — selenolate is the stronger nucleophile — so per Rule 12 I ran a positive control before
believing it.

**Control: SN2, CH₃Br + Nu⁻ → CH₃Nu + Br⁻**, where selenolate is experimentally the better nucleophile.

| Method | ΔE(Se) | ΔE(S) | Δ(Se−S) | Verdict |
|---|---|---|---|---|
| **GFN2 + ALPB water** | −2.55 | −41.32 | **+38.77** | **WRONG SIGN** |
| **GFN2 gas phase** | −3.39 | −34.52 | **+31.13** | **WRONG SIGN** |
| GFN1 + ALPB water | +32.44 | +39.18 | −6.73 | correct sign |
| GFN1 gas phase | +38.96 | +44.67 | −5.71 | correct sign |

**GFN2-xTB gets selenium–sulfur discrimination wrong by ~35 kcal/mol, in gas phase and in solvent
alike.** It is the Hamiltonian, not the solvation model. My first result was an artifact of the method,
not chemistry.

GFN1 gets the *ordering* right but its absolute SN2 energies are off by ~70 kcal/mol — usable as a
direction, worthless as a barrier.

**At GFN1, the target reaction favours selenolate by 7.7 kcal/mol.** Right direction. Not a number to
build on.

## What this invalidates, and what it does not

- **Does NOT invalidate §16 (the anchored covalent fit).** That used GFN2 to optimise adduct
  *geometry*, and compared steric overlap — not Se-vs-S energetics. Geometries are far more robust
  than reaction energies. **The 0.42 Å result stands, with a noted caveat.**
- **Does NOT invalidate §17 (potency by inheritance).** Those were C/N/O/H descriptors — Wiberg bond
  orders and atomic charges on the warhead — where GFN2 is well validated. **No selenium was involved.**
- **DOES invalidate any selenium reaction energetics from GFN2**, which is only ever this calculation.

## What is solid without QM — the protonation argument (Tier 1.4)

| Species | pKa | % anionic at pH 7.4 | Count in a cell | Reactive sites |
|---|---|---|---|---|
| Sec46 selenocysteine | 5.2 | **99.4%** | 1 | 0.99 |
| Generic cysteine | 8.3 | 11.2% | ~200,000 | **~22,000** |

**Population does not deliver selectivity — it argues against it.** Selenocysteine is essentially fully
reactive while cysteine is only 11% reactive, but 11% of 200,000 still swamps a single selenolate by
four orders of magnitude.

**So the selectivity must come from the masking kinetics — and that is exactly the number this
hardware cannot compute.** The argument in §9.2 remains an argument.

## The strongest remaining basis: selectivity by inheritance

The same logic that carried potency (§17) carries selectivity, and it is grounded in experiment rather
than computation:

**ML210 is experimentally selective for GPX4 and does *not* hit TXNRD1 — unlike ML162 and RSL3, whose
chloroacetamide warheads do.** GPX4-M3 carries ML210's warhead atom for atom. Selectivity is a property
of the masked warhead, and we did not touch it.

**Limit of the argument:** inheritance covers *warhead-driven* selectivity. It would not cover
off-targets reached because our modifications changed the molecule's shape. We changed only
solvent-facing positions, which makes that risk small but not zero.

## The DFT calculation that is needed, specified for elsewhere

- **Level:** ωB97X-D or M06-2X / def2-TZVP, with def2 ECP on Se; SMD water
- **Systems:** unmasked nitrile oxide + CH₃Se⁻ and CH₃S⁻; full TS optimisation and IRC
- **Also:** the HNO₂ elimination barrier (Tier 1.1) — is unmasking rate-limiting?
- **Controls:** the SN2 reaction above, plus ML162/RSL3 chloroacetamide, which **must** come out
  non-selective
- **Requires:** Linux + Psi4/ORCA/Gaussian. **pyscf does not build on Windows; no DFT engine is
  available here.**

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

**GPX4-M3 is the lead.** It is not a marginal preference — it wins or ties on every measured axis, and
it removes two liabilities (kidney, heart) that M1 carried.

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
had only ever been checked on ML210's pose. Recomputed in **M3's own** best anchored pose:

| | Max overlap | Mean burial | Atoms >50% buried |
|---|---|---|---|
| ML210 | 0.34 Å | 0.36 | 8 / 28 |
| **GPX4-M3** | 0.34 Å | **0.22** | 8 / 35 |

**M3 is less buried overall than ML210** (0.22 vs 0.36) despite being a larger molecule, and it has the
same absolute number of buried atoms — those extra atoms all went into solvent.

**The modified arms are at burial 0.00 — fully solvent-exposed.** The buried set in both compounds is
the warhead region (Se, the adjacent N/O/C), exactly as designed: **anchor buried, payload in water.**

This is the fourth independent line supporting the substitution, and the first computed on the actual
lead rather than on its parent.
