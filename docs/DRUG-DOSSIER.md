# GPX4-M3 — Complete Dossier

**Everything in one place: the molecule, every test run on it, the treatment plan, and how it would be
delivered.** Written for a reader who is not a biologist.

---

# PART 1 — THE MOLECULE

## 1.1 What it is

```
SMILES:  CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1
```

**In words:** three pieces bolted together.

1. **The warhead** — a small reactive ring (a nitro-isoxazole) that is *chemically disguised*. It does
   nothing until it quietly falls apart inside a cell and exposes a sticky, reactive tip.
2. **The linker** — a six-membered ring containing two nitrogens, one of which is deliberately tied up
   in an amide so it carries no charge.
3. **The two arms** — a matched pair of flat rings, each carrying a small amide group. These do the
   heavy lifting on solubility and safety and touch nothing on the protein.

**It is ML210** — a known laboratory compound — **with both chlorine-bearing arms replaced and the
linker rebuilt.** The warhead is untouched, atom for atom. That is deliberate: the warhead is what makes
it work and what makes it selective, so it was left alone.

## 1.2 Properties

| Property | Value | Why it matters |
|---|---|---|
| Formula / mass | C₂₇H₂₈N₆O₇ / 534.5 | Normal drug size |
| Greasiness (cLogP) | **1.68** | ML210 is 4.75. Lower is better for a drug you inject daily |
| Charged groups | **none** | Charged drugs get trapped in the kidney and concentrated there |
| Heart-rhythm risk pattern | **absent** | The chemical pattern that causes it needs a charged nitrogen. We removed it |
| Mirror-image forms | **none** | Symmetry means no left/right-handed versions to separate. Halves the manufacturing and safety work |
| Ease of synthesis | **2.65 / 10** | Easy end of the scale |
| Solubility | **~0.03 mg/mL** | **The problem.** Need >1 mg/mL to inject |

## 1.3 The backup

**GPX4-M1** — same molecule with the original linker, which keeps one charged nitrogen. That nitrogen is
a liability (kidney, heart) **but it is also the standard chemical handle for making a drug dissolve.**
Both are carried forward until a solubility measurement decides.

## 1.4 How it kills

Cells keep fats in their membranes. Those fats go rancid — the same chemistry as cooking oil turning —
and cells run a repair enzyme called **GPX4** whose only job is to reverse that damage continuously.

Block GPX4 and the damage runs away with itself. The membrane tears itself apart. The cell dies by a
route called **ferroptosis**, which is *not* the usual suicide programme cancers learn to switch off,
and which **does not require the cell to be dividing** — the reason it can reach dormant cancer stem
cells that chemotherapy misses.

Leukaemia stem cells run hotter and generate more of this damage than healthy blood stem cells, so they
depend on the repair enzyme more. That gap is the therapeutic window.

---

# PART 2 — EVERY TEST AND SIMULATION RUN

## 2.1 Structure and binding-site analysis

| Test | What it asked | Result |
|---|---|---|
| Pocket volume mapping | Is there a hole to put a drug in? | **26 Å³** within 5 Å of the reactive atom — essentially none |
| Per-atom burial | Which parts of the drug touch protein? | Warhead buried; the arms we changed at **0.06–0.17** (solvent) |
| Burial of the catalytic atom | How enclosed is the target? | **0.93** — strongly enclosed |
| Combined reading | | **Small volume + high burial = a narrow groove, not a cavity** |

## 2.2 Docking — all failed, informatively

| Test | Result | Why it failed |
|---|---|---|
| Non-covalent docking | −5.7 kcal/mol; crystal ligand redocked **5.9 Å off** | No cavity to score |
| Anchored docking, random directions | **0 poses from 1,860 — and 0 for a known binder** | Random directions from a buried atom point into protein |
| Straight-line exit vectors | **0 open from 400**, in the structure that contains a bound ligand | A ligand bends; it needs no straight channel |

**Conclusion: rigid docking cannot work on this target.** Established by measurement, not assumed.

## 2.3 Quantum chemistry

| Test | Result |
|---|---|
| Warhead bond strength vs parent | C–NO₂ bond order differs by **0.006** |
| Charge on the reactive carbon vs parent | differs by **0.0003 electrons** |
| Full-molecule orbital energy shift | −0.32 eV, uniform across the series |
| **Interpretation** | **The chemistry that makes the parent work is untouched by our changes** |
| Reaction barrier (selectivity) | **NOT OBTAINED** — three protocols failed (see §2.8) |

## 2.4 The covalent fit

Built the drug chemically bonded to the protein's reactive atom, generated ~150 shapes, aligned each
onto the bond direction seen in the crystal, and measured collisions.

| | Collision |
|---|---|
| Crystal ligand, in its own deposited position | −0.23 Å (none) |
| Same ligand re-derived by our method | 0.35 Å ← **this is our method's error bar** |
| ML210 | 0.31 Å |
| **GPX4-M3** | **0.29 Å** |

**Reading: no steric problem.** Differences between compounds are smaller than the method's own error,
so this test cannot rank them — only clear them.

## 2.5 Molecular dynamics — the physics movie

31,000 water molecules, protein free to move, 500 million timesteps on the graphics card.

| Measurement | Result |
|---|---|
| **The two modified arms** | **46% of the drug's total water contact, never buried in any frame** |
| Most buried atoms | the warhead region |
| Protein backbone stability | 0.76 Å average movement — fold intact |

**This is the design premise confirmed with the protein moving, not frozen.** Anchor buried, payload in
water.

## 2.6 Drug-property panel

| Test | GPX4-M3 | ML210 |
|---|---|---|
| Greasiness | 1.68 | 4.75 |
| Charged nitrogens | 0 | 1 |
| Heart-rhythm risk | low | high |
| Fraction free in blood | 30% | ~0% |
| Liver metabolism weak spots | 3 flagged | 4 flagged |
| Reactive-metabolite alerts | nitro group | **same** — inherited, not introduced |
| **Solubility (3 models, anchored on knowns)** | **0.03 mg/mL** | 0.0004 |

## 2.7 Systems modelling — populations, not molecules

| Model | Question | Answer |
|---|---|---|
| Resistance dynamics | Does gentle daily dosing suppress or breed escape? | **Delay, ~20 months**, vs ~10 for the approved comparator |
| Sensitivity scan | What actually controls the outcome? | **Not potency** — 10× potency buys 3.2 months |
| Dose scan | Does more drug help? | **4× dose buys 1.9 months.** Do not push |
| Schedule scan | Daily or pulsed? | **Daily continuous wins** |
| Covalent PK/PD | How long must it last in blood? | **~4 hours is enough** — the effect outlives the drug |
| Potency requirement | How strong must it be? | **Saturates** — beyond a modest threshold, nothing |
| Starting burden | Does depth of remission matter? | **3 logs deeper beats a 10× better drug** |
| Partner-drug scan | What should it be paired with? | **Not a second ferroptosis drug. An orthogonal one** |

## 2.8 What failed

| Attempt | Failure |
|---|---|
| Reaction barrier v1 | Basin hop — 46 kcal/mol cliff in one step |
| Reaction barrier v2 | Over-constrained — optimiser failed at the summit |
| Reaction barrier v3 | Same failure, one step later. **Stopped at three** |
| Selenoprotein-wide scan | **18 of 20 proteins absent from the structure database.** Not fixable |
| Frontier-orbital selectivity | Returned exactly 0.00 — method structurally incapable |

Full list with causes: `strategies/crack-the-shell.md` §20.

---

# PART 3 — TREATMENT PLAN

## 3.1 Who gets it

**Adults with acute myeloid leukaemia who have finished chemotherapy and are in remission** — blood
counts normal, disease undetectable or nearly so, but at high risk of relapse. This is *maintenance*:
treating people who currently look well, to stop the disease coming back.

**Deepest remission is the right moment.** The modelling is unambiguous — starting with fewer surviving
cancer cells is worth more than a stronger drug.

**Screening required before starting:**
- **Vitamin E level.** Healthy blood stem cells survive losing this repair enzyme *because vitamin E
  covers for them*. A depleted patient may have no safety margin. Chemotherapy patients are frequently
  depleted
- Baseline blood counts, kidney and liver function

## 3.2 The regimen

| | |
|---|---|
| **Drug** | GPX4-M3 |
| **Partner** | **Venetoclax** — an approved leukaemia drug that kills a completely different way |
| **Schedule** | **Once daily, continuous** |
| **Dose** | Lowest that achieves target engagement. **Do not escalate** — 4× the dose buys 2 months |
| **Duration** | Indefinite, while tolerated |
| **Missed doses** | Low impact by design — the effect outlasts the drug in the blood |

**Why venetoclax:** the escape route for this drug is cells that switch off the machinery making them
vulnerable to membrane damage at all. Once that happens, *any* drug working the same way is irrelevant
to them. Venetoclax kills by an unrelated route, so it still reaches them.

**This combination is already published** — with the parent compound, showing synergy specifically in
the leukaemia stem cells of venetoclax-resistant patients. The partner is de-risked; the new part is our
molecule.

## 3.3 Monitoring

| Watch for | How | Why |
|---|---|---|
| **Anaemia** | routine blood count | **The predicted dose-limiting toxicity.** Red-cell precursors are the sensitive population |
| Kidney function | standard panel | Designed against, but verify |
| Liver enzymes | standard panel | The warhead is chemically reactive |
| Vitamin E | periodic | The safety margin depends on it |

**Anaemia is a good toxicity to have** — routine blood tests catch it, transfusion and dose reduction
manage it, and it is unmistakable, unlike unpredictable organ damage.

## 3.4 What success looks like — and the honest bar

**The realistic claim is delay, not cure.** The model says roughly **+20 months to relapse**. The
approved comparator (azacitidine maintenance) delivered **+9.9 months of overall survival** and that was
enough for approval in 2020.

**The trap:** a drug can suppress every measurable marker and still not extend life. Iomab-B hit its
primary endpoint at p<0.0001 and was **refused filing for lack of survival benefit.**

**Pre-registered kill criterion:** if cancer stem cell counts fall but transplanting survivor cells into
fresh animals still produces leukaemia, the thesis is wrong and the programme stops — regardless of how
good the markers look.

---

# PART 4 — DELIVERY

## 4.1 The route

**Injection — subcutaneous or intravenous.** Oral was considered and dropped: it constrained the
chemistry for no benefit once daily injection was acceptable.

**Getting to the bone marrow is not a barrier.** Marrow blood vessels are *sinusoidal* — deliberately
leaky, with gaps large enough for whole blood cells to pass. This is the opposite of the brain, where
tight junctions exclude most drugs. A molecule that would never reach the brain reaches marrow freely.

## 4.2 The problem

**It does not dissolve well enough. ~0.03 mg/mL against a practical need above 1 mg/mL — 30 to 100×
short.**

For scale: that is the same range as griseofulvin, a drug famous for being hard to formulate.

**Two causes, one self-inflicted:**
1. **Symmetry.** Symmetric rigid molecules stack neatly like bricks and resist dissolving. Symmetry is
   what bought the no-mirror-image advantage — a real trade
2. **No charged group.** Removing it fixed the kidney and heart risks and simultaneously removed the
   standard trick for making a drug dissolve — forming a salt

## 4.3 Options, in order of preference

| Option | What it is | Cost |
|---|---|---|
| **1. Measure first** | Predictions are models. Melting point + true solubility, cheap and fast | Could dissolve the problem or confirm it |
| **2. Use GPX4-M1 instead** | The backup keeps the charged nitrogen, so it can be made into a salt | Reintroduces kidney and heart risk |
| **3. Co-solvent formulation** | Standard vehicles for injectables | Routine, some tolerability cost |
| **4. Cyclodextrin** | A sugar cage that wraps the molecule and carries it in solution | Well-precedented, adds cost |
| **5. Nanosuspension** | Grind to particles that stay suspended | Standard but more development |
| **6. Prodrug** | Attach a soluble group that the body cleaves off | Effective; adds a new molecule to qualify |
| **7. Break the symmetry** | Asymmetric arms disrupt packing | **Reintroduces mirror-image forms** — the thing symmetry was chosen to avoid |

**Recommended: measure first.** Every other option costs something real, and three prediction models are
not a measurement.

---

# PART 5 — WHAT WOULD DECIDE THIS

Three cheap bench experiments, then one animal study.

1. **Solubility and melting point.** Gates whether it can be injected at all
2. **Does it kill escape-competent cells?** Test against cells engineered to lack the machinery this
   drug depends on, with venetoclax as a comparator arm. **Prediction: our drug alone does nothing;
   venetoclax still works.** If venetoclax also fails, the whole combination rationale is wrong
3. **Proteome-wide reactivity profiling.** The only route to a selectivity answer, since the relevant
   protein structures do not exist to compute against
4. **Then: the animal study**, with serial transplantation as the deciding arm and the kill criterion
   fixed in advance
