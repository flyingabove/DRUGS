# In-Silico Design Pipeline — Execution Plan

Status: DRAFT. Covers the **computational build** for Phases 1–3 of
[aml-lsc-drug-discovery-plan.md](aml-lsc-drug-discovery-plan.md). Does not cover Phase 0 (target
selection) or Phases 4–6 (wet lab) — those gate this work on both ends.

## 0. What This Doc Is For

Once a target is chosen, this is the machinery that turns "protein X" into "here are 20 molecules
worth synthesizing." It is deliberately built to be **stood up and validated before we have a
target**, using a known benchmark, so that the day a target is picked we already trust the pipeline.

**The deliverable is not molecules.** It is a short, defensible, synthesizable candidate set with a
written mechanistic rationale and a specific proposed experiment. 20 good candidates with a clear
test beat 20,000 ranked by docking score.

---

## 1. Gate Zero: Modality Decision

**This must be answered before any tool is installed.** The generative stack for a small molecule
and the stack for a biologic share almost nothing.

| Target under consideration | Class | Modality | Branch |
|---|---|---|---|
| CLL-1 (CLEC12A) | Cell-surface antigen | Biologic (ADC / bispecific / CAR) | **B** |
| CD123 (IL3RA) | Cell-surface receptor | Biologic | **B** |
| CD47 | Cell-surface PPI | Biologic | **B** |
| CXCR4 | GPCR | Small molecule *or* antibody | **A** or **B** |
| BCL-2 / MCL-1 | Intracellular PPI groove | Small molecule | **A** |
| Menin–KMT2A | Intracellular PPI pocket | Small molecule | **A** |
| GPX4 / FSP1 | Intracellular enzyme | Small molecule | **A** |
| DRD2 | GPCR | Small molecule | **A** |
| OXPHOS complex I | Membrane enzyme complex | Small molecule | **A** |

**Branch A — small molecule.** The stack in Section 4. Requires a real, druggable *pocket*.

**Branch B — biologic.** Entirely different tools: RFdiffusion / RFantibody for binder backbones,
ProteinMPNN for sequence design, BindCraft for end-to-end binder generation, Chai-1 / Boltz for
complex prediction and validation. **None of FLOWR / GenMol / DiffSBDD apply.**

> **Consequence worth stating plainly:** the epitope-editing strategy in
> [nuke-everything-and-replace.md](nuke-everything-and-replace.md) is *definitionally* Branch B —
> that doc's own hard constraint is "biologics only, because epitope editing defeats antibodies but
> not small molecules." If we go that route, the entire FLOWR / GenMol stack is the wrong purchase.

**Recommendation:** build Branch A first regardless. It is far better documented, cheaper to run,
and the benchmark protocol in Section 5 validates our *methodology* in a way that transfers. But do
not let tooling momentum silently pick the modality — that is a target decision, made in Phase 0.

### RESOLVED (loop 40): Branch A, covalent

[strategies/break-the-shield-gpx4.md](strategies/break-the-shield-gpx4.md) selects **GPX4 + FSP1**.
Both are intracellular enzymes → **Branch A confirmed**, and M5 is unblocked.

Three consequences that reshape the rest of this doc:

1. **The program is covalent.** The stack in Section 4 is non-covalent by default. See Section 4b.
2. **The counter-screen targets are now concrete**, not hypothetical: **TXNRD1** first — it is the
   off-target that invalidated RSL3/ML210 — plus the wider selenoproteome and the GPX1–8 family.
3. **The pocket is bad.** GPX4 has a shallow active site with no drug-like pocket. Pocket-conditioned
   generators (FLOWR.root, DiffSBDD) are trained overwhelmingly on well-formed pockets. Expect
   degraded performance and validate against that specifically, not against an easy pocket.

---

## 2. Hardware Reality Check

**Titan Xp: 12 GB VRAM, Pascal (sm_61, 2017).** Specific limitations that will bite:

- **No usable FP16.** Titan Xp half-precision throughput is 1/64 of FP32. Mixed-precision paths that
  speed up modern cards will *slow this one down*. Run FP32.
- **No bf16, no tensor cores, no FlashAttention** (needs sm_80+). Transformer-heavy models fall back
  to slow attention paths.
- **12 GB is the binding constraint** for co-folding on large complexes.

| Stage | Titan Xp verdict |
|---|---|
| RDKit, descriptors, filtering | Fine (CPU anyway) |
| DiffSBDD / TargetDiff generation | Fine — these are small EGNNs |
| GenMol inference | Fine |
| REINVENT4 goal-directed optimization | Fine |
| ADMET-AI, Chemprop property models | Fine |
| Docking (Vina / smina / gnina) | **CPU-bound — core count matters far more than the GPU** |
| FLOWR.root | Marginal; expect small batches |
| Boltz-2 co-folding + affinity | Marginal to inadequate on large complexes |
| MD (OpenMM) | ~10x slower than a modern card; fine for short runs, painful beyond ns |
| FEP | **Not viable.** Do not attempt locally |

**Do not buy hardware yet.** Run everything above the line locally; burst-rent an A100/H100 hourly
(RunPod, Lambda, Vast.ai) for co-folding and MD. Those are episodic workloads measured in hours per
campaign, not continuous. Rent before you buy — we do not yet know which stage is our bottleneck.

### Environment: use WSL2, not native Windows

**This is the highest-value setup decision in the doc.** Every repo in this stack ships Linux conda
environments and depends on `torch-scatter` / `torch-cluster` / `torch-geometric` compiled
extensions, which are a persistent build problem on native Windows. GROMACS and gnina are
effectively Linux-only.

WSL2 supports CUDA passthrough. Install Ubuntu 22.04 under WSL2, install the CUDA toolkit inside it,
and treat Windows as the host OS only. Expect this to take a day and to save weeks.

---

## 3. The Revised Pipeline (Branch A)

The proposed flow, with the four gaps closed. **Additions in bold.**

```
                        TARGET (from Phase 0)
                              |
                              v
              ** STRUCTURE ACQUISITION **
        PDB if available -> else Boltz-2 / Chai-1 / AF3
        ** pocket detection + druggability scoring **
        ** GATE: is there a real pocket? If no -> Branch B **
                              |
              +---------------+---------------+
              v                               v
         FLOWR.root                        GenMol
    pocket-conditioned 3D            fragment / scaffold
              +---------------+---------------+
                              |
                    ** + REINVENT4 **
              goal-directed RL, closes the loop
              on whatever we actually score for
                              |
                              v
                            RDKit
              validity / dedup / descriptors / PAINS
                              |
                              v
            ** SYNTHESIZABILITY GATE (hard) **
              SA score -> RAscore -> AiZynthFinder
              no route, no candidate
                              |
                              v
                       pose generation
                  smina / gnina (CNN rescoring)
                              |
                              v
              ** AFFINITY RANKING (not docking) **
                    Boltz-2 predicted affinity
                              |
                              v
            ** SELECTIVITY COUNTER-SCREEN **
        same scoring against paralogs / anti-targets
        ** this is the project's core problem, not a filter **
                              |
                              v
              ** ADMET / DEVELOPABILITY **
              ADMET-AI: hERG, CYP, solubility, clearance
                              |
                              v
                  MD stability (OpenMM, rented)
                              |
                              v
              FEP — congeneric series ONLY, at lead-op
                              |
                              v
                    20–50 candidates + rationale
```

---

## 4. Stage-by-Stage Tool Selection

| Stage | Tool | License | Why this one |
|---|---|---|---|
| Structure | **Boltz-2** | MIT | Co-folds the complex *and* predicts affinity. Open weights. The most valuable single addition to the original framework |
| Structure (alt) | Chai-1 / AF3 | Varies — **check terms** | Cross-check Boltz-2. AF3 weights carry non-commercial restrictions |
| Pocket detection | fpocket, P2Rank | Open | Cheap, fast, decides Gate Zero |
| 3D generation | **FLOWR.root** | Check | Pocket-conditioned; ships checkpoint + tutorial |
| Fragment generation | **GenMol** | NVIDIA — **check terms** | Scaffold hopping and lead optimization |
| Baseline | **DiffSBDD** | MIT | Easiest first run. Use to learn the I/O contract, then keep as a sanity baseline |
| **Goal-directed opt** | **REINVENT4** | Apache 2.0 | *Missing from the original framework.* Diffusion generators are one-shot; REINVENT4 optimizes against our actual composite score, including selectivity. This is the workhorse |
| Cheminformatics | RDKit | BSD | Non-negotiable |
| **Synthesizability** | **AiZynthFinder** | MIT | *Missing.* SA score is a weak heuristic; this does real retrosynthesis against purchasable stock |
| Docking / pose | smina, **gnina** | Apache / GPL | gnina CNN rescoring beats Vina scoring. Use for *pose*, not ranking |
| **Affinity ranking** | **Boltz-2** | MIT | Replaces docking score as the ranking signal |
| **ADMET** | **ADMET-AI** | MIT | *Missing.* Fast, broad; catches hERG / CYP liabilities early |
| MD | OpenMM | MIT | Python-native, best WSL2 experience. Skip GROMACS |
| FEP | OpenFE | MIT | Lead-op only, rented compute only |

### Branch B additions (if modality goes biologic)

| Stage | Tool |
|---|---|
| Binder backbone | RFdiffusion / RFantibody |
| Sequence design | ProteinMPNN |
| End-to-end binder | BindCraft |
| Complex validation | Boltz-2, Chai-1 |
| Developability | TAP metrics, aggregation / immunogenicity predictors |

### 4b. Covalent lane — required by the GPX4 target choice

**The entire stack in Section 4 assumes non-covalent binding. Our program is covalent.** This is not
a tweak; it breaks three stages.

| Broken stage | Why | Fix |
|---|---|---|
| **Generation** | FLOWR.root, DiffSBDD, TargetDiff and GenMol are trained on non-covalent complexes. They will not place a warhead for attack on a specific residue, and they have no notion of reaction geometry | Generate the recognition scaffold, then **enumerate warheads combinatorially** onto it as a separate step. Constrain to a curated warhead set (see below) |
| **Docking** | Standard Vina/smina/gnina produce non-covalent poses. A covalent ligand's pose is constrained by the bond to the residue | **Covalent docking**: AutoDock-Vina covalent mode, or RxDock/AutoDock4 covalent protocols. Anchor to GPX4's catalytic **Sec46** |
| **Affinity ranking** | Covalent potency is *kinetic* (k_inact/K_I), not a single binding constant. Boltz-2 and every affinity predictor here estimate non-covalent ΔG | Rank on the **non-covalent recognition step** (K_I) with these tools; treat warhead reactivity as a separate, orthogonally-scored axis |

**Warhead strategy.** Part 7 of the strategy doc specifies **masked nitrile-oxide electrophiles** over
chloroacetamides, and a **reversible-covalent** mechanism. Both are constraints on warhead choice, so
build a small curated warhead library up front (reversible-covalent classes: cyanoacrylamides,
α-cyanoacrylates, activated nitriles, plus the masked nitrile-oxides) and enumerate rather than
generate. Reactivity should be estimated separately — quantum-chemical electrophilicity descriptors
or a trained reactivity model — because it is the axis that determines both potency *and*
proteome-wide promiscuity, and no generative model here scores it.

**Selectivity is the whole program here.** For a covalent agent, selectivity is not a docking
question — it is a question of which other nucleophilic residues in the proteome get hit. Structural
counter-screening against TXNRD1 and the selenoproteome is necessary but *not sufficient*; the real
readout is chemoproteomic (ABPP), which is wet-lab. Scope the in-silico claim honestly: we can
propose selective candidates, we cannot demonstrate selectivity computationally.

> **Verify before installing.** Several claims above — FLOWR.root checkpoint version, GenMol license
> terms, current Boltz-2 capabilities, current best covalent-docking tooling — come from a
> fast-moving field. Run `/research-loop` on this doc to confirm versions, licenses, and whether
> anything newer has displaced these choices before committing setup time.

---

## 5. Benchmark-First Protocol — Do This Before Any Real Target

**The single most important section in this doc.** A generative pipeline that has never been
validated produces confident, plausible, wrong answers, and we will not be able to tell.

So: before pointing it at a novel target, point it at one where we already know the answer.

### The benchmark target: BCL-2, with BCL-xL as the anti-target

Close to a perfect test case, because it *is* our problem in miniature:

- Rich structural data (many PDB entries, co-crystals with known ligands)
- Abundant known actives (venetoclax, navitoclax, and analog series)
- **Built-in selectivity challenge with a known clinical answer.** Navitoclax hits both BCL-2 and
  BCL-xL; BCL-xL inhibition kills platelets, causing dose-limiting thrombocytopenia. Venetoclax was
  deliberately engineered to spare BCL-xL. That is a documented real-world selectivity-engineering
  problem with a known correct outcome
- It sits inside our own project scope (Idea 2 in [brainstorm-topics.md](brainstorm-topics.md))

**If the pipeline can recover BCL-2-selective-over-BCL-xL chemistry, it has demonstrated exactly the
capability this project needs.** If it cannot, nothing downstream is trustworthy.

### Acceptance criteria — write these down before running

1. **Enrichment.** Seed known actives among decoys; the pipeline must rank actives well above
   chance. Use **LIT-PCBA** (experimentally validated inactives) rather than DUD-E — models are
   known to learn DUD-E decoy-construction artifacts rather than binding.
2. **Selectivity discrimination.** Scoring must separate BCL-2-selective compounds from dual
   BCL-2/BCL-xL compounds. If it cannot, our selectivity counter-screen is decorative.
3. **Pose accuracy.** Redock known co-crystal ligands; RMSD < 2 Å against the crystal pose.
4. **Synthesizability honesty.** What fraction of generated molecules get a real AiZynthFinder
   route? Expect this to be brutal. Record the number — it calibrates everything after.
5. **Novelty vs. memorization.** Are outputs genuinely novel, or lightly perturbed training-set
   molecules? Check Tanimoto similarity against ChEMBL and the generators' training sets.

### Second benchmark: BTK, for covalent selectivity

BCL-2/BCL-xL tests *paralog* selectivity in a non-covalent PPI groove. Our program is covalent
against a shallow site — a different capability, so it needs its own test.

**BTK is the closest available analogue with a known answer.** Ibrutinib is a covalent BTK inhibitor
whose off-target covalent hits (EGFR, TEC-family kinases) drive its characteristic toxicities;
acalabrutinib and zanubrutinib were deliberately engineered for covalent selectivity against exactly
those off-targets. Solved structures, known actives, documented selective/promiscuous pairs.

That maps one-to-one onto strategy doc design constraint #5 — "potent enough for a shallow pocket,
selective enough to avoid proteome-wide covalent promiscuity." **If the covalent lane can separate
acalabrutinib-like selectivity from ibrutinib-like promiscuity, it can be trusted on GPX4 vs.
TXNRD1. If it cannot, the counter-screen is theater.**

| Benchmark | Capability tested | Known answer |
|---|---|---|
| BCL-2 / BCL-xL | Paralog selectivity, non-covalent, shallow groove | Venetoclax spares BCL-xL; navitoclax does not |
| **BTK / EGFR+TEC** | **Covalent warhead selectivity** | **Acalabrutinib selective; ibrutinib promiscuous** |

**Gate: do not run a real campaign until criteria 1–3 pass on both benchmarks.** Budget 3–5 weeks.
This is not a detour; it is what makes the rest of the project mean anything.

---

## 6. Why the Original Framework's Ranking Step Will Not Work

Recorded explicitly, since it is the most likely way we waste months.

**Docking scores do not rank affinity.** Correlation with experimental binding is roughly r ≈ 0.3–0.4
across benchmarks. Docking is genuinely good at *pose generation* — where the ligand sits — and
genuinely bad at *scoring* — how tightly it binds. A pipeline that generates 20k molecules and sorts
by Vina score has produced a sorted list of noise, and the top of that list is enriched for molecules
that exploit the scoring function's blind spots (large, greasy, high-contact-area compounds), not
for binders.

**FEP cannot rescue this.** FEP computes the free-energy difference between *similar* molecules by
morphing one into another. It is accurate (~1 kcal/mol) but valid only within a congeneric series —
same scaffold, small substituent changes. You cannot FEP a diverse generated library against itself.
It belongs at lead optimization, after a series is chosen, on rented compute.

**Mitigation, in order of value:**

1. Rank with a learned affinity predictor (Boltz-2), not a docking score
2. Use consensus — agreement across gnina CNN + Boltz-2 + a Chemprop model beats any single score
3. Weight *selectivity margin* over absolute predicted potency. A predicted 100 nM binder with 50x
   selectivity is worth more to this project than a predicted 1 nM binder with none
4. Treat all scores as triage, never as truth. The output is a hypothesis list for a wet lab

---

## 7. Milestones

| # | Milestone | Gate to pass | Est. |
|---|---|---|---|
| M0 | WSL2 + CUDA + conda working; RDKit and DiffSBDD run end-to-end on the tutorial complex | Generate a valid .sdf from a .pdb | 2–4 days |
| M1 | Full Branch A stack installed **+ covalent lane (Section 4b)**; each tool runs standalone | Every tool produces expected output on its own example | 2–3 weeks |
| M2 | Pipeline wired end-to-end, automated | One command: pocket in → ranked candidates out | 1–2 weeks |
| M3 | **BCL-2 benchmark passes criteria 1–3** | See Section 5. **Hard gate** | 2–4 weeks |
| M4 | **BTK covalent-selectivity benchmark passes** | Separates acalabrutinib-like from ibrutinib-like. **Hard gate** | 1–2 weeks |
| M5 | ~~Phase 0 delivers a target~~ **DONE — GPX4/FSP1, Branch A covalent** | Gate Zero answered | ✅ loop 40 |
| M6 | GPX4 structure prep + TXNRD1/selenoproteome counter-screen panel assembled | Sec46 covalent anchor validated; redock ML162 co-crystal | 1 week |
| M7 | First real campaign | 20–50 candidates with routes + rationale | 2–4 weeks |

M0–M4 are **not blocked on further research** and can start now. M6 is data work and can run in
parallel with installation.

**Do M3 and M4 honestly.** The temptation with a target already chosen is to skip validation and go
straight to GPX4. Resist it — GPX4 is a shallow, pocket-less, covalent target, i.e. the hardest case
for every tool in this stack. A pipeline that has not been shown to work on easy targets will
certainly not work on this one, and we will not be able to tell the difference between a good
candidate and a hallucination.

---

## 8. Risks

- **Modality mismatch.** We build the small-molecule stack, Phase 0 picks CLL-1, and none of it
  applies. *Mitigation:* Gate Zero; treat M0–M4 as methodology validation whose real value is the
  benchmark discipline, which transfers to Branch B.
- **Benchmark passes, real target fails.** BCL-2 is data-rich; a novel target will not be.
  Performance will degrade and we will not know by how much. *Mitigation:* prefer targets with
  experimental structures and some known ligands. Treat "no known ligand, predicted structure only"
  as a materially harder problem, not an equivalent one.
- **Synthesizability collapse.** A plausible outcome is that <5% of generated molecules have a real
  route. *Mitigation:* measure it at M3; if dire, switch to synthesis-constrained generation
  (building-block + validated-reaction enumeration) rather than filtering after the fact.
- **No wet lab.** Everything here terminates in an untested hypothesis. *Mitigation:* scope the
  output to what a CRO can actually take — synthesizable compounds, a defined assay, a defined
  selectivity readout. CRO synthesis plus a CFU / LTC-IC selectivity assay is the real Phase 4
  unlock and should be costed early.
- **Compute underestimation.** MD and co-folding costs may dominate. *Mitigation:* rent, measure,
  then decide on hardware.

---

## 9. Immediate Next Actions

1. **Install WSL2 + Ubuntu 22.04 + CUDA.** Everything else blocks on this.
2. **Run DiffSBDD on its tutorial complex.** Cheapest possible end-to-end understanding of the
   input/output contract.
3. **Run `/research-loop` on this doc** to verify tool versions, licenses, and whether anything has
   displaced these choices.
4. **Set up the BCL-2 benchmark** — pull PDB structures, assemble the known-actives set, obtain the
   LIT-PCBA slice. Do this while installing, since it is data work, not compute work.
5. **Do not evaluate tools past M1** until the benchmark says the methodology works.

## Related Docs

- [aml-lsc-drug-discovery-plan.md](aml-lsc-drug-discovery-plan.md) — parent plan; this doc expands Phases 1–3
- [problem-definition.md](problem-definition.md) — what we are solving
- [challenges.md](challenges.md) — Challenge #1 (selectivity) is what Section 5's counter-screen exists to address
- [nuke-everything-and-replace.md](nuke-everything-and-replace.md) — the Branch B strategy
- [brainstorm-topics.md](brainstorm-topics.md) — candidate ideas feeding Gate Zero
