# Simulation Master Plan — Everything Computable Before the Wet-Lab Barrier

**Goal of this document:** get to the point where an experienced translational scientist reads it and
says *"the remaining uncertainty can only be resolved in animals — fund the study."*

That is the real bar. It is not 99.9%.

---

## 0. Why 99.9% is not the target, and what is

Computational confidence has a hard ceiling: **the model is not the system.** Every method here
approximates something — implicit solvent instead of real water, a rigid receptor instead of a
breathing protein, a force field instead of electrons, one cell line instead of a patient's marrow.
Stacking more simulation shrinks *some* error bars and cannot touch others at all.

Concretely, **no amount of compute can tell us:**

- whether suppressing LSCs extends survival (the Iomab-B failure mode — every biomarker passed, the
  endpoint did not)
- what the actual maximum tolerated dose is in a mammal
- whether a patient's marrow microenvironment rescues LSCs in ways no model contains

**What compute *can* do is eliminate failure modes one at a time**, so the animal study tests the
hypothesis rather than discovering an avoidable chemistry problem.

**Honest current state: roughly a third of the addressable computational risk has been retired.** This
plan targets the rest.

---

## 1. Confidence accounting — where we actually stand

### Established by measurement, not assumption

| Claim | Evidence | Confidence |
|---|---|---|
| No druggable pocket at the catalytic site | 26 Å³ within 5 Å of Se | **High** |
| Non-covalent docking uninformative here | crystal-ligand redock −5.7 kcal/mol, 5.9 Å RMSD | **High** |
| Modified positions face solvent | per-atom burial 0.06–0.17 | **High** |
| Warhead electronically insulated from our edits | C–NO₂ Wiberg Δ 0.006; electrophilic C Δ 0.0003 e | **High** |
| Adduct sterically accommodated | 0.42 Å vs 0.55 Å for crystal-bound ML162 | **Medium-High** (rigid receptor) |
| No stereocentres; SA 2.65 | RDKit | **High** |

### Assumed, argued, or hoped — the actual risk register

| Assumption | Status | Kill potential |
|---|---|---|
| Selective for GPX4 Sec over the cysteine proteome | **argued from masking, never computed** | **PROGRAM-ENDING** |
| Therapeutic window vs normal HSC | literature inference only | **PROGRAM-ENDING** |
| Chronic dosing suppresses rather than selecting FSP1-high escape | hand-waved | **PROGRAM-ENDING** |
| Reaches marrow at free concentration above IC₅₀ | transporter reasoning, no model | High |
| Not hepatotoxic from covalent burden | not assessed | High |
| Potency inherited from ML210 | inheritance argument, no barrier computed | Medium |
| Solubility adequate for injection | ESOL −4.3 only | Medium |

**The three PROGRAM-ENDING rows are where remaining compute should go.** Everything else is polish.

---

## 2. The six kill questions

Ordered by probability-of-killing × cost-of-finding-out-late.

### K1 — Does it hit GPX4 selectively, or alkylate the proteome?

**This kills more covalent drugs than any other single factor.** A reactive electrophile in a human
meets ~200,000 accessible cysteines. Our entire selectivity argument is that the nitroisoxazole is
*masked* and unmasks slowly, so only a highly nucleophilic selenol reacts fast enough. **That argument
has never been computed.**

**What decides it:** the difference in activation free energy for attack by selenolate (Sec46) versus
thiolate (generic Cys). Selenium is more nucleophilic and has a lower pKa, so it sits anionic and
reactive at pH 7.4 while most cysteines are protonated. **We need the number, not the story.**

### K2 — Is there a window between LSC and normal HSC?

The whole thesis is that AML blasts carry higher lipid-peroxidation load and depend more on GPX4.
Currently supported by literature only.

### K3 — Does gentle chronic dosing suppress, or breed escape?

Five redundant defence arms (FSP1, DHODH, GCH1–BH4, NQO1, GSH supply). Chronic sub-lethal pressure is
exactly the regime that selects resistance. **The maintenance framing makes this central, not a
footnote.**

### K4 — Does enough free drug reach marrow?

### K5 — Covalent hepatotoxicity?

### K6 — Does LSC suppression extend survival? — **not computable. This is the animal study.**

---

## 3. The experiment plan

Tiers ordered by kill-question priority, not by cost.

### TIER 1 — Reaction chemistry and selectivity *(K1 — highest remaining value)*

| # | Experiment | Method | Cost | Decides |
|---|---|---|---|---|
| 1.1 | **Unmasking barrier**: HNO₂ elimination from the nitroisoxazole | GFN2-xTB relaxed scan / NEB, DFT single-point | hours, local | Is unmasking rate-limiting? Sets the kinetic regime |
| 1.2 | **Se attack barrier** on the unmasked nitrile oxide | cluster QM (xTB path, DFT refine) | hours–days, local | Intrinsic reactivity toward selenolate |
| 1.3 | **Cys attack barrier**, same geometry | identical protocol, S for Se | hours, local | **The selectivity number: ΔΔG‡** |
| 1.4 | Protonation-state correction: selenolate vs thiol at pH 7.4 | pKa reasoning + QM | hours | Converts intrinsic → effective selectivity |
| 1.5 | Repeat 1.1–1.3 for **GPX4-M3, GPX4-M1, ML210, ML162, RSL3** | same | days | **ML162 and RSL3 must come out non-selective — if the method says otherwise it is broken** (Rule 12) |

**Kill criterion:** if ΔΔG‡(Cys − Se) is under ~2 kcal/mol, the compound is a promiscuous alkylator —
the program stops or the warhead changes. **This is the single most important calculation remaining.**

### TIER 2 — Dynamics and the real binding picture *(K1, potency)*

| # | Experiment | Method | Cost | Decides |
|---|---|---|---|---|
| 2.1 | **MD of the covalent adduct**, 3 × 200 ns | OpenMM/GROMACS, custom Sec parameters | GPU-days | Does the modified region stay solvent-facing? Retires the rigid-receptor caveat on 0.42 Å |
| 2.2 | Apo vs adduct comparison | same trajectories | included | Does binding distort the fold? |
| 2.3 | Non-covalent pre-complex free energy | metadynamics / umbrella sampling | GPU-days | Is there a recognition step at all, or a diffusion-limited reaction? |
| 2.4 | Solvent exposure of the amide substituents over time | trajectory analysis | minutes | Direct test of the core design premise |

**Blocker to clear first:** selenocysteine force-field parameters — derive RESP charges from the
QM-optimised adduct. This is the standing blocker on all MM work and it is solvable.

### TIER 3 — Proteome-scale selectivity *(K1, K5)*

| # | Experiment | Method | Cost |
|---|---|---|---|
| 3.1 | **Selenoproteome scan** — all 25 human selenoproteins; which have solvent-accessible Sec in a similar electrostatic environment? | AlphaFold/PDB + SASA + electrostatics | hours |
| 3.2 | TXNRD1/TXNRD2 focused analysis — the documented 26% cross-hit | structure comparison, covalent feasibility | hours |
| 3.3 | GPX1–GPX8 family discrimination | active-site alignment | hours |
| 3.4 | Hyper-reactive cysteine screen (KEAP1, GAPDH, etc.) | structure set + barrier proxy from 1.3 | days |

**This is the analysis that would have predicted the ML162/RSL3 TXNRD1 problem in advance.**

### TIER 4 — ADMET *(K4, K5)*

| # | Experiment | Method | Cost |
|---|---|---|---|
| 4.1 | CYP metabolic soft-spot prediction | SMARTS + literature rules; trained model if available | hours |
| 4.2 | hERG liability | pharmacophore + published models | hours |
| 4.3 | **Aqueous solubility, better than ESOL** | thermodynamic cycle, COSMO-RS-style with xtb | hours |
| 4.4 | Plasma protein binding | structure-based estimate | hours |
| 4.5 | Reactive-metabolite / covalent hepatotox risk | structural alerts + Tier 1 barriers | hours |
| 4.6 | IV/SC formulation feasibility | solubility + logD profile | hours |

**4.3 matters more than usual** — we chose an injectable route and predicted logS is −4.1 to −5.0,
which is borderline. **If it will not dissolve, nothing else matters.**

### TIER 5 — Systems modelling *(K3, K4 — the maintenance thesis)*

| # | Experiment | Method | Cost | Decides |
|---|---|---|---|---|
| 5.1 | **PBPK model** — marrow compartment, free fraction, schedule | ODE model | hours | Is there a schedule with marrow exposure above IC₅₀ and normal tissue below? **This IS the maintenance-window question** |
| 5.2 | **Resistance evolution model** — LSC population, 5 escape arms, chronic pressure | stochastic branching process | hours | Does gentle chronic dosing suppress or select? |
| 5.3 | Combination modelling — + FSP1 inhibitor, + azacitidine | extend 5.2 | hours | Does closing one arm change the trajectory qualitatively? |
| 5.4 | Dose-fractionation scan — daily low vs pulsed high | 5.1 + 5.2 coupled | hours | **The actual clinical design question** |

**Tier 5 is cheap and tests the core thesis directly. It should arguably run before Tier 2.**

### TIER 6 — Target validation from public data *(K2)*

| # | Experiment | Source | Cost |
|---|---|---|---|
| 6.1 | GPX4/FSP1/ACSL4/LPCAT3 expression: LSC vs HSC vs blast | public scRNA-seq (van Galen, GEO) | days |
| 6.2 | **DepMap GPX4 dependency** across AML lines vs other lineages | DepMap portal | hours |
| 6.3 | Co-dependencies when GPX4 is lost | DepMap correlations | hours |
| 6.4 | Patient-selection biomarker — which AML subtypes are ferroptosis-primed? | TCGA / BeatAML | days |
| 6.5 | **Normal HSC GPX4 dependency** — the safety half of the window | DepMap + literature | hours |

**6.2 + 6.5 together are the cheapest possible test of K2** and should run immediately. If normal HSC
lines are as GPX4-dependent as AML lines, the window does not exist and the program stops.

---

## 4. Recommended execution order

Cheapest disqualifying result first:

```
WEEK 1   6.2, 6.5   DepMap window check       -> no window?      STOP
         5.1, 5.2   PBPK + resistance model   -> no schedule?    STOP
         4.3        solubility                -> insoluble?      reformulate / change linker
WEEK 2   1.1-1.5    reaction barriers         -> not selective?  CHANGE WARHEAD
         3.1-3.3    selenoproteome scan
WEEK 3   4.1-4.6    full ADMET
         2.x        MD (derive Sec parameters first)
WEEK 4   consolidate, re-rank, final compound selection, synthesis
```

**Three STOP gates in week 1, all cheap.** That ordering is the point.

---

## 5. Compound set to carry forward

The linker vector was opened while drafting this plan and immediately produced a better molecule.
**Every simulation runs on the full set, not just the current lead:**

| ID | Linker | Basic N | Stereo | cLogP | logS | Note |
|---|---|---|---|---|---|---|
| GPX4-M1 | piperazine | **1** | 0 | 2.16 | −4.30 | previous lead; **carries the OCT2 liability** |
| **GPX4-M3** | 2-oxopiperazine | **0** | 0 | **1.68** | **−4.08** | **dominates M1 on every axis** |
| GPX4-M4 | piperidine, C-linked | 0 | 0 | 3.29 | −5.01 | neutral but greasier |
| ML210 | — | 1 | 0 | — | — | positive control |
| ML162 / RSL3 | — | — | — | — | — | **negative controls for selectivity** |

**GPX4-M3 is the new nominal lead**, pending the anchored-fit test: it removes a liability we
identified ourselves and improves logP and solubility at the same time.

---

## 6. What this plan cannot deliver, stated plainly

After every experiment above succeeds, these remain **completely open**:

1. **Whether it works in an animal.** Potency, selectivity and exposure can all be right and the drug
   still fail.
2. **The therapeutic index.** No simulation gives an MTD.
3. **Whether LSC suppression extends survival.** Iomab-B hit its primary endpoint at p<0.0001 and was
   refused filing for lack of survival benefit. **That failure mode is invisible to every computation
   in this document.**
4. **Immune, niche, and microenvironment effects.**
5. **Human-specific metabolism.**

**A successful outcome of this whole plan is a well-characterised molecule with a defensible
selectivity argument, a modelled dosing schedule, and no known disqualifying liability.** That is
exactly the package that justifies a rodent study — and it is the honest maximum.

---

## 7. The study this plan is designed to justify

If Tiers 1–6 pass:

- **Model:** AML PDX in NSG mice, established disease, post-chemotherapy residual disease
- **Arms:** vehicle / GPX4-M3 daily low-dose / azacitidine / combination
- **Primary:** LSC burden (CD34⁺CD38⁻ human chimerism) at fixed timepoint
- **Secondary:** survival, marrow histology, liver and kidney panels, blood counts
- **The decisive arm: serial transplantation of survivors** — the only test of whether
  leukemia-initiating capacity was actually removed
- **Tolerability focus:** kidney (the OCT2 concern, mitigated in M3), liver (covalent burden), normal
  haematopoiesis

**Pre-registered kill criterion:** if LSC burden falls but serial transplantation shows undiminished
engraftment, the maintenance thesis is wrong and the program stops — regardless of how good the
biomarkers look. **That is precisely the discipline the Iomab-B program lacked.**

---

## STATUS UPDATE — the compute barrier was self-imposed

**Every tool I declared unavailable is in fact available on this machine.**

| Capability | Earlier claim | Reality |
|---|---|---|
| DFT | "no engine on Windows" | **psi4 1.11 installs from conda-forge.** I had only tried `pip install pyscf`, which fails to compile, and stopped |
| MD | "OpenMM not installed" | **OpenMM 8.6 installs.** The first attempt failed only because `openmmforcefields` pulls `ambertools`, which has no win-64 build — `pip install openmmforcefields --no-deps` sidesteps it |
| GPU | not considered | **NVIDIA TITAN Xp, 12 GB.** CUDA fails on a PTX version mismatch, but **OpenCL runs at 203 ns/day** — 7.7× the CPU |
| PCM solvation | — | available; **but psi4 has no analytic PCM gradients** and silently falls back to finite differences. Gas-phase geometry + PCM single-point is the workable protocol |

**Lesson for the plan: "blocked" claims need the same verification as results.** I reported a hard
compute barrier on the single most important calculation after one failed `pip` command.

### Revised tier status

| Tier | Status |
|---|---|
| 1 — reaction chemistry | **UNBLOCKED.** Thermodynamics done; **barriers running** (the quantity that actually matters) |
| 2 — MD | **UNBLOCKED.** OpenCL GPU available; system built from the anchored pose |
| 3 — proteome selectivity | not started |
| 4 — ADMET | **done** — M3 sweeps |
| 5 — systems modelling | **done** — potency is not the lever; kG is |
| 6 — target validation | **done** — window real but vitamin-E-dependent; DLT predicted as anaemia |
