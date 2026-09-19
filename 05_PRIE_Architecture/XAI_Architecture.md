# XAI Architecture: Two-Tiered Descriptive Attribution & Prescriptive Counterfactual Engine (M07)

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/XAI_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Explainability Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Research Grounding & The "Descriptive-to-Prescriptive Chasm"

A pervasive void identified in Phase 02 (`02_Cross_Analysis/XAI_Comparison.md`) and validated in Phase 03 (`03_Research_Problem/Gap_Validation.md` — `RG3`) is that 100% of educational XAI literature stops at descriptive post-hoc attribution. Existing systems present students and advisors with static SHAP summary beeswarms or LIME bar charts that answer:
> *"Why did the model classify this student as At-Risk or Needs Remediation?"*

While descriptive diagnostics explain past academic deficits (e.g., low CGPA or missing DSA score), they provide **zero actionable recourse**. A student presented with a negative SHAP value on `cgpa` cannot alter completed past semesters.

PRIE bridges this chasm by architecting a **Two-Tiered Explainability Framework** (`DD-003`, `M07`):
1. **Tier 1 (Descriptive Attribution — TreeSHAP)**: Explains model reasoning, ensuring institutional trust, model debugging, and transparency.
2. **Tier 2 (Prescriptive Counterfactual Recourse — DiCE)**: Computes distance-constrained, feasible, and prerequisite-compliant feature interventions that answer:
> *"What is the minimum, realistic set of actions this student can execute over the next 30–60 days to transition into Placement Readiness ($P_{\text{ready}} \ge 0.75$)?"*

---

## 2. Two-Tiered Architectural Topology

```
                  ┌────────────────────────────────────────────────────────┐
                  │          M06: Prediction Engine Output                 │
                  │   Candidate Vector x_spv in R^22 | P_ready = 0.48      │
                  └───────────────────────────┬────────────────────────────┘
                                              │
                      ┌───────────────────────┴───────────────────────┐
                      ▼                                               ▼
       ┌──────────────────────────────┐                ┌──────────────────────────────┐
       │ TIER 1: DESCRIPTIVE XAI      │                │ TIER 2: PRESCRIPTIVE XAI     │
       │ TreeSHAP Feature Attribution │                │ DiCE Counterfactual Solver   │
       └──────────────┬───────────────┘                └──────────────┬───────────────┘
                      │                                               │
       ┌──────────────▼───────────────┐                ┌──────────────▼───────────────┐
       │ • Exact Shapley Axioms       │                │ • Feasibility Constraints    │
       │ • Local Instance Attributions│                │   (Immutable Features Locked)│
       │ • Global Cohort Importance   │                │ • L1 Proximity Minimization  │
       │ • O(T L D^2) Latency < 20ms  │                │ • L0 Sparsity Optimization   │
       └──────────────┬───────────────┘                └──────────────┬───────────────┘
                      │                                               │
                      ▼                                               ▼
       ┌──────────────────────────────┐                ┌──────────────────────────────┐
       │ Diagnostic Insights Payload  │                │ Prescriptive Recourse Target │
       │ "Low DSA (-0.22),            │                │ x* = [cgpa=same, dsa=+15,    │
       │  No Internship (-0.18)"      │                │       proj_qual=+20, ...]    │
       └──────────────┬───────────────┘                └──────────────┬───────────────┘
                      │                                               │
                      ├───────────────────────────────┐               │
                      ▼                               ▼               ▼
         [Faculty Advisor Workspace]          [Student Hub] ──► [M08: Dynamic Roadmap]
         (Transparency & Diagnostics)         (Usability)       (Topological DAG Search)
```

---

## 3. Tier 1: Descriptive Attribution Engine (TreeSHAP)

### 3.1 Mathematical Formulation
TreeSHAP computes exact Shapley values by leveraging the tree structure of gradient boosted decision trees (`XGBoost`), evaluating the marginal contribution of each feature $i$ across all possible feature subsets $S \subseteq F \setminus \{i\}$:
$$\phi_i(\mathbf{x}) = \sum_{S \subseteq F \setminus \{i\}} \frac{|S|! (|F| - |S| - 1)!}{|F|!} \big[ f_x(S \cup \{i\}) - f_x(S) \big]$$

TreeSHAP satisfies the four foundational axiomatic properties of cooperative game theory:
1. **Efficiency**: $\sum_{i=1}^{22} \phi_i(\mathbf{x}) = f(\mathbf{x}) - \mathbb{E}[f(X)]$.
2. **Symmetry**: If $f_x(S \cup \{i\}) = f_x(S \cup \{j\})$ for all $S$, then $\phi_i = \phi_j$.
3. **Dummy**: If $f_x(S \cup \{i\}) = f_x(S)$ for all $S$, then $\phi_i = 0$.
4. **Additivity**: For ensemble trees, $\phi_i(f_1 + f_2) = \phi_i(f_1) + \phi_i(f_2)$.

### 3.2 Computational Complexity & Execution Budget
- Standard model-agnostic KernelSHAP requires exponential time $O(2^D)$ or high-variance sampling ($>5,000$ model evaluations, taking $>2.5$s per student).
- In contrast, TreeSHAP evaluates exact attributions in polynomial time:
  $$\mathcal{O}\left(T \cdot L \cdot D^2\right)$$
  where $T$ is the number of trees ($T \approx 100$), $L$ is the maximum number of leaves ($L \le 32$), and $D$ is the maximum tree depth ($D \le 6$).
- **Runtime Execution**: $<15$ms on standard CPU inside `CMP-MDL-SHP`.

---

## 4. Tier 2: Prescriptive Counterfactual Engine (DiCE)

### 4.1 Constraint-Optimized Loss Formulation
DiCE formulates actionable career guidance as an optimization search over the continuous-categorical SPV feature space $\mathcal{X}$, finding an optimal counterfactual profile $\mathbf{x}^*$ that transitions the candidate to readiness tier while minimizing intervention effort:
$$\mathbf{x}^* = \arg\min_{\mathbf{x}' \in \mathcal{X}} \text{dist}(\mathbf{x}, \mathbf{x}') + \lambda \big( f(\mathbf{x}') - y^* \big)^2 + \gamma \, \text{feasibility}(\mathbf{x}')$$
where $y^* = 0.75$ (the threshold for the `Ready` tier), and:
- **Proximity Metric ($L_1$ Norm)**: Minimizes the absolute magnitude of required student changes:
  $$\text{dist}(\mathbf{x}, \mathbf{x}') = \sum_{i=1}^{22} \frac{|x_i - x_i'|}{\text{MAD}_i}$$
  scaled by the Median Absolute Deviation ($\text{MAD}_i$) of feature $i$ across the institutional cohort.
- **Sparsity Metric ($L_0$ Norm)**: Maximizes the number of unchanged features ($x_i' = x_i$) so students are not overwhelmed by simultaneous demands across all 22 dimensions. Target: $\le 3$ active feature modifications.

### 4.2 Strict Feature Mutability & Feasibility Bounds
To prevent generating unrealistic, illogical, or impossible recommendations, features in the SPV are partitioned into three immutable/mutable classes:

| Mutability Class | SPV Features | Enforced Optimization Constraints | Rationale |
|:---|:---|:---|:---|
| **Class 1: Strictly Immutable** | `F17: branch_encoded` | $\mathbf{x}_i^* = \mathbf{x}_i$ (Hard Equality Constraint) | Demographic and institutional branch cannot be changed; prevents discriminatory advice. |
| **Class 2: Semi-Mutable (Monotonic)**| `F01: cgpa`, `F09: project_count`, `F11: has_internship`, `F12: certifications_count`, `F19: assessment_attempts` | $\mathbf{x}_i^* \ge \mathbf{x}_i$ and $\mathbf{x}_i^* \le \mathbf{x}_i + \Delta_{\max}$ | Past marks and experiences cannot decrease; semester GPA increases are mathematically bounded by credit caps. |
| **Class 3: Fully Mutable Skills** | `F02: dsa_score`, `F03: dbms_score`, `F04: os_score`, `F05: cn_score`, `F06: programming_score`, `F13: resume_ats_score`, `F14: cosine_similarity`, `F16: consistency_score` | $\mathbf{x}_i^* \in [0.0, 1.0]$ subject to concept prerequisite DAG | Competency gaps can be closed through active deliberate practice and resume re-formatting. |

### 4.3 Prerequisite Concept DAG Integration
DiCE optimization is constrained by the Computer Science Concept Prerequisite DAG (`DD-008`, `M08`). For example:
- The solver cannot recommend increasing `dsa_score` (`F02`) to $90\%$ if the prerequisite `programming_score` (`F06`) is below $50\%$.
- Any proposed counterfactual transition must follow a topologically valid learning trajectory.

---

## 5. Epistemological Separation: Prediction vs Explanation vs Causal Claims

To preserve scientific validity and adhere to the **Anti-Hallucination Rules** (Section 50):

```
┌────────────────────────────────────────────────────────────────────────┐
│                        EPISTEMOLOGICAL DISTINCTION                     │
├───────────────────────────────────┬────────────────────────────────────┤
│ PREDICTIVE ATTRIBUTION (TreeSHAP) │ CAUSAL RECOURSE (DiCE + DAG)       │
├───────────────────────────────────┼────────────────────────────────────┤
│ • States: "Feature X contributed  │ • Hypothesizes: "If a student      │
│   Y% to the statistical score."   │   improves X by delta, the model   │
│ • Mathematical property of the    │   predicts an uplift in score."    │
│   fitted model surface.           │ • Subject to unobserved confounders│
│ • NOT a causal claim about the    │   and student extrinsic motivation.│
│   real world.                     │ • Formally framed as a hypothesis. │
└───────────────────────────────────┴────────────────────────────────────┘
```

**Guardrail Policy**: PRIE dashboards are forbidden from displaying:
> *"Doing this will guarantee you get placed."*
Instead, the user interface displays:
> *"Based on institutional predictive models, completing these targeted milestones elevates your statistical readiness probability to 78%."*

---

## 6. Failure Modes & Degradation Handling

1. **DiCE Solver Timeout ($>3,000$ms)**:
   - *Condition*: Gradient optimization fails to converge in highly non-linear feature sub-spaces.
   - *Mitigation*: Fallback to nearest pre-computed **Cohort Archetype Counterfactual** (e.g., standard remediation profile for "CS Student with High CGPA but Low Coding").
2. **Feature Collinearity Distortion in TreeSHAP**:
   - *Condition*: High collinearity between `cgpa` and individual subject marks (`dsa_score`, `os_score`).
   - *Mitigation*: Compute TreeSHAP with feature correlation grouping (evaluating the collective academic cluster attribution).

---

## 7. Experimental Validation Plan Linkage

The XAI architecture is directly evaluated under **`EXP-4`** (`Experimental_Decisions.md`):
- **Hypothesis H4**: Distance-constrained prescriptive counterfactual explanations (DiCE) produce a statistically significant increase in student-rated actionability ($\ge 40\%$ increase, $p < 0.001$) and 30-day milestone completion rate over standard descriptive SHAP attribution charts.
- **Experimental Protocol**: Double-blind randomized controlled trial with 60 engineering undergraduates; measure Actionability Usability Score ($\ge 80\%$), Counterfactual Proximity ($L_1 \le 0.15$), Sparsity ($L_0 \le 3$), and objective 30-day task completion rates.
