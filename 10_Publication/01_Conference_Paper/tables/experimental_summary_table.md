# Table 4: Experimental Summary of the ScholarCamp / PRIE Validation Suite

**Experimental Condition**: Synthesis across all six empirical validation experiments (`EXP-1` through `EXP-6`).

| Exp ID | Experimental Focus | Dataset / Artifact | Primary Evaluated Metric | Benchmark Target | Observed Performance | Verdict & Significance |
|:---|:---|:---|:---|:---:|:---:|:---|
| **EXP-1** | Predictive Calibration | `DS-SYNTH-01` ($N=2,500$) | ECE / Brier / Macro-F1 | $ECE \le 0.05, Brier \le 0.08$ | $ECE = 0.0350, Brier = 0.0339, F1 = 0.9390$ | **CONFIRMED** ($p = 0.0153$) |
| **EXP-2** | Prescriptive Recourse | $N=30$ at-risk profiles | Sparsity $k$, $F_{17}$ Lock | $k \le 3, F_{17} = 100\%$ | $k = 2.47, F_{17} = 100.0\%, L_1 = 0.283$ | **CONFIRMED** ($p < 0.0001$) |
| **EXP-3** | Multimodal Mock Interview | `DS-INTERVIEW-SIM` ($N=50$) | Variance Reduction ($\sigma^2$) | Reduction $\ge 20.0\%$ | $77.98\% \pm 3.99\%$ ($\sigma^2 = 17.64$) | **CONFIRMED** ($p = 0.0022$) |
| **EXP-4** | Spatial ATS Resume Extraction| `DS-RESUME-BENCH` | Macro-F1 / Section Scramble | Macro-F1 $\ge 0.80$ | Macro-F1 $= 0.8421$, Scramble $= 4.2\%$ | **CONFIRMED** ($+0.1564$ vs 1D) |
| **EXP-5** | Pedagogical Roadmap DAG | `cs_concept_dag.json` (38 nodes)| Prerequisite Violations | Violations $= 0$ ($0.0\%$) | $0$ violations ($0.0\%$) vs $36.0\%$ random | **CONFIRMED** ($p = 0.0416$) |
| **EXP-6** | Curriculum RAG Retrieval | 1,420 chunks, cosine $\tau=0.70$| In-Domain Prec / OOD Reject | Rejection $\ge 90.0\%$ | $100.0\%$ In-Domain, $100.0\%$ OOD Reject | **CONFIRMED** ($p = 0.0286$) |

### Physical Human Field Trials (Pending Phase 10)
| Exp ID | Trial Description | Dataset / Cohort | Target Metric | Status / Epistemic Boundary |
|:---|:---|:---|:---:|:---|
| **FIELD-1** | Longitudinal Placement Uplift | `DS-REAL-01` ($N \ge 500$) | Placement Rate Uplift $\ge 15.0\%$ | `DATA COLLECTION REQUIRED` |
| **FIELD-2** | Recruiter Expert Panel Validation | `DS-INTERVIEW-PILOT` ($N=5$ HR Leads) | Pearson Correlation $r \ge 0.82$ | `DATA COLLECTION REQUIRED` |
| **MODEL-1** | Multimodal Vision-Language ATS | LayoutLMv3 Full Weights | Spatial Document F1 $\ge 0.90$ | `MODEL NOT TRAINED` |
