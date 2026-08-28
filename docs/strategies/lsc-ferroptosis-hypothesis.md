# The LSC Ferroptosis Hypothesis — How We Kill What Survives Treatment

**Supersedes `gpx4-dependency-aml.md` and `break-the-shield-gpx4.md`.** Execution details in
[../compute-plan-gpx4.md](../compute-plan-gpx4.md). Research provenance in
[../research/loops/current-idea.md](../research/loops/current-idea.md) and
[../research/loops/dead-ideas.md](../research/loops/dead-ideas.md).

---

# PART 1 — THE PROBLEM WE ARE ACTUALLY SOLVING

A patient with AML goes through induction chemotherapy and reaches complete remission. The leukemia
is undetectable on a slide. And yet, in most cases, it comes back.

It comes back because **complete remission is only about a 200-fold reduction in leukemic burden.**
Start near 10¹² cells, divide by 200, and billions remain. What survives is not a random sample of
the original disease — it is the toughest slice of it, concentrated: **leukemic stem cells**, dormant
in the bone marrow niche, chemo-resistant, and capable of regrowing the entire disease from very few
cells.

Standard MRD testing goes deeper than a slide (flow ~1 in 10⁴; molecular ~1 in 10⁵–10⁶), yet **a
significant proportion of MRD-negative patients still relapse** — because LSCs are specifically what
those panels miss.

**That population is the target of this program.**

## Why everything else has failed

Across this project we mapped four challenges any solution must clear simultaneously.

**1. Selectivity.** LSCs closely resemble normal hematopoietic stem cells. Every surface target we
examined — CXCR4, CD44, CD45, CD33, CD123, and even CLL-1 — is shared with normal blood cells to a
degree that cuts against us. LSD1 and HMG20B failed the same way at the protein-complex level. The
recurring lesson: **LSCs differ from normal HSCs by degree, not by kind.** There is rarely an on/off
switch, only a dial.

**2. Physical access.** LSCs shelter in the endosteal niche — poorly perfused, hypoxic (<10 mmHg) —
gripping stromal cells through CXCR4, CD44, and VLA-4. Drugs delivered by bloodstream arrive there
last and weakest.

**3. Dormancy.** Most cytotoxics kill dividing cells. Cytarabine is S-phase specific. A quiescent cell
is close to invisible to that entire class of drug. Dormancy *is* the resistance mechanism.

**4. Heterogeneity.** AML is not one disease. Driver mutations differ between patients, and a single
patient carries multiple genetically distinct subclones. Mutation-targeted agents cover a slice.

And a fifth constraint we derived rather than found: **partial killing only delays relapse.** Killing
is logarithmic; regrowth is exponential. Iomab-B demonstrated this in humans — it met its primary
endpoint at p<0.0001 and the FDA still refused the filing, because overall survival did not follow
[a]. Deeper cytoreduction buys time, not cure.

---

# PART 2 — THE HYPOTHESIS

> **Lingering LSCs are defined by two properties — apoptosis resistance and dormancy — that defeat
> every conventional therapy. But the metabolic state that grants them those properties forces them
> to carry a heavy iron load, which they survive only by over-expressing GPX4 as armor against lipid
> peroxidation. That armor is a dependency. Removing GPX4 kills them through ferroptosis, a death
> pathway orthogonal to both of the properties that make them untouchable.**

Three claims, each load-bearing. Taken in turn.

## Claim 1 — Ferroptosis is orthogonal to their defenses

**Ferroptosis** is iron-dependent death by lipid peroxidation: iron catalyzes oxidation of membrane
fats until the membrane fails. It is mechanistically distinct from **apoptosis**, the orderly
self-destruct program that venetoclax, cytarabine, and most cytotoxics engage.

That distinction does two things at once:

- **It defeats apoptosis resistance.** A cell that has upregulated BCL-2 or lost TP53 has hardened the
  apoptotic machinery. Ferroptosis does not use that machinery.
- **It defeats dormancy.** Lipid peroxidation does not require the cell to divide. Chemotherapy needs
  a replicating genome to attack; ferroptosis needs only a membrane.

**Evidence:** persister cells across multiple tumor types and treatments are vulnerable to ferroptosis
induced specifically by GPX4 inhibitors; dormant cancer cells are highly ferroptosis-sensitive
**while normal cells are largely spared** [1][2].

## Claim 2 — Their metabolic state creates the liability

This is the part that makes the hypothesis more than opportunistic.

> Persister cells preferentially depend on **oxidative phosphorylation, a major source of ROS**, and
> this dependence generates oxidative stress which **sensitizes to ferroptosis** [1].

The OxPhos dependence of AML LSCs is the same fact that underpins venetoclax activity — established
early in this project from a completely different direction. **The metabolic commitment that makes
LSCs chemoresistant is the same commitment that creates their ferroptotic liability.** They cannot
abandon it without ceasing to be what they are.

## Claim 3 — The armor is the target

The naive version of this idea — "LSCs are iron-rich, so push them into ferroptosis" — is **wrong**,
and the literature says so:

> In CD34⁺CD38⁻ primitive-like leukemic stem cells, iron-homeostatic and anti-peroxidation networks
> including **SLC7A11–GPX4** collectively shape a **relatively ferroptosis-resistant state**. LSCs
> evade lipid-peroxidation-induced cell death by **upregulating antioxidant defense systems,
> including GPX4 and ferritin heavy chain 1** [3].

LSCs have already solved the ferroptosis problem. But note *how*: they did not remove the threat, they
built armor against it — and the armor is GPX4.

**Their resistance runs through GPX4, which makes GPX4 a dependency rather than merely a marker.**

| Where you attack | What happens |
|---|---|
| **Upstream** — SLC7A11 inhibition, iron loading, generic oxidative stress | Their elevated GPX4 absorbs the damage. **This is why upstream ferroptosis induction underperforms against LSCs.** |
| **GPX4 itself** | Removes the one protein they rely on to survive an iron load they cannot switch off |

**And the resistance is surmountable:** ferroptosis-inducing agents **eliminate 97% of CD34⁺/CD38⁻
LSCs** [4] — the stem-enriched fraction specifically, not bulk blasts.

---

# PART 3 — HOW THIS SOLVES THE FOUR CHALLENGES

The first approach in this project that scores on all four.

## Challenge 1 — Selectivity ✅ **Strongest evidence in the project**

- **GPX4 is highly expressed across most AML subtypes and lower in normal hematopoietic stem cells**,
  varying by myeloid differentiation stage [5].
- **Acquired GPX4 depletion has no significant effect on hematopoietic stem cells** [5].
- **A window has been measured, not assumed:** GPX4 inhibitors kill AML patient CD34⁺ cells with
  **blasts significantly more sensitive than non-blasts in the same marrow sample** [6].

The "degree, not kind" problem finally points the right way — and the degree has been quantified
inside a single patient's marrow.

## Challenge 2 — Physical access ⚠️ **Improved, not solved**

A small molecule diffuses into the hypoxic endosteal niche far better than a CAR-T cell, an
antibody, or a radioconjugate — the modalities that dominated earlier strategies here. Access remains
a real constraint, but it is the mildest version of it we have encountered.

**Caveat:** the niche is where drug delivery is worst, and this has not been measured for any GPX4
compound.

## Challenge 3 — Dormancy ✅ **This is the standout**

Ferroptosis does not require cell division. This is the property no earlier approach had.

Every prior strategy had to *break* dormancy first — wake the cells, then kill them — which
introduced timing windows, provocation agents, and the risk of converting a quiet disease into a
proliferating one. **Here dormancy simply stops mattering.** Persisters are not merely still
vulnerable; they are *preferentially* vulnerable, because their OxPhos dependence generates the ROS
that sensitizes them [1].

## Challenge 4 — Heterogeneity ✅ **Good**

GPX4 dependence is **not mutation-specific.** It is high across most AML subtypes [5], so this does
not fracture into a per-genotype menu the way FLT3, IDH, or menin-directed agents do.

**Better still, the enrichment points at the patients who need it most:** relapsed and refractory AML
shows the **highest GPX4 levels and enzyme activities** [5].

## Constraint 5 — Does it prevent relapse, or only delay it? ❓ **UNRESOLVED**

The honest gap. Killing LSCs is necessary but not sufficient — the Iomab-B precedent shows that
deeper cytoreduction can improve every intermediate endpoint and still fail on survival [a].

**Nobody has shown that ferroptosis induction eradicates leukemia-initiating capacity on serial
transplantation.** Searched directly; genuinely absent. **This is the single experiment that decides
whether the hypothesis is a therapy or a delay.**

---

# PART 4 — THE ESCAPE ROUTE, AND WHY THE DESIGN INCLUDES FSP1

A hypothesis is only as good as its account of how the disease escapes.

**FSP1 suppresses ferroptosis glutathione-independently**, regenerating CoQ10 whose reduced form traps
lipid peroxyl radicals. It runs parallel to GPX4 and rescues cells from GPX4 deletion [7][8].

**Under pressure, cells do not die — they switch arms:**

> **Upregulation of CoQ shifts ferroptosis dependence from GPX4 to FSP1** [9].

**Blocking GPX4 alone therefore pre-installs the resistance mechanism.** Pharmacological FSP1
targeting strongly synergizes with GPX4 inhibitors across cancer types [10], and one 2025 title
independently validates two of our design choices at once: **"FSP1 and histone deacetylases suppress
cancer persister cell ferroptosis"** [2].

## The niche supplies the escape — a prediction this project makes

- Mitochondrial electron transport is a **primary source of CoQ recycling**, and mitochondria-specific
  CoQ **potently blocks GPX4-inhibition-mediated ferroptosis in AML** [11].
- Marrow stroma **transfers functional mitochondria to AML cells** via tunneling nanotubes — and
  **metabolic attack induces that transfer** [12].

**Therefore we predict that attacking GPX4 will provoke the niche to hand LSCs fresh mitochondria,
more CoQ, and a reinforced FSP1 arm.** Untested, testable, and the strongest argument that FSP1
coverage is not optional.

**Prior art status:** dual GPX4/TXNRD1 in AML has been explored [13]. **Dual GPX4/FSP1 in AML has
not, and no FSP1 inhibitor has been tested in AML at all.**

---

# PART 5 — THE INTERVENTION

**A selective, reversible-covalent GPX4 inhibitor with hepatobiliary clearance, paired with an
FSP1 inhibitor, on a venetoclax/azacitidine backbone, in venetoclax-resistant AML.**

## Why that indication

> ML210 + venetoclax is synergistic in primary AML patient cells **including venetoclax-resistant
> ones** [11].

Venetoclax resistance is among the largest unmet needs in AML. Venetoclax kills by apoptosis;
ferroptosis is a different pathway; resistance to one does not confer resistance to the other. That
gives a defined population, a mechanistic rationale, primary-patient evidence, and an approved
backbone to build on.

## The regimen

| Component | Role | Status |
|---|---|---|
| **GPX4 inhibitor** | Strip the armor LSCs depend on | **The molecule we design** |
| **FSP1 inhibitor (icFSP1 class)** | Close the CoQ escape route | Exists [14]; never tested in AML |
| **Venetoclax** | Apoptotic arm; synergy in venetoclax-resistant primary cells [11] | Approved |
| **Azacitidine** | Backbone; independently sensitizes to ferroptosis via MAGEA6–AMPK–SLC7A11–GPX4 [15] | Approved |
| *HDAC inhibitor (optional)* | *Removes a second persister ferroptosis defense [2]; raises labile iron [16]* | *Approved* |
| **NOT NCOA4 inhibitor** | **Antagonizes** — NCOA4 depletion *inhibits* ferroptosis by removing free iron [17] | — |

**Patient selection:** a published model integrating **TfR1, GPX4, FTH1** predicts LSC ferroptosis
susceptibility [4]; GPX4-high/AIFM2-high adds a second axis [5].

## Why the molecule does not exist yet

**GPX4 has a shallow active site with no drug-like binding pocket** [18] — a textbook
difficult-to-drug target. Every existing compound failed on pharmacokinetics.

And the field's tools were partly mis-assigned: **RSL3 and ML162 are not direct inhibitors of GPX4 but
of TXNRD1** [19]. **ML210** — nitroisoxazole warhead — *is* genuinely selective, with low
proteome-wide reactivity [20].

**So selective chemistry exists; a drug does not.** The design problem is optimizing a validated
chemotype for PK and clearance route, not solving selectivity from scratch. Six coupled constraints —
shallow-site binding, covalent reactivity tuning, selenoprotein-family selectivity, clearance-route
steering, reversibility kinetics, dual-target pharmacology — optimized simultaneously on a target with
**solved crystal structures** [21]. That combination is why GPX4 resisted drugging for a decade with
serial medicinal chemistry, and why it is tractable now.

---

# PART 6 — WHAT WOULD FALSIFY THIS

Stated in advance, so the hypothesis is disprovable rather than merely defended.

| Finding that would kill it | Status |
|---|---|
| GPX4 inhibition kills LSCs but **does not reduce leukemia-initiating capacity** on serial transplant | **Untested — the decisive experiment** |
| No pharmacological therapeutic index exists — kidney or T-cell toxicity at every efficacious dose | **Never measured**; all kidney evidence is total genetic knockout [22], and an antidote exists (liproxstatin-1) [22] |
| Niche mitochondrial transfer fully rescues LSCs via FSP1 | **Predicted by us, untested** |
| Selectivity over TXNRD1 is unachievable in a drug-like compound | **Unlikely** — 74% of GPX4 hits were not dual inhibitors [23] |
| Ferroptosis-protective membrane domains in quiescent cells blunt the effect | **Real caution** [24] |
| **GADD45A-low LSCs** escape — loss increases self-renewal *and* ferroptosis resistance | **Known resistance mechanism to screen for** [25] |

---

# PART 7 — THE SHORT VERSION

1. Lingering LSCs survive because they are **apoptosis-resistant and dormant**.
2. Those same properties come from an **OxPhos-dependent state that floods them with ROS**.
3. To survive it they **over-express GPX4** — armor against lipid peroxidation.
4. **The armor is a dependency.** Strip GPX4 and they die by **ferroptosis**, which cares about
   neither apoptosis resistance nor dormancy.
5. They will escape via **FSP1**, so the regimen covers both arms.
6. The molecule does not exist because GPX4 is hard to drug — **a multi-parameter design problem on a
   structurally solved target**, which is precisely the kind of problem now tractable.
7. **The hypothesis stands or falls on one experiment: serial transplantation.**

---

# REFERENCES

- [a] [Randomized Phase III SIERRA trial of ¹³¹I-apamistamab (Iomab-B) — *JCO*](https://ascopubs.org/doi/10.1200/JCO.23.02018) · [FDA declined the filing](https://www.cancernetwork.com/view/sierra-results-do-not-support-bla-filing-for-131i-apamistamab-in-r-r-aml)
1. [Targeting dormant cancer cells: ferroptosis as a precision therapeutic strategy](https://link.springer.com/article/10.1186/s11658-026-00895-y)
2. [FSP1 and histone deacetylases suppress cancer persister cell ferroptosis — *Science Advances* (2025)](https://www.science.org/doi/10.1126/sciadv.aea8771)
3. [Regulating Ferroptosis in Leukemic Stem Cells — *Stem Cell Reviews and Reports* (2025)](https://link.springer.com/article/10.1007/s12015-025-11016-1)
4. [Ferroptosis in AML: nanoparticles, biomarkers, and immune rewiring — *Discover Oncology* (2025)](https://link.springer.com/article/10.1007/s12672-025-03777-5)
5. [The ferroptosis landscape in acute myeloid leukemia — *Aging*](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10713399/)
6. [Dual targeting of GPX4 and TXNRD1 triggers eradication of AML cells (HA344, #231)](https://www.biorxiv.org/content/10.1101/2024.04.03.584800.full.pdf)
7. [FSP1 is a glutathione-independent ferroptosis suppressor — *Nature* (2019)](https://www.nature.com/articles/s41586-019-1707-0)
8. [The CoQ oxidoreductase FSP1 acts parallel to GPX4 — *Nature* (2019)](https://www.nature.com/articles/s41586-019-1705-2)
9. [Upregulation of CoQ shifts ferroptosis dependence from GPX4 to FSP1](https://www.sciencedirect.com/science/article/pii/S1368764623001152)
10. [Inhibition of FSP1: A new strategy for the treatment of tumors (Review)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11228423/)
11. [Mitochondrial regulation of GPX4 inhibition–mediated ferroptosis in AML — *Leukemia*](https://www.nature.com/articles/s41375-023-02117-2)
12. [Bone marrow niche-mediated survival of leukemia stem cells in AML](https://pmc.ncbi.nlm.nih.gov/articles/PMC4944541/)
13. [Dual targeting of GPX4 and TXNRD1 in AML — preprint (2024)](https://www.biorxiv.org/content/10.1101/2024.04.03.584800.full.pdf)
14. [Phase separation of FSP1 promotes ferroptosis (icFSP1) — *Nature* (2023)](https://www.nature.com/articles/s41586-023-06255-6)
15. [Low-dose hypomethylating agents cooperate with ferroptosis inducers via MAGEA6-AMPK-SLC7A11-GPX4 in AML](https://link.springer.com/article/10.1186/s40164-024-00489-4)
16. [HDAC inhibitor enhances ferroptosis susceptibility of AML cells by stimulating iron metabolism](https://pubmed.ncbi.nlm.nih.gov/39756501/)
17. [The Role of NCOA4-Mediated Ferritinophagy in Ferroptosis](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6316710/)
18. [Targeting GPX4 in ferroptosis and cancer: chemical strategies and challenges](https://www.sciencedirect.com/science/article/abs/pii/S0165614724000981)
19. [The ferroptosis inducing compounds RSL3 and ML162 are not direct inhibitors of GPX4 but of TXNRD1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10149367/)
20. [Selective covalent targeting of GPX4 using masked nitrile-oxide electrophiles](https://pubmed.ncbi.nlm.nih.gov/32231343/)
21. [Crystal structures of GPX4 apo and covalently bound to ML162](https://pubmed.ncbi.nlm.nih.gov/33559612/)
22. [Inactivation of the ferroptosis regulator Gpx4 triggers acute renal failure in mice — *Nature Cell Biology*](https://www.nature.com/articles/ncb3064)
23. [Assay pipeline for discovery of small molecule inhibitors of human GPX1 and GPX4](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10220285/)
24. [Ferroptosis-protective membrane domains in quiescence — *Cell Reports*](https://www.cell.com/cell-reports/fulltext/S2211-1247(23)01573-5)
25. [Loss of GADD45A promotes stem cell activity and ferroptosis resistance in AML — *Blood* (2024)](https://ashpublications.org/blood/article/144/1/84/515642/Loss-of-the-stress-sensor-GADD45A-promotes-stem)
26. [Cysteine depletion targets leukemia stem cells through inhibition of electron transport complex II — *Blood*](https://ashpublications.org/blood/article/134/4/389/260692/Cysteine-depletion-targets-leukemia-stem-cells)
