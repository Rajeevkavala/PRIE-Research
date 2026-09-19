# Paper 07 — The Role of Perceived Social Support, Vocational Self-Efficacy and Vocational Outcome Expectation on Students’ Interest in the TVET Program

## 1. Bibliographic Information

- **Paper ID**: Paper07
- **Full Title**: The Role of Perceived Social Support, Vocational Self-Efficacy and Vocational Outcome Expectation on Students’ Interest in the TVET Program
- **Authors**: Nazia Azeem, Muhd Khaizer Omar, Abdullah Mat Rashid, Arnida Abdullah, Zeinab Zaremohzzabieh
- **Affiliation**: Faculty of Educational Studies, Universiti Putra Malaysia, 43400, Serdang, Selangor, Malaysia
- **Year**: 2021
- **Venue**: Turkish Journal of Computer and Mathematics Education (TURCOMAT)
- **Volume / Issue / Pages**: Vol. 12, No. 14 (2021), pp. 3228–3235
- **DOI**: [10.17762/turcomat.v12i14.11181 / ResearchGate](https://www.researchgate.net/publication/354523160)
- **PDF filename**: `Paper07_ismail2021role.pdf`
- **PDF path**: `01_Research_Foundation/Papers/PDFs/Paper07_ismail2021role.pdf`
- **Page count**: 8 pages

---

## 2. Research Problem

Technical and Vocational Education and Training (TVET) is essential for preparing youth for skilled industrial employment, yet institutions in developing countries (specifically Pakistan) struggle with low student interest and societal disinclination toward vocational education. While economic demand for vocational graduates is high, career decision-making is heavily influenced by complex cognitive and psychosocial forces. Educators lack empirical understanding of how cognitive self-efficacy, perceived support from family and friends, and expected career outcomes interact to determine whether students pursue technical vocational tracks.

### Source Evidence
- **Page**: PDF p. 3228–3230 (PDF pp. 1–3)
- **Section**: Section 1 (Introduction), Section 2 (Literature Review)

---

## 3. Research Objectives

The authors explicitly define the following research objectives:
1. Examine the predictive influence of vocational self-efficacy (VSE), perceived social support (PSS), and vocational outcome expectation (VOE) on secondary school students’ interest in TVET programs.
2. Operationalize Social Cognitive Career Theory (SCCT) within the secondary educational context of Pakistan.
3. Test a multiple linear regression model estimating the variance explained in student vocational interest.
4. Formulate evidence-based counseling and policy recommendations to strengthen technical education enrollment.

### Source Evidence
- **Page**: PDF p. 3228, 3230–3231 (PDF pp. 1, 3–4)
- **Section**: Abstract, Section 1, Section 3 (Methodology)

---

## 4. Research Questions & Hypotheses

Grounded in Lent et al.’s Social Cognitive Career Theory (SCCT):
- **Hypothesis 1**: Perceived social support (PSS) statistically predicts secondary students' interest in TVET programs.
- **Hypothesis 2**: Vocational self-efficacy (VSE) statistically predicts secondary students' interest in TVET programs.
- **Hypothesis 3**: Vocational outcome expectation (VOE) statistically predicts secondary students' interest in TVET programs.

### Source Evidence
- **Page**: PDF p. 3230–3231 (PDF pp. 3–4)
- **Section**: Section 2 (Literature Review), Section 3

---

## 5. Dataset

- **Dataset name**: Pakistan Secondary School TVET Career Interest Survey
- **Target population**: Secondary school students across public and private secondary schools in Pakistan
- **Sampling method**: Random sampling
- **Dataset size**: 386 student responses ($N = 386$)
- **Data collection instrument**: Self-reported questionnaire comprising 63 validated psychometric items
- **Target variable**: Student Interest in TVET Programs (continuous composite score, 1–5 scale)
- **Real / synthetic**: Real empirical survey data
- **Public / private**: Private survey dataset (Universiti Putra Malaysia research repository)
- **Measurement Reliability**:
  - Vocational Outcome Expectations (VOE): 12 items, Cronbach's $\alpha = 0.96$
  - Perceived Social Support (PSS): 12 items, Cronbach's $\alpha = 0.91$
  - Vocational Self-Efficacy (VSE): 20 items, Cronbach's $\alpha = 0.95$
  - TVET Interest Scale: 19 items, Cronbach's $\alpha = 0.92$

### Source Evidence
- **Page**: PDF p. 3228, 3231–3232 (PDF pp. 1, 4–5)
- **Section**: Abstract, Section 3.1 (Measures)

---

## 6. Features & Psychometric Scales

The study measures four primary constructs using 5-point Likert scales (1 = Strongly Disagree to 5 = Strongly Agree):

### Vocational Self-Efficacy (VSE) — 20 Items (Ali et al. 2005)
- Confidence in executing technical tasks, problem-solving in vocational domains, academic perseverance.

### Perceived Social Support (PSS) — 12 Items (Zimet et al. 1988)
- Family support ("My family tries to help me").
- Peer support ("I can talk about my problems with my friends").
- Significant others ("There is a special person around when I am in need").

### Vocational Outcome Expectations (VOE) — 12 Items (Metheny & McWhirter 2013)
- Anticipated career success, societal respect, occupational attainment ("I will have a career that is respected in our society").

### TVET Interest — 19 Items (Ainley 2011; Baker et al. 2015)
- Affection ("I like working with my hands").
- Cognition ("I know different ways to create a design").
- Conation ("I am persistent and willing to try a new process to get an invention to work").

### Source Evidence
- **Page**: PDF p. 3231–3232 (PDF pp. 4–5)
- **Section**: Section 3.1 (Measures)

---

## 7. Data Preprocessing

- **Internal Consistency Testing**: Cronbach's alpha verification for all four instruments ($\alpha \ge 0.91$ for all scales).
- **Normality & Collinearity Verification**: Tested for multicollinearity (VIF values within permissible bounds; tolerance > 0.1).
- **Scale Aggregation**: Item responses were averaged into composite construct scores for regression analysis.

### Source Evidence
- **Page**: PDF p. 3231–3232 (PDF pp. 4–5)
- **Section**: Section 3.1, Section 4

---

## 8. Algorithms and Models

- **Multiple Linear Regression (Ordinary Least Squares - OLS)**:
  - Task: Predict continuous TVET student interest from psychological and social constructs.
  - Mathematical Specification:
    $$\text{Interest} = \beta_0 + \beta_1 (\text{PSS}) + \beta_2 (\text{VSE}) + \beta_3 (\text{VOE}) + \epsilon$$
  - Model Fit: $F(3, 382) = 200.75, p < 0.001$, Multiple $R = 0.782$, Coefficient of Determination $R^2 = 0.612$.

### Source Evidence
- **Page**: PDF p. 3232 (PDF p. 5)
- **Section**: Section 4 (Results), Regression Table

---

## 9. Architecture

Conceptual Social Cognitive Career Theory (SCCT) Structural Architecture:
$$\begin{matrix}
\text{Perceived Social Support (PSS)} \\
\text{Vocational Self-Efficacy (VSE)} \\
\text{Vocational Outcome Expectation (VOE)}
\end{matrix} \longrightarrow \text{[Multiple OLS Regression]} \longrightarrow \text{TVET Career Interest} \longrightarrow \text{Enrollment Actions}$$

### Source Evidence
- **Page**: PDF p. 3230–3231 (PDF pp. 3–4)
- **Section**: Section 2 (Literature Review)

---

## 10. Methodology

1. Adapt four validated psychometric scales (VOE, PSS, VSE, and TVET interest).
2. Administer questionnaire to 386 randomly sampled secondary school students in Pakistan.
3. Compute Cronbach's alpha to verify measurement reliability.
4. Perform Pearson correlation analysis across constructs.
5. Execute multiple linear regression in SPSS to test predictive power and hypothesis significance.
6. Interpret standardized regression coefficients ($\beta$) through the cultural lens of vocational education in South Asia.

### Source Evidence
- **Page**: PDF p. 3231–3232 (PDF pp. 4–5)
- **Section**: Section 3, Section 4

---

## 11. Experimental Setup

- **Software**: SPSS (Statistical Package for the Social Sciences).
- **Sample**: $N = 386$ Pakistani secondary school students.

### Source Evidence
- **Page**: PDF p. 3228, 3231 (PDF pp. 1, 4)
- **Section**: Section 3.1

---

## 12. Evaluation Metrics

- Coefficient of Determination ($R^2 = 0.612$)
- Multiple Correlation ($R = 0.782$)
- Overall Model ANOVA ($F = 200.75, p = 0.000$)
- Unstandardized Regression Coefficients ($B$) and Standard Errors ($SE$)
- Standardized Coefficients ($\beta$) and $t$-statistics ($t$-values)
- Cronbach's Alpha ($\alpha$)

### Source Evidence
- **Page**: PDF p. 3231–3232 (PDF pp. 4–5)
- **Section**: Section 3.1, Section 4, Regression Table

---

## 13. Results

Reported regression parameters exactly as documented in Table on PDF p. 3232:

| Predictor Variable | Unstandardized $B$ | Std. Error ($SE$) | Standardized $\beta$ | $t$-statistic | $p$-value | Significance |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Constant** | 4.514 | 0.192 | — | 23.565 | 0.000 | $p < 0.001$ |
| **Vocational Self-Efficacy (VSE)** | **+0.191** | **0.040** | **+0.169** | **4.773** | **0.000** | **Positive & Significant** |
| **Perceived Social Support (PSS)** | **-0.271** | **0.040** | **-0.283** | **-6.724** | **0.000** | **Negative & Significant** |
| **Vocational Outcome Expectation (VOE)** | **-0.450** | **0.039** | **-0.480** | **-11.446** | **0.000** | **Negative & Significant** |

### Overall Model Fit:
- $R = 0.782$
- $R^2 = 0.612$ (61.2% of total variance explained)
- $F = 200.75, p < 0.001$

### Key Finding:
- **Vocational Self-Efficacy is the sole positive driver** ($\beta = +0.169, p < 0.001$).
- **Social Support and Outcome Expectations yielded negative beta coefficients**: The authors interpret this cultural paradox as reflecting deep societal stigma in Pakistan: family and peer networks actively discourage vocational training in favor of traditional white-collar university degrees.

### Source Evidence
- **Page**: PDF p. 3232 (PDF p. 5)
- **Section**: Section 4 (Results), Section 5 (Discussion and Conclusion)

---

## 14. Baselines

The single-construct correlations ($r$) serve as univariate baselines against the full multivariate regression model ($R^2 = 0.612$).

---

## 15. Ablation Study

Not applicable (psychometric survey regression study).

---

## 16. Explainability

Explainability is operationalized through **econometric standardized beta weights**:
- Quantifies that a 1 standard deviation increase in Vocational Self-Efficacy increases TVET interest by 0.169 standard deviations.
- Quantifies the drag imposed by negative social perceptions ($\beta = -0.283$) and perceived lack of societal prestige ($\beta = -0.480$).

### Source Evidence
- **Page**: PDF p. 3232–3233 (PDF pp. 5–6)
- **Section**: Section 4, Section 5

---

## 17. Main Findings

1. **High Variance Explanation (61.2%)**: Cognitive and social variables account for nearly two-thirds of secondary students' vocational interest, validating SCCT in South Asia.
2. **The Social Stigma Barrier**: Unlike Western cohorts where social support fosters vocational interest, family and peer influence in Pakistan acts as a significant deterrent ($\beta = -0.283$) due to the low social prestige attached to manual/technical labor.
3. **Self-Efficacy as the Lever**: Personal confidence in executing technical tasks is the primary vehicle to overcome social bias and spark vocational engagement.

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Cross-Sectional Self-Reporting**: Relies exclusively on cross-sectional questionnaires; causal pathways over time were not tracked.
- **Geographic Boundary**: Sample confined to Pakistani secondary schools; cannot be generalized globally without adaptation.
- **Exclusion of Structural Factors**: Macro-economic variables (job market wage differentials, regional institute funding) were not modeled.

### 18.2 Research Interpretation
- *Research team interpretation*: The study uses classical OLS regression rather than structural equation modeling (SEM) with latent variables, which would provide better measurement error handling.

---

## 19. Future Work

Explicitly proposed by the authors:
1. Conduct longitudinal studies tracking whether expressed TVET interest translates into actual technical college enrollment and career retention.
2. Expand modeling using Structural Equation Modeling (SEM) to test mediation and moderation pathways.
3. Design and test targeted psychological interventions (verbal persuasion, mastery experiences) to build vocational self-efficacy in early schooling.

### Source Evidence
- **Page**: PDF p. 3232–3233 (PDF pp. 5–6)
- **Section**: Section 5 (Discussion and Conclusion)

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **Relevant PRIE Module**: `01_Employability`, `05_Mock_Interview`, and `07_Recommendation`.
- **Psychometric Foundation**: Empirically confirms that student placement readiness is governed by self-efficacy and psychological confidence, not merely technical knowledge.
- **Intervention Scaffolding**: Provides justification for PRIE’s personalized motivational nudges and gamified mastery milestones, which directly foster self-efficacy to combat student imposter syndrome.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| 61.2% Variance Explained | Multiple linear regression yielded $R^2 = 0.612, F = 200.75, p = 0.000$ | PDF p. 3232, Section 4 | Experimental result |
| Dominance of Self-Efficacy | VSE was the sole positive predictor ($\beta = +0.169, t = 4.773, p = 0.000$) | PDF p. 3232, Table | Experimental result |
| Negative Social Support Influence | PSS yielded $\beta = -0.283 (t = -6.724, p = 0.000)$ | PDF p. 3232, Table | Experimental result |
| Negative Outcome Expectations | VOE yielded $\beta = -0.480 (t = -11.446, p = 0.000)$ | PDF p. 3232, Table | Experimental result |
| Sample Size & Demographics | 386 secondary school students in Pakistan | PDF p. 3228, Abstract | Direct statement |
| High Scale Reliabilities | Cronbach's alpha between 0.91 and 0.96 across all instruments | PDF p. 3231, Section 3.1 | Methodology |

---

## 22. Verification Checklist

- [x] PDF read
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected
- [x] Dataset verified
- [x] Features verified
- [x] Algorithms verified
- [x] Architecture inspected
- [x] Experiments inspected
- [x] Results verified
- [x] Limitations verified
- [x] Future work verified
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Fully verified from primary PDF source: `Paper07_ismail2021role.pdf`, 8 pages).
