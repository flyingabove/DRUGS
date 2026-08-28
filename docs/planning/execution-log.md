# Execution Log — GPX4 Program

Live build log. Strategy: [../strategies/lsc-ferroptosis-hypothesis.md](../strategies/lsc-ferroptosis-hypothesis.md).
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

# ▶ STEP 2 — IN PROGRESS: Structure preparation

RDKit **2026.03.5** installed. Still needed: covalent-capable docking engine, selenocysteine
force-field parameters.

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
