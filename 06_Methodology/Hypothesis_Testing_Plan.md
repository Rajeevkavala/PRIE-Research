# Hypothesis Testing Plan: Formal Decision Rules, Alpha Levels & Effect Size Criteria

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Hypothesis_Testing_Plan.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Hypothesis Testing Plan  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Epistemological Pre-Condition: Zero Fabricated Decisions

> [!IMPORTANT]
> **NO HYPOTHESES ARE MARKED ACCEPTED OR REJECTED IN PHASE 06**  
> In strict compliance with scientific method principles:  
> **Phase 06 establishes the formal Null ($H_0$) and Alternative ($H_1$) hypotheses, test statistics, significance thresholds ($\alpha$), and decision boundaries.**  
> Definitive empirical decisions (acceptance/rejection) will occur exclusively in Phase 09 (`09_Results`) following experimental execution in Phase 08 (`08_Experiments`).

---

## 2. Granular Hypothesis Testing Protocols (H1 to H6)

---

### Hypothesis 1 (H1): Spatial Layout Document Intelligence in ATS Screening
- **Statement**: Multimodal LayoutLMv3 incorporating 2D spatial bounding boxes achieves statistically superior entity Boundary-F1 over flat-text NER on multi-column resumes.
- **Null Hypothesis ($H_{0, 1}$)**: $\mu_{\text{LayoutLMv3}} \le \mu_{\text{BERT-Flat}}$ (No positive Boundary-F1 improvement).
- **Alternative Hypothesis ($H_{1, 1}$)**: $\mu_{\text{LayoutLMv3}} > \mu_{\text{BERT-Flat}}$ (Boundary-F1 improvement $\ge 0.15$).
- **Statistical Test**: Two-tailed Wilcoxon signed-rank test on paired document test instances.
- **Significance Level**: $\alpha = 0.01$.
- **Decision Rule**: Reject $H_{0, 1}$ if $p < 0.01$ and empirical difference $\Delta \text{Boundary-F1} \ge 0.15$.

---

### Hypothesis 2 (H2): Multimodal Conversational Latency & Human Panel Correlation
- **Statement**: A streaming chunked speech pipeline achieves sub-1.5s voice turnaround while maintaining high positive correlation ($r \ge 0.70$) with blinded recruiter evaluations.
- **Null Hypothesis ($H_{0, 2}$)**: $\mu_{\text{latency}} \ge 1,500\text{ms}$ or $\rho_{\text{recruiter}} < 0.70$.
- **Alternative Hypothesis ($H_{1, 2}$)**: $\mu_{\text{latency}} < 1,500\text{ms}$ and $\rho_{\text{recruiter}} \ge 0.70$.
- **Statistical Test**: One-sample $t$-test on turn latencies; Fisher $Z$-transformation test for Pearson correlation $r$.
- **Significance Level**: $\alpha = 0.001$.
- **Decision Rule**: Reject $H_{0, 2}$ if $p_{\text{latency}} < 0.001$ with mean latency $< 1500\text{ms}$, and $p_r < 0.001$ with $r \ge 0.70$.

---

### Hypothesis 3 (H3): Longitudinal Multi-Horizon Forecasting vs Static Modeling
- **Statement**: Temporal Fusion Transformer (TFT) sequence models achieve superior multi-horizon readiness forecasting (Quantile Loss reduction $\ge 12\%$) over static tabular XGBoost.
- **Null Hypothesis ($H_{0, 3}$)**: $\text{QL}_{\text{TFT}} \ge 0.88 \times \text{QL}_{\text{XGBoost}}$ (Quantile loss reduction $< 12\%$).
- **Alternative Hypothesis ($H_{1, 3}$)**: $\text{QL}_{\text{TFT}} < 0.88 \times \text{QL}_{\text{XGBoost}}$ (Quantile loss reduction $\ge 12\%$).
- **Statistical Test**: Diebold-Mariano test for predictive accuracy on rolling-origin backtesting folds.
- **Significance Level**: $\alpha = 0.01$.
- **Decision Rule**: Reject $H_{0, 3}$ if $p < 0.01$ and relative quantile loss reduction $\ge 12\%$.

---

### Hypothesis 4 (H4): Actionability and Usability of Prescriptive Counterfactuals
- **Statement**: DiCE distance-constrained counterfactuals yield statistically higher student actionability ratings ($\ge 40\%$ increase) and 30-day milestone completion rates over descriptive TreeSHAP attribution.
- **Null Hypothesis ($H_{0, 4}$)**: $\mu_{\text{actionability}}^{(\text{DiCE})} \le 1.40 \times \mu_{\text{actionability}}^{(\text{SHAP})}$.
- **Alternative Hypothesis ($H_{1, 4}$)**: $\mu_{\text{actionability}}^{(\text{DiCE})} > 1.40 \times \mu_{\text{actionability}}^{(\text{SHAP})}$.
- **Statistical Test**: Paired Student's $t$-test on Likert actionability scores; Chi-square test on 30-day milestone completions.
- **Significance Level**: $\alpha = 0.001$.
- **Decision Rule**: Reject $H_{0, 4}$ if $p < 0.001$ with Cohen's $d \ge 0.80$ (large effect size).

---

### Hypothesis 5 (H5): Psychometric Discrimination in Causal Concept AQG
- **Statement**: Automatic question generation guided by causal concept DAGs yields multiple-choice items with statistically higher Item Discrimination ($DI \ge 0.35$) and Distractor Plausibility ($DPI \ge 0.70$) than zero-shot LLMs.
- **Null Hypothesis ($H_{0, 5}$)**: $\mu_{DI}^{(\text{Causal})} \le \mu_{DI}^{(\text{Zero-Shot})}$ or $\mu_{DPI}^{(\text{Causal})} \le \mu_{DPI}^{(\text{Zero-Shot})}$.
- **Alternative Hypothesis ($H_{1, 5}$)**: $\mu_{DI}^{(\text{Causal})} > \mu_{DI}^{(\text{Zero-Shot})}$ with $DI \ge 0.35$, and $DPI \ge 0.70$.
- **Statistical Test**: Two-sample independent $t$-test for $DI$; Mann-Whitney $U$ test for $DPI$.
- **Significance Level**: $\alpha = 0.01$.
- **Decision Rule**: Reject $H_{0, 5}$ if $p < 0.01$ with mean $DI \ge 0.35$ and $DPI \ge 0.70$.

---

### Hypothesis 6 (H6): Placement Conversion Uplift in Closed-Loop Digital Twin
- **Statement**: Closed-loop triangular digital twin integration yields a statistically significant uplift ($\ge 15\%$ increase) in institutional campus placement conversion over disconnected point tools.
- **Null Hypothesis ($H_{0, 6}$)**: $P_{\text{placed}}^{(\text{PRIE})} - P_{\text{placed}}^{(\text{Control})} < 0.15$.
- **Alternative Hypothesis ($H_{1, 6}$)**: $P_{\text{placed}}^{(\text{PRIE})} - P_{\text{placed}}^{(\text{Control})} \ge 0.15$.
- **Statistical Test**: Two-proportion $Z$-test; Kaplan-Meier survival log-rank test for time-to-placement.
- **Significance Level**: $\alpha = 0.05$.
- **Decision Rule**: Reject $H_{0, 6}$ if $p < 0.05$ with absolute conversion uplift $\Delta \ge 0.15$.
