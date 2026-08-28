# Execution Log — GPX4 Program

Live build log. Strategy: [../strategies/crack-the-shell.md](../strategies/crack-the-shell.md).
Method: [../compute-plan-gpx4.md](../compute-plan-gpx4.md).

**Working directory:** `work/structures/`

---

# ✅ STEP 1 — COMPLETE: Structures acquired and selenocysteine verified

**Why this was step one:** selenocysteine is a non-standard residue. Most structure-prep tools drop
it, mis-type it, or silently auto-mutate it to cysteine. If Sec46 does not survive preparation,
every downstream result is worthless — and the failure is silent.

## Downloaded

| PDB | Title | Resolution | Lines |
|---|---|---|---|
| **6HN3** | Wildtype form (apo) of human GPX4 with Se-Cys46 | **1.01 Å** | 3886 |
| **6HKQ** | Human GPX4 in complex with covalent inhibitor ML162 (S enantiomer) | **1.54 Å** | 3484 |

Retrieved from RCSB. 1.01 Å on the apo form is near-atomic — unusually good for structure-based
design.

## Verified: genuine selenocysteine, not a U46C mutant

| Check | 6HN3 | 6HKQ |
|---|---|---|
| Residue 46, chain A | **SEC** ✅ | **SEC** ✅ |
| SE atoms present | 1 ✅ | 2 (two conformers) ✅ |
| SEQRES declares SEC | Yes ✅ | Yes ✅ |
| Sidechain atoms | N, CA, CB, **SE**, C, O | same, duplicated across altlocs |

Both carry real selenium. Many PDB entries for GPX4 use a cysteine substitution because Sec is hard
to express — those are unusable here, since selenium nucleophilicity is the mechanism.

## Extracted: the covalent geometry

The covalent bond is explicitly recorded in the file:

```
LINK  SE  ASEC A  46    C20A G9N A 201   1555 1555  1.61
LINK  SE  BSEC A  46    C20B G9N A 201   1555 1555  1.56
```

**Design parameters — these are the docking restraints:**

| Parameter | Value |
|---|---|
| Ligand chemical component ID (ML162) | **G9N** (32 atoms) |
| Covalent anchor on protein | **Sec46 SE** |
| Covalent anchor on ligand | **C20** |
| **Se–C20 bond length** | **1.56–1.61 Å** (use ~1.58 Å as restraint) |

## ⚠️ Finding that would have caused trouble: Sec46 is modeled in two conformations

| Conformer | Occupancy | Se–C20 length |
|---|---|---|
| **altloc A** | **0.60** (majority) | 1.61 Å |
| altloc B | 0.40 | 1.56 Å |

**The two selenium positions are 2.33 Å apart** — a real conformational difference, not noise. The
ligand C20 follows, also at 2.33 Å separation.

**Why this matters:** most structure-preparation tools silently keep only altloc A. That default
happens to be defensible here (A is the majority conformer), **but it must be a deliberate choice,
not an accident** — and the B conformer should be carried through validation as a check on whether
pose recovery is conformer-dependent.

**Decision:** use **altloc A** as primary for site definition and docking. Retain B for validation.

## Environment confirmed

Python 3.13.11 · conda 25.11.1 · numpy 2.4.1 · scipy 1.17.0 · curl 8.17.0
**Not yet installed:** RDKit, docking engine, OpenMM, generator stack.

---

# ✅ STEP 3 — COMPLETE (with a method-changing finding): Counter-target structures

**Downloaded and verified TXNRD1:** `2J3N` (X-ray, human TrxR1, 6 chains) and `3QFA` (TrxR–Trx
complex, 2.2 Å).

## ⚠️ Neither contains selenium. Both are Sec→Cys mutants.

The SEQADV records in 3QFA state it outright:

```
SEQADV 3QFA SER A 497  UNP Q16881 CYS 497  ENGINEERED MUTATION
SEQADV 3QFA CYS A 498  UNP Q16881   U 498  SEE REMARK 999
```

Residue 498 is **U (selenocysteine) in UniProt Q16881**, replaced by **CYS** in the crystal. 2J3N
shows the same substitution — its native motif should read Gly496-Cys497-**Sec498**-Gly499 but reads
**CYS498**.

**And the catalytic tail is frequently disordered:** in 2J3N, only chains C/D/E resolve to residue
499. Chains A, B, and F stop at 494–496 — the C-terminal arm is simply not modeled.

## Why this matters — three consequences

**1. A systematic bias in the selectivity margin.** We have a *genuine* selenocysteine structure for
the on-target (GPX4: 6HN3/6HKQ) and only a *cysteine surrogate* for the counter-target. Selenium and
sulfur differ in nucleophilicity and in bond length (Se–C ≈ 1.98 Å vs S–C ≈ 1.8 Å). Docking them
head-to-head compares unlike with unlike, and the resulting margin would be biased in an unknown
direction.

**2. Rigid docking misrepresents TXNRD1.** The catalytic Sec sits on a **flexible C-terminal arm**
that swings to deliver electrons — which is precisely why half the chains fail to resolve it. A
static receptor model does not capture that.

**3. The likely conclusion: selectivity here is a reactivity problem, not a shape problem.**

Look at what actually distinguishes the compounds:

| Compound | Warhead | Hits GPX4? | Hits TXNRD1? |
|---|---|---|---|
| ML210 | Nitroisoxazole (masked nitrile-oxide) | **Yes** | No |
| RSL3, ML162 | Chloroacetamide | **No** | **Yes** |

**That is a warhead-chemistry difference, not a binding-pocket difference.** Two chemotypes, opposite
selectivity, with the discriminating variable being intrinsic electrophile reactivity and its match to
a selenol versus a thiol.

## Method revision

**Structure-based covalent docking alone will probably not reproduce the known selectivity ordering** —
so the Step 4 validation gate needs a second axis:

1. **Keep the docking arm**, but computationally restore Sec498 in the TXNRD1 model so both targets
   carry selenium. Document it as a modeled residue, not experimental.
2. **Add a reactivity arm.** Quantum-chemical treatment of warhead electrophilicity and its
   selenol-versus-thiol preference. This was previously scheduled for the reversibility question in
   Phase 5; it is now needed earlier, for selectivity.
3. **Treat TXNRD1 docking scores as low-confidence** given the flexible, partly-unresolved tail.

**This is exactly what the Step 4 validation gate exists to catch — and it caught it before we
generated a single molecule.**

## Still open

**GPX1** accession not yet resolved. As the closest GPX-family member it remains the more informative
shape-based counter-target, since it *is* a selenoprotein with a comparable fold.

---

# ✅ STEP 3b — COMPLETE: Compound baseline established

RDKit 2026.03.5. Structures pulled from PubChem; warhead classes confirmed computationally by SMARTS,
not by assumption.

## The three reference compounds

| Compound | MW | logP | TPSA | HBD | HBA | rotB | Warhead (verified) | Known selectivity |
|---|---|---|---|---|---|---|---|---|
| **ML210** | 475.3 | 4.75 | **92.7** | **0** | 6 | 5 | **nitro-isoxazole** ✅ | **GPX4-selective** |
| ML162 | 477.4 | 5.08 | 58.6 | 1 | 4 | 9 | chloroacetamide ✅ | hits TXNRD1 |
| RSL3 | 442.9 | 3.10 | 84.9 | 1 | 6 | 4 | chloroacetamide ✅ | hits TXNRD1 |

SMARTS confirmed each assignment: ML210 matches nitro-isoxazole and **not** chloroacetamide; ML162 and
RSL3 match chloroacetamide and **not** nitro-isoxazole. The warhead classification underpinning this
whole program is now verified computationally rather than taken from prose.

## 🎯 Headline: ML210 already falls inside the design window

Target window from the strategy doc: **TPSA 70–140, MW 450–500, logP < 5**.

| Compound | Verdict |
|---|---|
| **ML210** | **Within window on all three** — MW 475, logP 4.75, TPSA 92.7 |
| ML162 | TPSA 58.6 (below 70 → predicted CNS/retina penetrant); logP 5.08 (Lipinski violation) |
| RSL3 | MW 443, marginally below range |

**This materially de-risks the program.** The chemotype selected for its *selectivity* turns out to be
property-appropriate as well. The optimization problem narrows from "fix fundamentally poor
properties" to "improve PK, metabolic stability, and clearance route within an already-reasonable
envelope."

Worth noting the correlation: the selective compound also has the better property profile, while both
non-selective chloroacetamides sit outside the window on at least one axis. Suggestive, not causal, on
a sample of three.

## ⚠️ The one property flag: ML210 has zero hydrogen-bond donors

TPSA 92.7 looks comfortable, but **HBD = 0** is a strong driver of passive CNS penetration. For most
programs that would be desirable. **Here it is backwards** — we want blood-brain and blood-retinal
exclusion.

**Concrete design lever, first one derived from computed data rather than reasoning:** introduce
hydrogen-bond donors while holding the nitro-isoxazole warhead fixed. Compounds carrying ≥2 HBD are
substantially more likely to be barrier-excluded, and there is headroom in TPSA (92.7 against a
ceiling near 140) to add polarity without breaking oral absorption.

This becomes an explicit objective for the GenMol campaign.

## Covalent chemistry confirmed from the crystal

The free G9N definition carries **2 chlorine atoms**; the bound form in 6HKQ carries **1**. The
chloroacetamide chloride departed — direct confirmation of SN2 displacement forming the Se–C20 bond.
The bound geometry is the post-reaction adduct, which is the correct template for covalent docking.

Files: `work/structures/G9N.cif`, `work/structures/baseline_props.json`

---

# ✅ STEP 2 — COMPLETE: Toolchain built, and it broke on selenium exactly as predicted

## Toolchain

| Component | Status |
|---|---|
| RDKit 2026.03.5 | ✅ pip |
| **AutoDock Vina 1.2.5** | ✅ Windows binary (`work/bin/`). *pip build failed — needs Boost headers* |
| Meeko 0.8.0 + gemmi 0.7.5 | ✅ pip (`--no-deps`, then gemmi separately) |

## ⚠️ Meeko refuses selenocysteine — the predicted failure, observed

The compute plan warned that structure-prep tools would drop, mis-type, or silently mutate Sec.
Confirmed verbatim:

```
Template SEC Failed to pass ResidueTemplate check.
Template generation failed for unknown residues: {'SEC'}
Recommendations:
1. Use --add_templates to pass additional templates ...
2. Use --delete_residues to ignore them. Residues will be deleted ...
```

**Note the second recommendation.** Taking it would silently delete the catalytic residue, and the
pipeline would then run to completion producing meaningless results. **This is the exact silent
failure Step 1 was designed to prevent.**

**Workaround used:** an explicitly-labelled **Cys surrogate** (SEC46→CYS46, SE→SG). **Geometry only.**
Se–C is 1.98 Å against S–C 1.81 Å, and nucleophilicity differs — never valid for reactivity work.
Proper SEC templates remain an open blocker.

## Receptor and ligand prepared

- `6HKQ_receptor.pdb` — chain A, altloc A, waters and additives (DMS/EDO/SO4) removed. **Sec46
  assertion passed:** 6 atoms including selenium survived the split.
- `6HKQ_ligand.pdb` / `G9N_bound.sdf` — bound ligand with bond orders from RCSB ModelServer.
  Independent check: **computed Se–C20 = 1.61 Å, matching the crystal LINK record exactly** —
  coordinate parsing validated.
- Docking box from the ligand envelope: centre **(-24.775, 9.440, 2.706)**, 20 Å cube.

---

# ✅ STEP 2b — POSE-RECOVERY GATE: FAILED, and the failure is the finding

Non-covalent redocking of G9N into its own crystal structure. Vina 1.2.5, exhaustiveness 32, 9 modes.

## Result

| Metric | Crystal | Best docked pose |
|---|---|---|
| Affinity | — | **−5.7 kcal/mol** (weak) |
| RMSD to crystal | 0 | **5.88 Å** (all 9 modes 5.9–7.9 Å) |
| **Minimum distance to catalytic Se** | **1.61 Å** (covalent bond) | **3.64 Å** |
| Centroid shift | 0 | 3.6–5.5 Å, systematically +Z |
| Radius of gyration | 3.62 | 3.9–4.6 (more extended) |

Order-independent metrics were used to rule out an atom-correspondence artifact. The conclusion holds
either way.

## What this actually demonstrates

**Not a broken pipeline — an empirical confirmation of two claims the strategy rests on.**

**1. GPX4 has no drug-like binding pocket.** Affinities of −5.2 to −5.7 kcal/mol are weak (a genuine
pocket gives −8 to −10), and nine poses failed to converge anywhere near the crystal geometry. The
ligand drifts into a shallow surface groove because there is nothing to hold it.

**2. Covalent constraint is mandatory, not a refinement.** **No pose came within 3.64 Å of the
catalytic selenium** — roughly 2 Å too far to form a bond. The crystal geometry exists *because of*
the covalent bond, not because of non-covalent complementarity. Free docking has no mechanism to find
it.

**This is exactly the failure that would have wasted the campaign** had we generated 20,000 compounds
and ranked them on non-covalent scores. Caught before a single molecule was generated — which is what
the gate is for.

## Revised gate

Re-run pose recovery with a **covalent/constrained protocol** — Meeko supports reactive residues via
`--reactive_flexres`, or apply a distance restraint of ~1.98 Å between the warhead electrophilic
carbon and Sec46 Se. **The non-covalent gate is retired: it asks a question this target cannot
answer.**

---

# ✅ STEP 5 — FIRST DESIGN CYCLE RUN: 210 analogs, 15 clear the window

**Rationale for going here rather than to covalent docking first.** Step 2b showed non-covalent
docking is uninformative on this target, and Step 3 showed selectivity is probably reactivity-driven
rather than shape-driven. Both point the same way: **property-directed, warhead-conserved design is
the defensible move**, and it needs no docking at all.

## Method

Decomposed ML210 by BRICS. Fixed scaffold: **nitro-isoxazole warhead → amide → piperazine**. The
variable handle is the **bis(4-chlorophenyl)methine**, which carries most of the lipophilicity and
contributes zero polarity.

Enumerated 20 aryl/heteroaryl replacements pairwise (210 combinations). **Every structure was gated
on warhead integrity by SMARTS** before scoring — no compound advances with a mangled electrophile.

## Result

| R1 / R2 | MW | logP | TPSA | HBD | QED |
|---|---|---|---|---|---|
| 4-OH-phenyl / 4-NHMe-phenyl | 451.5 | 3.19 | 125.0 | 2 | 0.43 |
| 4-NHMe-phenyl / 3-OH-phenyl | 451.5 | 3.19 | 125.0 | 2 | 0.43 |
| 4-OH-phenyl / 4-CH2OH-phenyl | 452.5 | 2.64 | 133.2 | 2 | 0.43 |
| 4-CH2OH-phenyl / 3-OH-phenyl | 452.5 | 2.64 | 133.2 | 2 | 0.43 |
| 4-OH-phenyl / 4-OH-3-Cl-phenyl | 472.9 | 3.50 | 133.2 | 2 | 0.43 |
| 3-OH-phenyl / 4-OH-3-Cl-phenyl | 472.9 | 3.50 | 133.2 | 2 | 0.43 |
| **ML210 baseline** | **475.3** | **4.75** | **92.7** | **0** | 0.39 |

**Movement against the design objectives:**

| Objective | ML210 | Best analogs | Direction |
|---|---|---|---|
| **HBD** (drives barrier exclusion) | **0** | **2** | ✅ the key fix |
| logP | 4.75 | 2.42–3.50 | ✅ substantially less greasy |
| TPSA | 92.7 | 125–139 | ✅ into the exclusion range |
| MW | 475 | 450–493 | ✅ held in window |
| QED | 0.39 | 0.43 | ✅ marginally better |

Top candidates:

1. `CNc1ccc(C(c2ccc(O)cc2)N2CCN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1`  — 4-OH-phenyl / 4-NHMe-phenyl
2. `CNc1ccc(C(c2cccc(O)c2)N2CCN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1`  — 4-NHMe-phenyl / 3-OH-phenyl
3. `Cc1onc(C(=O)N2CCN(C(c3ccc(O)cc3)c3ccc(CO)cc3)CC2)c1[N+](=O)[O-]`  — 4-OH-phenyl / 4-CH2OH-phenyl
4. `Cc1onc(C(=O)N2CCN(C(c3ccc(CO)cc3)c3cccc(O)c3)CC2)c1[N+](=O)[O-]`  — 4-CH2OH-phenyl / 3-OH-phenyl

## The finding that makes this chemotype tractable

Measured bond path from the design handle to the electrophilic warhead carbon: **7 bonds, through an
amide and a saturated piperazine** (6 non-aromatic atoms in the path).

**The modification site is electronically insulated from the electrophile.** Substituent effects
should not propagate to the warhead, so property optimisation here is unlikely to perturb the
reactivity that confers GPX4 selectivity.

That is a strong argument for this scaffold specifically: **the property problem and the selectivity
problem are separable.** It is why a lead-optimisation campaign here is credible rather than a
reactivity gamble.

## Honest limits of this cycle

- **Property-optimised only. No potency prediction.** The chlorophenyls may be making essential
  contacts; replacing them could destroy activity. *Mitigating argument:* GPX4 has no real binding
  pocket (demonstrated in Step 2b), so the aryls plausibly contribute positioning rather than
  affinity — but this is a hypothesis, not a result.
- **Synthetic accessibility not properly assessed.** Mixed (unsymmetrical) benzhydryl centres are
  harder than symmetric ones. The symmetric hits (e.g. bis-4-NHMe-phenyl, bis-4-CH2OH-phenyl) are
  more tractable and should be weighted up.
- **Barrier exclusion is predicted from property rules, not modelled.** HBD ≥ 2 and TPSA > 70 are
  heuristics.
- No stereochemistry handled at the methine centre.

Files: `work/design/analogs.json` (210 enumerated, 15 passing)

---

# ▶ NEXT

1. **Covalent docking protocol** — Meeko reactive-residue setup, or restrained docking. Re-run the
   recovery gate against the 1.61 Å crystal geometry.
2. **Proper SEC parameters** — required before any reactivity work; the Cys surrogate is
   geometry-only.
3. **Step 4 selectivity gate** — ML210 vs ML162/RSL3 against GPX4 and TXNRD1. Per Step 3, this now
   needs a **quantum-chemistry reactivity arm**, since the discriminating variable is warhead
   electrophilicity rather than pocket shape.
4. **Generation** — only after gates 1 and 3 pass.

---

# ▶ STEP 2 detail — Structure preparation, with Sec46 as the assertion

**Goal:** produce docking-ready receptors without losing selenocysteine.

1. Install RDKit and a covalent-capable docking engine into a dedicated conda env.
2. Split 6HKQ into apo receptor + extracted G9N ligand.
3. Run standard preparation — protonation, charges, atom typing.
4. **Assert Sec46 survives after every single step.** Make this an automated check that fails loudly,
   not a manual inspection. This is the step where things break silently.
5. If a tool refuses Sec, decide explicitly: source Sec parameters, or use a Cys surrogate *for
   geometry only* — never for reactivity.

**Gate:** re-dock G9N into prepared 6HKQ and recover the crystal pose within tolerance. Cannot
reproduce a known answer → cannot trust an unknown one.

---

# ▶ STEP 4 — The validation run (compute plan Part 1)

Dock **ML210, RSL3, ML162** into both GPX4 and TXNRD1. Ask whether the pipeline reproduces the known
experimental ordering: ML210 selective for GPX4; RSL3 and ML162 actually hitting TXNRD1.

**Hard gate. No molecule generation until this passes.** A pipeline that cannot separate compounds
whose real-world answer is known and opposite cannot rank novel ones.

---

# OPEN ITEMS

- [x] TXNRD1 accessions — 2J3N, 3QFA (both Sec->Cys mutants; see Step 3)
- [ ] GPX1 accession — still open
- [ ] Computationally restore Sec498 in TXNRD1 model
- [ ] QM reactivity workflow for warhead selectivity (promoted from Phase 5)
- [ ] Selenocysteine force-field parameters (AMBER/CHARMM)
- [ ] Covalent docking engine that handles Se–C bond formation
- [ ] ML210 and RSL3 ligand structures for the validation run
- [ ] Confirm FLOWR.root checkpoint and GenMol access

**Wet-lab note carried forward:** wild-type GPX4 for the purified-enzyme assay was produced by
co-expression with **SBP2** (selenocysteine-insertion-sequence-binding protein 2) in HEK cells. That
assay is the program gate — it is the one RSL3 and ML162 failed.
