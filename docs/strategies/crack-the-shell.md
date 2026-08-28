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
