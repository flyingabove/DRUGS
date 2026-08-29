# Tier 3.2 — GPX4 vs TXNRD1: the structural basis of selectivity

The counter-target that matters is **TXNRD1** — 26% of compounds hitting GPX4 in primary screens also
hit it, and it is what ML162 and RSL3 fail on. Both TXNRD1 structures were already local (2J3N, 3QFA),
so this cost nothing.

## Measured: solvent exposure of the catalytic chalcogen

| Site | Burial | Exposed | Neighbours within 6 Å |
|---|---|---|---|
| **GPX4 Sec46 (SE)** | **0.93** | **7%** | **45** |
| TXNRD1 Cys498 — the Sec498 position (3QFA) | 0.23 | 76% | 7 |
| TXNRD1 Cys498 (2J3N chain C) | 0.38 | 62% | 8 |

**TXNRD1's catalytic chalcogen is 3–10× more solvent-exposed than GPX4's, with six times fewer
neighbouring atoms.** It sits essentially naked on the C-terminal Gly-Cys-Sec-Gly tail at the protein
surface. GPX4's Sec46 is 93% enclosed.

## What this means — and it is not the obvious reading

The naive expectation is that a buried target is harder to hit and therefore harder to drug. **The
opposite conclusion follows here.**

**Accessibility cannot give selectivity for GPX4 — it runs the wrong way.** TXNRD1's selenolate is more
exposed, more reactive, and needs no shape complementarity whatsoever. Any bare electrophile
diffusing through a cell will meet it preferentially. **That is precisely why the chloroacetamides
(ML162, RSL3) hit TXNRD1 and why no amount of shape optimisation would have fixed them.**

**What GPX4's 93% burial buys is a binding site.** A molecule that fits that enclosed groove is *held*
next to Sec46 long enough to react. TXNRD1's exposed tail offers nothing to hold onto — an electrophile
that fails to react on first encounter simply diffuses away.

**So selectivity comes from two things acting together:**

1. **The masked warhead** keeps the free-electrophile concentration low everywhere, so the
   diffusion-limited reaction with the most exposed selenol never dominates
2. **GPX4's enclosed groove** provides residence time that TXNRD1's naked surface Sec cannot

Neither alone is sufficient. **This is a structural argument for never "simplifying" the nitroisoxazole
to a direct electrophile** — the thing that would look like a reasonable medicinal-chemistry
simplification is exactly the change that created the ML162/RSL3 liability.

## This reframes the "no pocket" finding

§7 measured **26 Å³ accessible within 5 Å of Sec46** and concluded there is no druggable pocket. Burial
of 0.93 says Sec46 is strongly enclosed. **Both are correct and they are not in tension:** the site is
enclosed *and* small — a **narrow, shallow groove**, not an open cavity.

That resolves a tension that had been sitting unexamined: rigid docking failed (§15) because there is no
cavity to fill, while the covalent adduct fits fine (§16) because a tethered ligand only needs to lie
along a groove. **Small volume plus high burial is a groove. It defeats docking and still supports
binding.**

## Correction to a first draft of this analysis

I initially wrote that TXNRD1's Sec-bearing tail is *"not resolved because that tail is mobile."* That
was overstated on two counts:

- The tail **is** fully resolved in 3QFA chains A/B and in 2J3N chain C. It is disordered only in 2J3N
  chains A/B. **Partially mobile, not absent.**
- Both structures are **Sec→Cys mutants** — SEQRES contains no SEC at all (2J3N: Gly-Cys-**Cys**-Gly;
  3QFA: Gly-**Ser**-**Cys**-Gly). This is standard for TXNRD1 crystallography, since selenoprotein
  expression requires SBP2 co-expression.

The quantitative exposure comparison above replaces the assertion, and it points the same way — but for
a measured reason rather than an assumed one.

## Caveat

Exposure is measured on a **Cys** standing in for **Sec**, in a crystal. Selenium is larger and the real
selenolate is anionic at pH 7.4 where most cysteines are not — both push TXNRD1's site toward *more*
reactivity, not less. **The comparison is conservative in the direction that matters.**

---

# Tier 3.1 — Selenoproteome-wide scan: **not possible from AlphaFold DB**

The plan called for scanning all ~25 human selenoproteins for accessible Sec in a GPX4-like environment.
**AlphaFold DB does not contain them.**

| | Entries present |
|---|---|
| Human selenoproteins queried (GPX1-4/6, TXNRD1-3, DIO1-3, SELENOP/K/S/W/N/O/V, MSRB1, SEPHS2) | **2 / 20** |
| Non-selenoprotein controls (EGFR, TP53) | **2 / 2** |

**Both apparent exceptions are false positives.** DIO1's entry is `AF-P49895-7` — a **113-residue
isoform** of a 249-residue protein whose sequence **contains no U (Sec) at all**. The Sec-containing
canonical sequences return HTTP 404.

**Verified as genuine absence, not a query artifact:** the failures are `404 Not Found`, not `429`
rate-limiting, and the controls return `200` under the identical protocol. **The first version of this
check used a guessed URL and 404'd on EGFR too** — had I not run a non-selenoprotein control, I would
have written up "selenoproteins are excluded" from what was actually my own malformed URL.

## Why, and what it means

Selenocysteine is encoded by UGA — normally a stop codon — and is a non-standard residue. Structure
prediction pipelines built on the 20 canonical amino acids have no token for it, so the sequences are
dropped rather than modelled.

**Consequence for this program:** a structure-based selectivity scan across the selenoproteome is not
available. The options are experimental structures — scarce, and as §Tier 3.2 showed, usually
**Sec→Cys mutants** — or custom modelling with a Sec residue built in.

**This is also why the field uses chemical proteomics (activity-based protein profiling) rather than
structure for selenoprotein selectivity.** It is not a methodological preference; the structures do not
exist. That elevates the proteome-wide covalent profiling experiment from "nice to have" to **the only
way to answer K1 across the selenoproteome**.

The focused GPX4-vs-TXNRD1 comparison in §Tier 3.2 stands, because both had experimental structures.
