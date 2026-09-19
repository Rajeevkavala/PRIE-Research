# Limitations and Epistemological Boundaries: ScholarCamp / PRIE

## 1. Executive Summary and Epistemological Position

The Placement Readiness Intelligence Engine (PRIE) framework has been subjected to rigorous statistical and computational evaluation across six core empirical experiments (`EXP-1` to `EXP-6`). While the quantitative benchmarks demonstrate high internal mathematical consistency, calibrated uncertainty estimation, and algorithmic feasibility, all findings must be contextualized within strict methodological boundaries. In accordance with open scientific integrity standards, this document articulates the structural, empirical, algorithmic, and observational limitations governing Phase 09 results.

The primary epistemological boundary of this research is:
$$\text{Simulated Algorithmic Efficacy} \neq \text{Causal Real-World Employment Uplift}$$

---

## 2. Dataset Limitations

### 2.1 Synthetic Nature of Primary Benchmark (`DS-SYNTH-01`)
* **Underlying Generator**: The primary predictive validation dataset, `DS-SYNTH-01` ($N = 2,500$), was generated via controlled parametric distributions informed by domain-informed academic priors (`Synthetic_Data_Generator.py`).
* **Lack of Unobserved Confounders**: Real-world placement hiring processes involve substantial latent noise, interpersonal networking dynamics, campus recruitment brand tiering, macroeconomic hiring freezes, and behavioral quirks that are absent from parametric synthetic generation.
* **Overly Well-Behaved Manifolds**: Synthetic tabular features exhibit cleaner class separability and smoother decision surfaces than real-world institutional educational records, which may yield artificially high ROC-AUC ($0.9922$) and Macro-F1 ($0.9390$).

### 2.2 Absence of Real Student Validation (`DS-REAL-01`)
* **Status**: `DATA COLLECTION REQUIRED`.
* Institutional review board (IRB) approval, student consent workflows, and longitudinal data governance frameworks are designed in Phase 06/07 but have not yet been executed with an active human cohort.
* Consequently, the empirical metrics reflect algorithmic performance on synthetic simulated student records rather than verified human undergraduate trajectories.

---

## 3. Sample Size Limitations

### 3.1 Simulated Multimodal Interview Sessions (`DS-INTERVIEW-SIM`)
* **Session Scale**: The multimodal evaluation (`EXP-3`) operates across $N = 50$ simulated student mock interview recordings.
* **Statistical Power**: While $N = 50$ is sufficient to demonstrate variance reduction in late fusion under parametric assumptions ($t = 9.88, p = 0.0022$), it is insufficiently powered to support deep representation learning, end-to-end multimodal transformers, or exhaustive sub-population demographic stratification.
* **Recruiter Benchmark Scale**: The human expert recruiter pilot dataset (`DS-INTERVIEW-PILOT`) remains uncollected (`DATA COLLECTION REQUIRED`), precluding empirical ground-truth human-to-algorithm correlation analysis ($r \ge 0.82$).

### 3.2 Counterfactual Recourse Profile Subset
* The prescriptive recourse optimization in `EXP-2` was evaluated across $N = 30$ at-risk student profiles ($P_{\text{pred}} < 0.50$).
* While sufficient to confirm mathematical invariance of immutable attributes (100% preservation) and $L_1$ sparsity convergence ($k = 2.47 \le 3.0$), larger cohort testing ($N > 500$) is required to map edge-case manifold regions where DiCE loss gradients could fail to converge.

---

## 4. Model and Architectural Limitations

### 4.1 Tree-Based Ensembles and Tabular Inductive Biases
* The primary classifier is an XGBoost gradient boosted tree ensemble. While superior for tabular heterogeneity, tree ensembles generate axis-aligned, step-function decision surfaces.
* Local gradients used in gradient-based explainability or recourse approximations can encounter zero-derivative plateaus, requiring DiCE to rely on sampling-based perturbations or surrogate models.

### 4.2 Calibration Constraints
* Platt Scaling (logistic sigmoid calibration) operates under the assumption that raw model margin outputs are monotonically transformable to true log-odds via a two-parameter affine mapping:
$$P(Y=1 \mid f(x)) = \frac{1}{1 + \exp(A \cdot f(x) + B)}$$
* If the true conditional risk distribution possesses multi-modal distortions or non-monotonic local anomalies, isotonic regression or spline calibration would be required, though both risk overfitting on small validation splits ($N_{\text{val}} = 250$).

### 4.3 Spatial ATS Feature Extraction
* The LayoutLMv3 spatial vision-language model remained untrained due to GPU cluster resource bounds (`MODEL NOT TRAINED`).
* Spatial evaluation in `EXP-4` was conducted using a PyMuPDF 2D bounding-box geometric heuristic parser. While outperforming 1D flat regex by $+0.1564$ Macro-F1, it lacks cross-modal visual attention for arbitrary multi-column graphical resumes.

---

## 5. Algorithmic and Optimization Limitations

### 5.1 Curriculum Graph Acyclicity Assumption
* The 38-node computer science concept network (`cs_concept_dag.json`) strictly assumes a Directed Acyclic Graph (DAG).
* In pedagogical reality, human learning is frequently non-linear and iterative, requiring cyclic reinforcement loops (e.g., revisiting dynamic programming while studying advanced graph theory). The current Kahn topological scheduler (`EXP-5`) cannot directly handle cyclic mutual dependencies without graph edge-pruning.

### 5.2 Heuristic Topological Scheduling
* The topological sort produces a valid linear ordering satisfying prerequisite constraints (0 violations, $0.0\%$), but does not compute globally optimal cognitive load scheduling across parallel student time constraints (an NP-hard bin packing / job-shop scheduling formulation).

---

## 6. Evaluation and Observational Limitations

### 6.1 Lack of Longitudinal Prospective Studies
* All evaluations are retrospective offline benchmarks. PRIE has not yet been deployed in an active prospective A/B trial comparing a cohort guided by PRIE vs. a control group guided by conventional placement cell advisory.
* Claims regarding "placement uplift" ($\ge 15\%$) remain theoretical targets awaiting multi-semester physical trial execution.

### 6.2 Non-Causal Nature of Explanations
* Consistent with the Phase 09 Epistemological Framework, SHAP feature importance values ($S_{\text{dsa}} = +0.1420$, $S_{\text{cgpa}} = +0.1080$) and counterfactual delta values ($\Delta \text{DSA} = +22.4$) represent **associative feature contributions within the predictive model**, NOT direct causal guarantees of recruitment success.
* Improving a student's DSA score in isolation may not yield placement if unmodeled market hiring conditions fluctuate.

---

## 7. Summary of Limitations, Severity, and Mitigation Roadmap

| ID | Limitation Dimension | Severity | Manifestation in Phase 09 | Mitigation / Future Phase Strategy |
|:---|:---|:---:|:---|:---|
| **LIM-01** | Synthetic Benchmark (`DS-SYNTH-01`) | High | All predictive metrics evaluated on simulated data | Deploy `DS-REAL-01` multi-institutional trial in Phase 10 |
| **LIM-02** | Uncollected Real Cohort | High | Inability to test real-world placement conversion | Execute longitudinal IRB-approved pilot across 500 students |
| **LIM-03** | Untrained LayoutLMv3 | Medium | ATS parsing relies on PyMuPDF geometric heuristics | Fine-tune LayoutLMv3 on 1,000 annotated multi-column resumes |
| **LIM-04** | Small Multimodal Sample ($N=50$) | Medium | High variance in sub-component speech features | Scale recording capture to $N \ge 1,000$ real mock sessions |
| **LIM-05** | Missing Recruiter Panel | Medium | Ground truth recruiter correlation unverified | Collect `DS-INTERVIEW-PILOT` panel ratings across 5 HR leads |
| **LIM-06** | DAG Acyclicity Constraint | Low | Graph cannot represent cyclic pedagogy | Implement Hierarchical Task Networks (HTN) with cyclical review nodes |
| **LIM-07** | Associative vs Causal Recourse | High | Counterfactual recommendations non-causal | Integrate Do-calculus structural causal models (SCM) |
| **LIM-08** | Offline Benchmark Only | High | Zero prospective randomized trial evidence | Conduct 2-arm randomized controlled trial (RCT) over 1 academic year |
