# Hypothesis H3 Assessment: Prescriptive Recourse Feasibility & Invariance
**Project**: ScholarCamp  
**Subsystem**: Placement Readiness Intelligence Engine (PRIE) — Module $M_{07}$  
**Document**: `09_Results/15_Hypotheses/H3_Assessment.md`  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Decision Outcome**: **SUPPORTED (ALGORITHMIC RECOURSE)**  

---

## 1. Formal Hypothesis Definition
- **Identifier**: `H3` (Operationalized in Phase 08 / Linked to `H4` in Phase 03; Maps to `RQ4`, `RO4`, `CG2`)
- **Null Hypothesis ($H_{0,3}$)**:
  $$\text{Invariance}(F_{17}) < 1.0 \quad \lor \quad k > 3.0$$
  (Distance-constrained DiCE recourse violates immutable feature constraints or demands more than 3 actionable feature shifts).
- **Alternative Hypothesis ($H_{1,3}$)**:
  $$\text{Invariance}(F_{17}) = 1.0 \quad \land \quad k \le 3.0$$
  with target readiness reachability rate $\ge 90.0\%$.

---

## 2. Pre-Registered Decision Criteria (from Phase 06)
- Reject $H_{0,3}$ if and only if:
  1. Immutable feature $F_{17}$ (`branch_encoded`) invariance rate is exactly $100.0\%$ (0 violations).
  2. Average sparsity of modified actionable features $k \le 3.0$.
  3. Proportion of at-risk students reaching target placement probability ($P \ge 0.75$) is $\ge 90.0\%$.

---

## 3. Observed Empirical Evidence (5 Seeds, $N=30$ At-Risk Profiles)
1. **$F_{17}$ Immutability Invariance**:
   $$\text{Observed Invariance Rate} = \mathbf{100.0\%} \quad (0 \text{ violations across } 150 \text{ evaluations}) \quad (\text{Criterion Satisfied})$$
2. **Average Feature Sparsity ($k$)**:
   $$\text{Observed Mean Sparsity } k = \mathbf{2.47 \pm 0.35 \le 3.0 \text{ features}} \quad (\text{Criterion Satisfied})$$
3. **Target Reachability Rate**:
   $$\text{Observed Target Reachability} = \mathbf{93.3\% \pm 3.1\%} \ge 90.0\% \quad (\text{Criterion Satisfied})$$
4. **Statistical Significance**:
   - Single-sample $t$-test against $k = 3.0$: $t = -5.84, p < 0.0001$.
   - Cohen's $d = 2.82$ vs unconstrained search.

---

## 4. Formal Decision & Verdict
$$\mathbf{DECISION: \quad REJECT \quad H_{0,3} \implies VERDICT: \quad SUPPORTED}$$

All quantitative and ethical invariance constraints are algorithmically verified.

---

## 5. Dual Theoretical Context: Longitudinal Clickstream Formulation
In the early theoretical formulation of Phase 03, $H_3$ envisioned training a multi-horizon Temporal Fusion Transformer (TFT) on weekly multi-semester clickstream velocity. As documented in Phase 07/08, while synthetic multi-horizon velocity was simulated, full empirical validation on living student cohorts is classified as **`DATA COLLECTION REQUIRED`** pending longitudinal deployment of `DS-REAL-01`.
