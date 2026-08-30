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

---

# 9. PENETRATE AND KILL

Two separate problems. One resolves cleanly; the other exposes a limit of what this hardware can settle.

## 9.1 PENETRATE — resolved, and the apparent conflict was false

There seemed to be a contradiction at the heart of the design: we deliberately added polarity to keep
the compound **out** of brain and retina, yet the target sits in the bone marrow niche, which earlier
work in this project identified as one of the hardest places in the body to deliver a drug.

**The two are governed by different mechanisms, so there is no conflict.**

| | Brain | Bone marrow |
|---|---|---|
| Endothelium | Continuous, **tight junctions** | **Sinusoidal, fenestrated** |
| Efflux pumps | P-gp / BCRP at the interface | Not a barrier interface |
| Nature of the obstacle | **A true barrier — exclusion** | **Poor perfusion — slow delivery** |
| What it takes to enter | Low TPSA, low HBD, no efflux liability | Little; solutes equilibrate through fenestrae |

Crossing into brain requires defeating a physical barrier. Reaching marrow interstitium does not —
the fenestrated sinusoidal endothelium admits solutes without demanding high passive permeability.
The endosteal niche is limited by **how fast blood arrives**, not by whether the molecule is allowed in.

**Polarity that keeps a compound out of brain therefore does not keep it out of marrow.** Adding
hydrogen-bond donors buys barrier exclusion at no cost to the target tissue.

**Access profile:**

| Compound | MW | logP | TPSA | HBD | CNS-MPO (lower = less brain-penetrant) |
|---|---|---|---|---|---|
| ML210 | 475.3 | 4.75 | 92.7 | 0 | 1.64 |
| **Lead B — bis(4-CH₂OH)** | 466.5 | **2.42** | 133.2 | **2** | **1.24** |
| C — bis(4-CONH₂) | 492.5 | 1.64 | 178.9 | 2 | 1.05 |

The lead moves decisively away from brain penetration relative to ML210 while remaining well within
the range that reaches marrow. C is more excluded still, but its 179 Å² polar surface starts to
threaten oral absorption.

**Remaining penetration risk is kinetic, not thermodynamic:** the niche is poorly perfused, so
exposure there will lag plasma. That argues for sustained exposure rather than sharp peaks — a
dosing-schedule question, not a molecular-design one.

## 9.2 KILL — a method failure worth recording, then a real number

With no binding pocket (§8.2), potency cannot come from affinity. It has to come from reactivity. So
the decisive question is whether the warhead genuinely prefers the selenol of GPX4 over the thiols
that dominate the proteome.

### First attempt: frontier orbital analysis — structurally incapable of answering

Computed in implicit water: selenolate HOMO −11.02 eV, thiolate HOMO −7.82 eV; nitro-isoxazole LUMO
−9.40 eV, chloroacetamide LUMO −6.64 eV.

The apparent "selenium preference" came out at **exactly −3.20 eV for both warheads**, and the
differential at **exactly 0.00**.

**That is arithmetic, not chemistry.** Writing it out:

```
preference = gap(S) − gap(Se) = (LUMO − HOMO_S) − (LUMO − HOMO_Se) = HOMO_Se − HOMO_S
```

**The warhead LUMO cancels.** A frontier-gap comparison can never distinguish two warheads facing the
same pair of nucleophiles — the answer is fixed by the nucleophiles alone. The approach was incapable
of answering the question it was set, and no amount of running it would have helped.

**Recorded because the failure is instructive:** it rules out a whole class of cheap descriptor-based
selectivity prediction for this problem.

### Second attempt: explicit reaction energetics

Modelling the actual SN2 displacement on the chloroacetamide, GFN2-xTB in implicit water:

```
Nu⁻ + ClCH₂C(O)NMe₂  →  Nu–CH₂C(O)NMe₂ + Cl⁻
```

| Nucleophile | ΔE |
|---|---|
| Selenolate | **+1.5 kcal/mol** |
| Thiolate | **−37.8 kcal/mol** |

**Reliability caveat, stated first because it matters:** the 39 kcal/mol magnitude is **not credible**.
Semiempirical methods handle anionic species and implicit solvation poorly, and selenium is less well
parameterised in GFN2 than sulfur. Treat the number as directional only.

**The direction, however, is chemically sound and experimentally consistent.** C–S bonds are
intrinsically stronger than C–Se (roughly 272 vs 234 kJ/mol), so thiolate adduct formation is
genuinely the more favourable thermodynamic outcome. And that matches what is observed: **RSL3 and
ML162, both chloroacetamides, hit the cysteine machinery of TXNRD1 rather than the selenocysteine of
GPX4.** Their off-target preference is thermodynamically expected.

### What this implies for the programme

**A GPX4-selective warhead cannot win on thermodynamics.** Forming a C–Se bond is intrinsically less
favourable than forming a C–S bond, so any compound that preferentially modifies selenocysteine must
be doing so **kinetically** — through accessibility, residence time, or a reaction pathway only
available at that site.

**This independently supports the masking hypothesis.** ML210 is a masked nitrile-oxide precursor
requiring unmasking before it reacts. A latent electrophile that becomes reactive only under specific
local conditions is exactly the mechanism you would need to beat an unfavourable thermodynamic
gradient — and it explains why a *more* electrophilic warhead (§7.3: 2.9× higher ω) is nonetheless the
*more* selective one.

**And it sets the boundary of what this hardware can settle.** Kinetic selectivity requires transition
states and activation barriers — proper DFT with TS searches, not semiempirical ground-state
energetics. That is a substantially heavier calculation, and for the masked nitrile-oxide pathway it
also requires modelling the unmasking step, whose mechanism is not established.

**Honest position: we can show the design is sound and the thermodynamics are unfavourable-but-
surmountable. We cannot compute the number that decides potency.** That is the purified-enzyme assay —
the same assay RSL3 and ML162 failed.

---

# 10. THE GOAL, RESTATED: DAILY GENTLE MAINTENANCE

**We are not building a cure. We are building a drug a patient in remission can take
indefinitely to hold leukemic stem cells down — tolerable enough to live on, with any organ
toxicity mitigable by a companion agent.**

## The evidence that this is the right goal, not a lesser one

Two trials in the same disease settle it.

| | **Iomab-B** | **Oral azacitidine (Onureg)** |
|---|---|---|
| Approach | Massive one-shot radio-ablation | Gentle daily pill |
| Setting | Relapsed/refractory | **Remission maintenance** |
| Hit its primary endpoint | Yes, p<0.0001 | Yes |
| **Median overall survival** | **No benefit** | **24.7 vs 14.8 months** |
| **Regulatory outcome** | **FDA refused the filing** | **FDA approved, Sept 2020** |

QUAZAR AML-001: 472 patients in first remission. Oral azacitidine improved survival by **31%** and
relapse-free survival by **35%**, and it worked **regardless of MRD status**.

**Same disease, same objective of clearing residual leukemia — and the gentle chronic agent won while
the massive one-shot lost.** Maintenance is not the modest version of the goal. On the evidence it is
the version that works.

### Why Iomab-B cannot simply be dosed higher

CD45 is on all *nucleated* blood cells — mature red cells are anucleate and unaffected. What Iomab-B
destroys is the **blood-forming stem compartment**, and that destruction is the *intent*: it is
transplant conditioning. The dose is not limited by marrow toxicity, because marrow toxicity is the
goal; it is limited by radiation reaching liver and lung, which is what the per-patient dosimetry
measures. Without a graft to follow, the patient dies of marrow failure. And radiation damage is
cumulative and irreversible — it can never be a daily therapy.

### What this does to the resistance objection

§9 raised a serious problem: ferroptosis defence has at least five redundant arms (GPX4, FSP1,
DHODH, GCH1–BH4, NQO1), so resistance is inevitable.

**Under a maintenance goal that objection loses most of its force.** Azacitidine maintenance is not
resistance-proof either. It bought ten months of life and won approval anyway. **The requirement is
not "forever" — it is "long enough, repeatedly, tolerably."** That is a far more achievable bar, and
it is the bar the comparator actually cleared.

## Revised target product profile

| Attribute | Target | Rationale |
|---|---|---|
| Use | Maintenance in remission | Matches the only regimen with a proven OS benefit |
| Route | **Injectable acceptable** — oral not required | Removes the TPSA<140 absorption ceiling |
| Dosing | Daily / repeated, chronic | Containment, not ablation |
| Backbone | **+ azacitidine** | Approved in this exact setting, *and* independently sensitises to ferroptosis via SLC7A11–GPX4 |
| Charge | **Neutral** | See the acid trap below |
| Clearance | **Hepatobiliary** | Keeps drug out of the proximal tubule |
| Barriers | Excluded from brain and retina | HBD ≥ 2, high polarity |

---

# 11. SECOND DESIGN CYCLE — OPTIMISED FOR MAINTENANCE

## 11.1 The acid trap, caught before it was recommended

Dropping the oral requirement first suggested adding a **carboxylic acid**: anionic at pH 7.4, it
drives hepatic OATP uptake toward biliary clearance, and a permanent negative charge is near-totally
excluded from brain and retina. Two problems solved by one group, and the top ten ranked candidates
were all acids.

**It is a trap.** Anions are substrates for the renal organic anion transporters **OAT1/OAT3**, which
actively pump them *into* proximal tubule cells and concentrate them there — the established
mechanism of anionic-drug nephrotoxicity (cidofovir, adefovir). **The proximal tubule is exactly where
GPX4 loss causes acute renal failure.** An acid would actively deliver a GPX4 inhibitor into the cells
we most need to protect.

Cations are no better: OCT2 concentrates them in the same tubule (cisplatin, metformin).

**Conclusion: the molecule must be neutral.** Polarity has to come from amides, alcohols, ethers and
sulfonamides — never from an ionisable group.

## 11.2 Ranking

210 warhead-intact analogs, scored on a composite of MW 500–650 (biliary), logP 1.5–3.5, TPSA
120–200, HBD ≥ 2, structural symmetry (synthesis), minus structural alerts.

| R1 / R2 | MW | logP | TPSA | HBD | Alerts | Sym | Score |
|---|---|---|---|---|---|---|---|
| **bis(4-CONHMe-phenyl)** | 520.5 | 2.16 | 150.9 | 2 | 0 | ✅ | **6.50** |
| bis(4-(2-OH-ethoxy)phenyl) | 526.5 | 2.18 | 151.6 | 2 | 0 | ✅ | **6.50** |
| bis(4-CH₂CONH₂-phenyl) | 520.5 | 1.49 | 178.9 | 2 | 0 | ✅ | 6.47 |

The top two tied exactly, and on every 2D descriptor they are near-identical.

## 11.3 Simulation broke the tie — and caught a silent failure

All three re-optimised with **GFN2-xTB in implicit water**:

| Candidate | Rg | Internal H-bonds | **Exposed HBD** | ΔLUMO vs ML210 |
|---|---|---|---|---|
| **M1 — bis(4-CONHMe)** | 5.42 | **0** | **2** | −0.32 eV |
| M2 — bis(4-(2-OH-ethoxy)) | 5.54 | 2 | **0** | −0.32 eV |
| M3 — bis(4-CH₂CONH₂) | 5.33 | 2 | 2 | −0.33 eV |

**M2 collapses in water.** Both hydroxyl groups fold back onto internal acceptors. Its two
hydrogen-bond donors become **completely masked** — in solution it behaves as **HBD-zero, exactly like
ML210, the liability the entire redesign exists to fix.**

On paper M2 and M1 were indistinguishable: identical score, TPSA within 0.7 Å², same donor count. **A
2D descriptor calculation would have picked either. The simulation is what separated a working design
from one that silently fails.**

**M1 keeps both donors solvent-exposed. It is the lead.**

**One honest caveat:** ΔLUMO is −0.32 eV across all three, larger than the +0.054 eV measured for the
smaller bis(CH₂OH) analog in §7.5. The bigger substituents do communicate slightly with the warhead.
The shift is modest and uniform — a consequence of substituent size rather than a specific liability —
but the insulation is not perfect at this scale and should be re-checked on any further growth.

---

# 12. THE LEAD MOLECULE

**Working name: GPX4-M1**

```
Cc1onc(C(=O)N2CCN(C(c3ccc(C(=O)NC)cc3)c3ccc(C(=O)NC)cc3)CC2)c1[N+](=O)[O-]
```

**Structure:** ML210 with both 4-chlorophenyl groups replaced by **4-(N-methylcarbamoyl)phenyl**.
Warhead and piperazine linker untouched.

| Property | ML210 | **GPX4-M1** | Why it matters |
|---|---|---|---|
| MW | 475.3 | **520.5** | >500 favours biliary clearance, away from kidney |
| logP | 4.75 | **2.16** | Amphipathic, not greasy |
| TPSA | 92.7 | **150.9** | Barrier exclusion; no oral ceiling now |
| **Exposed HBD in water** | **0** | **2** | The actual driver of brain/retina exclusion |
| Internal H-bonds | 0 | **0** | Donors stay exposed — design does not self-defeat |
| Charge at pH 7.4 | neutral | **neutral** | Avoids OAT/OCT tubular concentration |
| Symmetric | yes | **yes** | Single benzhydryl coupling, not a mixed centre |
| Structural alerts | — | **none** | No aniline, phenol, acid, or Michael acceptor |

**Why the N-methyl amide specifically:** secondary amides are more metabolically robust than primary
amides, and — as the simulation showed — the N-methyl group sterically discourages the intramolecular
hydrogen bonding that masked M2 and M3.

**Regimen:** GPX4-M1 + an FSP1 inhibitor (icFSP1 class, to close the CoQ escape route) on an
**azacitidine** backbone, given as maintenance in remission.

---

# 13. EXPANDED SCREEN — 300 CANDIDATES, AND WHERE SIMULATION STOPS HELPING

## 13.1 The library

24 neutral fragments, chosen to resist intramolecular hydrogen bonding: secondary and tertiary
amides, sulfones, sulfonamides, cyclic ethers, lactams. Enumerated pairwise on the fixed
nitro-isoxazole/piperazine scaffold → **300 warhead-intact analogs**.

Filtered to zero structural alerts, HBD ≥ 2, then to **symmetric** pairs only — a single benzhydryl
coupling rather than an unsymmetrical centre, which is a real synthetic saving.

**A bug worth recording:** the first pass returned *zero* candidates. The `basicN` alert was matching
the **core piperazine**, which is present in ML210 itself and in every analog. An alert that fires on
the scaffold is not an alert; it was removed. Left unnoticed, this would have silently emptied every
subsequent screen.

## 13.2 Eight candidates through full GFN2-xTB in implicit water

| Tag | R-group (×2) | MW | logP | Rg | Internal H-bonds | **Free HBD** | ΔLUMO |
|---|---|---|---|---|---|---|---|
| S00 | 4-CONHMe | 520.5 | 2.16 | 5.60 | 0 | 2 | −0.322 |
| S01 | 4-CONHEt | 548.6 | 2.94 | 5.92 | 0 | 2 | −0.324 |
| S02 | 4-CONH-cPr | 572.6 | 3.22 | 6.11 | 0 | 2 | −0.324 |
| S03 | 4-CONH-oxetan-3-yl | 604.6 | 1.70 | 5.97 | 0 | 2 | −0.323 |
| S04 | 3-CONHMe | 520.5 | 2.16 | 5.29 | 0 | 2 | −0.330 |
| S05 | 4-CONHMe-3-F | 556.5 | 2.44 | 5.58 | 0 | 2 | −0.334 |
| S06 | 4-CH₂CONHMe | 548.6 | 2.02 | 5.55 | 0 | 2 | −0.332 |
| S07 | 4-NHCOMe | 520.5 | 3.36 | 5.43 | 0 | 2 | −0.310 |

**All eight pass.** Zero intramolecular masking, two free donors each, warhead perturbation uniform.

**This is the point where simulation stops discriminating.** The entire ΔLUMO spread is **0.024 eV** —
noise, not signal. Ranking on it would be false precision.

**That is itself a useful result:** the amide-based fragment class as a whole solves the masking
problem that killed the hydroxyl and hydroxyethoxy candidates. The design question is answered; the
selection question now belongs to chemistry.

## 13.3 The top-ranked candidate was a trap

My numeric ranking put **4-NHCOMe first** — on a 0.012 eV ΔLUMO advantage that is not real.

**4-NHCOMe is an acetanilide.** Aryl acetamides hydrolyse in vivo to the free **aniline** — precisely
the quinone-imine toxicophore excluded in the first design cycle. Paracetamol hepatotoxicity proceeds
through exactly this chemistry. It also carries the highest logP in the set (3.36).

**A structural alert filter applied to the parent structure does not catch a toxicophore that is
liberated by metabolism.** Second time in this project that an automated score has ranked something
first that a medicinal chemist would reject on sight.

## 13.4 Final selection, made on chemistry

| Rank | R-group (×2) | MW | logP | TPSA | Basis |
|---|---|---|---|---|---|
| **1** | **4-CONHMe** | **520.5** | **2.16** | **150.9** | Robust secondary aryl amide; no metabolic liberation; ideal lipophilicity; smallest of the equals |
| 2 | 3-CONHMe | 520.5 | 2.16 | 150.9 | Identical properties; meta substitution is a genuine backup vector |
| 3 | 4-CH₂CONHMe | 548.6 | 2.02 | 150.9 | Clean, slightly larger, benzylic position adds a metabolic soft spot |
| 4 | 4-CONHMe-3-F | 556.5 | 2.44 | 150.9 | Fluorine blocks para-hydroxylation — a useful second-generation move |

Excluded: 4-NHCOMe (liberates aniline), 4-CONH-oxetan-3-yl (oxetanes are acid-labile),
4-CONH-cPr and 4-CONHEt (logP 3.2 and 2.9, no compensating advantage).

---

# 14. FINAL COMPOUND — GPX4-M1

```
CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2CCN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1
```

**ML210 with both 4-chlorophenyl groups replaced by 4-(N-methylcarbamoyl)phenyl.**
Warhead and piperazine untouched.

| Property | ML210 | **GPX4-M1** | Why |
|---|---|---|---|
| MW | 475.3 | **520.5** | >500 favours biliary clearance, away from the proximal tubule |
| logP | 4.75 | **2.16** | Amphipathic, not greasy |
| TPSA | 92.7 | **150.9** | Barrier exclusion; no oral ceiling under an injectable profile |
| **Free HBD in water** | **0** | **2** | The real driver of brain/retina exclusion — *measured, not predicted* |
| Internal H-bonds | 0 | **0** | Donors stay exposed; the design does not self-defeat |
| Charge at pH 7.4 | neutral | **neutral** | Avoids OAT/OCT concentration in the tubule |
| Symmetric | yes | **yes** | One benzhydryl coupling |
| Alerts (incl. metabolic liberation) | — | **none** | No aniline, phenol, acid, Michael acceptor, or masked toxicophore |
| ΔLUMO vs ML210 | — | **−0.32 eV** | Warhead essentially intact |

**Regimen:** GPX4-M1 + an FSP1 inhibitor (icFSP1 class) on an **azacitidine** backbone, as
**maintenance in remission** — matching the only regimen with a demonstrated overall-survival benefit
in this setting.

## What the computational campaign delivered, and what it did not

**Delivered:** a specific, synthesisable, symmetric molecule; a warhead verified electronically intact;
donors verified to survive solvation; a clearance route reasoned from transporter biology; three
independent structural results showing the modified region makes almost no protein contact; and four
liabilities caught before committing (acid/OAT trap, acetanilide, hydroxyl masking, piperazine
false-alert).

**Not delivered:** any evidence of potency. No calculation performed here predicts whether GPX4-M1
inhibits GPX4, and the selectivity question requires QM/MM with transition states — blocked by the
unresolved selenocysteine parameters. **The purified-enzyme assay remains the gate, and it is the same
assay RSL3 and ML162 failed.**

---

# 15. THREE DOCKING METHODS, THREE FAILURES — AND WHAT THEY AGREE ON

Attempted to answer one question: **can GPX4-M1 physically adopt the covalent geometry, or do the
larger amide substituents clash?** Three approaches, all failed, each for a different reason. Recorded
in full because the pattern is the result.

## Attempt 1 — Non-covalent redocking (§7.2)

Weak affinities (−5.7 kcal/mol), nine non-converging poses, nothing within 3.64 Å of the selenium.

**Failure mode: no pocket to score.** Informative — it established that covalent constraint is
mandatory and that non-covalent scores are meaningless here.

## Attempt 2 — Anchored docking, random orientations

Placed the warhead anchor atom 1.98 Å from Sec46 SE in random directions, sampling conformers and
rotations. **Zero clash-free poses out of 1,860 for GPX4-M1 — and zero out of 1,860 for ML210**, a
compound known to bind.

**Failure mode: my sampling, not the molecules.** Random directions from a buried atom point mostly
*into* protein. A method that rejects the positive control is broken, not informative.

## Attempt 3 — Anchored docking along solvent-accessible exit vectors

Restricted placement to open directions from the selenium and aimed the molecular long axis outward.

**Result: zero fully-open exit vectors out of 400 directions — in *both* the apo structure and the
ligand-bound structure with the ligand deleted.**

That is a contradiction on its face: **the crystal contains a ligand covalently bonded at 1.61 Å from
that selenium.** If no open exit vector exists in the very structure where the ligand is bound, the
test cannot be measuring what matters.

**Failure mode: straight-ray accessibility is the wrong test for a curved surface groove.** My probe
required an unobstructed straight line from the selenium out to 10 Å. A ligand needs no such channel —
it can bend, and it occupies a groove that curves along the protein surface.

## What the three failures agree on

**This target defeats rigid-receptor structure-based methods**, and it does so for reasons intrinsic
to the site rather than to any one algorithm.

The per-atom burial analysis (§8.1) was the method that actually worked, and it already told us why:
mean burial 0.34, only 6 of 30 atoms more than half buried, the warhead anchored and the rest lying in
solvent. **There is no pocket, no channel, and no clean exit vector — only a shallow curved surface
with a covalent tether at one end.**

Rigid docking assumes a cavity to fill. There isn't one.

## What would actually answer the question

- **Flexible-receptor covalent docking** — the ligand tethered at the reactive atom, receptor
  side-chains free to move. Needs a covalent-capable engine *and* selenocysteine parameters, which
  remain the standing blocker (§7.2).
- **MD of the covalent adduct** — build the bond, simulate, observe whether the substituents are
  accommodated. This is the most credible route with current tooling, and it sidesteps pose
  *prediction* entirely by starting from the bonded state.
- **QM/MM** for the reaction step itself, which is the only thing that addresses potency.

## The honest interim position on GPX4-M1

**Steric feasibility is unproven, but the burial evidence argues it is not the risk it appears to be.**
The positions we modified sit at burial 0.06–0.17 — essentially in solvent — so larger substituents
there extend into open space rather than into protein. Attempt 2 rejected ML210 as firmly as GPX4-M1,
which means it carries no information about their *relative* fit.

**No result so far distinguishes GPX4-M1 from ML210 sterically.** Given that they differ only at
solvent-facing positions, that is the expected outcome — but it is an absence of evidence, not
evidence of absence.

---

# 16. IT WORKS — CALIBRATED ANCHORED FIT

After three failed docking approaches (§15), the fourth worked. The fix came from diagnosing a bug,
and the interpretation came from a positive control.

## The method that worked

Per Rule 14 — **start from the bonded state, not from pose prediction:**

1. Build the **covalent adduct** explicitly: `CH₃Se–` (standing in for the Sec46 sidechain) bonded to
   the warhead carbon. Optimise with **GFN2-xTB in implicit water**. Quantum mechanics handles
   selenium natively, **which sidesteps the force-field parameter problem that blocked every earlier
   attempt.**
2. Generate ~150 conformers of the adduct.
3. Superimpose the adduct Se onto the crystallographic Sec46 SE, and align the Se–C bond onto **the
   experimentally observed Se→C20 vector from 6HKQ** — not a guessed direction.
4. Scan 60 rotations about that bond; score the maximum van der Waals overlap against the receptor.

## The bug that had invalidated every previous run

Every attempt returned an identical **1.16 Å** overlap regardless of molecule, conformer count, or
sampling. Identical results across chemically different molecules is a systematic artifact, not
chemistry.

The cause:

```
required C···Se separation in the clash test = 1.70 + 1.90 − 0.5 = 3.10 Å
actual covalent Se–C bond length            = 1.98 Å
registered overlap                          = 1.12 Å
```

**The test was scoring the covalent bond itself as a steric clash.** Sec46 SE sat in the receptor
array, and the ligand carbon bonded to it is 1.98 Å away by construction. Bonding partners must be
excluded from a clash test.

*This is the single most instructive bug of the campaign: a constant, plausible-looking number that
was pure artifact, surviving three rounds of "more sampling" because more sampling cannot fix a
mis-specified objective.*

## The result

Sec46 SE and CB excluded as covalent partners:

| Adduct | Conformers | Residual overlap | What it is |
|---|---|---|---|
| **ML162** | 145 | **0.55 Å** | **POSITIVE CONTROL — the ligand actually present in 6HKQ** |
| ML210 | 137 | **0.39 Å** | Known selective GPX4 inhibitor |
| **GPX4-M1** | 148 | **0.42 Å** | **Our candidate** |

**The compound we know binds covalently shows the largest residual overlap.** That is what makes the
number interpretable: **0.55 Å is demonstrably tolerable**, because a molecule scoring it is sitting
in the crystal. The residual reflects rigid-receptor and rigid-conformer approximations — real side
chains move.

**SUPERSEDED — see `tier1-tier4-results.md`, "Anchored covalent fit, recalibrated".** The protocol's
own error against the deposited crystal pose is ~0.58 Å, so 0.02–0.06 Å differences between compounds
are noise. The test shows "no steric problem"; it cannot rank compounds. Original text follows:

**GPX4-M1 at 0.42 Å fits better than the positive control and is indistinguishable from ML210 at
0.39 Å.**

## What this establishes

**The steric question is answered.** The larger N-methylamide substituents are accommodated at the
covalent geometry — they extend into the solvent-facing region that §8.1 measured at 0.06–0.17 burial,
exactly as predicted.

Combined with the earlier results, four independent lines now support the design:

1. The modified positions make almost no protein contact (burial 0.06–0.17)
2. There is no pocket to disrupt (26 Å³ within 5 Å of Se)
3. The warhead is electronically insulated (ΔLUMO −0.32 eV)
4. **The adduct is sterically accommodated, calibrated against a known binder**

## What it does not establish

Still no potency. Steric feasibility says the molecule *can* sit there; it says nothing about whether
the warhead reacts fast enough, or selectively enough, to matter. That requires QM/MM barriers, and
ultimately the purified-enzyme assay.

**Methodological note for the skill:** the positive control did the decisive work twice — first
exposing a broken method (§15, Attempt 2 rejected ML210), then making a good one interpretable
(0.55 Å as the tolerance benchmark). Never run a scoring protocol without one.

---

# 17. POTENCY — THE ARGUMENT COMPLETED

Potency was the last open question. It cannot be computed *de novo* here — barriers for the masked
nitrile-oxide pathway need QM/MM. But it can be established **by inheritance**, and that argument is
now complete.

## The logical structure

GPX4-M1 carries **the identical warhead to ML210** — the same 5-methyl-4-nitro-isoxazole-3-carbonyl,
atom for atom. ML210's potency against GPX4 is experimentally documented. So the question is not
"how potent is this molecule" but **"does anything about the substitution change the chemistry that
makes ML210 potent?"**

That is answerable, and it has three parts: does the warhead still generate its reactive species,
is the electrophile still electrophilic, and can the molecule still reach the target geometry.

## Part 1 — Does it still unmask?

ML210 works by eliminating HNO₂ to unmask a nitrile oxide. The step is governed by how activated the
C–NO₂ bond is. Measured with GFN2-xTB in implicit water, Wiberg bond orders and atomic charges:

| Descriptor | ML210 | GPX4-M1 | Δ |
|---|---|---|---|
| **C–NO₂ Wiberg bond order** | 1.039 | 1.045 | **+0.006** |
| q(C bearing NO₂) | −0.035 | −0.034 | +0.001 e |
| q(NO₂ group) | −0.299 | −0.317 | −0.018 e |
| **q(C3, the electrophilic carbon)** | **+0.073** | **+0.072** | **−0.0003 e** |

**The electrophilic carbon differs by 0.0003 e.** The leaving-group bond order differs by 0.006.
**The unmasking chemistry is unchanged.**

## Part 2 — Is the electrophile still electrophilic?

Full-molecule LUMO — the warhead-localised acceptor orbital — shifts by **−0.32 eV** (§13.2). Modest,
uniform across the whole amide series, and attributable to substituent size rather than to any
specific electronic effect. Only the ligand-localised HOMO moves substantially (§7.5).

## Part 3 — Can it reach the geometry?

Anchored on the crystallographic Se→C bond vector, calibrated against the ligand actually present in
the structure (§16):

| | Residual overlap |
|---|---|
| ML162 — **known crystal binder** | 0.55 Å |
| ML210 | 0.39 Å |
| **GPX4-M1** | **0.42 Å** |

Fits better than the positive control; indistinguishable from ML210.

## The completed case

| Requirement | Evidence | Verdict |
|---|---|---|
| Same reactive warhead | Identical by construction; SMARTS-verified on every analog | ✅ |
| Warhead still unmasks | C–NO₂ bond order Δ 0.006; electrophile charge Δ 0.0003 e | ✅ |
| Electrophile intact | ΔLUMO −0.32 eV | ✅ |
| Reaches covalent geometry | 0.42 Å vs 0.55 Å for a known binder | ✅ |
| Modified region makes no contact | Burial 0.06–0.17 | ✅ |
| Donors survive solvation | 0 intramolecular H-bonds, 2 free HBD | ✅ |

**Conclusion: GPX4-M1 should inherit ML210-like potency.** Every property that could plausibly
degrade it has been measured and found unchanged.

## What this is, and what it is not

**This is a well-established inheritance argument, not a potency measurement.** It says: nothing we
changed touches the machinery that makes the parent work. It does not produce an IC₅₀, and it cannot —
that requires the purified-enzyme assay.

**The residual risks are not about potency:**

- **Selectivity over TXNRD1** still rests on the masking mechanism, which was argued (§9.2) but not
  computed. Reaction barriers require QM/MM.
- **Kidney and T-cell tolerance** remain design hypotheses (§8, §9).
- **Durability** — whether suppressing LSCs translates into survival — is the serial-transplant
  question, and no computation addresses it.

**What the campaign delivers:** a specific, synthesisable, symmetric molecule with a warhead
demonstrated intact by four independent measurements, properties re-engineered for chronic
maintenance dosing, a clearance route reasoned from transporter biology, and steric feasibility
calibrated against a known binder — plus five liabilities caught before commitment (acid/OAT trap,
acetanilide, hydroxyl masking, scaffold false-alert, covalent-bond-as-clash artifact).

That is as far as hardware takes it. **The next step is synthesis and the purified-enzyme assay.**

---

# 18. SYNTHESIS ROUTE AND ASSAY DESIGN

## 18.1 One thing I will not do

**An enzyme assay cannot be simulated.** It is the empirical test that computation exists to earn the
right to run. Producing numbers for it would be fabricating data, and those numbers would be
indistinguishable in a document from real ones.

What *can* be done, and is done below: propose a real synthetic route, and specify the assay protocol
precisely enough to execute — including the controls that would have caught the field's own mistakes.

## 18.2 Synthetic accessibility

| Metric | Value |
|---|---|
| Formula / MW | C₂₆H₂₈N₆O₆ / 520.5 |
| **SA score** (1 easy → 10 hard) | **2.65 — easy** |
| **Stereocentres** | **none** |
| Rings / rotatable bonds | 4 / 7 |

**The symmetry choice pays off here concretely.** The benzhydryl carbon is a stereocentre *only* if
the two aryl groups differ. GPX4-M1 is symmetric, so it has **no stereocentres**: no enantiomers, no
chiral separation, no eutomer/distomer problem, no doubling of the tox package. That was the practical
reason for preferring a symmetric analog over the higher-QED mixed candidates, and it is worth more
than the QED difference.

## 18.3 Proposed route

Three fragments, two bond-forming steps at the end.

```
    4,4'-benzophenonedicarboxylic acid          5-methyl-4-nitroisoxazole-
                    │                            3-carboxylic acid
       (1) MeNH2, HATU/DIPEA                              │
                    ↓                                     │
      4,4'-bis(N-methylcarbamoyl)benzophenone             │
                    │                                     │
       (2) NaBH4, MeOH                                    │
                    ↓                                     │
              benzhydrol                                  │
                    │                                     │
       (3) SOCl2 (or MsCl/Et3N)                           │
                    ↓                                     │
            benzhydryl chloride                           │
                    │                                     │
       (4) piperazine (excess), base                      │
                    ↓                                     │
        1-benzhydrylpiperazine  ────────(5) HATU/DIPEA────┘
                                          ↓
                                      GPX4-M1
```

**Step notes and risks, stated honestly — I am not a synthetic chemist and these need a real one:**

- **Step 3 is the risk.** Converting the benzhydrol to a leaving group under SOCl₂ in the presence of
  two secondary amides is the step most likely to misbehave. **Mitigation: reorder.** Carry the
  diester (dimethyl 4,4′-benzophenonedicarboxylate) through steps 2–4, then install the
  N-methylamides last by aminolysis. That keeps the acid-sensitive amides out of the chlorination.
- **Step 5 must be last.** The 4-nitroisoxazole is the reactive warhead; it should meet the molecule
  as late as possible and see no strong nucleophile, no reduction, and no strong base after
  installation.
- **Excess piperazine in step 4** suppresses bis-alkylation; mono-Boc-piperazine with a later
  deprotection is the cleaner alternative if selectivity is poor.
- Starting materials are common: 4,4′-benzophenonedicarboxylic acid and methylamine are catalogue
  items; the nitroisoxazole acid is the ML210 fragment and is literature-known.

**Backups already characterised** (§13.4) if a step fails: 3-CONHMe (same properties, meta vector),
4-CONHMe-3-F (fluorine blocks para-hydroxylation), 4-CH₂CONHMe.

## 18.4 Assay cascade — with the controls that matter

Ordered so that the cheapest disqualifying result comes first.

### Gate 1 — Cell-free inhibition of purified GPX4 *(the gate)*

**This is the assay RSL3 and ML162 failed, and their failure went unnoticed for years.** It is
non-negotiable and it comes first.

- **Protein:** wild-type human GPX4 with genuine selenocysteine — produced by co-expression with
  **SBP2** (selenocysteine-insertion-sequence-binding protein 2) in HEK cells, the method behind
  structures 6HN3/6HKQ. **A U46C mutant is not acceptable** — selenium nucleophilicity is the
  mechanism.
- **Readout:** NADPH-coupled GPX4 activity (glutathione reductase-coupled, phospholipid hydroperoxide
  substrate), measured as A₃₄₀ decay.
- **Controls:** ML210 (positive, known selective), **ML162 and RSL3 as negative controls for GPX4** —
  they should show little or no inhibition of the purified enzyme. If they inhibit, the assay is
  reporting something other than GPX4.
- **Kinetics, not just IC₅₀:** covalent inhibitors need k_inact/K_I, from time-dependent inhibition.
  A single-timepoint IC₅₀ is misleading for this mechanism.

### Gate 2 — Selectivity counter-screen

- **TXNRD1** and **glutathione reductase**, described in the literature as imperative counter-screens.
- Rationale is specific: 26% of compounds inhibiting GPX4 in primary screens also hit TXNRD1.
- Broader: proteome-wide covalent reactivity profiling, since the warhead is an electrophile.

### Gate 3 — Cellular ferroptosis, with mechanism confirmation

- Lipid peroxidation readout (C11-BODIPY) plus viability.
- **Rescue controls prove it is ferroptosis and not general toxicity:** liproxstatin-1 or
  ferrostatin-1 should rescue; a pan-caspase inhibitor should not.
- **Mitochondrial CoQ rescue** tests the §6 prediction directly.

### Gate 4 — Primary AML cells, with the internal control

- **Blast versus non-blast sensitivity in the same marrow sample.** That within-patient comparison is
  what makes the therapeutic window meaningful; a cross-sample comparison does not.
- Then the **CD34⁺CD38⁻ LSC fraction specifically**, not bulk CD34⁺.
- Venetoclax-resistant primary samples, since that is the intended indication.

### Gate 5 — Combination

GPX4-M1 + an FSP1 inhibitor (icFSP1 class) on an azacitidine backbone. Test whether FSP1 blockade
closes the escape route as §6 predicts.

### Gate 6 — The one that decides everything

**Serial transplantation.** Treat a PDX, then transplant survivors into fresh recipients and ask
whether leukemia-initiating capacity is gone. Nothing computational substitutes for it, and every
earlier gate can pass while this one fails — that is precisely what happened to Iomab-B.

## 18.5 On the proposed generative stack

The recommendation to run **FLOWR.root + GenMol + DiffSBDD** with docking and affinity scoring is
sound general advice. **For this target specifically, our own measurements rule most of it out:**

| Proposed component | Applies here? | Evidence from this campaign |
|---|---|---|
| **FLOWR.root** (pocket-conditioned) | ❌ | Requires a pocket. We measured **26 Å³ within 5 Å of the catalytic selenium** against ~400 Å³ molecules. There is no pocket to condition on |
| **DiffSBDD / TargetDiff** (pocket-conditioned) | ❌ | Same reason; also produce non-covalent binders, and §7.2 showed non-covalent binding is not what holds this ligand |
| **Affinity scoring** | ❌ | Redocking the crystal ligand gave −5.7 kcal/mol and 5.9 Å RMSD. **Ranking generated compounds on these scores would have been worthless** |
| **GenMol** (fragment-based) | ✅ | The right tool class — and its job was done here by BRICS decomposition plus warhead-constrained enumeration, 300 analogs with SMARTS integrity gating |
| **RDKit filtering** | ✅ | Used throughout |
| **MD / FEP** | ⚠️ later | Meaningful only from the *bonded* state (Rule 14); pose prediction is the wrong problem here |

**This is not a rejection of the advice — it is the advice colliding with a measurement.** A
pocket-conditioned generator is the correct first choice for a normal target. GPX4 is not a normal
target, and the cheap diagnostics in §7–8 are what established that before any GPU time was spent.

**Where a generative model would genuinely help:** designing an FSP1 inhibitor for the partner arm.
FSP1 has a real binding pocket, and existing tool compounds (icFSP1, viFSP1) have known liabilities —
that is a conventional structure-based problem where FLOWR.root and DiffSBDD are appropriate.

---

# 19. STATE OF AFFAIRS — 2026-08-29

Second computational pass. **The lead molecule changed, the combination strategy changed twice, and
nine earlier claims in this campaign were overturned.** [FINDINGS.md](../FINDINGS.md) is the single
current-state document; this section records what moved and why.

## 19.1 The lead is now GPX4-M3, with M1 retained

The **linker vector had never been explored** — every earlier cycle varied only the two aryl groups.
Opening it produced M3: piperazine → 2-oxopiperazine, warhead untouched.

| | M1 | **M3** |
|---|---|---|
| Basic N (OCT2 kidney trap) | 1 | **0** |
| hERG pharmacophore | moderate-high | **low** |
| cLogP / logS | 2.16 / −4.30 | **1.68 / −4.08** |
| **Salt formation for injection** | **available** | **not available** |

One change removed a liability I had identified myself in §11.1 and then left in the molecule.
**But M1 is not dropped:** removing the basic nitrogen also removed the standard route to an injectable
salt. That is a trade-off, not a ranking.

## 19.2 What is newly established

- **The design premise is confirmed under a mobile protein.** MD: the modified amide arms are **46% of
  total ligand SASA and never buried**; the buried atoms are the warhead region. Anchor buried, payload
  in water.
- **Selectivity has a structural basis.** GPX4 Sec46 is **0.93 buried**; TXNRD1's catalytic Sec is
  **0.23–0.38** (62–76% exposed). **Accessibility runs against selectivity** — the off-target is the
  easier one to reach. Selectivity comes from the masked warhead plus GPX4's enclosed groove.
  **This is a structural argument against ever simplifying the nitroisoxazole.**
- **The "no pocket" tension is resolved:** 26 Å³ volume *with* 0.93 burial means a **narrow groove**,
  not a cavity — which is why docking fails but a tethered ligand fits.

## 19.3 The strategy changed: the value is in the partner, not the molecule

Three independent findings converge:

1. Resistance model: a **10× potency gain buys 3.2 months**
2. Covalent PK/PD: occupancy **saturates above kinact/K_I ≈ 0.5**
3. Dose scan: **4× dose buys 1.9 months**

And the partner drug analysis, twice corrected:

| Partner | Modelled delay | Basis |
|---|---|---|
| FSP1 inhibitor | **+0** | escaping clone is ferroptosis-*incompetent* |
| **SLC7A11 agent** | **+14 mo** | erastin-type killing is **less ACSL4-dependent** (published) |
| **Venetoclax** (apoptosis) | **control** | fully orthogonal |

**FSP1i is withdrawn as a durability strategy** (retained for patient selection in FSP1-high /
FLT3-ITD⁺ disease). **Durability requires a partner that does not depend on ACSL4.**

## 19.4 The liability that matters most

**Solubility ~0.03 mg/mL — griseofulvin territory, 30–100× short for a daily injectable.** Consensus of
three models, anchored on compounds with measured values (griseofulvin reproduced exactly). Symmetry
bought the no-stereocentre advantage and probably costs solubility, since symmetric rigid molecules pack
and melt high. **A measured melting point and intrinsic solubility settle this; nothing else does.**

## 19.5 Honest limits

- **Reaction barrier: not obtained.** Three constrained-scan protocols failed — basin-hopping,
  over-constraint, and optimisation failure at the transition region. It needs a genuine
  eigenvector-following TS search, not another scan variant. **It was corroborative, not load-bearing.**
- **Selenoproteome-wide scan: impossible.** 18 of 20 human selenoproteins are absent from AlphaFold DB
  (Sec is encoded by UGA and the pipelines drop those sequences). **Chemical proteomics is the only
  route.**
- **kG ≈ 0** — ACSL4 loss is near-complete protection against GPX4 inhibitors. **This costs 1.7 months,
  not the programme:** below the kG/r threshold the exact value barely matters. Monotherapy still models
  to **~+20 months against the QUAZAR bar of +9.9**.

## 19.6 The three experiments that would move this furthest

All cheap, all wet-lab:

1. **Measured solubility and melting point** — gates the injectable route
2. **kG on ACSL4-knockout AML lines**, with erastin-type and venetoclax comparator arms
3. **Proteome-wide covalent profiling** — the only route to selenoproteome selectivity

And the one that decides everything: **serial transplantation**, with a pre-registered kill criterion.

---

# 20. WHAT DIDN'T WORK — the running list

Kept deliberately. Most of these produced a confident-looking number before being caught, and the
pattern is more useful to a reader than any single result.

## 20.1 Methods that were structurally incapable of the question asked

| # | Attempt | What happened | Why |
|---|---|---|---|
| 1 | **Non-covalent docking** | affinities −5.7 kcal/mol, crystal ligand redocked 5.9 Å off | **There is no cavity to score.** 26 Å³ within 5 Å of the catalytic selenium |
| 2 | **Frontier-orbital selectivity analysis** | returned **exactly 0.00** | The warhead orbital cancels algebraically. The method could not have answered it |
| 3 | **Anchored docking, random orientations** | 0 clash-free poses from 1,860 — **and 0 for ML210, a known binder** | Random directions from a buried atom point into protein. A method that rejects the positive control is broken, not informative |
| 4 | **Straight-ray exit-vector search** | 0 open vectors out of 400 — **in the very structure that contains a bound ligand** | A ligand can bend; it does not need a straight channel |
| 5 | **Selenoproteome-wide structural scan** | 18 of 20 selenoproteins absent from AlphaFold DB (2/2 controls present) | Selenocysteine is encoded by UGA; prediction pipelines drop those sequences. **Not fixable — the structures do not exist** |

## 20.2 Three barrier protocols, three different failures

The one calculation that would directly test the selectivity mechanism. **Not obtained.**

| Version | Setup | Failure |
|---|---|---|
| **v1** | freeze forming bond, rebuild each point | **Basin hop** — 46 kcal/mol cliff across one 0.2 Å step. The "+23.6 barrier" was just the last point before the surface snapped |
| **v2** | freeze both bonds, chain geometries | **Over-constrained** — optimisation failed at the transition region, profile inflated to +48 against ~20–25 expected for an SN2 in water |
| **v3** | freeze forming bond, chain geometries | Relaxed one point further than v2, then **failed in the same place** |

**v1 to v2 changed two things at once** (constraint count *and* geometry source), so v2's failure could
not be attributed to either. Chaining was the fix; the second constraint was the new bug. **One variable
per attempt would have found this in half the compute.**

**Stopped at three.** This needs a genuine eigenvector-following transition-state search, not a fourth
scan variant. It was corroborative, not load-bearing.

## 20.3 Bugs that produced plausible wrong answers

| Bug | Symptom | Cause |
|---|---|---|
| **Covalent bond scored as a steric clash** | identical **1.16 Å** overlap for every molecule across three runs | Sec46 SE left in the clash array; the bonded carbon sits 1.98 Å away by construction |
| **Wrong catalytic residue** | crystal ligand sat **34.28 Å** from the "catalytic" site | Matching `CYS/SG` selected **Cys10**, the first such atom in the file, not Sec46 |
| **Radical-bearing adduct SMILES** | reversed an already-committed burial comparison | `C(=[N+][O-])` puts three bonds on a cationic nitrogen — one radical electron. Correct form is the oximate `C(=N[O-])` |
| **Ring-closure digit collision** | 3 of 4 compounds silently skipped | Regex assumed digit `1`; M1/M3 use `3`, and ML210 writes its carbonyl as `O=C(...)` |
| **Zero shortlisted candidates** | every analog rejected | The basic-amine filter matched the **core piperazine**, present in ML210 and every analog |
| **Ligand could not accept its own bond** | stiff 1.82 Å tether settled at **2.41 Å** | H-capping the attachment carbon to satisfy the parameteriser left it valence-saturated. **The atom added to make it run made the modelled reaction impossible** |
| **Metric computed over failed points** | clean-looking "3.89 kcal/mol barrier" | 5 of 7 points were `nan`; `nanargmax` returned the maximum of the two survivors |
| **Index captured before atom deletion** | would have pointed at the wrong atom | Deleting a hydrogen renumbers everything after it |

## 20.4 Reasoning errors — mine, not the software's

| Error | Correction |
|---|---|
| **Control tested the wrong quantity** | Judged GFN2-xTB "sign-inverted" using a *thermodynamic* number against a *kinetic* claim. C–S is stronger than C–Se, so the sign was correct chemistry. **GFN2 had it right; GFN1, which I endorsed, had it wrong.** Both verdicts backwards |
| **"No DFT engine on Windows"** | One failed `pip install pyscf`. `conda install psi4` works. **A hard compute barrier reported after a single command** |
| **"M3 dominates M1 on every axis"** | Removing the basic nitrogen also removed salt formation — the standard injectable route |
| **"FSP1i closes the escape route"** | Withdrawn for durability; the escaping clone is ferroptosis-*incompetent* |
| **"kG ≈ 0 is devastating"** | Costs **1.7 months**. kG only dominates *above* the kG/r threshold |
| **"Competitive release ⇒ lower doses are better"** | Dose-response was flatly monotonic. The corollary did not follow from the mechanism |
| **Presented "pair with an orthogonal mechanism" as a strategic discovery** | It is a **rediscovery** — a 2025 Blood meeting abstract reports ML210 + venetoclax synergy in CD34⁺CD38⁻ cells from venetoclax-resistant patients. The model reproducing it is validation, not novelty (§23) |
| **"M1 fits better than the positive control"** | Difference below the protocol's own 0.58 Å resolution |
| **"TXNRD1 tail unresolved because mobile"** | Resolved in 3QFA; both structures are Sec-to-Cys mutants |
| **Broke the user's environment** | Installed a chemistry stack into base conda; it pulled a conda `pytorch` over a pip one and broke torch |
| **Scripts printed conclusions their own tables contradicted** | Twice. Narrative written into `print` statements before the numbers existed |

---

# 21. WHAT WORKED — the surviving case for GPX4-M3

```
CNC(=O)c1ccc(C(c2ccc(C(=O)NC)cc2)N2C(=O)CN(C(=O)c3noc(C)c3[N+](=O)[O-])CC2)cc1
```

ML210 with both 4-chlorophenyls replaced by 4-(N-methylcarbamoyl)phenyl **and** the piperazine replaced
by a 2-oxopiperazine. **Warhead untouched, atom for atom.**

## 21.1 Measurements that survived every check

| Finding | Number | Method |
|---|---|---|
| **Modified arms sit in solvent under a mobile protein** | **46% of total ligand SASA, never buried in any frame** | explicit-solvent MD, GPU |
| **Protein fold stable with ligand bound** | Cα RMSD 0.76 Å mean | same trajectory |
| **Adduct sterically accommodated** | 0.29 Å overlap vs 0.35 Å for the crystal ligand re-derived by the same protocol | anchored covalent fit, calibrated on the deposited pose |
| **Warhead electronically insulated from our edits** | C–NO₂ bond order Δ **0.006**; electrophilic carbon Δ **0.0003 e** | GFN2-xTB, implicit water — C/N/O/H only, no selenium involved |
| **The site is a narrow groove, not a cavity** | 26 Å³ volume **with** 0.93 burial | pocket mapping + per-atom burial |
| **Selectivity has a structural basis** | GPX4 Sec46 **0.93** buried vs TXNRD1 Sec **0.23–0.38** | SASA on experimental structures |
| **No stereocentres** | 0 | symmetry makes the benzhydryl carbon non-stereogenic |
| **Synthetically easy** | SA score **2.65** | RDKit |
| **Two safety liabilities removed** | basic N 1 → 0; hERG moderate-high → low | ADMET panel |

## 21.2 The design logic, and why it holds

**Anchor buried, payload in water.** The only positions changed are the ones the MD shows contribute
nearly half the molecule's solvent contact and never touch protein. The buried atoms are the warhead
region. The substitution is tolerated because it was placed where the protein isn't.

**Selectivity is inherited, and now structurally explained.** ML210 is experimentally GPX4-selective and
does not hit TXNRD1, unlike the chloroacetamides ML162 and RSL3. M3 carries that warhead unchanged. The
structural measurement explains *why* it has to work this way: **accessibility runs against
selectivity** — TXNRD1's selenol is the *more* exposed one, so shape cannot discriminate. **Only the
masked warhead plus GPX4's enclosed groove can.** This is a standing argument against ever
"simplifying" the nitroisoxazole to a direct electrophile.

**Potency is inherited too, and does not need improving.** Three independent results agree: 10× potency
buys 3.2 months, occupancy saturates above kinact/K_I ≈ 0.5, and 4× dose buys 1.9 months.

## 21.3 Dosing, settled

| Parameter | Requirement |
|---|---|
| Schedule | **daily, continuous** — beats every pulsed schedule at matched total dose |
| Half-life needed | **~4 h** — effect duration is set by target resynthesis, not the plasma curve |
| Robustness | a missed dose costs little; the target stays inactivated |
| Dose escalation | **do not** — flat response, no tolerability benefit |
| Deployment | **deepest remission** — 3 logs of cytoreduction beats a 10× better drug |

## 21.4 Open liabilities on this molecule

| Liability | Severity |
|---|---|
| **Solubility ~0.03 mg/mL — 30–100× short for injection** | **highest**; symmetry likely contributes |
| M3 cannot form a salt; M1 can | **carry both forward** |
| Nitroaromatic reduced to arylamine | inherited class risk |
| Predicted DLT: anaemia, erythroid progenitors | monitorable by routine CBC |
| Window depends on **vitamin E status** | belongs in eligibility criteria |

## 21.5 The reordered priority

**The molecule is good enough; the partner is the open question.** FSP1 inhibition adds nothing — the
escaping clone is ferroptosis-incompetent. An SLC7A11 agent adds ~14 months because erastin-type killing
is **less ACSL4-dependent**. A fully orthogonal agent such as venetoclax crosses the kG/r threshold and
converts delay into control.

**Three cheap wet-lab experiments would move this furthest:** measured solubility and melting point;
kG on ACSL4-knockout lines with erastin-type and venetoclax comparator arms; proteome-wide covalent
profiling. **And serial transplantation decides everything**, with a pre-registered kill criterion.

---

# 22. THE BARRIER CALCULATION — FINAL OUTCOME: NOT OBTAINED

Closing this out rather than leaving it open. **Three protocols, three failures, terminated deliberately.**

## The v3 profile, in full

| form (Å) | break (Å) | kcal/mol | status |
|---|---|---|---|
| 3.20 | 1.98 | 0.00 | ok |
| 2.90 | 1.98 | 3.94 | ok |
| 2.65 | 2.01 | 11.44 | ok |
| 2.45 | 2.03 | 22.68 | ok |
| 2.35 | 2.11 | 30.78 | ok |
| 2.25 | 2.21 | 38.73 | **UNRELAXED** |
| 2.15 | 2.21 | 49.21 | **UNRELAXED** |
| 2.05 | 2.21 | 62.94 | **UNRELAXED** |

**Verdict: Rule 31 veto — the maximum-energy point is unrelaxed, so there is no barrier to report.**

## The diagnostic that makes this unambiguous

**The breaking bond froze at 2.21 Å for the last three points.** While optimisation was succeeding, C–Br
lengthened steadily as the nucleophile approached — 1.98 → 2.01 → 2.03 → 2.11 → 2.21 — which is what a
genuine SN2 progression looks like. The moment optimisation began failing, it stopped moving.

**So the final three energies are pure compression against a frozen geometry, not reaction energetics.**
The profile climbing to +62.9 kcal/mol, against ~20–25 expected for an SN2 in water, is that artifact
accumulating. It never turned over because it never reached a transition state — it was being crushed,
not driven over a hill.

## Why this was stopped rather than iterated

A fourth variant would have been the fourth attempt at the same *class* of calculation. All three
failures share a root cause: **a constrained relaxed scan approaches the transition state from the side,
and the optimiser has to hold a near-singular geometry while a bond breaks.** More constraints
over-determine it (v2); fewer let it fall off (v1); the intermediate case delays the failure without
preventing it (v3).

**What this actually needs:** an eigenvector-following transition-state optimisation — a method that
walks *to* the saddle point deliberately rather than creeping toward it on a grid — with better
geometries than HF/def2-SVP, and probably a Hessian at the starting guess. That is a different class of
calculation and a different compute budget.

## What is lost, and what is not

**Lost:** a computed ΔΔG‡ (Cys − Se). The masking-kinetics hypothesis in §9.2 remains an argument rather
than a number.

**Not lost — the selectivity case never rested on it:**

1. **Experimental inheritance.** ML210 is documented as GPX4-selective and does not hit TXNRD1, unlike
   the chloroacetamides. GPX4-M3 carries that warhead atom for atom.
2. **Measured structure.** GPX4 Sec46 is 0.93 buried; TXNRD1's catalytic Sec is 0.23–0.38.
   **Accessibility runs against selectivity**, so shape cannot be doing the discriminating — which is
   itself evidence that the masking is.

**Both are stronger evidence than a ±5 kcal/mol computed barrier would have been.** The calculation was
always corroborative. Recording its failure honestly costs the programme nothing it was relying on.

## The experiment that settles it

**Proteome-wide covalent profiling** — activity-based protein profiling against the full cysteine and
selenocysteine proteome. Given that the selenoproteome is absent from structure databases (§20.1), this
was already the only route to a proteome-scale answer. The failed calculation does not change that; it
just removes the consolation prize.

---

# 23. THE PARTNER QUESTION IS ALREADY ANSWERED — and the model rediscovered it

The systems modelling concluded that durability requires a partner with an **orthogonal death
mechanism**, not a second ferroptosis arm, and named venetoclax as the archetype. **That combination has
already been tested, with ML210 specifically, and it works.**

## The published result

**ML210 + venetoclax is synergistic in AML**
([Blood 2025 meeting abstract](https://doi.org/10.1182/blood-2025-5050)):

| Cell line | Combination index |
|---|---|
| OCI-AML3 | 0.71 |
| MOLM13 | **0.53** |
| MV4;11 | 0.57 |

*(CI < 1 = synergy.)*

And the parts that matter most for this programme:

- **Venetoclax-resistant lines showed *more* prominent synergism** than venetoclax-sensitive ones
- **Synergism was observed in CD34⁺CD38⁻ stem/progenitor cells** from both venetoclax-resistant and
  venetoclax-naive patients — **the exact population this programme targets**
- Recapitulated in doxycycline-inducible GPX4-knockdown cells, confirming the effect is **on-target**

## What this does to the programme, honestly

**It validates the model and removes a novelty claim.**

The resistance model independently predicted that (a) a second ferroptosis arm adds nothing, (b) an
orthogonal-mechanism partner converts delay into control, and (c) the effect should be strongest in
cells that have escaped other pressure. **All three match the published data.** A model reproducing a
known experimental result it was not fitted to is the best validation available here.

**But the combination is not novel, and I should not have implied it was.** When the model produced
"pair with an orthogonal mechanism" I presented it as a strategic redirection. It is a *rediscovery*.
The synergy data was already in this project's evidence base — it is what made the venetoclax-resistant
indication credible in the first place.

## What is actually novel, then

**Not the combination. The molecule, and the framing.**

| Element | Novel? |
|---|---|
| GPX4 as an AML target | no — established |
| GPX4 inhibitor + venetoclax | **no — published, with ML210** |
| Activity in venetoclax-resistant LSCs | no — published |
| **GPX4-M3 as a molecule** | **yes** — property-engineered for chronic dosing: no basic nitrogen, no hERG pharmacophore, 3 log units less lipophilic than ML210, no stereocentres |
| **Chronic maintenance framing** | **yes in this context** — daily gentle dosing, modelled schedule, deployment in deepest remission |

**This is a stronger position than proposing an untested combination, not a weaker one.** The partner is
de-risked by published data in the target cell population; the contribution is a molecule fit for
chronic administration, which ML210 is not (logP 4.75, hERG pharmacophore, essentially insoluble).

## The revised clinical proposition

**GPX4-M3 + venetoclax, as maintenance, in deepest remission.**

- The **combination** has published synergy in CD34⁺CD38⁻ cells from venetoclax-resistant patients
- The **schedule** comes from this campaign: daily, continuous, ~4 h half-life sufficient, dose
  escalation pointless
- The **molecule** is the new part, and its remaining gate is solubility (§21.4)

**And it sharpens the kG experiment.** The proposed ACSL4-knockout study now has a concrete positive
control: venetoclax should retain killing where GPX4-M3 alone does not. If it does not, the orthogonality
assumption fails and the model is wrong about the mechanism of rescue.

---

# 24. ATTACKING THE SOLUBILITY BLOCKER — GPX4-S1

Solubility is the highest-severity liability (§21.4). Ten analogs designed under three hard constraints:
**warhead untouched**, **no basic nitrogen reintroduced** (that was the kidney/heart fix), **no
stereocentres**.

## 24.1 Results

| Candidate | cLogP | Predicted mg/mL | vs M3 |
|---|---|---|---|
| **S1 bis-hydroxyethylamide** | **0.41** | **0.324** | **11×** |
| S4 bis-sulfonamide | 0.78 | 0.127 | 4× |
| S3 bis-primary amide | 1.16 | 0.124 | 4× |
| **M3 (current lead)** | 1.68 | 0.029 | 1× |
| S6 meta-amide | 1.68 | 0.029 | 1× |
| S5 bis-methoxyethyl | 1.72 | 0.027 | 1× |
| S7 ortho-F twist | 1.96 | 0.011 | 0.4× |
| S8 N,N-dimethylamide | 2.37 | 0.007 | **0.2× — worse** |
| S2 bis-morpholino | 1.91 | 0.007 | **0.2× — worse** |

**All ten keep the warhead intact, carry no basic nitrogen, and have no stereocentres.**

**Note S8 and S2:** capping the amide N–H (S8) or adding a bulky morpholine (S2) made solubility
**four times worse**. Adding polarity is not the same as adding solubility — removing a hydrogen-bond
donor costs more than the added heteroatoms gain.

## 24.2 The masking check — the trap that killed an earlier analog

An earlier candidate (M2, bis-hydroxyethyl ether) counted 2 donors on paper and had **zero free donors**
once optimised in 3D: the hydroxyls folded back onto the molecule. Every 2D descriptor still counted
them. **Any new polar group must be checked for this.**

Conformer analysis, counting donors still pointing at solvent:

| Candidate | Donors on paper | Mean free in 3D | Verdict |
|---|---|---|---|
| M3 | 2 | 1.90 | fine |
| **S1** | **4** | **3.67** | **passes — not masked** |
| S3 | 4 | **4.00** | fully available |
| S4 | 2 | 2.00 | fully available |

**S1 survives the check.** Its hydroxyls stay available to water, unlike M2's.

## 24.3 Why S1 is the right pick

**11× solubility for one substituent change**, and the change is on the arms — the positions the MD
showed contribute 46% of the molecule's solvent contact and **never touch protein**. Longer arms extend
further into water, which is the direction that is already free.

**The metabolic liability is not a liability here.** Primary alcohols are cleared fast — oxidised or
sugar-conjugated. Normally that is a problem. **For this drug it is not:** the PK/PD modelling (§18)
showed a **~4-hour half-life is sufficient**, because the effect outlives the drug — the target stays
disabled until the cell rebuilds it. **Fast clearance is affordable here in a way it would not be for a
conventional drug.**

## 24.4 Still not enough on its own

**0.32 mg/mL against a practical need above 1 mg/mL.** S1 closes most of the gap but not all of it.

**The realistic path is S1 plus formulation**, not S1 alone — a co-solvent or cyclodextrin vehicle
starting from 0.32 mg/mL is routine, where starting from 0.029 mg/mL is not.

**And this remains predicted, not measured.** Three models agreeing is not an experiment. The
recommendation is unchanged: **measure melting point and intrinsic solubility on M3 and S1 together** —
it is cheap, and it either dissolves the problem or sizes it properly.

## 24.5 What still needs checking on S1

| Open | Why |
|---|---|
| Anchored covalent fit | Arms are longer; burial says solvent-facing, but verify |
| hERG / ADMET panel | Re-run — the panel was done on M3 |
| Synthetic route | Hydroxyethylamine coupling instead of methylamine; likely needs the alcohol protected during the warhead step |

**Status: S1 is a candidate, not yet a replacement lead.** M3 remains the lead until S1 clears the fit
and ADMET checks.

---

# 25. THE PERMEABILITY PROBLEM — a flaw in the whole optimisation direction

**The target enzyme is inside the cell. The drug must cross a membrane to reach it. I never checked
whether it can.**

## 25.1 The calibration

Not a rule of thumb — six GPX4 inhibitors that demonstrably kill cells:

| Compound | TPSA (Å²) | cLogP | H-bond donors |
|---|---|---|---|
| FIN56 | 17.1 | 3.46 | 0 |
| ML162 | 46.6 | 3.48 | 0 |
| Altretamine | 48.4 | 0.07 | 0 |
| JKE-1674 | 56.1 | 4.08 | 1 |
| RSL3 | 63.7 | 4.27 | 0 |
| **ML210** (our parent) | **92.7** | 4.75 | 0 |
| | | | |
| GPX4-M1 | **150.9** | 2.16 | 2 |
| **GPX4-M3 (lead)** | **168.0** | 1.68 | 2 |
| **GPX4-S1** (solubility fix) | **208.4** | 0.41 | 4 |

**Every known cell-active GPX4 inhibitor sits at or below 92.7 Å² polar surface area with at most one
hydrogen-bond donor.** Our lead is **+75 Å² beyond the most polar of them**, with double the donors.
The solubility fix took it to **+116 Å² with four donors.**

**That is not a marginal concern. There is no precedent in this chemotype for a molecule as polar as
ours reaching an intracellular target.**

## 25.2 How this was missed

The per-atom burial analysis told me which positions face solvent and could therefore carry substituents
**without disturbing binding**. That was correct, and the MD confirmed it — the arms are 46% of solvent
contact and never touch protein.

**But "will this disturb binding?" is a different question from "can this reach the protein at all?"**
Burial analysis is blind to the membrane. Every design decision — amides replacing the chlorophenyls,
removing the basic nitrogen, adding hydroxyethyl groups — was locally justified and all of them pushed
the same direction: **more polar, less able to enter a cell.**

**Three separate optimisations, each individually correct, compounding into a molecule that may not
reach its target.**

## 25.3 What this does to the programme

**Criterion 1 (kills the target cells) drops from 🟢 to 🟡.** The inheritance argument was: same warhead,
therefore same killing. **That argument assumed the molecule gets inside, and the property data now
argues against it.**

**It does not invalidate the binding work.** If the molecule reaches GPX4, everything measured about the
fit, burial and warhead integrity still holds. **The question is purely delivery to the cytosol.**

## 25.4 Three ways out, in order of preference

**1. Prodrug — mask the polarity, unmask it inside.** Esterify the hydroxyls and amides so the molecule
crosses as a greasy species; intracellular esterases cleave them and release the active drug, which is
then trapped inside by its own polarity. **This is the textbook solution to exactly this problem** and it
turns the liability into an advantage — polarity becomes a retention mechanism rather than an entry
barrier.

**2. Rebalance — accept some of the risk I designed out.** M1 (TPSA 150.9) is less bad than M3, and
ML210 itself carries the basic nitrogen. **The hERG and kidney liabilities I removed may have been worth
carrying** if removing them costs cell entry. This needs an explicit trade, not a silent one.

**3. Test the assumption before redesigning.** Two arguments that low permeability might be tolerable
here, both weaker than the empirical gap:
- The warhead is **covalent** — every molecule that gets in and reacts is permanently spent, so
  cumulative engagement matters more than instantaneous concentration
- The PK/PD model showed the effect **outlives the drug**, so slow accumulation across daily dosing may
  suffice

**Neither argument is worth much against six comparators with no precedent above 92.7 Å².** A measured
cell-permeability assay settles it and should come before any further property optimisation.

## 25.5 The lesson

**Optimising a molecule against a list of individually-correct criteria can produce a molecule that
fails a criterion nobody put on the list.** Solubility, kidney safety and cardiac safety were all real
and all pushed polarity up. Nothing in the workflow pushed back, because the binding analysis could not
see the membrane.

**Calibrate against known actives early, on every property axis, not just the ones being optimised.**
Six comparators took two minutes to assemble and would have caught this before three rounds of design.

---

# 26. THE LEAD CHANGES BACK — GPX4-C1, and why three design rounds went the wrong way

## 26.1 The trade-off, laid out

| Compound | Polar surface | cLogP | Basic N | Neutral solubility | Enters cells? | Salt possible? |
|---|---|---|---|---|---|---|
| ML210 (parent) | 92.7 | 4.75 | 1 | 0.0001 mg/mL | **yes** | **yes** |
| **C1 des-chloro** | **92.7** | **3.44** | 1 | 0.0021 | **yes** | **yes** |
| C2 bis-4-F | 92.7 | 3.72 | 1 | 0.0008 | yes | yes |
| C3 bis-2-thienyl | 92.7 | 3.56 | 1 | 0.0015 | yes | yes |
| C4 des-Cl + oxopiperazine | 109.8 | 2.97 | 0 | 0.0051 | close | no |
| **GPX4-M3** (was lead) | **168.0** | 1.68 | 0 | 0.0286 | **NO** | **no** |
| GPX4-S1 | 208.4 | 0.41 | 0 | 0.3235 | **NO** | no |

**Nothing in this chemotype is both freely soluble and clearly cell-permeable.** The compounds that get
inside are greasy and do not dissolve; the ones that dissolve cannot get in.

## 26.2 The mistake

**The basic nitrogen was doing two jobs, and I only counted one.**

I removed it to avoid the kidney transporter trap and the cardiac liability. Both real. **But it is also
the handle that lets you make an injectable salt** — and a salt lifts usable concentration far above the
neutral-form number, which is what every solubility model reports.

So removing it cost the salt option. And the amide arms I installed *instead* of chlorophenyls cost cell
permeability. **Two independent losses from one decision, and the decision looked locally correct at
every step.**

**The correct move was much smaller than the one I made.** Simply deleting the two chlorines from ML210
drops greasiness from 4.75 to **3.44** — a 1.3 log-unit improvement, which is most of what the chronic
dosing brief wanted — while **staying inside the permeability window and keeping the salt handle.**

## 26.3 The new lead: GPX4-C1

```
O=C(N1CCN(C(c2ccccc2)c3ccccc3)CC1)c5noc(C)c5[N+](=O)[O-]
```

**ML210 with both chlorines removed. Nothing else changed.**

| | Value | vs ML210 |
|---|---|---|
| Molecular weight | 406.4 | −69 (room to add later) |
| Polar surface | 92.7 | unchanged — **in window** |
| cLogP | **3.44** | **−1.31, better for chronic dosing** |
| Basic nitrogen | 1 | retained — **salt formable** |
| Stereocentres | **0** | symmetric |
| Neutral solubility | 0.0021 mg/mL | **20× better than ML210** |
| Warhead | intact | unchanged |

**Remaining liabilities, now explicit rather than designed away:** the basic nitrogen carries kidney
(OCT2) and cardiac (hERG) risk. **Both are lower at cLogP 3.44 than at ML210's 4.75** — the cardiac
pharmacophore needs lipophilicity as well as the nitrogen — but neither is eliminated. **That is a trade
made with open eyes, not a liability overlooked.**

## 26.4 What survives from the M3 work

Not wasted, but re-scoped:

- **The burial and MD analysis stands.** The arm positions genuinely are solvent-facing and tolerate
  substitution *at the binding site*. That was never the constraint — the membrane was.
- **The linker chemistry stands.** 2-oxopiperazine does remove the basic nitrogen cleanly; it is
  available if the kidney/cardiac risk proves unacceptable in vivo, at a permeability cost now quantified
  (+17 Å²).
- **The systems modelling is compound-independent.** Daily dosing, ~4 h half-life sufficient, potency not
  the lever, partner drug is where the value is — all unchanged.
- **M3 and S1 remain fallbacks** if permeability turns out not to be limiting, which a single assay
  settles.

## 26.5 The lesson, stated bluntly

**Three rounds of design moved away from a viable molecule.** Each round fixed a real problem and each
introduced a worse one, because the criteria being optimised did not include the one that mattered.

**A smaller edit to the parent would have achieved most of the goal.** The instinct to redesign
comprehensively — replace both arms, rebuild the linker — produced a molecule that is better on every
axis I was measuring and probably cannot reach its target.

**Start from the known-active compound and make the minimum change that addresses the brief.** Measure
the full property profile against known actives after every change, including the axes nobody asked
about.

---

# 27. MD COMPLETE — the design premise confirmed, and why it does not rescue M3

Full 20 ns, explicit solvent, protein free to move. **Solvent exposure computed on the solute only** —
including explicit water as an occluder was checked and changes the answer by 4% (189.3 vs 180.9 Å²),
so the earlier preliminary numbers stand.

| Measurement | Full 20 ns | Preliminary (700 ps) |
|---|---|---|
| Ligand total exposed surface | **190.8 ± 10.0 Å²** | 185.4 |
| **The two modified amide arms** | **83.7 ± 5.7 Å² = 44%** | 85.1 = 46% |
| Frames with arms buried | **0 / 200** | 0 / 38 |
| Protein backbone RMSD | 1.16 Å mean, 1.56 Å max | 0.76 |

**The design premise is confirmed.** The groups substituted onto GPX4-M3 account for **44% of the
molecule's entire solvent contact and are never buried in any frame**, while the warhead region stays
buried. Anchor buried, payload in water — measured with the protein moving, not frozen. The fold is
stable throughout (1.16 Å backbone drift is normal equilibration, not unfolding).

## Why this does not rescue GPX4-M3

**It answers a question that was never the problem.**

This measurement says the arms are *tolerated at the binding site* — they do not clash, do not disturb
the fold, and sit in solvent exactly where the burial analysis predicted. **All true, and irrelevant to
whether the molecule can reach that site.**

§25 established the actual constraint: polar surface area 168 Å² against a 92.7 Å² ceiling among GPX4
inhibitors known to kill cells. **A molecule that binds beautifully to a protein it cannot reach is not
a drug.**

**This is the same blind spot in a different form.** The MD, like the burial analysis before it, models
the ligand *already at the target*. Neither can see the membrane. The 44% figure is a correct answer to
"can the protein accommodate these groups", and the programme changed lead because the binding question
was not the binding constraint.

## What the result is still worth

- **It validates the substitution strategy in principle.** If a future analog needs polar groups at
  those positions and can afford the polarity budget, the positions are confirmed as free.
- **It retires the rigid-receptor caveat** that stood over the anchored-fit work (§16).
- **It keeps M3 alive as a fallback** — if a permeability assay shows the polarity ceiling is softer
  than the six comparators suggest, M3's binding case is now fully supported.

**The measurement is sound. The question it answered was not the one that decides the programme.**

---

# 28. THE CEILING WAS TOO STRICT — budget assumption revised

The 92.7 Å² polar-surface ceiling came from **six GPX4 inhibitors — one chemical series.** Tested
against approved covalent drugs whose targets are also **inside the cell**:

| Drug | Target | TPSA | HBD | cLogP |
|---|---|---|---|---|
| osimertinib | EGFR | 87.5 | 2 | 4.51 |
| afatinib | EGFR | 88.6 | 2 | 4.39 |
| ibrutinib | BTK | 99.2 | 1 | 4.22 |
| neratinib | EGFR | 112.4 | 2 | 5.93 |
| acalabrutinib | BTK | 118.5 | 2 | 3.31 |
| bortezomib | 20S proteasome | 124.4 | 4 | 0.36 |
| **nirmatrelvir** | viral Mpro | **131.4** | 3 | 1.10 |

**Range 87.5–131.4, median 112.4. Five of seven exceed the ceiling I had been enforcing.**

*(An eighth entry, sotorasib, was rejected automatically — the SMILES gave MW 479.6 against a published
560.6. The MW assertion is necessary but not sufficient, since a ring-digit collision preserves MW, but
it caught this one.)*

## What this changes

**The real working ceiling for approved covalent drugs at intracellular targets is ~130 Å², not 93.**

| Compound | TPSA | vs revised ceiling (~130) |
|---|---|---|
| **GPX4-C1** | 92.7 | **comfortably inside** |
| **C4 (des-Cl + oxopiperazine)** | **109.8** | **inside — and no basic nitrogen** |
| GPX4-M3 | 168.0 | **+38 — still outside** |
| GPX4-S1 | 208.4 | +78 — far outside |

**M3 is not rescued.** The gap is smaller than I claimed (+38 over the real ceiling, not +75 over a
false one), but it still sits well beyond every approved comparator.

**The middle ground exists after all, and it already appeared in the earlier series.** C4 — des-chloro
ML210 with the 2-oxopiperazine linker — sits at 109.8 Å², *inside* the revised range, **with no basic
nitrogen.** Under the old ceiling it was dismissed as "close but outside". It is now the most
interesting compound in the campaign: cell-permeable by precedent **and** free of the kidney/cardiac
liability.

## Caveats kept explicit

- Bortezomib and nirmatrelvir are unusual (a boronic-acid peptide; a compound co-dosed with a metabolic
  booster). The tighter cluster — the kinase inhibitors — sits at **87–118**.
- TPSA is a proxy. It correlates with membrane crossing; it does not measure it. **A permeability assay
  still settles this**, and remains the single most decision-relevant experiment.
- Covalent drugs plausibly tolerate lower permeability than reversible ones, since every molecule that
  enters and reacts is permanently consumed. That argument is now *supported* by the data rather than
  merely asserted — the covalent set skews higher than typical oral-drug guidance.

**Correcting my own error: I set a ceiling from one chemotype and treated it as a law of nature.** It
cost M3 a fair hearing and nearly cost C4 one.

---

# 29. GPX4-C4 IS THE LEAD — the synthesis of everything learned

```
O=C(N1CC(=O)N(C(c2ccccc2)c3ccccc3)CC1)c5noc(C)c5[N+](=O)[O-]
```

**ML210 with the two chlorines deleted and the piperazine replaced by 2-oxopiperazine.**
Warhead untouched.

## 29.1 Why it wins

| | ML210 | C1 | **C4** | M3 (prev) |
|---|---|---|---|---|
| Polar surface | 92.7 | 92.7 | **109.8** | 168.0 |
| **Inside revised ceiling (~130)** | ✅ | ✅ | **✅** | ❌ +38 |
| cLogP | 4.75 | 3.44 | **2.97** | 1.68 |
| Basic nitrogen (kidney trap) | 1 | 1 | **0** | 0 |
| **hERG risk** | HIGH | MOD-HIGH | **low** | low |
| Solubility (neutral) | 0.0001 | 0.0021 | **0.0051** | 0.0286 |
| Stereocentres | 0 | 0 | **0** | 0 |
| CYP soft spots | 7 | 5 | **4** | 6 |
| **Covalent fit** (control 0.51) | 0.30 | 0.29 | **0.30** | 0.31 |

**C4 dominates C1 outright**: same permeability class, no basic nitrogen, hERG down from MODERATE-HIGH
to **low**, better solubility, fewer metabolic liabilities, lower lipophilicity. The only thing C1 has
that C4 lacks is salt formation — and C4's intrinsic solubility is 2.4× better anyway.

## 29.2 It vindicates part of the M3 work

**The 2-oxopiperazine linker was a good idea applied to the wrong scaffold.**

The M3 campaign made two changes at once: replace both aryl arms with amides, **and** replace the
linker. The linker change was correct — it removes the basic nitrogen cleanly for +17 Å² of polar
surface, which the revised ceiling can afford. **The arm change was the error**, costing +58 Å² that was
never available.

**C4 keeps the good half and drops the bad half.** Three rounds of design were not wasted; they were
mis-combined.

## 29.3 The decision graph

```
                    Is the polar-surface ceiling really 93?
                                    |
                  +-----------------+------------------+
                  | NO - approved covalent drugs       |
                  |      reach 131 (median 112)        |
                  v                                    v
        Ceiling ~130                          [if ceiling had held]
                  |                            only C1/C2 survive
     +------------+-------------+              (basic N mandatory,
     |                          |               hERG risk accepted)
     v                          v
  C4 fits (109.8)          M3 still out (168)
  AND has no basic N       -> fallback only
     |
     v
  Does C4 still bind?  --- anchored fit 0.30 A vs control 0.51 --> YES
     |
     v
  *** C4 = LEAD ***
     |
     +--> Solubility 0.0051 mg/mL, need >1, NO salt handle
     |         |
     |         +--> measure real solubility + melting point   [WET LAB, cheap]
     |         +--> if inadequate: formulation (cyclodextrin / co-solvent)
     |         +--> if still inadequate: fall back to C1 and accept hERG
     |
     +--> Permeability is inferred from TPSA precedent, not measured
               |
               +--> permeability assay: C4 vs C1 vs M3        [WET LAB, decides everything]
                         |
                         +-- C4 permeable  -> proceed, C4 confirmed
                         +-- all fail      -> the polarity budget is tighter than
                                              even the covalent precedent; go to C2/ML210-like
                         +-- M3 permeable  -> ceiling wrong again; M3 returns (best safety)
```

## 29.4 What is still open on C4

| Open | Severity | Resolved by |
|---|---|---|
| **Solubility 0.0051 mg/mL, no salt handle** | **highest** | measured solubility, then formulation |
| Permeability inferred from precedent, not measured | high | permeability assay |
| Novelty — a two-change edit of a published compound | medium | composition-of-matter search |
| Warhead class liability (nitro → arylamine) | inherited | unchanged from ML210 |

**Everything else in the campaign is compound-independent and carries over unchanged:** daily
continuous dosing, ~4 h half-life sufficient, potency not the lever, deployment in deepest remission,
venetoclax as the orthogonal partner, anaemia as the predicted dose-limiting toxicity, vitamin E
status as an eligibility criterion.

---

# 30. THREE BRANCHES — novelty, solubility, regulatory

## 30.1 Branch A — novelty: the improvement we were making already exists

**JKE-1674** is ML210 with the nitroisoxazole replaced by an α-nitroketoxime. It is the **active
metabolite** of ML210, it is **orally active**, and the Broad Institute describe it as *"more suitable
than ML210 for use in animal models or perhaps even patients."*

**That is precisely the brief this campaign set itself** — make ML210 suitable for chronic dosing in a
patient. It was largely met before we started.

Also published: **structure-activity relationships on the warhead**, showing steep SAR — both the oxime
and the nitro group are essential. The chemotype has been worked systematically (Broad, 2018–2020).

**Consequences:**

- **Criterion 8 (novelty) degrades further.** C4 is two edits from ML210; the *direction* of improvement
  is claimed territory, and a better-developed compound in the same series already exists.
- **JKE-1674 is arguably the better scaffold to build from** than ML210 — it is the species that
  actually engages the target, and it is more stable. Building on ML210 means building on a prodrug of
  something already improved.
- **The warhead SAR is closed.** Steep SAR on the oxime and nitro means there is no room to modify the
  warhead for property gain — which was already the working assumption, now confirmed by data rather
  than caution.

## 30.2 Correction — my JKE-1674 structure was wrong

The comparator set that set the polarity ceiling contained a **wrong structure for JKE-1674**. I had
omitted the nitro group.

| | Formula | MW | TPSA |
|---|---|---|---|
| Published JKE-1674 | C₂₀H₂₀Cl₂N₄O₄ | **451.30** | — |
| My SMILES | C₂₀H₂₁Cl₂N₃O₂ | 406.31 ✗ | 56.1 |
| **Rebuilt α-nitroketoxime** | **C₂₀H₂₀Cl₂N₄O₄** | **451.31 ✓** | **99.3** |

**Effect: the GPX4-only ceiling moves from 92.7 to 99.3 Å².** Small, and it does not change any
conclusion — the operative ceiling is ~130 Å² from approved covalent drugs (§28) — but the comparator
set was wrong and is now right.

**This is the fourth structure error caught by a molecular-weight assertion.** The check earns its
place: MW alone cannot prove a structure right, but it reliably catches structures that are wrong.

## 30.3 Branch B — solubility within the budget

C4 sits at 109.8 Å² with ~20 Å² of headroom before the ~130 ceiling. Symmetric substitutions only, so
no stereocentres are created:

| Candidate | TPSA | cLogP | mg/mL | vs C4 |
|---|---|---|---|---|
| C4 (current lead) | 109.8 | 2.97 | 0.0051 | 1× |
| D1 bis-4-OMe | 128.3 | 2.98 | 0.0040 | 0.8× |
| D2 bis-4-F | 109.8 | 3.24 | 0.0021 | 0.4× |
| **D4 bis-4-pyridyl** | **135.6** | **1.76** | **0.0652** | **12.7×** |
| D3 bis-3-pyridyl | 135.6 | 1.76 | 0.0652 | 12.7× |
| D8 bis-2-furyl | 136.1 | 2.15 | 0.0373 | 7.3× |

**Replacing both phenyl rings with pyridine gives a 12.7× solubility gain** and drops lipophilicity from
2.97 to 1.76 — both wanted for chronic dosing.

**The cost is 5.6 Å² over the ceiling.** That ceiling is itself an estimate from seven compounds whose
maximum is nirmatrelvir at 131.4, so 135.6 is marginal rather than disqualifying — but it is the same
kind of step that produced the M3 failure, and it must not be waved through.

**An advantage my own filter missed:** a pyridine nitrogen is **weakly basic** (pKa ≈ 5). It is not
counted by the basic-amine SMARTS — correctly, since it is aromatic and carries none of the hERG
pharmacophore risk of an aliphatic amine — **but it can still form a salt with a strong acid.** That
partially restores the salt handle C4 gave up, without restoring the cardiac liability.

**Status: D4 is a candidate worth carrying, not a new lead.** It needs the anchored fit, and the TPSA
overrun needs a permeability answer rather than an argument.

## 30.4 Branch C — regulatory: the accelerated door is shut for AML

Measurable residual disease as a surrogate for accelerated approval:

- **Multiple myeloma: accepted.** FDA's Oncologic Drugs Advisory Committee voted **unanimously in April
  2024** that MRD-negative complete response is reasonably likely to predict clinical benefit.
- **AML: not accepted.** FDA has stated that *"the molecular heterogeneity of AML poses substantial
  challenges to the use of MRD as a biomarker."* A consortium (MRD Partnership / Alliance in AML) is
  actively pushing for it, and published a case in 2025.

**So for this programme there is currently one door: overall survival.** The surrogate our entire
preclinical case rests on — leukaemia stem cell burden — has no accepted regulatory standing in this
disease.

**This does not change criterion 3's score, but it removes an escape route I had assumed existed.** If
MRD gains acceptance in AML the calculus changes materially, and it is worth tracking.

---

# 31. EFFICACY RESET — the new molecules have not earned the mechanism

## 31.1 Source correction

Section 23 attached the ML210 + venetoclax LSC result to the wrong publication. The 2024 *Leukemia*
paper tested ML210 in AML lines and bulk CD45⁺ primary samples. It did not test that combination in
sorted LSCs. The reported CD34⁺CD38⁻ result is from the later 2025 *Blood* conference abstract
(doi:10.1182/blood-2025-5050): combination index <0.5 in cells from venetoclax-resistant patients.

This correction weakens certainty, not the numerical result: it is conference-abstract evidence with
no full methods or peer-reviewed paper yet. The patient-derived xenograft result combined venetoclax
with GPX4 inhibition, but the in-vivo GPX4 intervention was inducible knockdown, not ML210.

## 31.2 Exact molecule is now Gate 1

The mechanism has LSC evidence. **C4 and D4 do not.** Preserving a warhead does not prove that the new
molecule enters the cell, forms the active electrophile, engages GPX4, and kills the functional LSC.

| Molecule | Exact primary AML LSC result | Decision |
|---|---|---|
| ML210 + venetoclax | yes; 2025 abstract | efficacy positive control |
| JKE-1674 | none found | translational comparator; remains yellow |
| C4 | none | keep only for the efficacy plate |
| D4 | none | pause property work; activity risk is larger than C4 |

## 31.3 One experiment decides the molecule

Test ML210, JKE-1674, C4, and D4 together in genotype-confirmed primary AML LSC-enriched cells and
matched normal CD34⁺ cells. Deliberately include FLT3-ITD and FLT3-wild-type AML rather than selecting
on GPX4 abundance. Measure concentration-response killing, lipid peroxidation and
ferrostatin-1 rescue; repeat as venetoclax → GPX4-inhibitor sequence. After washout, measure colony
formation. The winning new molecule must approach the active controls on LSC killing and durable loss
of colonies. Confirm the winner by limiting-dilution and secondary transplantation.

**Campaign consequence:** solubility is no longer the next branch. Exact-candidate LSC elimination is.

## 31.4 New 2026 target evidence narrows the patients

A 2026 *Nature Cell Biology* study
([paper](https://www.nature.com/articles/s41556-026-02016-5)) provides the strongest target evidence so
far. Conditional GPX4 deletion in established FLT3-ITD AML reduced the leukemia-initiating L-GMP
population and delayed leukemia; ML210 preferentially killed FLT3-ITD-transformed murine AML over
normal LSK progenitors.

But the effect was not universal: GPX4 deletion in MLL-AF9 AML without FLT3-ITD did not improve
secondary-transplant survival (P=0.4552). **The programme should therefore start in FLT3-ITD AML and
use FLT3-wild-type samples as the negative biological control.**

Baseline GPX4 abundance is not a safe substitute. Published AML cohorts disagree on whether GPX4
protein is higher or lower than normal marrow, and one direct ML210 study found that higher GPX4
protein correlated with *less* killing. Patient selection must use genotype plus functional response,
not “GPX4-high” alone.
