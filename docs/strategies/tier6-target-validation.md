# Tier 6 — Target Validation, and Two Corrections to My Own Findings

---

## 1. K2 — the therapeutic window: **it exists, and it has a named dependency**

The safety-critical half of the thesis was "normal HSCs tolerate GPX4 loss." That claim is
**supported**, with an important qualifier I did not have before.

**Supporting:** GPX4 deletion restricted to the haematopoietic system has **no significant effect on
the number or function of HSPCs in mice under normal conditions**
([Cell Death & Disease](https://www.nature.com/articles/s41419-021-04008-9)).

**The qualifier — and it is a big one:** that tolerance is **vitamin E dependent**. α-Tocopherol
rescues Gpx4-deficient HSPCs from ferroptosis *in vitro*, and **Gpx4-knockout mice on a
vitamin E-depleted diet show reduced HSPC numbers and impaired haematopoiesis.**

### What this changes

1. **The window is real but conditional.** Normal HSCs survive GPX4 loss *because* vitamin E covers for
   it. That safety margin is not intrinsic — it is a nutritional reserve.
2. **Vitamin E status becomes a safety-critical covariate.** AML patients post-induction are frequently
   nutritionally compromised. **A vitamin E-deficient patient may have no protective margin at all.**
   This belongs in eligibility criteria and in on-study monitoring.
3. **Vitamin E supplementation is a candidate window-widener — and a candidate efficacy-killer.**
   α-Tocopherol is a lipophilic radical-trapping antioxidant; it protects *any* cell it reaches. It may
   rescue the leukaemia as readily as the marrow. **This is a real experiment, not a plan:** does
   vitamin E supplementation preserve the therapeutic window or abolish it?

### Predicted dose-limiting toxicity — now specific

GPX4 knockdown in mouse haematopoietic cells causes **haemolytic anaemia and increased splenic
erythroid progenitor death**, and GPX4 has a distinct role in
[human erythroblast enucleation](https://ashpublications.org/bloodadvances/article/4/22/5666/474197/A-new-role-of-glutathione-peroxidase-4-during).

**The predicted DLT is anaemia, and erythroid progenitors are the sensitive compartment.** That is a
good kind of toxicity to have: monitorable by routine CBC, manageable by transfusion and dose
adjustment, and unambiguous — unlike idiosyncratic organ toxicity.

## 2. AML side — confirmed, with subtype structure

GPX4 knockdown induces ferroptosis in AML cells with mitochondrial lipid peroxidation and anti-AML
effects *in vitro and in vivo*
([Leukemia](https://www.nature.com/articles/s41375-023-02117-2)), and GPX4 sustains blasts and LSCs in
BCR-ABL⁺ leukaemia
([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11514791/)).

**Mitochondrial CoQ blocks GPX4-inhibition-mediated ferroptosis** — confirming the §6 prediction and
giving a clean mechanistic control for the cell assay.

---

## 3. CORRECTION 1 — "FSP1i does nothing" was too strong

The literature is explicit: **high-FSP1 AML lines and primary FLT3-ITD⁺ blasts survive pharmacologic
GPX4 inhibition but undergo rapid ferroptosis when FSP1 is co-inhibited.** My systems model said FSP1
combination added ~0.1 months.

**Both are right, about different parameters.** My model only ever encoded FSP1 as a route of *acquired*
escape. The literature describes *pre-existing* subtype biology.

| | What FSP1i does | Model parameter |
|---|---|---|
| **FSP1-high / FLT3-ITD⁺ patient** | **Converts a non-responder into a responder** | baseline kS |
| Depth of remission | 1–2 logs deeper initial kill → +3.5 to +7 months | S0 |
| **Acquired ferroptosis incompetence** (ACSL4/LPCAT3 loss) | **Nothing — the cell cannot do ferroptosis at all** | kG |

**Corrected position: FSP1i is a patient-selection and depth-of-remission tool, not a durability tool.**
The orthogonal-mechanism partner is still required for durability. **These are two different partner
drugs doing two different jobs**, and the earlier doc collapsed them into one question.

---

## 4. CORRECTION 2 — competitive release is real; "use a lower dose" does not follow

A paradox appeared: in an FSP1-high scenario, *restoring* drug sensitivity **shortened** time to relapse
(29.4 → 25.4 months). I tested whether it was a bug by removing the shared carrying capacity:

| | Shared niche | No competition |
|---|---|---|
| Weak kill (kS = 0.03) | **29.4 mo** | 6.5 mo |
| Strong kill (kS = 0.30) | 25.4 mo | 24.2 mo |

**Confirmed competitive release, not a bug.** Killing sensitive LSCs frees niche capacity the resistant
clone expands into — the documented basis of adaptive therapy in evolutionary oncology.

**But the tempting conclusion is wrong.** I initially wrote that dose-response would therefore be
non-monotonic with an intermediate optimum. **The dose scan says otherwise:**

| Dose (× EC₅₀) | 0.1 | 0.5 | 1.0 | 2.0 | 5.0 | 10.0 |
|---|---|---|---|---|---|---|
| TTP (months) | 22.1 | 24.2 | 25.4 | 26.5 | 27.6 | **28.1** |

**Monotonically increasing. There is no intermediate optimum.**

**Why the two differ:** lowering *kS* weakens killing of sensitive cells only, preserving competition.
Lowering *dose* weakens killing of **every** compartment — including the resistant clone, where
pressure matters most. **kG dominates again.**

**So: competitive release is real, but it is not an argument for dose reduction.** The argument for
gentle dosing remains tolerability and the flat dose-response (10× dose buys 6 months), not a
competitive-release optimum.

---

## 5. Method note

**Twice in this session my scripts printed conclusions that their own tables contradicted** — once
claiming a 30-minute half-life sufficed (the table said 24% trough, "inadequate"), once claiming
non-monotonic dose-response (the table was monotonic). Both were narrative text written into `print`
statements *before* seeing the numbers.

**Do not pre-write the interpretation.** Print the table, read it, then write what it says.
