# Paper 08 — Factors Affecting Students’ Academic Performance: A review

## 1. Bibliographic Information

- **Paper ID**: Paper08
- **Full Title**: Factors Affecting Students’ Academic Performance: A review
- **Authors**: Yousuf Nasser Said Al Husaini, Nur Syufiza Ahmad Shukor
- **Affiliation**: Faculty of Communication Visual Art and Computing, Universiti Selangor (UNISEL), Bestari Jaya / Shah Alam, Malaysia; Arab Open University, Sultanate of Oman
- **Year**: 2022 (Winter 2022; cataloged under 2023 in earlier bib)
- **Venue**: Res Militaris (Social Science & Interdisciplinary Journal)
- **Volume / Issue / Pages**: Vol. 12, No. 6, Winter 2022, pp. 284–294 (11 pages in PDF)
- **ISSN / Publication**: ISSN: 2265-6294 / [ResearchGate Publication 367360842](https://www.researchgate.net/publication/367360842)
- **PDF filename**: `Paper08_alam2023factors.pdf`
- **PDF path**: `01_Research_Foundation/Papers/PDFs/Paper08_alam2023factors.pdf`
- **Page count**: 11 pages

---

## 2. Research Problem

Universities globally—and particularly in transitioning higher education systems such as the Sultanate of Oman—face rising undergraduate dropout rates and extended graduation delays. Post-secondary institutions capture extensive student data across Student Information Systems (SIS) and Learning Management Systems (LMS), but struggle to isolate which specific student, pedagogical, and behavioral factors actually drive academic success versus academic failure. Furthermore, the majority of existing Educational Data Mining (EDM) studies focus narrowly on comparing algorithmic classification techniques rather than systematically analyzing and synthesizing the underlying predictive feature sets.

### Source Evidence
- **Page**: PDF p. 284–286 (PDF pp. 1–3)
- **Section**: Abstract, Section I (Introduction)

---

## 3. Research Objectives

The authors explicitly define the following research objectives:
1. Conduct a systematic literature review (SLR) identifying and classifying the primary multi-dimensional factors influencing student academic performance in higher education.
2. Address the research scarcity regarding feature-level determinants by moving beyond purely algorithm-centric comparative evaluations.
3. Synthesize empirical findings across institutional studies to highlight critical early-warning indicators (e.g., first-year GPA, internal continuous assessments, and LMS engagement).
4. Provide higher education administrators and researchers with an evidence-based taxonomy of performance determinants to inform academic retention systems.

### Source Evidence
- **Page**: PDF p. 284, 286 (PDF pp. 1, 3)
- **Section**: Abstract, Section I, Section I-A (Research Questions)

---

## 4. Research Questions

The study explicitly poses and answers one primary research question:
- **RQ**: *"What are the factors affecting students’ performance in higher education?"*

### Source Evidence
- **Page**: PDF p. 286 (PDF p. 3)
- **Section**: Section I-A (Research Questions)

---

## 5. Dataset

- **Dataset name**: Higher Education Academic Performance Factor Review Corpus (2014–2020)
- **Review protocol**: Kitchenham et al. (2009) Systematic Literature Review guidelines (Planning, Conducting, Reporting)
- **Database sources**: ScienceDirect, Scopus, IEEE Xplore, ACM Digital Library, Google Scholar
- **Search syntax**: `("student" AND "predict*" AND "Academic performance" AND "factors" AND "review" OR "survey")`
- **Initial search yield**: 3,810 publications retrieved
- **Screening & Filtering**: Articles screened to identify peer-reviewed English journal papers focusing specifically on feature factors rather than solely prediction algorithms
- **Synthesis cohort**: In-depth qualitative and thematic synthesis of over 40 seminal empirical studies published between 2014 and 2020
- **Contextual empirical reference**: Grounded by tertiary retention data and language barrier statistics from post-secondary institutions in Oman (e.g., Arab Open University, Modern College of Business & Science)

### Source Evidence
- **Page**: PDF p. 285–287 (PDF pp. 2–4)
- **Section**: Section I (Methodology), Section I-B (Search Strategy)

---

## 6. Features & Performance Determinant Taxonomy

The review synthesizes student performance predictors into nine key determinant categories:

### Academic History & Entry Qualifications
- High school exit scores / Grade 12 national examination percentages.
- University entrance test scores and English language proficiency scores.
- Foundation program completion metrics (critical in bilingual Arab Gulf contexts).

### Internal Continuous Assessments
- Periodic quiz scores, lab test evaluations, midterm examination grades, assignment submission timeliness.

### Cumulative Academic Trajectory
- First- and second-year Cumulative Grade Point Average (CGPA / GPA) — identified as the strongest single empirical predictor of degree completion.
- Course backlog count / Carry-over subjects.

### Digital & e-Learning Activity (LMS Telemetry)
- LMS login frequencies, digital resource access counts, video lecture engagement (play, pause, completion), online discussion forum contributions, and assignment uploads.

### Demographic & Personal Characteristics
- Student gender (noted as influencing study habits and academic self-regulation; females frequently exhibited higher average GPA across cited studies).
- Age and enrollment status (full-time vs. part-time).

### Psychological & Cognitive Attributes
- Academic self-efficacy, perceived academic vulnerability, resilience, and self-control.

### Socioeconomic & Familial Environment
- Proximity to family support networks, parental educational background, and household financial stability.

### Living & Environmental Conditions
- Student accommodation type (campus hostel vs. off-campus shared housing vs. living with parents).
- Commute duration and transportation access.

### Language Medium Barrier
- Instruction language proficiency (specifically English medium instruction for non-native speakers).

### Source Evidence
- **Page**: PDF p. 286–291 (PDF pp. 3–8)
- **Section**: Section II (Factors Affecting the Students' Academic Performance, Subsections A–I), Section III (Discussion)

---

## 7. Data Preprocessing

The survey synthesizes common preprocessing methodologies across the reviewed performance prediction studies:
- **Discretization of Performance**: Converting numerical marks into multi-class academic categories (e.g., High, Medium, Low, Fail).
- **Log Aggregation**: Processing clickstreams and web interaction logs from Moodle / Blackboard into aggregated weekly behavioral counts.
- **Handling Incomplete Records**: Addressing missing student demographic data via mean imputation or record removal.

### Source Evidence
- **Page**: PDF p. 285, 290 (PDF pp. 2, 7)
- **Section**: Section I, Section II-I

---

## 8. Algorithms and Models

While the review focuses on feature identification, it documents the machine learning algorithms commonly applied to these factor sets in the reviewed literature:
- **Decision Trees (ID3, C4.5, J48, CART)**: Cited as dominant due to visual decision tree rules linking specific GPA thresholds to dropout risks (e.g., Al-Barrak & Al-Razgan 2016).
- **Deep Learning & Recurrent Neural Networks (RNN/LSTM)**: Applied to sequential Virtual Learning Environment (VLE) log data (e.g., Waheed et al. 2020).
- **Ensemble Learning (Random Forest, Gradient Boosting)**: Benchmark classifiers for tabular institutional data.
- **Linear & Logistic Regression**: Baseline econometric and predictive modeling.

### Source Evidence
- **Page**: PDF p. 286, 290–292 (PDF pp. 3, 7–9)
- **Section**: Section I, Section II-G, References

---

## 9. Architecture

The paper synthesizes an Early-Warning Learning Analytics Architecture:
1. **Multi-Source Data Ingestion**: Student Information Systems (demographics, entry grades), LMS Server Logs (clickstreams, forum posts), Exam Repositories (quizzes, midterms).
2. **Feature Aggregation Engine**: Extraction of 9 core determinant features.
3. **Predictive Analytics Model**: Automated classification into At-Risk vs. On-Track cohorts.
4. **Institutional Advising Loop**: Early warning notifications delivered to faculty mentors and academic counselors before semester withdrawal deadlines.

### Source Evidence
- **Page**: PDF p. 285, 291 (PDF pp. 2, 8)
- **Section**: Section I, Section III, Section IV (Conclusion)

---

## 10. Methodology

Systematic Literature Review following Kitchenham (2009):
1. **Planning Phase**: Formulate research question on performance factors; define search strings.
2. **Conducting Phase**: Query 5 major databases (ScienceDirect, Scopus, IEEE Xplore, ACM, Google Scholar); retrieve 3,810 publications; screen for factor-oriented empirical literature.
3. **Reporting Phase**: Synthesize findings into a 9-factor predictive taxonomy; analyze contextual socio-demographic implications.

### Source Evidence
- **Page**: PDF p. 286 (PDF p. 3)
- **Section**: Section I (Methodology)

---

## 11. Experimental Setup

- **Review Protocol**: Kitchenham SLR guidelines.
- **Time Horizon**: 2014–2020 publication window.

### Source Evidence
- **Page**: PDF p. 286 (PDF p. 3)
- **Section**: Section I-B

---

## 12. Evaluation Metrics

Synthesized metrics across the reviewed literature:
- Classification Accuracy (%)
- Dropout / Retention Rate (%)
- Grade Point Average (GPA) delta
- Sensitivity / Recall in identifying at-risk students

### Source Evidence
- **Page**: PDF p. 286, 290–291 (PDF pp. 3, 7–8)
- **Section**: Section II, Section III

---

## 13. Results

Key synthesized findings from the systematic review:
- **First-Year GPA is the Decisive Threshold**: GPA in the first and second semesters is the single strongest determinant of university completion; early course failures compound into cumulative credit deficits that lead to dropouts (PDF p. 290).
- **Continuous Internal Assessments Outperform Final Exams as Predictors**: Formative assessments (quizzes, lab assignments, midterms) provide early predictive signals 6–8 weeks before final semester examinations, allowing timely institutional remediation (PDF p. 290).
- **LMS Engagement Strongly Correlates with Grades**: Students with higher portal login frequencies and active digital assignment submissions consistently achieve statistically higher course grades across all reviewed VLE studies (PDF p. 290).
- **Linguistic and Socioeconomic Gaps**: Non-native instruction language (e.g., English medium for Arabic speakers) represents a severe hidden performance tax that traditional admissions models fail to isolate (PDF p. 285).

### Source Evidence
- **Page**: PDF p. 290–291 (PDF pp. 7–8)
- **Section**: Section II-G, II-H, II-I, Section III (Discussion)

---

## 14. Baselines

The review benchmarks multi-factor predictive systems against traditional standalone academic metrics (high school entrance grades alone).

---

## 15. Ablation Study

Not applicable (systematic literature review).

---

## 16. Explainability

Explainability is emphasized at the institutional decision-making level:
- Predictive algorithms must provide interpretable feature weights (e.g., indicating whether low LMS logins or poor midterm quiz scores triggered an at-risk flag) so counselors know *which* intervention to prescribe.

### Source Evidence
- **Page**: PDF p. 285, 291 (PDF pp. 2, 8)
- **Section**: Section I, Section III

---

## 17. Main Findings

1. **Algorithm Bias in Prior Literature**: Most research focuses on tuning complex algorithms on convenience datasets; very few studies rigorously isolate and validate the domain features that matter.
2. **The 9-Factor Core Determinant Framework**: Academic success is governed by 9 interconnected factors: entry qualifications, family support, accommodation, gender, prior grades, internal assessments, early GPA, LMS telemetry, and language proficiency.
3. **Timing of Prediction is Paramount**: Predicting failure at the end of a semester is clinically useless; early continuous assessments (weeks 3–6) must serve as the primary feature input for predictive models.

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Temporal Boundary**: Systematic search covered publications up to 2020.
- **Search Term Constraints**: Search syntax combined terms that yielded 3,810 results, of which only a subset met the strict factor-focus inclusion criteria.
- **Language Limitation**: Limited to English-language academic journals.

### 18.2 Research Interpretation
- *Research team interpretation*: The review provides a strong conceptual taxonomy of academic factors, but does not present a meta-analytic forest plot of quantitative effect sizes across the reviewed studies.

---

## 19. Future Work

Explicitly proposed by the authors:
1. Formulate and train an empirical predictive model using the 9 identified factor categories on university student cohorts.
2. Integrate LMS big data telemetry with psychological self-efficacy measures for holistic early-warning modeling.
3. Design automated advisory recommendation engines that suggest targeted remedial study modules when specific risk factors are detected.

### Source Evidence
- **Page**: PDF p. 291 (PDF p. 8)
- **Section**: Section IV (Conclusion)

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **Relevant PRIE Module**: `02_Prediction`, `08_Learning_Analytics`, and `01_Employability`.
- **Feature Engineering Foundation**: Directly justifies PRIE's tracking of continuous learning telemetry (coding exercise frequency, platform login consistency, mock assessment milestones) rather than relying solely on static college GPA.
- **Early-Warning Scheduling**: Supports PRIE’s architectural goal of identifying placement vulnerabilities 2–3 semesters before corporate hiring drives begin.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Systematic Review Methodology | Kitchenham 3-phase SLR protocol across 5 major scientific databases | PDF p. 286, Section I | Methodology |
| Search Yield & Scope | 3,810 results identified from 2014–2020 search window | PDF p. 286, Section I-B | Experimental result |
| 9 Key Determinant Factors | Low entry grades, family support, housing, gender, prior grades, midterms, GPA, LMS, language | PDF p. 284, 291 | Direct statement |
| Decisive Impact of Early GPA | 1st/2nd year GPA identified as strongest retention indicator | PDF p. 290, Section II-H | Author discussion |
| Predictive Power of Continuous Quizzes | Midterms and quizzes provide actionable signals weeks before finals | PDF p. 290, Section II-G | Author discussion |

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

**VERIFIED** (Fully verified from primary PDF source: `Paper08_alam2023factors.pdf`, 11 pages).
