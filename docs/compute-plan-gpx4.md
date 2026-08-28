# Compute Plan — GPX4 Inhibitor Design

Execution plan for the program in
[strategies/gpx4-dependency-aml.md](strategies/gpx4-dependency-aml.md). Assumes ample compute and
**no model training** — pretrained generators plus separate scoring and simulation.

---

# PART 0 — FRAME THE PROBLEM CORRECTLY FIRST

## This is constrained lead optimization, not de novo discovery

The instinct with a target-aware generative stack is to point it at a pocket and generate. **That is
the wrong default here**, and getting this wrong wastes the whole first campaign.

We already have a **validated chemotype**: ML210's nitroisoxazole / masked nitrile-oxide warhead is
the group that confers GPX4 selectivity, and replacing it yields less selective analogs. We are not
searching for a binder. We are optimizing a known-selective covalent binder for pharmacokinetics,
clearance route, and reversibility.

**Consequence for tool priority — this inverts the suggested stack:**

| Tool | Suggested role | **Revised role** |
|---|---|---|
| **GenMol** | Secondary | **PRIMARY** — fragment/scaffold manipulation is exactly the job. Hold the warhead fixed, redesign everything else. |
| **FLOWR.root** | Primary | **Secondary** — use for pocket-conditioned exploration of alternative binding modes, and as a source of chemically-distinct scaffolds |
| **DiffSBDD** | Easy baseline | **Agreed** — pipeline sanity check only |
| **TargetDiff** | Baseline | **Skip initially** — superseded by flow models; revisit only if the newer ones underperform |

## Five things that will break a standard SBDD pipeline on this target

These are GPX4-specific and none are handled by default tooling. Solve them in Phase 0 or the whole
campaign produces garbage.

### 1. Selenocysteine is a non-standard residue

The catalytic residue is **Sec46 (U)**, not cysteine. Most force fields, docking engines, PDB parsers,
and structure-prep tools do not recognize it. Expect silent failures: dropped atoms, mis-typed
residues, or auto-mutation to Cys.

**Mitigation:** obtain or build Sec parameters (AMBER/CHARMM), verify the residue survives every
preparation step, and explicitly confirm atom typing before running anything expensive. A Cys
surrogate is acceptable for *docking geometry* but **not** for reactivity modeling — selenium's
nucleophilicity is the entire mechanism.

### 2. This is covalent chemistry, and standard generators produce non-covalent binders

GPX4 has a **shallow active site with no drug-like binding pocket**. Non-covalent affinity is exactly
what fails here — which is why every real inhibitor is covalent.

**Mitigation:** the pipeline must be covalent from the start.
- Covalent docking: AutoDock4 covalent mode, CovDock-style protocols, or constrained docking with a
  distance restraint between the warhead electrophilic carbon and Sec46 Se.
- Generation must be **warhead-constrained** — fix the reactive group, vary the rest. GenMol's
  fragment conditioning is the natural fit.
- **Non-covalent docking scores are near-meaningless on this target.** Do not rank on them.

### 3. Pocket detection will underperform

Pocket-conditioned generators need a pocket. This one barely qualifies.

**Mitigation:** do not rely on automated pocket detection. Define the site from the **ML162-bound
covalent complex** and use the observed ligand envelope as the conditioning volume.

### 4. Selectivity is a multi-target problem, and the suggested pipeline is single-target

The failure that invalidated RSL3 and ML162 was off-target TXNRD1 inhibition. A single-target
pipeline cannot see that failure mode.

**Mitigation:** every scoring stage runs against a **panel**, not one protein — GPX4 (on-target),
plus TXNRD1, GPX1, and other selenoproteins as counter-targets. Rank on a **selectivity margin**, not
on-target score.

### 5. Clearance route is a property problem, not a docking problem

Hepatobiliary-vs-renal clearance and reversibility kinetics will never appear in a docking score.

**Mitigation:** a separate ADMET/property stage with explicit objectives, treated as a hard filter and
not a tiebreaker.

---

# PART 1 — THE FIRST EXPERIMENT SHOULD NOT BE GENERATION

**Highest-value first run: a retrospective selectivity analysis.**

We have an unusual gift — a labeled dataset of exactly the property we need to engineer:

| Compound | Warhead | GPX4 | TXNRD1 |
|---|---|---|---|
| **ML210** | Nitroisoxazole / masked nitrile-oxide | **Inhibits** | Selective against |
| **RSL3** | Chloroacetamide | Does **not** inhibit purified GPX4 | **Hits this instead** |
| **ML162** | Chloroacetamide | Does **not** inhibit purified GPX4 | **Hits this instead** |
| **HA344, #231** | (from the dual GPX4/TXNRD1 work) | Active in AML CD34+ | — |

**Run:** dock all four into both GPX4 and TXNRD1, covalently, with proper Sec parameters. Compute the
selectivity margin. Then ask: **does the computational pipeline reproduce the known experimental
answer?**

**Why this before generating anything:**
- If the pipeline cannot distinguish ML210 from ML162 — compounds whose real-world selectivity is
  known and opposite — then it cannot rank 20,000 novel compounds either. **This is the pipeline's
  validation gate.**
- It reveals the *structural determinant* of GPX4-vs-TXNRD1 selectivity, which becomes the design
  objective for everything downstream.
- It is cheap: four compounds, two targets.

**Do not proceed to production generation until this run reproduces the known ordering.**

---

# PART 2 — PHASED EXECUTION

## Phase 0 — Environment and target preparation

**Structures to obtain:**
- GPX4 apo
- **GPX4 covalently bound to ML162** — this defines the site geometry
- TXNRD1 (counter-target)
- GPX1 (counter-target, closest family member)
- FSP1 (for the parallel partner campaign, lower priority)

*Look up exact PDB accessions rather than assuming; do not proceed on a homology model where a
crystal structure exists.*

**Deliverables:**
- Sec46 parameters validated end-to-end
- Site definition derived from the covalent complex
- Counter-target structures prepared identically
- Conda environment: RDKit, docking engine, OpenMM, the generator stack

**Gate:** re-dock the ML162 crystal pose and recover it. If pose recovery fails, nothing downstream is
trustworthy.

## Phase 1 — Selectivity validation run (Part 1 above)

**Gate:** pipeline reproduces ML210-selective / ML162-non-selective ordering.

## Phase 2 — Pipeline shakedown with DiffSBDD

Agreed with the suggested approach: DiffSBDD is the fastest way to learn the input/output contract.
Feed it the GPX4 structure plus the ML162 reference ligand, generate a small set, push it through the
full downstream pipeline.

**Purpose is plumbing, not chemistry.** Expect the output to be non-covalent and largely unusable on
this target — that is fine and expected.

## Phase 3 — Production generation

Two complementary sources, as suggested, with the revised priority:

**GenMol (primary) — warhead-constrained scaffold optimization**
- Hold the nitroisoxazole warhead fixed as a required fragment
- Vary the scaffold and periphery
- Drive property controls (QED, logP) toward the **PSA and MW window** that steers clearance away from
  renal excretion
- Target volume: ~10–20k

**FLOWR.root (secondary) — pocket-conditioned exploration**
- Conditioned on the covalent-complex site definition
- Purpose: chemically distinct scaffolds and alternative binding modes GenMol will not reach from the
  ML210 starting point
- Post-process to graft the warhead where geometry permits
- Target volume: ~10k

**Why both:** the two draw from genuinely different distributions — one anchored in known chemistry,
one in pocket geometry. Betting on a single model family is the failure mode.

## Phase 4 — Triage

1. **RDKit** — validity, duplicates, descriptors, PAINS, synthetic accessibility
2. **Warhead integrity check** — reject anything where the reactive group was mangled during generation
3. **Covalent docking into GPX4** — with Sec46 restraint
4. **Counter-screen: covalent docking into TXNRD1 and GPX1**
5. **Rank on selectivity margin**, not on-target score

## Phase 5 — Property and clearance filtering (hard filter)

| Objective | Target | Why |
|---|---|---|
| Renal clearance avoidance | Steer toward hepatobiliary elimination | Kidneys concentrate what they excrete; this is the primary kidney-sparing lever |
| Covalent reactivity | Tuned — reactive enough for a shallow site, not promiscuous | Chloroacetamides were too indiscriminate |
| Reversibility | Reversible-covalent preferred | Enables differential recovery between doses |
| Standard ADMET | Solubility, permeability, hepatotoxicity flags | Table stakes |

**Reversibility is the hardest to predict computationally** and may need quantum-chemistry treatment
of the warhead–selenol adduct rather than an ML property model. Flag as a methods risk.

## Phase 6 — Simulation on survivors

- **MD (OpenMM/GROMACS)** on the covalent complex — stability of the adduct and the surrounding site
- **FEP** only on a small, focused set — expensive, and covalent FEP is non-trivial
- Prioritize on **relative selectivity** (GPX4 vs TXNRD1) over absolute affinity, since covalent
  potency is dominated by reactivity rather than binding

## Phase 7 — Wet-lab handoff specification

The computational campaign delivers a ranked, synthesizable list plus **the assay cascade the
compounds must clear**, in this order:

1. **Cell-free inhibition of purified GPX4.** *The gate.* This is precisely the assay RSL3 and ML162
   failed. Nothing advances without it.
2. **Counter-screen: TXNRD1 and glutathione reductase.** Established practice, described as
   imperative.
3. **Primary AML patient cells**, with the internal control that makes the result meaningful:
   **blast vs non-blast sensitivity in the same marrow sample**.
4. **CD34+CD38− LSC fraction specifically** — not bulk CD34+.
5. **Serial transplantation.** The one experiment that decides whether self-renewal is eliminated or
   cells are merely killed. Nothing computational substitutes for it.

---

# PART 3 — PARALLEL TRACK: THE FSP1 PARTNER

Lower priority. icFSP1 already exists with improved microsomal stability and in vivo activity, so
this is a *characterization* effort rather than a design effort.

**Useful compute:** model the GPX4-inhibitor / FSP1-inhibitor combination for
pharmacokinetic compatibility — matched exposure windows matter more than co-optimized potency, since
the two agents need to be present simultaneously.

---

# PART 4 — WHAT COMPUTE CANNOT DECIDE

Stating this plainly so the campaign is not oversold:

- **Whether ferroptosis eradicates leukemia-initiating capacity.** The decisive biological question.
  No simulation touches it.
- **The therapeutic index.** Never measured for any GPX4 inhibitor because none had adequate PK. A
  compound is required before the question can even be asked.
- **Whether the niche resupplies CoQ** and rescues LSCs via the FSP1 arm.
- **Covalent reactivity in a real proteome.** Predicted selectivity and measured proteome-wide
  reactivity diverge routinely.

**The campaign's honest deliverable:** a compound good enough to *ask* those questions. Nobody has had
one — that is the entire gap.

---

# PART 5 — OPEN ITEMS BEFORE STARTING

- [ ] Look up exact PDB accessions for GPX4 apo, GPX4–ML162, TXNRD1, GPX1
- [ ] Source or build validated selenocysteine force-field parameters
- [ ] Confirm which covalent docking engine handles Se–C bond formation properly
- [ ] Obtain ML210, RSL3, ML162 structures for the Phase 1 validation run
- [ ] Decide the reversible-covalent warhead strategy — reversibility may need QM, not ML
- [ ] Confirm FLOWR.root checkpoint version and GenMol access
