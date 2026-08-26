# Research Log

Running log from `/research-loop`. Each entry is a hypothesis cycle.

---

## Loop 1 — Senescence induction + senolytic ("one-two punch")

**Hypothesis:** force LSCs into senescence (permanent, irreversible growth arrest) rather than killing
them, then clear them with a senolytic. Addresses the requirement we derived earlier — *leave no cell
capable of regrowing the disease* — without needing to kill every cell.

**Status: ALIVE, with a serious caveat.**

- The one-two punch (pro-senescence agent → senolytic) is an established concept in oncology,
  demonstrated including in T-cell malignancies via p53-dependent senescence.
- **Key find (ASH 2025):** *"Therapy-induced senescence reprograms non-M3 AML into a
  drug-exploitable APL-like state."* Therapy-induced senescence is described as a unifying, plastic
  state across genetically diverse non-M3 AML that pushes blasts toward an **APL-like phenotype with
  distinct plasticity-related therapeutic vulnerabilities.**
- **Counter-evidence:** *"Senescence Promotes the Recovery of Stemness among Cancer Cells via
  Reprogramming."* Senescent cancer cells can escape and return **more** stem-like. Senescence is
  double-edged — it may create a vulnerable state *and* breed stemness.

**Why the APL finding matters:** APL (acute promyelocytic leukemia) is the one AML subtype that is
reliably curable — because ATRA forces the cells to differentiate. If ordinary AML can be pushed into
an APL-*like* state, differentiation therapy might work on AML broadly.

---

## Loop 2 — Chemical reprogramming of LSC identity

**Hypothesis (Sinclair-derived):** partial epigenetic reprogramming resets cell identity. Yamanaka
factors are gene therapy, but **chemical** reprogramming achieves the same with small molecules —
which satisfies the "must be a molecule" requirement.

**Status: ALIVE.**

- The **7C cocktail** (valproic acid, CHIR99021, RepSox, tranylcypromine, forskolin, TTNPB, DZNep)
  reprograms somatic cells to pluripotency with **no genetic manipulation**.
- **DLC79** (DAPT, LDN193189, CHIR99021, I-BET762, Isx9) reprograms human glioma cells into
  neuron-like cells by activating endogenous ASCL1 — proof that a defined small-molecule cocktail can
  forcibly rewrite a cancer cell's identity.
- **Direct hit:** reprogramming tumor populations "leads to loss of diverse cancer cell identity...
  resets the population to the CSC state and **sensitizes them to differentiation stimuli**" —
  explicitly demonstrated in non-solid leukemias.

Note the mechanism: reprogramming doesn't cure — it **collapses heterogeneity into one state and
makes that state differentiation-sensitive.** That directly attacks Challenge #4 (heterogeneity),
which nothing else in this project addressed.

---

## Convergence after 2 loops

Two independent threads point at the same target:

1. Therapy-induced **senescence** → APL-like, differentiation-vulnerable state.
2. Chemical **reprogramming** → collapsed identity, differentiation-sensitized.

**Emerging theory:** don't kill LSCs and don't out-target their heterogeneity. **Force them into a
single, uniform, differentiation-sensitive state — then apply differentiation therapy**, the one
approach that reliably cures a leukemia (ATRA in APL).

Satisfies all three constraints: doesn't exist as a designed agent, plausible on two independent
literature threads, and is a molecule (a defined small-molecule cocktail, or ideally a single agent
replacing it).

Uses **Malone** (epigenetic reactivation, differentiation, RARB/ATRA adjacency) and **Sinclair**
(reprogramming, epigenetic identity reset).

**Open threads for next loops:** the stemness-recovery counter-evidence must be resolved; which
single node in the 7C/DLC79 cocktails is load-bearing; whether the APL-like state is reachable
without cytotoxic senescence induction; whether normal HSCs get reprogrammed too (the recurring
selectivity question).
