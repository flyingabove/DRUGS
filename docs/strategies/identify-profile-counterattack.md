# Strategy 2: Knock Some Loose, Profile Them, Then Target Harder

**The strategy in one line:** deliberately dislodge a sample of the hardest-gripping LSCs, run full
genetic and epigenetic profiling on *those specific cells*, then build the attack around what you
actually find — instead of guessing the mechanism in advance.

Contrast with [Strategy 1: Nuke Everything and Replace](nuke-everything-and-replace.md), which
sidesteps identification entirely by shielding a clean graft and carpet-bombing. This strategy does
the opposite — it invests heavily in identification precisely so the attack can be narrow.

## Why identification is the weak link worth attacking

Current flow-based MRD detection is limited by immunophenotypic variability, similarity to normal
HSPCs, and no standardized panels. The consequence: **a significant proportion of patients called
MRD-negative still relapse**, because routine panels miss the LSCs that matter.

Second structural problem: **AML LSCs live in the marrow**, so blood-based liquid biopsy — the
standard serial-monitoring approach — under-samples the exact population we care about.

## Step 1: Dose-Fractionated Mobilization as a Grip Assay

Give a niche-disruption agent (plerixafor, or a dual CXCR4/CD44 agent — see
[plerixafor-combination-brainstorm.md](../plerixafor-combination-brainstorm.md)) at **escalating
doses**, drawing blood after each.

- Low dose → the weak grippers let go first.
- High dose → only the tight grippers come out.

**The dose required to dislodge a cell is itself a direct measure of its grip strength.** This turns
mobilization into a functional assay, not just a sampling trick.

**This fixes a flaw that would otherwise sink the whole strategy:** if you mobilize once and profile
what comes out, you've sampled the cells that let go *most easily* — the exact opposite of the hard
grippers you're hunting. Fractionating by dose inverts that. Profiling what stays behind in the
marrow versus what came out at each dose gives the same information from the other direction.

## Step 2: Capture and Sort

Sort the mobilized cells by **Grip Score** — a composite per-cell readout of CXCR4, CD44, Wnt
activity, and Notch silencing (see
[wnt-persister-hypothesis.md](../wnt-persister-hypothesis.md), Part 3).

Practical note: a 29-color single-tube full-spectrum flow assay now exists with high concordance to
conventional multi-tube MRD — enough channels to carry the full Grip Score panel plus a
label-retention readout (dormant cells retain a fluorescent dye while dividing cells dilute it out)
in one run.

## Step 3: Profile Them — the Malone-derived part

Malone's own results aren't credible (see [research/marc_malone.md](../research/marc_malone.md)), but
the *measurement categories* he leans on are real techniques. Three readouts, run on the sorted
high-grip population specifically:

**3a. Clone tracking — which family survived.** Serial ctDNA / mutation VAF measurement. From his
mutation-burden claims (TP53, KMT2C, PMS2). Real and already clinical standard for AML MRD. Tells you
*who* survived, empirically, without guessing the mechanism.

**3b. Epigenetic lock mapping — why it's stuck.** ChIP or CUT&Tag on the surviving clone, mapping
where repressor complexes sit on the genome. From his "SIN3-HDAC repressor release" claim —
SIN3-HDAC is a real, well-studied complex. Tells you which specific genes that clone has padlocked
shut, which is what determines whether maturation is even available as an option.

**3c. Mitotic clock — how dormant it actually is.** DNA-methylation-based mitotic clocks (epiTOC2 and
similar) count how many times a cell has divided. Borrowed from the epigenetic-clock measurement tech
underpinning Sinclair's work (see [research/david-sinclair.md](../research/david-sinclair.md)).

Why 3c matters: every other method asks *"what are you"* — which fails, because LSCs look like HSCs.
A mitotic clock asks *"what have you been doing."* Dormant persisters should show a slower-ticking
clock than the proliferating bulk within the same patient. It's a functional readout of the exact
trait we care about. Also doubles as a free lineage barcode, since methylation patterns are inherited
through divisions — an alternative to 3a that reads epigenetics instead of mutations.

**Gap worth noting:** mitotic clocks have been applied to cancer risk broadly, not to AML LSC
dormancy specifically. That's the opening.

## Step 4: Target Based on What You Found

Match the attack to the profile rather than applying every idea uniformly:

| Finding | Response |
|---|---|
| High grip, low dormancy | Sever both hooks, then kill (BCL-2i or CLL-1 CAR-T) |
| Maturation genes epigenetically locked | Unlock them — HDAC/DNMT + Notch reactivation (differentiation route) |
| Wnt-driven self-renewal dominant | Wnt/β-catenin inhibitor |
| Multiple distinct clones found | Multi-target combination, or reconsider Strategy 1 |

## Why This Beats Guessing

- **Doesn't assume the mechanism up front.** The Grip Score alone bets that CXCR4/CD44/Wnt/Notch are
  the right four things to measure. This finds the surviving clone first, then finds what's actually
  driving it.
- **Addresses heterogeneity (Challenge #4)** — profiling is per-patient, so it doesn't depend on one
  marker being universal.
- **Sacrificial sampling.** You deliberately give up a few LSCs to learn how to kill the rest.

## Risks and Open Threads

- **Mobilization isn't selective.** Normal HSCs carry the same hooks and get dislodged too, with a
  real risk of ROS/exhaustion damage and — if both hooks are severed — inability to home back. See
  the risk check in [plerixafor-combination-brainstorm.md](../plerixafor-combination-brainstorm.md).
- **Does the mobilized population actually represent the marrow-resident one?** Dose-fractionation is
  the proposed fix, but this needs direct validation against paired marrow samples.
- **Time cost.** Full profiling takes days to weeks. Whether that's compatible with clinical
  decision-making windows is unresolved.
- Confirm mitotic clocks can resolve dormancy differences *within* a leukemia, not just between
  cancer and normal tissue.

---

# Technical Appendix: Dose-of-Release as a Machine-Learning Label

## The core insight

The LSC identification problem is **unlabeled**. Nearly every marker panel is circular — you define
LSCs by markers, then validate markers against that definition. The one non-circular ground truth,
serial xenotransplantation (transplant cells into a mouse, see if leukemia regrows, repeat), takes
months.

Dose-fractionated mobilization produces a **physical label in hours**, converting identification from
guesswork into a supervised learning problem.

**Definitions:**
- **Label / ground truth** — the known correct answer for each training example.
- **Feature** — any measurable property of that example (a gene's expression, a protein's abundance,
  a methylation value).
- **Supervised learning** — training a model to predict labels from features.
- **Feature discovery** — finding *which* features carry the signal, rather than assuming them up
  front. The Grip Score assumes CXCR4/CD44/Wnt/Notch are the right four. This finds out.

## Step A — Generate labeled fractions

Escalating doses D₁ < D₂ < D₃ < D₄ of a niche-disruption agent, collecting mobilized cells after
each, plus the **residual marrow fraction** (never released — tightest grip of all).

Each cell inherits a label: the dose at which it let go. This is an **ordinal label** (ordered
categories, not binary), which carries far more information than yes/no.

Formally this is a per-population **dose-response curve**, summarized as a **mobilization EC₅₀**
(EC₅₀ = concentration producing half of maximal effect, standard pharmacology) — an EC₅₀ for letting
go of the marrow.

## Step B — Profile each fraction

- **scRNA-seq** (single-cell RNA sequencing) — full transcriptome per individual cell.
- **CITE-seq** — surface proteins *and* RNA measured simultaneously in the same cell, via antibodies
  carrying DNA barcodes (**ADTs**, antibody-derived tags) sequenced alongside the transcriptome.
  Directly relevant, since grip is a surface-protein phenomenon.
- **scATAC-seq** — maps which chromatin regions are physically open, i.e. which genes are *available*
  to be read.
- **Methylation array / bisulfite sequencing** — for the mitotic clock.

## Step C — Rank features against the ordinal label

Don't use naive pairwise comparisons. Use a **test for ordered alternatives** (e.g.
Jonckheere–Terpstra) or ordinal regression. The question "does this feature increase monotonically
with release dose" is stronger and less noise-prone than "is fraction 4 different from fraction 1."

## Step D — Build a sparse classifier

Train a **regularized regression** — specifically **LASSO** (Least Absolute Shrinkage and Selection
Operator), which applies a penalty driving useless features' coefficients to exactly zero.

**Sparsity is the point:** the goal isn't a 20,000-gene signature, it's ~10 markers that fit on a
flow cytometry panel a hospital can actually run. LASSO's output *is* the discovered marker panel.

## Step E — Validate on two levels

1. **Technical** — held-out patients. Does the signature predict release dose in samples the model
   never saw?
2. **Clinical** — the real test. Does it predict actual relapse? Grip strength only matters if it
   tracks outcome.

## Why the design is unusually clean

**Confounding is controlled by construction.** All fractions come from the same patient, same
timepoint, same tube — differing *only* in release dose. That eliminates patient-level and batch
effects, which normally destroy this kind of analysis.

## Four technical problems

**1. Dose ≠ pure grip.** Release dose reflects receptor count × binding affinity × *local drug
concentration*. A cell in poorly-perfused endosteal marrow sees less drug and reads as "tight
gripper" when it's really "badly perfused." Grip strength and spatial location are confounded.

*Counterpoint:* both cause treatment failure. "Hard to reach for any reason" may be the clinically
correct trait regardless of mechanism — in which case the confound damages mechanistic
interpretation but not practical utility.

**2. Normal HSC contamination.** Normal HSCs release by dose too. Without gating them out
(CD34+CD38−, plus leukemia-specific mutations or immunophenotype), the model learns normal stem cell
biology and mislabels it a leukemia signature.

**3. Time/dose confounding.** A cell might release at low dose given enough time. Collection
intervals must be fixed and identical across doses, or you're measuring kinetics and calling it
affinity.

**4. Single-cell methylation is low-coverage and noisy** — hence sorting first, then running bulk
methylation per fraction.

## Note on where ML belongs in this project

The main plan doc puts the ML effort on generative molecule design. This is arguably the better
placement: the project's actual bottleneck is identification, not molecule generation, and this is a
well-posed supervised problem with a real physical label — rarer and more valuable than another
generative pipeline.

## Sources

- [Flow cytometric detection of LSCs in AML: current status and future directions](https://pmc.ncbi.nlm.nih.gov/articles/PMC12727649/)
- [A new timepiece: an epigenetic mitotic clock](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5072295/)
- [Comparison of epigenetic mitotic-like clocks for cancer risk prediction](https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-020-00752-3)
- [CD44, Hyaluronan, the Hematopoietic Stem Cell, and Leukemia-Initiating Cells](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4443741/)
- [Tempus xF liquid biopsy validation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8253837/)
