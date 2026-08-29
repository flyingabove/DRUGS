---
name: drug-simulation
description: Computational drug design workflow — structure prep, docking, QM/xTB reactivity, conformer analysis, property optimisation, and the specific traps that silently produce garbage. Use when designing or optimising a small molecule against a protein target, running docking or QM, or evaluating candidate compounds.
---

# Drug Simulation

Hard-won workflow from the GPX4 campaign. **Most of the value here is the traps** — every one of these
silently produced plausible-looking wrong answers before being caught.

Tooling that works: `rdkit` (pip), `xtb` (conda-forge, GFN2 semiempirical QM), AutoDock Vina
(download the binary — the pip build needs Boost headers), `meeko` + `gemmi` (pip, `--no-deps` then
gemmi separately).

---

## RULE 1 — Assert the catalytic residue survives every preparation step

**The single highest-value check.** Non-standard residues (selenocysteine, phosphorylated residues,
modified bases) are silently dropped, mis-typed, or auto-mutated by structure-prep tools.

Meeko refused selenocysteine outright and *offered to delete it*:

```
Template generation failed for unknown residues: {'SEC'}
Recommendations: ... 2. Use --delete_residues to ignore them.
```

Taking that suggestion removes the catalytic residue, and **the pipeline then runs to completion
producing meaningless results.**

- Make it an **automated assertion after every step**, failing loudly. Never a manual eyeball.
- Check the PDB actually contains the real residue, not a surrogate — many deposited structures use
  Sec→Cys or similar mutants for expression convenience. Grep for the element (`SE`), read `SEQADV`.
- If you must use a surrogate, label it in the filename and **restrict it to geometry**. Never
  reactivity: Se–C is 1.98 Å vs S–C 1.81 Å, and nucleophilicity differs.

## RULE 2 — Check that reference compounds hit their nominal target

Before trusting any literature chemotype, search for whether it was validated **cell-free against
purified protein**.

RSL3 and ML162 are the field-standard "GPX4 inhibitors". They **do not inhibit purified GPX4** — they
hit TXNRD1. Years of downstream work inherited the misattribution. Imetelstat had the same problem in
the same research run.

Also: **do not confuse similar compound codes.** ML162 is misattributed; ML210 is genuinely selective.
One character.

## RULE 3 — Diagnose the site before designing for it

Run these three before generating a single molecule. Each is cheap and each can redirect the campaign.

**Per-atom burial of a known ligand** — 1.4 Å probe against the receptor, per ligand atom.
Tells you which parts of the molecule actually touch protein. In the GPX4 case the warhead was 0.90
buried while the distal aryls were 0.06–0.17 — **so the region we wanted to modify made almost no
contact**, which justified the whole design strategy structurally.

**Grid-map the accessible volume around the anchor atom.** Only 26 Å³ within 5 Å of the catalytic
selenium, against ~400 Å³ molecules. **Conclusion: affinity is not the optimisation axis** — there is
no pocket to fill. That single number reframed the programme from shape-fitting to reactivity.

**Redock the crystal ligand into its own structure.** If you cannot reproduce a known answer, nothing
downstream is trustworthy.

## RULE 4 — A failed docking run is a diagnosis, not a bug

Non-covalent redocking of a covalently-bound ligand gave −5.7 kcal/mol (weak), RMSD 5.9–7.9 Å across
nine modes, and **no pose within 3.64 Å of the catalytic atom** — about 2 Å too far to bond.

That is not a broken pipeline. It is proof that **the crystal geometry exists because of the covalent
bond, not because of shape complementarity**, and that non-covalent scores are meaningless on this
target. Had 20,000 generated compounds been ranked on those scores, the campaign would have been
worthless.

**Weak scores plus non-convergence across all modes = no real pocket.** Read it as information.

Use order-independent metrics (centroid, radius of gyration, minimum distance to the anchor atom) to
rule out atom-correspondence artifacts before concluding.

## RULE 5 — 2D descriptors lie about polarity; simulate in water

**The single most valuable routine check.** TPSA and HBD counts assume donors are solvent-exposed.
They frequently are not.

Two candidates scored identically — same composite score, TPSA within 0.7 Å², both HBD=2. After
GFN2-xTB optimisation in implicit water (ALPB), one had **zero free donors**: both hydroxyls folded
back onto internal acceptors. In solution it behaved as HBD-zero — **exactly the liability the redesign
existed to fix.**

Protocol: 25–40 conformers → MMFF minimise → lowest-energy conformer → `xtb --gfn 2 --opt --alpb water`
→ count polar hydrogens with an N/O acceptor at 1.5–2.6 Å (masked) versus none (free).

**Report free HBD, never the 2D count.** Also check radius of gyration for conformational collapse.

## RULE 6 — Prove electronic insulation before optimising a covalent scaffold

When modifying a molecule that carries a reactive warhead, **measure whether the warhead notices.**

Compute the bond path from the modification site to the electrophilic atom, then compare full-molecule
LUMO before and after. A shift of +0.054 eV across 7 bonds (amide + saturated piperazine) proved the
LUMO — the warhead-localised acceptor orbital — was unmoved while only the ligand-localised HOMO
shifted. **That is the signature of insulation, and it converts "properties and reactivity are
separable" from an assertion into a measurement.**

Re-check on any further growth: larger substituents gave −0.32 eV, still modest but no longer
negligible.

## RULE 7 — Frontier-orbital gap analysis cannot compare warheads

Tempting and structurally useless:

```
preference = gap(Nu1) − gap(Nu2) = (LUMO − HOMO_1) − (LUMO − HOMO_2) = HOMO_2 − HOMO_1
```

**The warhead LUMO cancels.** The answer is fixed by the nucleophiles alone, identical for every
warhead. Selectivity between electrophiles requires **reaction energetics or transition-state
barriers**, not descriptors.

And gas-phase or implicit-solvent small models omit the protein — but electrostatic polarisation by
the active site is decisive for barrier heights and selectivity. **QM/MM is the real answer**
(it is how nirmatrelvir was designed; barriers 12–18 kcal/mol). QM/ML hybrids trained on QM descriptors
are the cheaper credible option.

## RULE 8 — Structural-alert filters miss metabolically liberated toxicophores

A filter applied to the parent structure sees only what is drawn.

**4-NHCOMe scored top of an 8-compound screen. It is an acetanilide — hydrolysed in vivo to the free
aniline**, the quinone-imine toxicophore the earlier cycle had explicitly excluded. Paracetamol
hepatotoxicity runs through exactly this.

Screen for **what the molecule becomes**, not only what it is: acetanilides → anilines; esters →
acids/alcohols; nitro → hydroxylamines; benzylic positions → hydroxylated.

## RULE 9 — An alert that fires on the scaffold is not an alert

A `basicN` SMARTS matched the **core piperazine**, present in the parent drug and every analog. The
screen returned **zero candidates** and looked like a legitimate result.

**Always sanity-check a filter against the parent compound.** If the parent fails your filter, the
filter is wrong.

## RULE 10 — Charge dictates clearance route and therefore organ exposure

Do not optimise polarity blindly. Ionisation state decides which organ concentrates the drug.

| Character | Clearance | Organ risk |
|---|---|---|
| Small, polar, neutral | Renal filtration | Kidney concentrates it in the proximal tubule |
| **Anionic** | Hepatic OATP uptake — *but* renal **OAT1/OAT3 pump it into tubule cells** | Classic anionic nephrotoxicity (cidofovir, adefovir) |
| **Cationic** | **OCT2 concentrates in the same tubule** | cisplatin, metformin |
| Large (>500 Da), amphipathic, **neutral** | **Hepatobiliary** | Avoids the tubule |

In the GPX4 case an acid initially looked ideal — biliary uptake plus near-total CNS exclusion from
the charge. It was a trap: it would have actively delivered a GPX4 inhibitor into the proximal tubule,
which is exactly where GPX4 loss causes acute renal failure.

**Barriers are also not equivalent.** Brain has tight junctions and efflux — a true barrier. Bone
marrow is sinusoidal and fenestrated — no barrier, only perfusion limits. **Polarity that excludes a
drug from brain does not exclude it from marrow.**

## RULE 11 — Recognise when simulation saturates, and stop ranking

Eight candidates: all zero intramolecular H-bonds, all 2 free donors, ΔLUMO spread **0.024 eV**.

That spread is noise. Ranking on it is false precision — and doing so put an acetanilide first.

**When the discriminating metric collapses to noise, the simulation has answered its question**
(here: the amide fragment class solves masking). Selection then belongs to medicinal chemistry —
metabolic stability, synthetic symmetry, lipophilicity — not to another decimal place.

## RULE 12 — Always run a positive control through your docking protocol

Three anchored-docking attempts failed. The second rejected **ML210, a compound known to bind**, as
firmly as the novel candidate — 0 clash-free poses out of 1,860 for both. A method that rejects the
positive control is broken, and its verdict on your candidate is worthless.

**Run the reference ligand through every scoring protocol before trusting it on anything new.**

## RULE 13 — Straight-ray accessibility is the wrong test for a surface groove

A probe requiring an unobstructed straight line from the anchor atom outward found **zero open exit
vectors in the very crystal structure that contains a covalently bound ligand.** That is a
contradiction, and it means the test measured the wrong thing.

Ligands bend. Grooves curve. Straight-ray channel-finding suits buried pockets with a mouth; it fails
completely on shallow curved surfaces.

**Use per-atom burial of a known ligand instead** — it is order-independent, needs no sampling, and it
answered the question the ray-casting could not.

## RULE 14 — For covalent targets, start from the bonded state

Pose *prediction* is the hardest part and the least necessary. If a covalent complex exists, build the
bond and run MD from there. That sidesteps docking entirely and directly answers whether substituents
are accommodated.

Reserve docking for cases where you genuinely do not know where the ligand sits.

## RULE 15 — Exclude covalent bonding partners from clash tests

A constant, plausible **1.16 Å overlap** appeared for every molecule, every conformer count, every
sampling scheme. Identical results across chemically different molecules is an artifact, not a result.

```
required C...Se separation in the clash test = 1.70 + 1.90 - 0.5 = 3.10 A
actual covalent Se-C bond length             = 1.98 A
registered overlap                           = 1.12 A
```

**The test was scoring the covalent bond itself as a clash.** The anchor residue sat in the receptor
array, and the bonded ligand atom is necessarily ~2 Å away.

Exclude the anchor residue sidechain (the bonded atom and its neighbour) from the steric test. **More
sampling cannot fix a mis-specified objective** — three rounds of "add more conformers" left the
number untouched, which was itself the clue.

## RULE 16 — A positive control turns a raw number into a verdict

The same control did decisive work twice, in opposite directions:

- **Exposing a broken method:** anchored docking rejected ML210 — a known binder — as firmly as the
  novel candidate. Verdict on the candidate: worthless.
- **Making a working method interpretable:** the ligand actually present in the crystal scored a
  residual overlap of **0.55 Å**. That *calibrates the scale* — 0.55 Å is demonstrably tolerable,
  because a molecule scoring it is sitting in the structure. The candidate at 0.42 Å is therefore
  fine, and ML210 at 0.39 Å indistinguishable from it.

Without the control, 0.42 Å is an uninterpretable number. With it, it is a pass.

**Never run a scoring protocol without putting a known binder through it first.**

---

## Standard cascade

1. Fetch structures; **verify the catalytic residue is real**, check `SEQADV` for engineered mutations
2. Split receptor/ligand with an **assertion** the residue survived; note altloc occupancies and choose deliberately
3. Extract covalent geometry from `LINK` records; verify by computing the distance yourself
4. **Diagnose the site** — burial, pocket volume, pose recovery
5. Decompose the reference ligand (BRICS); fix the pharmacophore/warhead, identify the variable handle
6. Enumerate; **gate every structure on warhead integrity by SMARTS**
7. Score against an explicit target profile; **sanity-check filters against the parent**
8. **xTB in implicit water** on the shortlist — free HBD, conformational collapse, ΔLUMO
9. Screen for metabolic liberation, not only parent-structure alerts
10. Stop when the metric saturates; decide the rest on chemistry
11. Record what was **not** established — potency almost always remains unaddressed
