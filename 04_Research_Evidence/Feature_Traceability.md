# Feature Traceability Matrix: 22-Dimensional Student Profile Vector (SPV) & Multi-Modal Telemetry

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `04_Research_Evidence/Feature_Traceability.md`  
**Phase**: 04 — Research Evidence & Traceability  
**Status**: Authoritative Reference Matrix  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`)  
**Date**: September 2026  

---

## 1. Executive Summary & Epistemological Framework

The Placement Readiness Intelligence Engine (PRIE) models student career trajectory through a foundational **22-Dimensional Student Profile Vector (SPV)** augmented by domain-specific feature spaces in Resume Intelligence (ATS), Multimodal Mock Interviews, and Formative Learning Analytics. 

A central tenet of Phase 04 is the **Non-Fabrication Rule**: the existence of a feature in PRIE's codebase does not constitute scientific evidence of its validity. Every feature must be evaluated against empirical research in the 44-paper verified corpus (`Paper01`–`Paper44`), cross-paper syntheses from Phase 02, and validated research gaps from Phase 03.

### Status Taxonomy:
- **`DIRECTLY SUPPORTED`**: Feature is explicitly measured, validated, and proven predictive in one or more primary papers in the corpus (e.g., academic grades, coding metrics, internships).
- **`PARTIALLY SUPPORTED`**: Feature concept exists in literature, but prior studies used coarser proxies or different measurement scales (e.g., self-reported vs. automated paralinguistics).
- **`INDIRECTLY SUPPORTED`**: Feature is supported by adjacent educational data mining or human resources literature, but not evaluated in campus placement specifically.
- **`PROPOSED`**: Novel feature introduced by PRIE to resolve a validated Phase 03 research gap; requires empirical experimental validation.
- **`IMPLEMENTATION-DERIVED`**: Engineering telemetry or pipeline artifact necessary for software operation, with baseline heuristic validity.
- **`NOT YET JUSTIFIED`**: Feature currently lacks sufficient empirical or theoretical grounding; designated for ablation testing.

---

## 2. Master Student Profile Vector (SPV) Traceability Matrix

The 22 features comprising PRIE's core Student Profile Vector are comprehensively mapped below:

| Feature ID | Feature Name | PRIE Role | Literature Support | Supporting Papers | Evidence Location | Phase 02 Finding | Phase 03 Gap | Status | Validation Need |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| **F01** | `cgpa` (Float, 0.0–10.0) | Global academic foundation; primary filtering signal for corporate placement eligibility. | Extensive empirical consensus across tabular placement and performance prediction. | **Paper01**, **Paper04**, **Paper06**, **Paper08**, **Paper09**, **Paper10**, **Paper22**, **Paper24** | P01: Table 2, p. 3; P06: Section 4.2; P09: Table 4; P22: Section 3.1 | Top-3 predictor across all tabular studies; mean feature importance 0.22–0.34. | Baseline signal in RG1 & RG2; static when uncoupled from longitudinal trajectory. | `DIRECTLY SUPPORTED` | Validated; test non-linear thresholding effects in corporate cutoffs. |
| **F02** | `dsa_score` (Float, 0.0–100.0) | Core algorithmic reasoning metric; gateway for technical software engineering rounds. | Strongly validated in technical hiring and automated placement screening literature. | **Paper03**, **Paper04**, **Paper14**, **Paper28**, **Paper30**, **Paper38** | P04: Section 3.2, p. 4; P28: Table 3; P38: Section 4.1 | Strongest technical discriminator for product/software engineering profiles. | Addressed in RG1 & RG5; requires objective code sandboxing. | `DIRECTLY SUPPORTED` | Benchmark against live LeetCode/HackerRank style problem difficulty curves. |
| **F03** | `dbms_score` (Float, 0.0–100.0) | Systems core competency (SQL querying, indexing, transaction management, schema design). | Assessed within core computer science subject performance benchmarks. | **Paper04**, **Paper08**, **Paper10**, **Paper24** | P08: Table 3; P10: Section 3.4; P24: Table 2, p. 4 | Computer science domain subject grades correlate with technical interview pass rates. | Addressed in RG1 (multi-dimensional skill aggregation). | `DIRECTLY SUPPORTED` | Validate via standardized conceptual and practical query tests. |
| **F04** | `os_score` (Float, 0.0–100.0) | Systems core competency (concurrency, virtualization, memory management, processes). | Assessed as an essential engineering curriculum component in CS employability studies. | **Paper04**, **Paper08**, **Paper10**, **Paper24** | P04: Section 3.2; P24: Section 4.1 | Foundational system subject scores predict candidate resilience in system design interviews. | Addressed in RG1; part of CS competency profile. | `DIRECTLY SUPPORTED` | Evaluate predictive power across systems vs. web engineering roles. |
| **F05** | `cn_score` (Float, 0.0–100.0) | Systems core competency (TCP/IP protocols, socket programming, routing, network security). | Core technical domain feature in engineering academic tracking. | **Paper04**, **Paper08**, **Paper10**, **Paper24** | P08: Section 3.2; P10: Table 2 | High correlation with cloud, DevOps, and infrastructure engineering placement. | Addressed in RG1; needed for comprehensive domain profiling. | `DIRECTLY SUPPORTED` | Calibrate weight dynamically based on candidate target role. |
| **F06** | `programming_score` (Float, 0.0–100.0) | Hands-on syntax mastery, code execution efficiency, and unit test pass rates. | Emphasized as distinct from theoretical CS knowledge in modern placement literature. | **Paper03**, **Paper04**, **Paper24**, **Paper28**, **Paper38**, **Paper41** | P28: Section 3.3; P38: Table 2; P41: Section 4.2 | Live coding ability frequently overrides mediocre CGPA in final corporate rounds. | Addressed in RG1 & RG5; requires automated test runner execution. | `DIRECTLY SUPPORTED` | Validate test-case coverage metrics within isolated Docker sandboxes. |
| **F07** | `aptitude_score` (Float, 0.0–100.0) | Cognitive speed, quantitative reasoning, and logical puzzle problem-solving. | Universally validated as the first-round corporate screening filter in Indian campus recruitment. | **Paper01**, **Paper04**, **Paper06**, **Paper09**, **Paper22**, **Paper24** | P01: Table 1; P06: Table 3; P22: Section 3.2; P24: Table 3 | Essential gating filter; failure here prevents candidate from reaching technical rounds. | Addressed in RG1; historical filter feature. | `DIRECTLY SUPPORTED` | Benchmark against enterprise assessment platforms (AMCAT, CoCubes, eLitmus). |
| **F08** | `soft_skills_score` (Float, 0.0–100.0) | Verbal articulation, interpersonal collaboration, and workplace adaptability. | Validated in surveys and employability studies as a major determinant of offer issuance. | **Paper01**, **Paper06**, **Paper07**, **Paper14**, **Paper15**, **Paper30**, **Paper41** | P06: p. 4; P07: Table 4; P15: Section 3.2; P41: Table 1 | Frequently rated by employers as equally important to technical ability, but poorly measured. | Addressed in RG1 & RG5; historically measured via coarse Likert surveys. | `PARTIALLY SUPPORTED` | Validate automated speech/NLP extraction against human expert interview panels. |
| **F09** | `project_count` (Integer, 0–20) | Volume of end-to-end technical applications built and documented. | Evaluated in resume screening and placement profiling as evidence of applied capability. | **Paper04**, **Paper11**, **Paper12**, **Paper17**, **Paper28**, **Paper36**, **Paper37** | P04: Table 2; P17: Section 3.1; P37: Table 2 | High project counts correlate with resume shortlisting rates by human screeners. | Addressed in RG1 & RG4; requires parsing from resume unstructured text. | `DIRECTLY SUPPORTED` | Audit for vanity counts vs. actual deployment; coupled with F10. |
| **F10** | `project_quality_score` (Float, 0.0–100.0) | Structural complexity, full-stack integration, production deployment, and documentation. | Proposed in advanced ATS and resume intelligence systems to counter shallow project counts. | **Paper11**, **Paper17**, **Paper36**, **Paper42** | P17: Section 4.2; P36: Table 3; P42: Section 3.1 | Shallow keyword counting in resumes fails to distinguish production apps from basic tutorials. | Directly addresses RG4 (semantic ATS analysis). | `PROPOSED` | Experimentally validate rubric (GitHub commits, API complexity, live URL verification). |
| **F11** | `has_internship` (Binary, 0/1) | Industrial work exposure and professional software engineering experience. | Validated across multiple studies as one of the highest positive coefficients in placement models. | **Paper01**, **Paper06**, **Paper07**, **Paper09**, **Paper22**, **Paper41** | P01: Table 2; P09: Section 4.2; P22: Table 3; P41: Table 2 | Candidates with $\ge 1$ internship exhibit $2.1\times$ higher placement probability in campus drives. | Addressed in RG1 & RG8 (industry alignment). | `DIRECTLY SUPPORTED` | Check for duration, enterprise tier, and role relevance weighting. |
| **F12** | `certifications_count` (Integer, 0–15) | Validated industry credentials (e.g., AWS, Azure, GCP, CKA, Oracle). | Included in resume ranking algorithms and employability models as verified skill signals. | **Paper04**, **Paper12**, **Paper17**, **Paper24**, **Paper36**, **Paper37** | P04: Section 3.1; P17: Table 2; P37: Section 3.3 | Acts as a tiebreaker in automated resume filtering for specialized tracks (cloud/security). | Addressed in RG1 & RG4; parsed from resume text. | `DIRECTLY SUPPORTED` | Restrict credit to proctored, recognized industry credentials vs. attendance certificates. |
| **F13** | `resume_ats_score` (Float, 0.0–100.0) | Quantitative measure of structural formatting hygiene, parseability, and section completeness. | Validated in document processing and resume intelligence studies. | **Paper11**, **Paper12**, **Paper17**, **Paper36**, **Paper37**, **Paper42** | P11: Section 3.2; P17: Table 3; P37: Fig. 3; P42: Section 4.1 | Poor layout hygiene causes 40–60% of resumes to fail OCR and layout parsers before screening. | Directly addresses RG4 (spatial layout parsing). | `DIRECTLY SUPPORTED` | Evaluate parser pass-rate across standard single-column and complex multi-column formats. |
| **F14** | `cosine_similarity` (Float, 0.0–1.0) | Dense semantic vector similarity between resume content and target job description (JD). | Established in modern semantic recruitment systems using transformer bi-encoders. | **Paper11**, **Paper12**, **Paper13**, **Paper17**, **Paper35**, **Paper36**, **Paper37** | P13: Section 3.3; P17: Table 4; P35: Section 4.2; P36: Table 2 | Dense semantic embeddings (Sentence-BERT) outperform sparse TF-IDF keyword counting by 23% in NDCG. | Directly addresses RG4 (deep semantic matching). | `DIRECTLY SUPPORTED` | Benchmark `all-MiniLM-L6-v2` against domain fine-tuned JobBERT models. |
| **F15** | `gap_score` (Float, 0.0–1.0) | Normalized Euclidean/cosine distance representing missing mandatory technical competencies. | Conceptually grounded in skill gap analysis and automated career trajectory mapping. | **Paper04**, **Paper13**, **Paper16**, **Paper35**, **Paper41** | P04: Section 4.1; P13: Section 3.4; P16: Table 2; P41: Fig. 2 | Missing required skills penalize placement probability non-linearly. | Directly addresses RG1 & RG7 (remediation targets). | `DIRECTLY SUPPORTED` | Validate distance calculation against market requirement hierarchies. |
| **F16** | `consistency_score` (Float, 0.0–1.0) | Longitudinal telemetry metric capturing login regularity, quiz cadence, and habit persistence. | Grounded in learning analytics and self-regulated learning (SRL) literature. | **Paper02**, **Paper05**, **Paper33**, **Paper44** | P02: Table 2; P05: Section 4.2; P33: Section 3.1; P44: Table 3 | Regular weekly platform activity in Weeks 3–6 is more predictive of success than total crammed hours. | Directly addresses RG2 (longitudinal sequence dynamics). | `DIRECTLY SUPPORTED` | Track temporal decay and burstiness using exponential moving averages. |
| **F17** | `branch_encoded` (Float, 0.0–1.0) | Categorical normalized encoding of engineering academic department (CS, IT, ECE, MECH, etc.). | Standard demographic/academic feature in all university placement predictive models. | **Paper01**, **Paper06**, **Paper09**, **Paper10**, **Paper22**, **Paper24** | P01: Table 1; P06: Table 2; P22: Table 1; P24: Section 3.2 | CS/IT candidates experience higher campus placement rates due to software industry quota dominance. | Addressed in RG1; institutional context feature. | `DIRECTLY SUPPORTED` | Audit for demographic algorithmic bias to prevent unfair cross-branch penalization. |
| **F18** | `target_role_encoded` (Float, 0.0–1.0) | Normalized difficulty weight and competency threshold of target corporate role (e.g., SDE vs QA). | Formulated in job matching and recruitment systems to adjust readiness thresholds. | **Paper13**, **Paper17**, **Paper35**, **Paper41** | P13: Section 3.2; P35: Table 1; P41: Section 3.3 | A readiness score of 75% for SDE-1 may represent 95% readiness for technical support or QA. | Directly addresses RG1 & RG7 (role-specific modeling). | `PARTIALLY SUPPORTED` | Empirically calibrate role vectors using real corporate hiring test thresholds. |
| **F19** | `assessment_attempts` (Integer, 0–100) | Cumulative volume of diagnostic quiz and practice assessment iterations completed. | Standard engagement telemetry in learning management systems and formative testing. | **Paper02**, **Paper05**, **Paper33**, **Paper44** | P02: Section 4.1; P05: Table 3; P44: Section 4.2 | High assessment attempt counts indicate proactive student remediation and mastery seeking. | Directly addresses RG2 & RG6 (iterative evaluation). | `DIRECTLY SUPPORTED` | Evaluate correlation with score progression slopes over time. |
| **F20** | `behavior_score` (Float, 0.0–100.0) | Composite paralinguistic metric (speech rate, pause ratio, filler frequency, gaze stability). | Grounded in automated multimodal video/audio interview assessment literature. | **Paper03**, **Paper14**, **Paper15**, **Paper28**, **Paper29**, **Paper30**, **Paper38** | P03: Section 3.2; P15: Table 2; P29: Section 3.3; P38: Table 3 | High interview nervousness and excessive pause latency correlate with recruiter rejection. | Directly addresses RG5 (multimodal interview modeling). | `PARTIALLY SUPPORTED` | Establish inter-rater reliability with senior technical recruiters and HR panels. |
| **F21** | `engagement_score` (Float, 0.0–1.0) | Multi-factor interaction metric combining session duration, resource clicks, and hint requests. | Central predictive feature across educational data mining and at-risk student detection. | **Paper02**, **Paper05**, **Paper33**, **Paper44** | P02: Table 3; P05: Section 3.2; P33: Table 2; P44: Section 3.1 | Early LMS disengagement is the strongest early-warning precursor to course failure and unreadiness. | Directly addresses RG2 (early warning telemetry). | `DIRECTLY SUPPORTED` | Normalize against student cohort baseline to prevent penalizing efficient learners. |
| **F22** | `roadmap_completion_rate` (Float, 0.0–1.0) | Proportion of recommended personalized remediation milestones successfully completed. | Grounded in personalized learning pathways and prescriptive remediation frameworks. | **Paper13**, **Paper16**, **Paper41**, **Paper44** | P13: Section 4.1; P16: Table 3; P41: Fig. 3; P44: Section 5.1 | Closing diagnosed skill gaps measurably increases downstream interview success rates. | Directly addresses RG3 & RG7 (actionable remediation). | `PARTIALLY SUPPORTED` | Measure causal uplift in placement conversion following completed roadmap milestones. |

---

## 3. Ancillary Multi-Modal & Telemetry Features

In addition to the 22 core SPV features, PRIE captures subsystem-specific features during interactive student workflows:

### 3.1 Resume Intelligence & Document Geometry Features
- `bbox_spatial_continuity`: Bounding box vertical and horizontal alignment score across parsed PDF tokens.
  - *Status*: `PROPOSED` (Addresses RG4; LayoutLMv3 integration).
  - *Validation*: Compare layout preservation against standard PDFMiner flat text stream.
- `section_header_confidence`: Softmax classification score assigning text spans to standard resume sections (Education, Skills, Experience, Projects).
  - *Status*: `DIRECTLY SUPPORTED` (**Paper11**, **Paper12**, **Paper17**).
- `skill_mention_density`: Ratio of extracted technical entity tokens to total resume word count.
  - *Status*: `DIRECTLY SUPPORTED` (**Paper12**, **Paper36**, **Paper37**).

### 3.2 Multimodal Mock Interview Telemetry Features
- `turn_taking_latency_ms`: Response turnaround latency from question completion to candidate speech start.
  - *Status*: `DIRECTLY SUPPORTED` (**Paper03**, **Paper15**, **Paper29**). High latency ($>3.5$s) indicates hesitation or processing difficulty.
- `speech_pause_ratio`: Proportion of silence/pauses exceeding 1.2s within candidate response utterance.
  - *Status*: `DIRECTLY SUPPORTED` (**Paper15**, **Paper30**).
- `filler_word_frequency`: Count of disfluencies ("um", "uh", "like", "you know") per 100 spoken words.
  - *Status*: `DIRECTLY SUPPORTED` (**Paper15**, **Paper29**, **Paper38**).
- `facial_valence_stability`: Variance of detected facial emotion expressions during technical problem solving.
  - *Status*: `PARTIALLY SUPPORTED` (**Paper03**, **Paper15**; MediaPipe/DeepFace). Requires validation to ensure cultural neutrality.
- `code_sandbox_execution_success`: Binary pass/fail status of live coding unit test suite in Docker container.
  - *Status*: `IMPLEMENTATION-DERIVED` (Addresses RG5; security and execution validity).

### 3.3 Formative Assessment & Psychometric Features
- `item_response_time_sec`: Time elapsed between question presentation and answer submission.
  - *Status*: `DIRECTLY SUPPORTED` (**Paper02**, **Paper33**, **Paper44**). Differentiates automatic retrieval from guessing or struggle.
- `distractor_selection_pattern`: Indicator of which incorrect option was selected in multiple-choice questions.
  - *Status*: `DIRECTLY SUPPORTED` (**Paper25**, **Paper26**, **Paper39**). Maps specific conceptual misconceptions via Causal DAG.

---

## 4. Feature Redundancy, Collinearity & Data Leakage Audit

### 4.1 Multicollinearity Risk Analysis
- **`cgpa` vs Subject Scores (`dsa_score`, `dbms_score`, `os_score`, `cn_score`)**:
  - *Risk*: High Pearson correlation ($r \approx 0.65\text{–}0.78$) observed between overall CGPA and individual technical subject marks.
  - *Mitigation*: Tree ensembles (Random Forest, XGBoost) natively handle collinear features via split randomization, but for linear baseline models, compute Variance Inflation Factor (VIF). If $\text{VIF} > 5.0$, evaluate principal component aggregation or use regularization ($L_1 / L_2$).
- **`project_count` vs `project_quality_score`**:
  - *Risk*: High project count with low quality score indicates superficial portfolio padding.
  - *Mitigation*: Formulate interaction term `project_volume_quality_product = project_count * project_quality_score`.

### 4.2 Temporal Data Leakage Safeguards
- **Look-Ahead Bias in Telemetry**: Features like `consistency_score`, `assessment_attempts`, and `roadmap_completion_rate` are time-dependent.
  - *Safeguard*: When training tabular models on historical cohorts, all features must be computed **strictly up to the point of prediction** (e.g., end of Semester 6 or end of Semester 7). Future telemetry generated after on-campus recruitment starts must be masked.
- **Label Leakage**:
  - *Safeguard*: Features that are direct consequences of receiving a job offer (e.g., post-placement survey responses, exit interview ratings) are strictly excluded from the SPV.

---

## 5. Summary of Feature Support Statuses

| Category | Count | Features |
|:---|:---:|:---|
| **`DIRECTLY SUPPORTED`** | 16 | `cgpa`, `dsa_score`, `dbms_score`, `os_score`, `cn_score`, `programming_score`, `aptitude_score`, `project_count`, `has_internship`, `certifications_count`, `resume_ats_score`, `cosine_similarity`, `gap_score`, `consistency_score`, `branch_encoded`, `assessment_attempts`, `engagement_score` |
| **`PARTIALLY SUPPORTED`** | 4 | `soft_skills_score`, `target_role_encoded`, `behavior_score`, `roadmap_completion_rate` |
| **`INDIRECTLY SUPPORTED`** | 0 | None in core SPV |
| **`PROPOSED`** | 1 | `project_quality_score` |
| **`IMPLEMENTATION-DERIVED`** | 1 | `code_sandbox_execution_success` (Ancillary) |
| **`NOT YET JUSTIFIED`** | 0 | None retained; all retained features have defined validation pathways |

**Quality Conclusion**: 72.7% of core SPV features are directly grounded in published peer-reviewed empirical evidence. The remaining 27.3% represent targeted enhancements directly motivated by Phase 03 research gaps and equipped with rigorous empirical validation protocols.
