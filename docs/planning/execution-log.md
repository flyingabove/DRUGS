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

# ▶ STEP 2 — NEXT: Structure preparation, with Sec46 as the assertion

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

# ▶ STEP 3 — Counter-target structures

Still to resolve: **TXNRD1** and **GPX1** accessions. Required before any selectivity scoring —
ranking on on-target score alone reproduces exactly the failure that invalidated RSL3 and ML162.

---

# ▶ STEP 4 — The validation run (compute plan Part 1)

Dock **ML210, RSL3, ML162** into both GPX4 and TXNRD1. Ask whether the pipeline reproduces the known
experimental ordering: ML210 selective for GPX4; RSL3 and ML162 actually hitting TXNRD1.

**Hard gate. No molecule generation until this passes.** A pipeline that cannot separate compounds
whose real-world answer is known and opposite cannot rank novel ones.

---

# OPEN ITEMS

- [ ] TXNRD1 and GPX1 PDB accessions
- [ ] Selenocysteine force-field parameters (AMBER/CHARMM)
- [ ] Covalent docking engine that handles Se–C bond formation
- [ ] ML210 and RSL3 ligand structures for the validation run
- [ ] Confirm FLOWR.root checkpoint and GenMol access

**Wet-lab note carried forward:** wild-type GPX4 for the purified-enzyme assay was produced by
co-expression with **SBP2** (selenocysteine-insertion-sequence-binding protein 2) in HEK cells. That
assay is the program gate — it is the one RSL3 and ML162 failed.
