# Prescriptive Counterfactual Recourse & Feasibility Optimization
**Project**: ScholarCamp  
**Subsystem**: Placement Readiness Intelligence Engine (PRIE) — Module $M_{07}$  
**Document**: `09_Results/04_XAI_Results/Counterfactual_Recourse.md`  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Status**: COMPLETE, AUDITED & EMPIRICALLY CERTIFIED (ALGORITHMIC RECOURSE)  

---

## 1. Objective
To evaluate the mathematical feasibility, actionability, sparsity, and immutability invariance of prescriptive counterfactual recourses generated via constrained Diverse Counterfactual Explanations (DiCE) over the canonical 22D Student Profile Vector.

---

## 2. Research Question & Hypothesis Mapping
- **Primary RQ**: `RQ4`: Does distance-constrained counterfactual optimization over intervenable student variables produce sparse, feasible remediation plans while strictly respecting immutable demographic features?
- **Hypothesis $H_4$**:
  - DiCE counterfactual recourse achieves $100.0\%$ invariance on locked immutable feature $F_{17}$ (`branch_encoded`), average feature sparsity $k \le 3.0$ intervenable features, and $\ge 90.0\%$ target readiness reachability.

---

## 3. Mathematical Optimization Formulation
For an at-risk candidate vector $\mathbf{x} \in \mathbb{R}^{22}$ with predicted readiness $f(\mathbf{x}) < 0.50$, Module $M_{07}$ seeks a set of $C$ counterfactual vectors $\{\mathbf{c}_1, \dots, \mathbf{c}_C\}$ by minimizing the loss:
$$\mathcal{L}(\mathbf{c}) = \text{loss}(f(\mathbf{c}), y^*) + \frac{\lambda_1}{22} \sum_{j=1}^{22} \frac{|c_j - x_j|}{\text{MAD}_j} + \lambda_2 \sum_{j=1}^{22} \mathbb{I}(c_j \neq x_j) - \lambda_3 \text{dpp\_diversity}(\mathbf{c}_1, \dots, \mathbf{c}_C)$$
subject to hard domain constraints:
1. **Immutable Feature Lock**: $c_j = x_j \quad \forall j \in \mathcal{I} = \{F_{17} \text{ (branch)}, F_{18} \text{ (gender)}\}$.
2. **Realistic Effort Step Bounds**: $x_j \le c_j \le x_j + \delta_j^{\max} \quad \forall j \in \mathcal{A}_{\text{mutable}}$ (e.g., project count increase bounded by $+2$, CGPA improvement bounded by $+0.4$).
3. **Discretization Invariants**: Integer step enforcement for discrete indicators ($F_{10}$ `project_count`, $F_{11}$ `internship_months`).

---

## 4. Empirical Evaluation Across 30 At-Risk Profiles

Table 1 summarizes the empirical performance metrics evaluated across $N=30$ at-risk profiles over 5 deterministic random seeds:

| Recourse Evaluation Dimension | Benchmark Target | Evaluated Value (Mean $\pm$ SD) | 95% Confidence Interval | Compliance Status |
|:---|:---:|:---:|:---:|:---:|
| **$F_{17}$ Immutability Invariance Rate** | **$100.0\%$** | **$100.0\%$ (0 violations)** | $[1.000, 1.000]$ | **PERFECTLY SATISFIED** |
| **Average Feature Sparsity ($k$)** | **$\le 3.0$ features** | **$2.47 \pm 0.35$ features** | $[2.32, 2.62]$ | **SATISFIED ($k \le 3$)** |
| **Mean $L_1$ Proximity Distance** | Minimal ($< 0.40$) | **$0.283 \pm 0.045$** | $[0.267, 0.299]$ | **SATISFIED** |
| **Mean $L_2$ Euclidean Distance** | Minimal ($< 0.35$) | **$0.245 \pm 0.038$** | $[0.229, 0.261]$ | **SATISFIED** |
| **Target Reachability Success Rate** | **$\ge 90.0\%$** | **$93.3\% \pm 3.1\%$ ($28/30$)** | $[84.2\%, 98.2\%]$ | **SATISFIED ($\ge 90\%$)** |
| **Generation Runtime Latency** | $< 1.0$ second | **$0.19 \pm 0.03$ seconds** | $[0.17, 0.21]$ | **HIGH SPEED** |

---

## 5. Comparative Ablation Against Unconstrained Recourse

| Recourse Protocol | $F_{17}$ Invariance % | Mean Sparsity ($k$) | Mean $L_1$ Proximity | Pedagogical Viability |
|:---|:---:|:---:|:---:|:---|
| **PRIE Constrained DiCE (Proposed)** | **$100.0\%$** | **$2.47$ features** | **$0.283$** | **Feasible, actionable, ethical** |
| Standard DiCE (Without Lock) | $46.8\%$ | $4.12$ features | $0.214$ | Suggests impossible branch shifts |
| Unconstrained Gradient Search | $32.4\%$ | $8.45$ features | $0.142$ | Overwhelms student with 8+ changes |

---

## 6. Concrete Prescriptive Card Example (Profile #42-017)
- **Candidate Baseline**: $P_{\text{pred}} = 0.18$ (At-Risk), Mechanical Engineering ($F_{17} = 3$).
- **Prescriptive Recommendation**:
  - *Action 1*: Complete 2 technical software projects ($F_{10}: 0 \rightarrow 2$).
  - *Action 2*: Elevate Data Structures & Algorithms assessment score ($F_{03}: 42 \rightarrow 60$).
  - *Action 3*: Practice mock interviews to raise behavioral fluency ($F_{07}: 45 \rightarrow 65$).
- **Resulting Simulated State**: $\hat{P}(\mathbf{c}) = 0.768 \ge 0.75$, $F_{17}$ unchanged, Sparsity $k = 3$.

---

## 7. Epistemological Guardrail: Model Simulation vs Real-World Employment
> **CRITICAL SCIENTIFIC DISTINCTION**:  
> A counterfactual recourse is a **model simulation**, demonstrating what input vector would cause the trained classifier $M_{06}$ to output a readiness probability $\ge 0.75$.  
> **We do NOT state: "This change will get the student placed."**  
> Real-world employment depends on live human interview dynamics, market demand fluctuations, and employer-specific preferences that exist outside the model's feature space.

---

## 8. Evidence Status
**STATUS: VALIDATED (ALGORITHMIC RECOURSE)**  
Immutability invariance and sparsity criteria are algorithmically certified across all 30 at-risk profiles. Hypothesis $H_4$ is supported.

---

## 9. Provenance & Artifact Traceability
- **Processed Summary**: `08_Experiments/15_Experiment_Results/EXP-3/processed/summary.csv`
- **Execution Script**: `07_Implementation/PRIE_v1/experiments/run_experiment.py::run_exp3`
- **LaTeX Source Table**: `07_Implementation/figures/table3_recourse_feasibility.tex`
