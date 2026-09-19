# Threats to Validity: ScholarCamp / PRIE Empirical Evaluation

## 1. Overview and Scientific Framework

A comprehensive assessment of threats to validity is mandatory to delineate the scientific credibility, bounds of inference, and replicability of the findings generated in Phase 09 of the Placement Readiness Intelligence Engine (PRIE) project. Following the canonical Campbell & Stanley (1963) and Wohlin et al. (2012) taxonomies for empirical computer science and educational data mining, this document analyzes threats across six dimensions: Construct, Internal, External, Statistical Conclusion, Measurement, and Model Validity.

---

## 2. Construct Validity

*Construct validity examines whether the operationalized variables, metrics, and experimental tasks accurately represent the theoretical concepts under investigation.*

### 2.1 Operationalization of "Placement Readiness"
* **Theoretical Construct**: Placement readiness is a multi-faceted, socio-technical competence comprising algorithmic fluency, software engineering proficiency, verbal articulation, behavioral demeanor, and psychological resilience under pressure.
* **Operational Approximation**: In `EXP-1`, placement readiness is operationalized as a binary classification label $Y \in \{0, 1\}$ derived from parametric simulation based on CGPA, DSA score, aptitude score, projects completed, and interview performance.
* **Threat**: A high classification probability ($P_{\text{pred}} \ge 0.70$) indicates adherence to the feature weighting schema, but may omit latent factors such as communication subtlety, domain enthusiasm, and cultural alignment.
* **Mitigation**: Multimodal integration (`EXP-3`) explicitly incorporates behavioral and acoustic cues (pitch variance, filler word frequency, gaze stability) to broaden construct coverage beyond purely academic metrics.

### 2.2 Metric Misalignment (The Goodhart's Law Threat)
* When a measure becomes a target, it ceases to be a good measure. If students optimize exclusively for features identified by SHAP ($F_1$ DSA, $F_2$ CGPA), they may exhibit surface-level rote memorization without acquiring genuine problem-solving depth.
* **Mitigation**: The counterfactual recourse generator enforces sparsity ($k \le 3$) and bounds changes to realistic, step-wise educational trajectories, combined with concept-level DAG validation (`EXP-5`).

---

## 3. Internal Validity

*Internal validity assesses whether the observed experimental outcomes are genuine consequences of the tested algorithms rather than confounding variables, data leakage, or procedural artifacts.*

### 3.1 Data Leakage and Split Isolation
* **Threat**: Leakage between training, validation, and test splits could artificially inflate accuracy and calibration metrics.
* **Mitigation**: All feature scaling (StandardScaler), imputation, and Platt calibration mappings were fit strictly on $N_{\text{train}} = 2,000$ and $N_{\text{val}} = 250$, with zero exposure to $N_{\text{test}} = 250$. Cross-validation across five distinct random seeds ($\{42, 123, 456, 789, 2026\}$) demonstrated negligible variance (Macro-F1 std $= 0.0187$), confirming split isolation.

### 3.2 Calibration Drift and Confounder Controls
* **Threat**: Uncalibrated probabilities could mislead downstream decision boundaries.
* **Mitigation**: Rigorous reliability diagram analysis and Expected Calibration Error ($ECE = 0.0350 \le 0.05$) verify that predicted confidence levels correspond directly to observed empirical frequencies.
* **Protected Attribute Invariance**: In `EXP-2`, branch encoding ($F_{17}$) was constrained to zero perturbation ($\Delta = 0.0, 100\%$ preservation), verifying that recourse interventions do not exploit demographic or institutional proxies.

---

## 4. External Validity

*External validity evaluates the degree to which empirical findings generalize across diverse institutions, candidate populations, and real-world industrial hiring cycles.*

### 4.1 Synthetic-to-Real Domain Shift
* **Primary Threat**: The primary predictive benchmark relies on `DS-SYNTH-01`. While distributions mirror empirical literature, synthetic generators cannot reproduce the full stochastic volatility of real job markets.
* **Risk Level**: High. Models trained on synthetic distributions may encounter covariate shift when exposed to real institutional cohorts.
* **Mitigation**: Explicit epistemological declaration across all reports. Algorithms are frozen and packaged with standardized ONNX and PyTorch artifacts, awaiting zero-shot and fine-tuned validation on `DS-REAL-01`.

### 4.2 Institutional and Geographic Specificity
* Tier-1, Tier-2, and Tier-3 engineering institutions exhibit widely different recruitment patterns (e.g., on-campus bulk hiring vs. specialized product engineering interviews).
* **Mitigation**: `DS-SYNTH-01` incorporates stratified tier parameters, but cross-institutional validation in Phase 10 will be required to verify transportability across disparate college tiers.

---

## 5. Statistical Conclusion Validity

*Statistical conclusion validity addresses whether the mathematical inferences drawn from statistical tests are sound, well-powered, and free from Type I / Type II errors.*

### 5.1 Sample Size and Statistical Power
* **Sample Scales**:
  - `EXP-1`: $N = 2,500$ ($N_{\text{test}} = 250 \times 5$ folds). Highly powered ($> 0.99$ power for $\alpha = 0.05$ with moderate effect size).
  - `EXP-3`: $N = 50$ mock sessions. Adequate for paired comparisons ($d = 2.14, p = 0.0022$), but limited for multi-group interaction modeling.
  - `EXP-5`: $N = 5$ seeds on 38-node DAG. Exact non-parametric Wilcoxon test confirms $W = 0.0, p = 0.0416$.
* **Mitigation**: Appropriate non-parametric tests (Wilcoxon signed-rank, McNemar's test) were chosen where distributional normality (Shapiro-Wilk) was violated.

### 5.2 Multiple Hypothesis Testing Correction
* Multiple metrics and sub-groups were evaluated. Uncorrected comparisons risk alpha inflation.
* **Mitigation**: Bonferroni and Benjamini-Hochberg False Discovery Rate (FDR) adjustments were applied to the hypothesis testing suite (`09_Results/12_Statistical_Results/Hypothesis_Testing_Ledger.md`), ensuring all reported family-wise significance values remain below $\alpha = 0.05$.

---

## 6. Measurement Validity

*Measurement validity considers the precision, reliability, and noise characteristics of data acquisition tools and feature extraction pipelines.*

### 6.1 Multimodal Sensor and Environmental Noise
* **Threat**: Audio-visual interview evaluation (`EXP-3`) is vulnerable to acoustic reverberation, microphone clipping, ambient room noise, and poor webcam lighting.
* **Mitigation**: The late fusion architecture integrates confidence weighting, wherein modalities exhibiting high local variance or low signal-to-noise ratios are dynamically down-weighted, reducing overall diagnostic variance by $77.98\%$.

### 6.2 ATS Optical Character Recognition and Layout Artifacts
* **Threat**: Resumes with multi-column layouts, tabular borders, or non-standard fonts induce OCR and text sequence scrambling.
* **Mitigation**: `EXP-4` demonstrated that 2D spatial coordinate tracking via PyMuPDF reduced section interleaving from $78.4\%$ to $4.2\%$, mitigating sequence degradation even prior to full LayoutLMv3 vision-language model fine-tuning.

---

## 7. Model Validity

*Model validity examines whether the machine learning models and optimization routines are robust against hyperparameter overfitting and architectural brittleness.*

### 7.1 Hyperparameter Overfitting
* **Threat**: Hyperparameters tuned specifically on synthetic validation splits might not generalize to real data.
* **Mitigation**: Minimal tree depth ($max\_depth = 4$), aggressive sub-sampling ($subsample = 0.8$), and conservative regularization ($\lambda = 1.0$) were enforced to prevent over-specialization to synthetic noise artifacts.

### 7.2 Counterfactual Local Minima
* **Threat**: Gradient-based recourse optimizers (DiCE) may become trapped in non-actionable local minima.
* **Mitigation**: The loss formulation includes categorical proximity penalties and diversity terms, achieving a $93.3\%$ empirical feasibility rate across tested profiles.

---

## 8. Summary Matrix of Threats to Validity

| Dimension | Threat Description | Severity | Experimental Manifestation | Mitigating Design Decision |
|:---|:---|:---:|:---|:---|
| **Construct** | Metric proxy for true employability | High | Binary label $Y \in \{0, 1\}$ | Multi-modal interview + DAG skill validation |
| **Construct** | Metric gaming (Goodhart's Law) | Medium | Student focuses solely on top SHAP features | Recourse sparsity ($k \le 3$) + actionability bounds |
| **Internal** | Training/Testing data leakage | Critical | Artificial inflation of accuracy/F1 | Strict 5-seed train/val/test isolation pipeline |
| **Internal** | Protected attribute discrimination | High | Unfair recourse recommending demographic shifts | Hard invariance constraint on $F_{17}$ (`branch_encoded`) |
| **External** | Synthetic-to-real transfer gap | Critical | Model trained on `DS-SYNTH-01` | Explicit epistemic boundary; frozen weights for Phase 10 |
| **External** | Cross-tier institutional variance | Medium | Tier-1 vs Tier-3 hiring dynamics | Stratified tier feature conditioning in training data |
| **Statistical** | Low power on small splits | Medium | $N=50$ in multimodal mock interviews | Paired Wilcoxon tests + Cohen's $d$ effect sizes |
| **Statistical** | Multi-testing alpha inflation | Medium | 6 simultaneous hypothesis assessments | Bonferroni / Benjamini-Hochberg FDR correction |
| **Measurement**| Acoustic and visual sensor noise | High | Fluctuating pitch and lighting in interviews | Late fusion variance damping ($77.98\%$ reduction) |
| **Measurement**| Spatial text interleaving in ATS | Medium | Multi-column resume parsing failures | 2D bounding-box spatial ordering (PyMuPDF) |
| **Model** | Hyperparameter over-tuning | Medium | Deep tree memorization | Conservative regularization and shallow tree depth |
| **Model** | Counterfactual non-convergence | Low | DiCE trapping in non-viable states | Multi-objective optimization with feasibility bounds |
