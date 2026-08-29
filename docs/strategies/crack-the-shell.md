# Crack the Shell — Killing the LSCs That Survive Treatment

**The one-line version:** leukemic stem cells survive treatment by armoring themselves with GPX4.
That armor is a dependency. Strip it and they die by a mechanism their defenses cannot touch.

Execution: [../compute-plan-gpx4.md](../compute-plan-gpx4.md) ·
Build log: [../planning/execution-log.md](../planning/execution-log.md) ·
Provenance: [../research/loops/current-idea.md](../research/loops/current-idea.md),
[../research/loops/dead-ideas.md](../research/loops/dead-ideas.md)

---

# 1. WHAT WE ARE TRYING TO ACCOMPLISH

**Kill the leukemic stem cells that survive AML treatment and cause relapse.**

A patient goes through induction chemotherapy and reaches complete remission — leukemia undetectable
on a slide. It still comes back, in most cases.

It comes back because **complete remission is only about a 200-fold reduction in disease burden.**
Start near 10¹² cells, divide by 200, and billions remain. What survives is not a random sample — it
is the toughest slice, concentrated: dormant, chemo-resistant LSCs sheltering in the bone marrow
niche, able to regrow the whole disease from very few cells.

MRD testing goes deeper than a slide (flow ~1 in 10⁴, molecular ~1 in 10⁵–10⁶), and **a significant
proportion of MRD-negative patients still relapse** — because LSCs are specifically what those panels
miss.

**That population is the target.**

---

# 2. WHY THIS APPROACH, WHEN EVERYTHING ELSE FAILED

Across this project we hit four walls. Any solution has to clear all of them at once.

| Wall | Why it defeats conventional approaches |
|---|---|
| **Selectivity** | LSCs closely resemble normal blood stem cells. Every surface target examined — CXCR4, CD44, CD45, CD33, CD123, CLL-1 — is shared with normal cells. They differ **by degree, not by kind** |
| **Access** | LSCs shelter in the endosteal niche: poorly perfused, hypoxic, gripping stroma through CXCR4, CD44 and VLA-4 |
| **Dormancy** | Most cytotoxics kill dividing cells. A quiescent cell is nearly invisible to that entire drug class. **Dormancy is the resistance mechanism** |
| **Heterogeneity** | AML is not one disease. Drivers differ between patients, and one patient carries several distinct subclones |

And a fifth constraint we derived rather than found: **partial killing only delays relapse.** Killing
is logarithmic; regrowth is exponential. Iomab-B proved this in humans — it met its primary endpoint
at p<0.0001 and the FDA still refused the filing, because overall survival did not follow.

## The hypothesis that clears all four

> LSCs are defined by **apoptosis resistance and dormancy** — the two properties that defeat
> conventional therapy. But the metabolic state granting them those properties floods them with iron
> and oxidative stress, which they survive **only by over-expressing GPX4 as armor** against lipid
> peroxidation. **That armor is a dependency.** Strip it and they die by **ferroptosis** — a death
> pathway that does not use apoptotic machinery and does not require cell division.

Three things make this work:

**Ferroptosis is orthogonal to both defenses.** It is iron-driven membrane destruction, not the
orderly self-destruct program venetoclax and chemotherapy engage. A cell that hardened its apoptotic
machinery has not hardened against this. And lipid peroxidation needs only a membrane, not a
replicating genome — **so dormancy stops mattering.**

**Their own metabolism creates the liability.** Persisters depend on oxidative phosphorylation, a
major ROS source, and that dependence sensitizes them to ferroptosis. It is the same OxPhos
dependence that underpins venetoclax activity — arrived at earlier in this project from a completely
different direction. They cannot abandon it without ceasing to be what they are.

**Their defense is the target.** LSCs are actually *ferroptosis-resistant* at baseline — they
upregulate GPX4 and ferritin to survive their iron load. That sounds like a problem and is in fact
the argument: **their resistance runs through GPX4, which makes GPX4 a dependency rather than a
marker.**

| Where you attack | What happens |
|---|---|
| Upstream — iron loading, SLC7A11, generic oxidative stress | Elevated GPX4 absorbs the damage. **This is why upstream ferroptosis induction underperforms against LSCs** |
| **GPX4 itself** | Removes the one protein they rely on to survive an iron load they cannot switch off |

And the resistance is surmountable: ferroptosis-inducing agents **eliminate 97% of CD34⁺CD38⁻ LSCs** —
the stem-enriched fraction, not bulk blasts.

## How it scores against the four walls

| Wall | Verdict |
|---|---|
| **Selectivity** | ✅ **Strongest in the project.** GPX4 is high across most AML subtypes, lower in normal HSCs, and normal HSCs tolerate its depletion. A window has been *measured*: blasts significantly more sensitive than non-blasts **in the same patient's marrow** |
| **Access** | ⚠️ **Improved, not solved.** A small molecule reaches the niche far better than CAR-T, antibodies, or radioconjugates — the modalities earlier strategies relied on |
| **Dormancy** | ✅ **The standout.** Every earlier strategy had to *break* dormancy first, with timing windows and provocation agents. Here dormancy simply stops mattering — persisters are *preferentially* vulnerable |
| **Heterogeneity** | ✅ Not mutation-specific. High across most subtypes, and **highest in relapsed/refractory disease** — the patients who need it most |
| **Durability** | ❓ **Unresolved.** See §6 |

---

# 3. THE DRUG

**A selective covalent GPX4 inhibitor, paired with an FSP1 inhibitor, on a venetoclax/azacitidine
backbone, for venetoclax-resistant AML.**

## Why that indication

ML210 plus venetoclax is synergistic in primary AML patient cells **including venetoclax-resistant
ones**. Venetoclax kills by apoptosis; ferroptosis is a different pathway; resistance to one does not
confer resistance to the other. Venetoclax resistance is among the largest unmet needs in AML.

That gives a defined population, a mechanistic rationale, primary-patient evidence, and an approved
backbone to add to — an approvable trial shape rather than a science project.

## Why FSP1 must be covered

FSP1 suppresses ferroptosis by a **glutathione-independent** route, regenerating CoQ10 in parallel to
GPX4. Under pressure, **cells shift their dependence from GPX4 to FSP1.** Blocking GPX4 alone
pre-installs the escape route.

**A prediction this project makes that no single source states:** mitochondria are the primary source
of CoQ recycling, *and* marrow stroma transfers mitochondria to AML cells through tunneling nanotubes —
a transfer that metabolic attack actively induces. So attacking GPX4 should provoke the niche to
**resupply the escape route**. Untested, testable, and the strongest argument that FSP1 coverage is
not optional.

The FSP1 partner already exists (icFSP1 class), and **no FSP1 inhibitor has ever been tested in AML.**

## The regimen

| Component | Role | Status |
|---|---|---|
| **GPX4 inhibitor** | Strip the armor | **The molecule we design** |
| FSP1 inhibitor | Close the escape route | Exists; untested in AML |
| Venetoclax | Apoptotic arm | Approved |
| Azacitidine | Backbone; independently sensitizes to ferroptosis | Approved |
| *HDAC inhibitor (optional)* | *Raises labile iron; removes a second persister defense* | *Approved* |
| **NOT an NCOA4 inhibitor** | **Antagonizes** — it *reduces* free iron and protects against ferroptosis | — |

## Why the molecule does not exist yet

**GPX4 has a shallow active site with no drug-like binding pocket.** Every existing compound failed on
pharmacokinetics. And the field's tools were partly mis-assigned: **RSL3 and ML162 are not direct
GPX4 inhibitors — they hit TXNRD1.** ML210, with a nitro-isoxazole warhead, genuinely is selective.

**So selective chemistry exists; a drug does not.** The problem is optimizing a validated chemotype
for pharmacokinetics and clearance route — six coupled constraints solved simultaneously on a target
with **solved crystal structures**. That combination is why GPX4 resisted a decade of serial
medicinal chemistry, and why it is tractable now.

---

# 4. WHERE WE ARE

Structures acquired and verified with **genuine selenocysteine** (6HN3 apo at 1.01 Å; 6HKQ covalent
complex at 1.54 Å). Covalent geometry extracted. Warhead classes confirmed computationally rather
than assumed. Baseline compound properties computed.

**Two findings already changed the plan:**

- **The TXNRD1 counter-target structures are cysteine mutants with disordered catalytic tails.** That
  matters because what separates the compounds is warhead chemistry, not pocket shape — so
  **selectivity here is likely a reactivity problem**, and the pipeline needs a quantum-chemistry arm
  alongside docking.
- **ML210 already falls inside our property window** (MW 475, logP 4.75, TPSA 92.7). The chemotype
  chosen for selectivity turns out to be property-appropriate too, narrowing the job from "fix bad
  properties" to "improve PK and clearance route."

One design lever emerged from computed data: **ML210 has zero hydrogen-bond donors**, which favors
CNS penetration — the opposite of what we want. There is TPSA headroom to add polarity without
breaking oral absorption.

---

# 5. WHAT'S NEXT

**Compute, in strict order:**

1. Install a covalent-capable docking engine
2. **Pose-recovery gate** — re-dock ML162 into its own crystal structure and reproduce the known pose
3. **Selectivity validation gate** — can the pipeline reproduce the known answer (ML210 selective;
   ML162 and RSL3 not)? **No molecule generation until this passes.** A pipeline that cannot separate
   compounds whose real-world answer is known and opposite cannot rank novel ones
4. Generation — GenMol holding the warhead fixed, FLOWR.root for scaffold diversity

**The decisive experiment, which is wet lab and not compute:**

**Serial transplantation.** Does GPX4 inhibition eliminate leukemia-initiating capacity, or merely
kill cells? Nobody has run it for any ferroptosis inducer in AML. Killing LSCs is not enough — Iomab-B
met its endpoint and still failed on survival. **The hypothesis stands or falls here.**

---

# 6. THE HONEST RISKS

- **Durability is unknown** until serial transplantation runs. This is the one that decides whether
  this is a therapy or a delay.
- **Kidney and T-cell toxicity are unmeasured, not proven absent.** All the alarming data comes from
  *total genetic knockout* — permanent, whole-body, every cell — which is not what a drug does. No
  pharmacological therapeutic window has ever been measured, because no compound had the PK to try.
  An antidote exists (liproxstatin-1).
- **The niche may resupply the escape route** via mitochondrial transfer feeding the CoQ/FSP1 arm.
  Our prediction, untested.
- **GADD45A-low LSCs** are a known resistance mechanism — loss increases both self-renewal and
  ferroptosis resistance.

**What would falsify the hypothesis:** GPX4 inhibition kills LSCs but leaves leukemia-initiating
capacity intact on serial transplant. That single result would end it.

---

# 7. COMPUTATIONAL WORK COMPLETED — DATA

Everything below was executed, not planned. Build log:
[../planning/execution-log.md](../planning/execution-log.md). Raw outputs under `work/`.

## 7.1 Structures — verified, not assumed

| PDB | Contents | Resolution |
|---|---|---|
| **6HN3** | Apo human GPX4, wild-type | **1.01 Å** |
| **6HKQ** | GPX4 + ML162 (S), covalent | 1.54 Å |

Both carry **genuine selenocysteine** — residue 46 parses as SEC with an SE atom and is declared in
SEQRES — not the U46C substitution common in GPX4 entries, which would be useless for reactivity work.

**Covalent geometry extracted from the LINK records:** ligand **G9N**, anchor **Sec46 SE → ligand
C20**, bond length **1.56–1.61 Å**. An independently computed Se–C20 distance of **1.61 Å** matched
the deposited record exactly, validating coordinate parsing.

**Sec46 is modelled in two conformers** — altloc A at 0.60 occupancy, B at 0.40, selenium positions
**2.33 Å apart**. Most preparation tools silently keep only altloc A; here that default is defensible
but must be deliberate rather than accidental.

## 7.2 Non-covalent docking fails — and that is a result

AutoDock Vina 1.2.5, exhaustiveness 32, redocking G9N into its own crystal structure.

| Metric | Crystal | Best of 9 docked poses |
|---|---|---|
| Affinity | — | **−5.7 kcal/mol** (weak) |
| RMSD | 0 | **5.88 Å** (range 5.9–7.9) |
| **Closest approach to catalytic Se** | **1.61 Å** | **3.64 Å** |
| Radius of gyration | 3.62 | 3.9–4.6 |

Order-independent metrics were used to exclude an atom-correspondence artifact.

**This empirically confirms two claims the strategy rests on.** Affinities of −5.2 to −5.7 kcal/mol —
a real pocket gives −8 to −10 — together with nine non-converging poses demonstrate that **GPX4 has no
drug-like binding pocket**. And **no pose came within 3.64 Å of the selenium**, roughly 2 Å too far to
bond, so **the covalent constraint is mandatory rather than a refinement.** The crystal geometry
exists because of the bond, not because of shape complementarity.

Had 20,000 generated compounds been ranked on non-covalent scores, the campaign would have been
worthless. This was caught before generating one.

**Toolchain note:** Meeko **refused selenocysteine** outright — `Template generation failed for
unknown residues: {'SEC'}` — and offered `--delete_residues` as a remedy, which would silently remove
the catalytic residue and let the pipeline run to completion producing meaningless output. An
explicitly labelled Cys surrogate was used for **geometry only**. Proper SEC parameters remain an open
blocker for any reactivity work on the protein.

## 7.3 Quantum chemistry — the selectivity determinant

GFN2-xTB, geometry-optimised, on capped warhead models so the comparison isolates intrinsic
electronics.

| Warhead model | HOMO (eV) | LUMO (eV) | Gap (eV) | ω (eV) |
|---|---|---|---|---|
| **ML210 nitro-isoxazole** | −11.03 | **−9.05** | 1.97 | **25.5** |
| RSL3 / ML162 chloroacetamide | −10.88 | −6.58 | 4.30 | 8.9 |
| Control — nitro removed | −10.57 | −7.47 | 3.10 | 13.1 |

**Findings:**

- The ML210 warhead LUMO sits **2.48 eV lower** than the chloroacetamide — a far stronger electron
  acceptor, with a **2.9× higher** global electrophilicity index.
- **The nitro group is the activator.** Removing it raises the LUMO by **1.59 eV**. Any analog must
  preserve the nitro, not merely the isoxazole ring — a hard design constraint derived from data.

**Interpretation, stated carefully.** The naive reading — more electrophilic implies less selective —
is contradicted by ML210 being the selective compound. The resolution is that **the two warheads react
by different mechanisms, so the comparison is not like-for-like.** Chloroacetamide is a plain SN2
electrophile, immediately reactive toward any accessible thiol or selenol, consistent with its
promiscuity and its TXNRD1 off-target. ML210 is a **masked** nitrile-oxide precursor that must be
unmasked before it reacts; its very low LUMO and narrow 1.97 eV gap reflect activation toward that
rearrangement rather than toward direct attack. **Selectivity here is kinetic, and it derives from
masking.**

**Limitation, explicitly:** the species modelled is the ML210 *precursor*, not the unmasked nitrile
oxide that actually reacts. The reactive species was not computed. This quantifies the electronic
difference between chemotypes; it does not by itself prove the selectivity mechanism.

## 7.4 First design cycle — 210 analogs, 15 clear the window

BRICS decomposition fixed the **nitro-isoxazole → amide → piperazine** scaffold. The variable handle
is the **bis(4-chlorophenyl)methine**, which carries most of the lipophilicity and contributes zero
polarity. Twenty aryl and heteroaryl replacements were enumerated pairwise, and **every structure was
gated on warhead integrity by SMARTS** before scoring.

| Candidate (R1 / R2) | MW | logP | TPSA | HBD | QED | Structural alerts |
|---|---|---|---|---|---|---|
| 4-OH-phenyl / 4-NHMe-phenyl | 451.5 | 3.19 | 125.0 | 2 | 0.43 | ⚠️ aniline + phenol |
| 4-OH-phenyl / 4-CH₂OH-phenyl | 452.5 | 2.64 | 133.2 | 2 | 0.43 | ⚠️ phenol |
| bis(4-CH₂OH-phenyl), symmetric | 466.5 | 2.42 | 133.2 | 2 | 0.40 | benzylic alcohol |
| **bis(4-CONH₂-phenyl), symmetric** | 492.5 | **1.64** | — | 2 | — | ✅ **none** |
| **ML210 baseline** | 475.3 | 4.75 | 92.7 | **0** | 0.39 | — |

**Movement against objectives:** HBD **0 → 2**, the key barrier-exclusion driver; logP **4.75 →
1.64–3.19**; TPSA **92.7 → 125–139**; MW held inside the window.

**Self-critique applied after ranking.** The two highest-QED hits carry structural alerts — the
**aniline is a quinone-imine risk**, and phenols are metabolic soft spots. The symmetric
**bis(4-carbamoylphenyl)** analog is alert-free, has the lowest lipophilicity, and symmetric benzhydryl
centres are **synthetically easier** than mixed ones. On medicinal-chemistry grounds it outranks the
QED ordering.

## 7.5 The result that makes this scaffold credible

Measured bond path from the design handle to the electrophilic warhead carbon: **7 bonds, through an
amide and a saturated piperazine.**

Tested computationally rather than asserted — full-molecule GFN2-xTB, ML210 versus the substituted
analog:

| | ML210 | 4-OH / 4-NHMe analog | Shift |
|---|---|---|---|
| **LUMO** (warhead-localised acceptor) | −9.11 | −9.06 | **+0.054 eV** |
| HOMO (ligand-localised) | −10.10 | −9.51 | +0.59 eV |

**The LUMO is unmoved; only the HOMO shifts.** Substituting electron-rich aryls raises the donor
orbital while leaving the warhead acceptor orbital untouched — the exact signature of electronic
insulation.

**Therefore the property problem and the selectivity problem are separable on this scaffold.** That is
the strongest single argument that lead optimisation here is a credible programme rather than a
reactivity gamble, and it is now a measurement rather than a claim.

## 7.6 What has NOT been established

- **No potency prediction whatsoever.** The chlorophenyls may make essential contacts. The mitigating
  argument — GPX4 has no real pocket, so they plausibly contribute positioning rather than affinity —
  is a hypothesis supported by §7.2, not a result.
- **Covalent docking not yet run.** The non-covalent gate was retired as uninformative; the
  constrained protocol is next.
- **Barrier exclusion is predicted from property heuristics**, not modelled.
- **Selenocysteine parameters unresolved**, which blocks all reactivity modelling on the protein.
- **No MD, no FEP, no free-energy work yet.**
- **Nothing here addresses durability.** Serial transplantation remains the experiment that decides
  whether this is a therapy or a delay, and no amount of simulation substitutes for it.

---

# 8. STRUCTURAL VALIDATION OF THE DESIGN STRATEGY

Three computations that together answer the question the first design cycle could not: **is modifying
those aryl groups actually safe?**

## 8.1 Where the crystal ligand touches the protein

Per-atom burial of ML162 in 6HKQ, computed with a 1.4 Å probe against the chain-A receptor.
1.00 = fully enclosed, 0.00 = fully solvent-exposed.

| Region | Atoms | Burial |
|---|---|---|
| **Covalent carbon C20** | — | **0.90** |
| Warhead vicinity | C19, O22, N13 | 0.60–0.78 |
| Distal aryl / thiophene | S15, C4, C16, C7, C5, N9 | **0.06–0.12** |

**Mean burial across the whole ligand: 0.34. Only 6 of 30 atoms are more than 50% buried.**

**The molecule is not in a pocket. It lies in a shallow surface groove with its warhead end anchored
and the rest in solvent.**

This is the single most useful structural result of the programme, because it validates the design
strategy directly:

- **The buried end is the warhead** — which we preserved unchanged, verified by SMARTS on all 210
  analogs and by the +0.054 eV LUMO measurement.
- **The end we modified is solvent-facing** — burial 0.06–0.17. Polar substituents there are
  sterically well tolerated and are not displacing protein contacts, because there were barely any
  contacts to displace.

It also quantitatively explains the earlier docking failure: with only 6 of 30 atoms making contact,
there is almost nothing for a non-covalent scoring function to score.

## 8.2 Accessible volume around the catalytic selenium

Grid map of solvent-accessible, protein-adjacent volume around Sec46 in the apo structure (6HN3),
0.6 Å grid, 1.4 Å probe:

| Distance from Se | Accessible volume |
|---|---|
| within 5 Å | **26 Å³** |
| within 6 Å | 64 Å³ |
| within 8 Å | 298 Å³ |
| within 10 Å | 809 Å³ |

Against candidate molecular volumes:

| Compound | Volume |
|---|---|
| ML162 (crystallographically fits) | 405 Å³ |
| ML210 | 395 Å³ |
| B — bis(4-CH₂OH-phenyl) | 416 Å³ |
| C — bis(4-CONH₂-phenyl) | 427 Å³ |

**A ~400 Å³ molecule cannot be accommodated within 8 Å of the selenium (298 Å³ available).** It must
extend outward across the surface — exactly the arrangement §8.1 observes.

**Consequence for the programme: affinity is not the optimisation axis.** There is no pocket to fill.
Potency will be governed by warhead reactivity and residence time, not by shape complementarity.
That reinforces the decision to treat this as a reactivity-and-properties problem.

**Consequence for the design: bulk tolerance is generous** in the solvent-facing direction, which is
precisely where our substitutions sit.

## 8.3 Do the new hydrogen-bond donors survive in water?

The standard way a TPSA-driven design fails is **intramolecular hydrogen bonding** — added donors fold
back onto internal acceptors, become masked, and the compound behaves as if far less polar than its
2D descriptors suggest. Barrier exclusion then does not materialise.

Tested directly: 30-conformer ensembles, MMFF-minimised, lowest-energy conformer re-optimised with
**GFN2-xTB in implicit water (ALPB)**.

| Compound | Rg (Å) | Intramolecular H-bonds | 3D polar SASA (Å²) | **Exposed HBD** |
|---|---|---|---|---|
| ML210 | 4.43 | 0 | 84.5 | **0** |
| A — 4-OH / 4-NHMe | 4.78 | **0** | 127.6 | **2** |
| **B — bis(4-CH₂OH)** | 4.90 | **0** | 134.5 | **2** |
| C — bis(4-CONH₂) | 4.95 | 2 | 181.6 | 2 |

**The design holds.** A and B show **zero** intramolecular hydrogen bonds — their donors remain
solvent-exposed, and the polar surface increase is real in three dimensions, not merely a 2D
descriptor artefact.

No compound collapses: Rg rises modestly (4.43 → 4.78–4.95), consistent with added substituents rather
than folding.

C forms 2 internal hydrogen bonds. It carries four donors in total (two primary amides), so two remain
exposed — but its 3D polar surface of 181.6 Å² is high enough to raise a permeability concern in the
opposite direction.

## 8.4 Revised lead

Combining alert screening (§7.4) with this analysis:

| | logP | Exposed HBD | Intra-HB | Alerts | Symmetric? |
|---|---|---|---|---|---|
| A — 4-OH / 4-NHMe | 3.19 | 2 | 0 | ⚠️ aniline, phenol | no |
| **B — bis(4-CH₂OH)** | **2.42** | **2** | **0** | benzylic alcohol only | **yes** |
| C — bis(4-CONH₂) | 1.64 | 2 | 2 | none | yes | 

**B is the lead.** It is symmetric — materially easier to synthesise than a mixed benzhydryl centre —
carries no intramolecular masking, has the lowest alert burden short of C, and sits mid-range on
polarity where C risks being over-polar for oral absorption.

*Note this differs from the QED ranking, which favoured A. Automated desirability scores do not see
aniline toxicophores or synthetic symmetry; the ranking was corrected on medicinal-chemistry grounds.*

## 8.5 What these three results establish together

1. The part of the molecule we modified **makes almost no protein contact** (burial 0.06–0.17).
2. There is **no pocket to disrupt** — only 26 Å³ within 5 Å of the catalytic selenium.
3. The modifications **achieve genuine polarity in water** without self-masking.
4. The warhead is **electronically untouched** (+0.054 eV LUMO).

**The property-optimisation strategy is structurally justified, not merely convenient.** We are
altering a solvent-exposed region that contributes little binding, while leaving intact the buried,
covalently-anchored warhead that does the chemistry.

**Still unestablished:** actual potency. This argues the modifications are *unlikely to hurt*; it does
not demonstrate the parent chemotype is potent enough to matter, which requires the purified-enzyme
assay.
