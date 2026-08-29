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
