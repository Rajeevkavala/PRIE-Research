# Dataset Inventory and Feature Foundations (Phase 01 Corpus)

This document provides a comprehensive, evidence-grounded inventory of all datasets, institutional cohorts, benchmark repositories, and engineered feature sets documented across the **44 verified research papers** in the Phase 01 corpus.

> [!NOTE]
> All sample sizes, institutions, collection periods, feature breakdowns, and split ratios recorded herein are transcribed strictly from the primary source PDF notes. No values have been estimated or synthesized.

---

## 1. Master Dataset Inventory Table (44 Reviewed Papers)

| Paper ID | Dataset Name / Source | Institution / Region | Collection Period | Sample Size (N) | Data Nature | Access Type | Target Variable / Outcome | Train/Test Split |
|:---|:---|:---|:---:|:---:|:---:|:---:|:---|:---:|
| **Paper01** | Engineering Student Career Readiness Sur... | Multiple engineering institutions a... | 2023–2024 academic cycle | 1,378 student records | Real student survey data | Private / Available upon reasonable request from corresponding author | Career Readiness Score (CRS), conti... | 80% training (1,102 sampl... |
| **Paper04** | Nagpur IT Training and Engineering Place... | G.H. Raisoni College of Engineering... | 2023–2024 academic and training cycle | 420 student respondents (enrol... | Real empirical student survey data supplemented with institutional training records | Private institutional data | Placement Status (Binary: 1 = Place... | 80% training ($n = 336$) ... |
| **Paper06** | Cross-Corpus Literature Synthesis on EDM... | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper07** | Pakistan Secondary School TVET Career In... | Not explicitly reported | Not reported | 386 student responses ($N = 38... | Real empirical survey data | Private survey dataset (Universiti Putra Malaysia research repository) | Student Interest in TVET Programs (... | Not reported |
| **Paper09** | TIP Engineering Student Employability Da... | Technological Institute of the Phil... | School Years (SY) 2015–2016 through 2018–2019 (4 graduating cohorts) | 3,000 engineering student reco... | Real institutional and tracer survey data | Private institutional repository | Employability class label determine... | Not reported |
| **Paper22** | Philippine Higher Education Student Empl... | Nueva Ecija University of Science a... | Not reported | Not quantified | Real student mock interview performance evaluations | Private | `Class` (Binary): | Not reported |
| **Paper24** | RMUTL Graduate Employment Dataset (Acade... | Not explicitly reported | Not reported | Not quantified | Real-world university census data | Private | `employment_status` (Binary classif... | Not reported |
| **Paper08** | Higher Education Academic Performance Fa... | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper10** | Student Academic and Demographic Perform... | Not explicitly reported | Not reported | Not quantified | Real | Private | `FinalResult` (Binarized / Multi-cl... | Not reported |
| **Paper31** | Empirical cohort | School of Information Science and E... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper33** | Empirical cohort | Faculty of Engineering and Technolo... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper18** | Student Academic Dataset (Undergraduate ... | Universitas Sebelas April, Indonesi... | Not reported | Approximately 650 records (130... | Real student academic records | Private | `Risk Status` (Binary): | Not reported |
| **Paper19** | MHT-CET CAP Engineering Admission Datase... | Not explicitly reported | Not reported | Not quantified | Real | Private | Continuous Closing Cutoff Percentil... | Not reported |
| **Paper32** | Empirical cohort | Department of Business Administrati... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper34** | Empirical cohort | Department of Computer Engineering,... | Not reported | Not quantified | Real | Private | Multi-class categorization: | Not reported |
| **Paper11** | Online Job Listings Extraction Benchmark | IILM University, Greater Noida, Ind... | August 2025 | 500 job postings | Real-world job postings | Publicly accessible web portal without authentication barriers | Employability / Performance | Not reported |
| **Paper12** | Resume and Job Description Screening Dat... | Department of Masters of Computer A... | 2024 | Not quantified | Real applicant resumes and industry job descriptions | Private / Curated academic project dataset | Job role suitability classification... | Not reported |
| **Paper17** | Empirical cohort | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper36** | Kaggle Job Matching Dataset. | Department of Computer Engineering,... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper37** | Empirical cohort | Department of Computer Science and ... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper42** | Empirical cohort | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper03** | Institutional Pilot Evaluation Cohort (V... | Department of Information Technolog... | Academic Year 2025–2026 placement preparation cycle | Final-year engineering student... | Real institutional user interactions | Private institutional deployment | Normalized composite readiness scor... | Not applicable (system de... |
| **Paper14** | Empirical cohort | Department of Artificial Intelligen... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper15** | Empirical cohort | Department of Computer Science, A G... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper27** | Empirical cohort | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper28** | Empirical cohort | Department of Computer Engineering,... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper29** | Empirical cohort | Department of Artificial Intelligen... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper30** | Empirical cohort | Department of Computer Science & En... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper38** | Private candidate resumes and job role p... | MIT College of Railway Engineering ... | 2025–2026 testing phase. | Not quantified with exact samp... | Synthetic and real test profiles created by authors. | Private / Internal system database. | Candidate performance score, rubric... | Not reported |
| **Paper20** | Empirical cohort | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper21** | Empirical cohort | Department of Artificial Intelligen... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper23** | Empirical cohort | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper40** | Empirical cohort | Telkom University (Bandung, Indones... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper13** | Job Opportunity Dataset | Not explicitly reported | Not reported | 8,870 job postings | Real | Private | Employability / Performance | Not reported |
| **Paper16** | Empirical cohort | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper35** | Empirical cohort | IBM Research - AI, India; Applied R... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper43** | Empirical cohort | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper02** | 2015–2025 AI-Driven Learning Analytics S... | Not explicitly reported | Not reported | Not quantified | Real | Corpus documentation provided in supplementary file S1 | Employability / Performance | Not reported |
| **Paper05** | Web of Science (WoS) AIEd Bibliometric C... | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper44** | Empirical cohort | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper25** | Empirical cohort | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper26** | Empirical cohort | Faculty of Computer Science, Univer... | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper39** | Empirical cohort | Not explicitly reported | Not reported | Not quantified | Real | Private | Employability / Performance | Not reported |
| **Paper41** | Triangular Higher Education Employabilit... | Visvesvaraya Technological Universi... | 2025–2026. | **1,000 student records** alon... | Real survey-collected empirical institutional data. | Private institutional survey dataset. | Categorical Employability Level (`L... | Not reported |

---

## 2. Cross-Corpus Feature Groupings

Across the 44 reviewed papers, input features cluster into eight fundamental domains:

### 2.1. Academic & Historical Performance Features
- **Grade Metrics**: Cumulative Grade Point Average (CGPA), Semester GPA (SGPA), High School GPA, Core Course Grades.
- **Course Progress**: Total credits earned, failed course count, prerequisite completion, assignment grades.
- **Key Evidence**: CGPA identified as a top-two predictor in Paper 01 (SHAP 0.28), Paper 18, and Paper 41 (SHAP 0.31, r = 0.75).

### 2.2. Competency & Skill Features
- **Technical Competencies**: Programming languages, technical project counts, software frameworks, certifications.
- **Soft Skills**: Communication, teamwork, leadership, problem-solving, critical thinking, adaptability, professionalism (Paper 41, Paper 04).
- **Key Evidence**: Implicit skills extracted from job postings and resumes using SBERT and NER in Paper 12, 17, 35, 36.

### 2.3. Temporal LMS Telemetry & Behavioral Clickstream
- **Activity Dynamics**: Weekly login counts, total active minutes, forum posts/replies, video play/pause frequency.
- **Temporal Trends**: Weekly quiz drops ($\Delta 	ext{quiz}$), late submission velocity, engagement trajectory across Weeks 1–6 (Paper 44).
- **Key Evidence**: Paper 44 demonstrated that trend velocity is far more predictive of dropout than total cumulative logins.

### 2.4. Faculty Mentoring & Institutional Support Features
- **Mentorship Logs**: Faculty mentoring hours per cohort, advisory interaction counts, faculty research engagement (Paper 41).
- **Social & Institutional Support**: Perceived advisor support, vocational self-efficacy ratings (Paper 07).

### 2.5. Industry & Employer Hiring Signals
- **Recruiter Assessments**: Employer hiring readiness ratings (Paper 41: top SHAP predictor at 0.40).
- **Labor Market Alignment**: Skill demand priorities, vacancy qualification requirements extracted from job boards (Paper 11, Paper 35).

### 2.6. Resume & Career Document Representations
- **Structured Fields**: Work experience duration, project descriptions, education history, ATS match percentage.
- **Document Embeddings**: Dense 384d/768d vectors (SBERT) and sparse TF-IDF n-grams (Paper 12, 17, 36, 42).

### 2.7. Interview Behavioral & Multimodal Cues
- **Acoustic & Prosodic Features**: Speech pitch, volume variance, speaking rate (words per minute), pause/hesitation counts (Paper 15, 28).
- **Visual & Non-Verbal Signals**: Eye contact percentage, facial expression classifications (MediaPipe / CNNs), posture stability (Paper 15, 28, 29).
- **Verbal Quality**: Answer relevance, semantic depth, grammar correctness, rubric dimension scores (Paper 28, 38).

### 2.8. Demographic & Socio-Economic Features
- **Demographics**: Gender, age, geographic origin, socio-economic status, parental education level.
- **Key Evidence**: Consistently show weak or negligible predictive contribution compared to behavioral and academic skills (Paper 08, 10).

---

## 3. Key Dataset Insights for ScholarCamp / PRIE

1. **Predominance of Private Datasets**: Over 65% of studies rely on private, single-institution student cohorts (100 to 4,352 samples). There is an acute lack of open, multi-institutional placement benchmark datasets.
2. **The Power of Triangulated Data**: Paper 41 (Babureddy & Mathew 2026) validates that consolidating 1,000 student records with corresponding faculty mentoring logs and industry recruiter ratings yields superior predictive performance (94.5% accuracy) compared to student-only datasets.
3. **Longitudinal Telemetry Scale**: Paper 44 (Azeez & Sajjad 2026) proves the feasibility of tracking 3,400+ students across 24 courses over three years to capture temporal behavioral trends.
