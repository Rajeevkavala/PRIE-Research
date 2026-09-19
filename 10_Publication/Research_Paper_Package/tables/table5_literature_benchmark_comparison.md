# Table 5: Comparison of Existing Methods with the Proposed PRIE Method

**Condition**: Benchmark evaluation against published educational data mining and employability prediction architectures on engineering student placement cohorts.

| Authors & Citation | Methodology / Classifier Architecture | Reported Accuracy | Improvement by Proposed PRIE | Key Limitations of Prior Baseline |
|:---|:---|:---:|:---:|:---|
| **Rao & Swamy (2022)** [10] | Decision Tree (CART) | 78.40% | **+16.20%** | Prone to overfitting on small cohorts; lacks probability calibration and recourse mechanisms. |
| **Casuat & Festijo (2021)** [9] | Multi-Classifier Ensemble (Voting) | 84.50% | **+10.10%** | Treats placement as terminal binary classification in final semester; high false-positive rate. |
| **Olipas, C.N. (2024)** [1] | Random Forest Ensemble | 88.40% | **+6.20%** | Uncalibrated risk estimates ($ECE > 0.08$); provides descriptive SHAP without actionable recourse. |
| **Patel & Nair (2024)** [5] | Multi-Variable Machine Learning | 91.20% | **+3.40%** | Point-in-time assessment lacking multimodal interview fusion and prerequisite-preserving roadmaps. |
| **Proposed PRIE Model** | **Cost-Sensitive Platt-Calibrated XGBoost** | **94.60%** | **Baseline** | **Calibrated ($ECE=0.0350$), Constrained Recourse ($k \le 3$), Tri-Modal Late Fusion, Zero DAG Violations.** |

### Key Observations
1. **Predictive Superiority**: PRIE surpasses traditional CART decision trees by $16.20\%$ and advanced multi-variable ML baselines by $3.40\%$ on hold-out test folds.
2. **Reliability & Actionability**: Unlike prior systems that terminate at risk prediction, PRIE bridges predictive classification to closed-loop remediation via TreeSHAP and constrained DiCE counterfactual optimization.
