# GPX4-M3 — Consolidated Findings

**Single current-state document.** The per-tier documents contain the working and the corrections;
this is what survives all of it. Where an earlier claim was overturned, the correction is stated here
rather than only appended downstream.

Last updated: 2026-08-29. Two computations still running (noted in §7).

---

## 1. The compound

```
GPX4-M3   CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1
```

ML210 with both 4-chlorophenyl groups replaced by 4-(N-methylcarbamoyl)phenyl, **and** the piperazine
replaced by a 2-oxopiperazine. **The warhead is untouched, atom for atom.**

| | GPX4-M1 | **GPX4-M3** | ML210 |
|---|---|---|---|
| MW | 520.5 | 534.5 | 477.3 |
| cLogP | 2.16 | **1.68** | 4.75 |
| Basic N (OCT2 kidney risk) | 1 | **0** | 1 |
| hERG pharmacophore | moderate-high | **low** | high |
| Plasma protein binding (est.) | 79% | **70%** | ~100% |
| Stereocentres | 0 | 0 | 0 |
| Synthetic accessibility | 2.65 | ~2.7 | — |
| **Salt formation for injection** | **available** | **not available** | available |

**Both M1 and M3 are carried forward.** M3 removes two safety liabilities; M1 retains the basic nitrogen
that allows salt formation, the standard route to an injectable. That is a genuine trade-off, not a
ranking — see §4.

---

## 2. What is established by measurement

| Claim | Evidence |
|---|---|
| No cavity at the catalytic site | 26 Å³ accessible within 5 Å of Sec46 |
| Non-covalent docking is uninformative here | crystal-ligand redock −5.7 kcal/mol, 5.9 Å RMSD |
| **The site is a narrow groove, not a cavity** | 26 Å³ volume *with* 0.93 burial — resolves why docking fails but a tethered ligand fits |
| Warhead electronically insulated from our edits | C–NO₂ Wiberg Δ 0.006; electrophilic carbon Δ 0.0003 e |
| Adduct is sterically accommodated | 0.29 Å overlap vs 0.35 Å for the crystal ligand re-derived by the same protocol |
| **Modified arms sit in solvent under a mobile protein** | **46% of total ligand SASA; never buried in any frame** (MD, preliminary) |
| No stereocentres | symmetry makes the benzhydryl carbon non-stereogenic |

---

## 3. Selectivity — the strongest part of the case

**Measured structural asymmetry:**

| Site | Burial | Exposed |
|---|---|---|
| **GPX4 Sec46** | **0.93** | 7% |
| TXNRD1 catalytic Sec | 0.23–0.38 | 62–76% |

**Accessibility runs *against* selectivity.** The off-target selenol is the *more* exposed one, sitting
on a C-terminal tail needing no shape complementarity. That is why bare chloroacetamides (ML162, RSL3)
hit TXNRD1, and why no shape optimisation would have rescued them.

**Selectivity therefore comes from two things acting together:** the masked warhead keeping free
electrophile concentration low, and GPX4's enclosed groove providing residence time that TXNRD1's naked
surface Sec cannot. **This is a structural argument against ever simplifying the nitroisoxazole to a
direct electrophile.**

**Inherited experimental evidence:** ML210 is documented as GPX4-selective and does not hit TXNRD1.
M3 carries that warhead unchanged. The limit of the argument is that inheritance covers *warhead-driven*
selectivity, not off-targets reached through changed shape — and we changed only solvent-facing groups.

**Not available:** a selenoproteome-wide structural scan. **18 of 20 human selenoproteins are absent
from AlphaFold DB** (both apparent exceptions are Sec-free isoforms; non-selenoprotein controls are
present). Selenocysteine is encoded by UGA and structure-prediction pipelines drop those sequences.
**That is why the field uses chemical proteomics for this question, and it makes proteome-wide covalent
profiling the only route to answering it.**

---

## 4. The liability that matters most

**Solubility.** Consensus of three models, anchored on compounds with measured values:

| | mg/mL |
|---|---|
| *griseofulvin* (measured 0.009) | *0.009* — model reproduces it |
| **GPX4-M3** | **0.029** |
| GPX4-M1 | 0.012 |
| ML210 | 0.0004 |

A daily injectable needs roughly **>1 mg/mL**. **We are 30–100× short.** M3 is the best of the series
but sits in griseofulvin territory — a textbook poorly-soluble drug.

**And the safety fix cost the formulation lever:** removing the basic nitrogen removed the option of
salt formation. **Symmetry compounds the problem** — symmetric rigid molecules pack efficiently and melt
high, which suppresses solubility, and symmetry is what bought the no-stereocentre advantage.

**A measured melting point and intrinsic solubility settle this and nothing else does.** Both are cheap
and belong in the first wet-lab batch.

---

## 5. What the systems models changed

**Potency is not the lever.** Two unrelated models agree: a 10× potency gain buys 3.2 months
(resistance dynamics), and target occupancy saturates above kinact/K_I ≈ 0.5 (covalent PK/PD).

**The lever is kG** — whether anything still kills the escaping clone faster than it divides. Sharp
phase transition at kG/r = 1: below it relapse is arithmetically inevitable, above it disease is
controlled past any clinical horizon. **kG is unmeasured, and measuring it (ACSL4-knockout lines) is
more decision-relevant than any IC₅₀.**

**Combination strategy, corrected.** An FSP1 inhibitor was the original recommendation; it is
**withdrawn as a durability strategy**. The escaping clone is ferroptosis-*incompetent*, so every
ferroptosis arm is irrelevant to it. FSP1i remains valuable as a **patient-selection and
depth-of-remission tool** for FSP1-high / FLT3-ITD⁺ disease, which is what the published data show.
**Durability requires a partner with an orthogonal death mechanism** — and it need not be potent, only
fast enough to out-pace a 30-day doubling time.

**Dosing.** Daily, continuous, ~4 h half-life sufficient (effect duration is set by GPX4 resynthesis,
not the plasma curve), schedule-robust to missed doses. **Do not push dose** — 4× buys 1.9 months.

**Deploy in deepest remission** — three logs of extra cytoreduction beats a 10× better drug.

---

## 6. Safety

**The therapeutic window is real but conditional.** Gpx4 deletion in the haematopoietic system has no
significant effect on HSPCs under normal conditions — **because vitamin E covers for it.** Knockout mice
on vitamin E-depleted diet show impaired haematopoiesis.

- **Vitamin E status belongs in eligibility criteria.** Post-induction AML patients are frequently
  nutritionally compromised.
- **Supplementation is an open experiment, not a plan** — α-tocopherol may protect the leukaemia as
  readily as the marrow.

**Predicted dose-limiting toxicity: anaemia**, with erythroid progenitors the sensitive compartment.
Monitorable by routine CBC, manageable by transfusion and dose adjustment.

**Class liability:** the nitroaromatic warhead is subject to nitroreduction to an arylamine, a known
idiosyncratic-toxicity route. **Inherited from ML210, not introduced by us**, and the strongest argument
for eventually exploring a non-nitro masked warhead.

---

## 7. Open

| Item | Status |
|---|---|
| ΔΔG‡ (Cys − Se) reaction barrier | **running** — three protocol attempts, two failed and were discarded; see below |
| MD, full 20 ns | **running** — preliminary 700 ps result already supports the design premise |
| kG on ACSL4-null cells | **wet-lab; the single most decision-relevant experiment** |
| Measured solubility + melting point | **wet-lab; cheap; gates the injectable route** |
| Proteome-wide covalent profiling | **wet-lab; the only route to selenoproteome selectivity** |

**On the barrier:** it is corroborative, not load-bearing. At the achievable resolution (~±5 kcal/mol)
it will support or fail to support a selectivity argument that already rests on stronger evidence —
ML210's experimental selectivity and the measured structural asymmetry in §3.

---

## 8. What no computation here can answer

1. **Whether it works in an animal.** Potency, selectivity and exposure can all be right and the drug
   still fail.
2. **The therapeutic index.** No simulation gives an MTD.
3. **Whether LSC suppression extends survival.** Iomab-B hit its primary endpoint at p<0.0001 and was
   refused filing for lack of survival benefit. **That failure mode is invisible to everything in this
   document.**

**The decisive experiment is serial transplantation** — treat a PDX, transplant survivors into fresh
recipients, and ask whether leukemia-initiating capacity is actually gone. Pre-registered kill
criterion: **if LSC burden falls but serial transplantation shows undiminished engraftment, the
maintenance thesis is wrong and the programme stops**, regardless of how good the biomarkers look.

---

## 9. Corrections made to this campaign's own conclusions

Recorded because the pattern matters more than any single result.

| Claim | Correction |
|---|---|
| "GFN2-xTB is sign-inverted for selenium" | **The control was mis-specified** — a thermodynamic quantity tested against a kinetic claim. GFN2 had the right sign; GFN1, which I had endorsed, had it wrong |
| "M3 dominates M1 on every axis" | Removing the basic N also removed salt formation — a genuine trade-off |
| "FSP1i closes the escape route" | Withdrawn for durability; retained for patient selection |
| "M3 is less buried than ML210" | Artifact of a radical-bearing SMILES; reversed on correction |
| "M1 fits better than the positive control" | Difference was below the protocol's own 0.58 Å resolution |
| "TXNRD1's tail is unresolved because it is mobile" | Resolved in 3QFA; both structures are Sec→Cys mutants |
| "No DFT engine available on Windows" | psi4 installs from conda-forge; the blocker was one failed `pip` command |
| "Competitive release means lower doses are better" | Dose-response was monotonic; the corollary did not follow |
| "Barrier = 23.6 kcal/mol" (v1) | Profile was discontinuous — five of seven points `nan` or basin-hopped |
