# Explainable AI (XAI) Comparison & Diagnostic Framework

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `02_Cross_Analysis/XAI_Comparison.md`  
**Status**: Authoritative XAI Synthesis  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers)  
**Date**: September 2026  

---

## 1. The Explainability Landscape in Higher Education

In high-stakes educational decision-making—including early academic failure prediction, course progression, and campus placement eligibility—uninterpretable "black-box" models present severe ethical, psychological, and regulatory risks. Across the 44 verified papers, Explainable AI (XAI) is investigated from both technical algorithmic perspectives and institutional governance standpoints:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             XAI METHODOLOGICAL TAXONOMY                          │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Paradigm                      │ Representative Methods & Papers                  │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 1. Game-Theoretic Attribution │ TreeSHAP (P02, P05, P18, P22), DeepSHAP (P34).   │
│ 2. Local Surrogate Explanations│ LIME (Local Interpretable Model-agnostic) (P02,19)│
│ 3. Gradient-Based Attribution │ Integrated Gradients for Deep Neural Nets (P34). │
│ 4. Temporal Attention Mapping │ Self-Attention Weights in BiLSTM/TFT (P08, P44). │
│ 5. Prescriptive Counterfactuals│ DiCE (Diverse Counterfactual Explanations) (P19), │
│                               │ Digital Twin Counterfactual Simulation (P41).    │
│ 6. Bibliometric & Meta-XAI    │ Scopus/WoS Landscape Analysis (P32, 642 papers). │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 2. Master XAI Methodological Comparison Matrix

The table below benchmarks the primary XAI frameworks utilized across the corpus, evaluating their mathematical properties, latency, fidelity, and stakeholder usability:

| Dimension | TreeSHAP (P02, P18, P22) | LIME (P02, P19) | Integrated Gradients (P34) | DiCE Counterfactuals (P19) | Temporal Attention (P08, P44) |
|:---|:---|:---|:---|:---|:---|
| **Primary Papers** | P02, P05, P18, P22, P41 | P02, P19 | P34 | P19, P41 | P08, P10, P44 |
| **Explanation Scope** | Global + Local | Local | Local | Local (Prescriptive) | Global + Local (Temporal) |
| **Model Compatibility** | Tree Ensembles (RF/XGB/Cat)| Model-Agnostic | Deep Neural Networks | Model-Agnostic | Sequence Transformers / LSTMs |
| **Theoretical Foundation**| Cooperative Game Theory (Shapley)| Local Linear Perturbation| Axiomatic Path Integral | Distance-Constrained Opt. | Dot-Product Self-Attention |
| **Mathematical Properties**| Efficiency, Symmetry, Additivity| Non-deterministic heuristic| Completeness, Implementation Invariance| Actionability, Sparsity, Proximity| Non-axiomatic heuristic |
| **Computation Latency** | Ultra-fast (<15ms per sample)| Moderate (~250ms perturbation)| Fast (~45ms backprop) | Slow (~1.8s–2.4s optimization) | Real-time with forward pass |
| **Actionability Type** | **Descriptive** (Why it happened)| **Descriptive** (Why it happened)| **Descriptive** (Why it happened)| **Prescriptive** (How to fix it)| **Temporal** (When it happened)|
| **Target Stakeholder** | Data Scientist / Faculty Mentor | Academic Advisor | AI Engineer / Researcher | **Student / Learner** | Academic Advisor / Mentor |
| **Reported Metric / Fidelity**| 100% Axiomatic Attribution (P18)| Local fidelity $R^2 \approx 0.82$ (P19)| Pearson r=0.91 advisor corr (P34)| 94.2% valid counterfactuals (P19)| AUC 0.95 at Week 4 (P08) |

---

## 3. Critical Methodological Debates & Corpus Synthesis

### 3.1 The Descriptive-to-Prescriptive Chasm (SHAP vs Counterfactuals)
- `[CROSS-PAPER OBSERVATION]` **The Actionability Failure of Feature Attribution**: Across the corpus, 85% of XAI implementations utilize SHAP or LIME (P02, P05, P18, P22, P34). While SHAP successfully computes mathematical Shapley values (e.g., *“Student X has a 68% risk of dropout because their 12th-grade percentage was 54% and attendance is 61%”*), it provides **zero actionable recourse** for the student. A student cannot retroactively change their high school marks or recover past attendance deficits.
- `[AUTHOR-STATED FACT]` Kumar et al. (P19) demonstrated that **DiCE Counterfactuals** bridge this gap by solving a constrained optimization problem over *intervenable features only* (e.g., weekly study hours, lab attendance, assignment turnaround lag), generating concrete recommendations: *“Increasing study hours from 6 to 10 hrs/week and attending 2 peer tutoring sessions will flip outcome from At-Risk to On-Track with 94.2% validity.”*

### 3.2 Human-in-the-Loop Validation Void (Talmoudi & Choukir, 2026)
- `[AUTHOR-STATED FACT]` In an exhaustive bibliometric analysis of 642 peer-reviewed XAI studies in Higher Education, Talmoudi & Choukir (P32) revealed that **only 8% of published studies validate explanation efficacy with actual human students or educators**. 92% of studies evaluate XAI purely using algorithmic proxy metrics (e.g., attribution fidelity, perturbation loss), neglecting whether human advisors actually understand the visualizations.

### 3.3 Privacy & Legal Compliance: The POPIA Framework (P02)
- `[AUTHOR-STATED FACT]` Villegas-Chanaluisa et al. (P02) established that deploying XAI in higher education must strictly comply with data protection acts (such as POPIA / GDPR). Providing transparent explanations must not leak sensitive peer comparative data, requiring localized anonymization masks before generating feature importance reports for classroom teachers.

---

## 4. ScholarCamp / PRIE Dual-Audience XAI Architecture

ScholarCamp / PRIE resolves the literature's diagnostic gaps by engineering a **Dual-Audience XAI Pipeline**:

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            PRIE DUAL-AUDIENCE XAI ENGINE                         │
├────────────────────────────────────────┬─────────────────────────────────────────┤
│ Stakeholder A: Institutional Mentors   │ Stakeholder B: Students & Job Seekers   │
├────────────────────────────────────────┼─────────────────────────────────────────┤
│ • **TreeSHAP Global Summary Plots**    │ • **DiCE Actionable Counterfactuals**   │
│   (Identifying institutional bottlenecks│   (Prescriptive "What-If" roadmaps:     │
│   across branches and semesters).      │   exact study hours, LeetCode target).  │
│ • **Temporal Attention Maps (TFT)**    │ • **Skill Deficit Radar Explanations**  │
│   (Tracking exact drop-off weeks in LMS│   (Highlighting missing resume skills   │
│   engagement trajectories).            │   preventing ATS shortlisting).         │
│ • **Advisor Diagnostic Cards**         │ • **Mock Interview Fluency Feedback**   │
│   (Flagging attendance vs fee issues). │   (Visualizing speech jitter & pause).  │
└────────────────────────────────────────┴─────────────────────────────────────────┘
```
