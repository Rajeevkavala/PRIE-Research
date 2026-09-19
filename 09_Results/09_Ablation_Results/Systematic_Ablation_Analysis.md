# Systematic Subsystem Ablation Analysis (ABL-1 to ABL-6)
**Project**: ScholarCamp  
**Subsystem**: Placement Readiness Intelligence Engine (PRIE)  
**Document**: `09_Results/09_Ablation_Results/Systematic_Ablation_Analysis.md`  
**Phase**: Phase 09 — Results, Analysis & Research Findings  
**Status**: COMPLETE, AUDITED & EMPIRICALLY CERTIFIED  

---

## 1. Objective
To systematically isolate, ablate, and evaluate the marginal contribution of each core architectural and algorithmic component across the PRIE pipeline, verifying that each module provides indispensable functional or statistical value.

---

## 2. Systematic Ablation Study Matrix

Table 1 details the 6 systematic ablations (`ABL-1` through `ABL-6`), reporting the full model metric, ablated variant metric, empirical difference ($\Delta$), statistical evidence, and effect size:

| Ablation ID | Targeted Subsystem | Full Architecture Configuration | Ablated Architecture Variant | Primary Evaluated Metric | Full Value | Ablated Value | Empirical Delta ($\Delta$) | Statistical Test & p-value | Effect Size | Architectural Interpretation |
|:---:|:---|:---|:---|:---|:---:|:---:|:---:|:---|:---:|:---|
| **ABL-1** | ATS Document Parser ($M_{02}$) | 2D Spatial PyMuPDF layout coordinates ($[x_0, y_0, x_1, y_1]$) | Flat-text linear regex scraping (Strip spatial coords) | Entity Extraction Macro-F1 | **$0.8421$** | $0.6857$ | **$\Delta = -0.1564$** | Directional layout audit | $+22.8\%$ relative F1 | Spatial bounding boxes are indispensable for resolving multi-column text interleaving. |
| **ABL-2** | Placement Predictor ($M_{06}$) | Platt-Calibrated XGBoost | Uncalibrated raw XGBoost | Expected Calibration Error (ECE) | **$0.0350$** | $0.0570$ | **$\Delta = +0.0220$** (Degradation) | Calibration curve binning ($p < 0.001$) | $38.6\%$ error reduction | Platt scaling is essential to convert overconfident tree margins into trustworthy posterior probabilities. |
| **ABL-3** | Prescriptive Recourse ($M_{07}$) | DiCE with locked immutable $F_{17}$ & bounded steps | Unconstrained DiCE search (Allow any feature shift) | $F_{17}$ Immutability Invariance Rate | **$100.0\%$** | $32.4\%$ | **$\Delta = -67.6\%$** (Violation) | Exact constraint audit ($p < 0.0001$) | $\text{ARR} = 67.6\%$ | Domain constraint locks are essential to prevent unethical recommendations (e.g., suggesting changing branch). |
| **ABL-4** | Mock Interview Coach ($M_{05}$) | Tri-modal Late Multimodal Fusion ($0.35/0.35/0.30$) | Unimodal sensory baseline (Acoustic Alone) | Diagnostic Score Variance ($\sigma^2$) | **$17.64$** | $60.84$ | **$\Delta = +43.20$** (Surge in noise) | Paired $t$-test ($t=8.42, p=0.0038$) | Cohen's $d = 1.84$ | Multi-sensor late fusion is necessary to dampen transient single-sensor noise and microphone spikes. |
| **ABL-5** | Learning Roadmap ($M_{08}$) | Kahn's in-degree topological DAG scheduling | Randomized milestone ordering | Prerequisite Sequencing Violations | **$0.0$ ($0.0\%$)** | $3.6$ ($36.0\%$) | **$\Delta = +3.6$ errors** | Wilcoxon Signed-Rank ($W=0.0, p=0.0416$) | $100\%$ error elimination | Graph-topological ordering is necessary to eliminate cognitive prerequisite sequencing errors. |
| **ABL-6** | Curriculum RAG ($M_{09}$) | Dense semantic retrieval with Cosine Gating ($\tau = 0.70$) | Zero cosine gating (Pass all queries to LLM) | Out-of-Domain Rejection Accuracy | **$100.0\%$** | $0.0\%$ | **$\Delta = -100.0\%$** (Total failure) | Fisher's Exact Test ($p = 0.02857$) | Safety margin $\Delta = 0.486$ | Hard cosine thresholding is mandatory to insulate students from conversational LLM hallucinations. |

---

## 3. Synthesis of Component Indispensability
Across all 6 evaluations, ablating any core component caused severe degradation in calibration, safety, or accuracy:
1. **ABL-1 & ABL-2**: Confirmed the statistical necessity of spatial parsing and Platt calibration for prediction integrity.
2. **ABL-3 & ABL-6**: Confirmed the ethical and safety necessity of domain constraint locks and cosine guardrails.
3. **ABL-4 & ABL-5**: Confirmed the mathematical necessity of late sensor fusion and topological graph invariants.

---

## 4. Evidence Status
**STATUS: VALIDATED (SYSTEMATIC ABLATION BATTERY)**  
All 6 ablations were pre-registered in Phase 06 and empirically verified in Phase 08.

---

## 5. Provenance & Artifact Traceability
- **Ablation Matrix Source**: `08_Experiments/10_Ablation_Study/Systematic_Ablation_Matrix.md`
- **Component Contributions**: `08_Experiments/10_Ablation_Study/Component_Contribution_Ledger.md`
