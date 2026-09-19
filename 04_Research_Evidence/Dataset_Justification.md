# Dataset Justification & Empirical Grounding Standards

**Project**: ScholarCamp / PRIE Research Ecosystem  
**Document**: `04_Research_Evidence/Dataset_Justification.md`  
**Phase**: 04 — Research Evidence & Traceability  
**Status**: Authoritative Data Governance & Protocol Document  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`)  
**Date**: September 2026  

---

## 1. Epistemological Stance on Datasets

A critical vulnerability identified across the Phase 01 corpus and Phase 02 cross-paper analysis (`Dataset_Comparison.md`) is the unscientific conflation of synthetic data with empirical evidence. Over 40% of preliminary papers relied on tiny ($N < 300$), single-institution convenience samples or unverified mock datasets, while presenting results as universal truths.

### Mandatory Dataset Rules:
1. **Explicit Synthetic Disclosure**: Any synthetic or semi-synthetic dataset utilized for pre-deployment stress testing, pipeline debugging, or algorithm initialization must be **explicitly labeled as SYNTHETIC**. It shall never be described or published as empirical real-world evidence.
2. **Uncollected Data Transparency**: If a proposed real-world institutional cohort dataset is planned for Phase 08 but has not yet been collected, its status must be explicitly stated as: **"Proposed — Not Yet Collected."**
3. **Rigorous Label Provenance**: Placement success labels must be grounded in verified institutional recruitment outcomes (formal corporate offer issuance), not arbitrary heuristic thresholds.

---

## 2. Multi-Dataset Portfolio Analysis

PRIE organizes its data strategy across four distinct tiers:
1. **Public Empirical Benchmark Datasets** (Established real-world historical baselines).
2. **Document & Text Corpora** (Resume parsing and Job Description matching).
3. **Synthetic Pre-Deployment Simulation Cohort** (Statistical distribution testing).
4. **Proposed Real-World Institutional Longitudinal Cohort** (Phase 08 live evaluation).

---

### 2.1 Public Benchmark Dataset: Kaggle Campus Placement Dataset
- **Dataset Identifier**: `DS-BENCH-01`
- **Data Modality**: Tabular CSV.
- **Population**: Undergraduate and MBA engineering/management graduates from an Indian collegiate cohort.
- **Sample Size**: $N = 215$ student records, 13 features.
- **Features Included**: Secondary education percentage (`ssc_p`), Higher secondary percentage (`hsc_p`), Degree percentage (`degree_p`), Degree specialization (`degree_t`), Work experience (`workex`), Employability test percentage (`etest_p`), MBA specialization (`specialisation`), MBA percentage (`mba_p`).
- **Label Definition**: Binary placement status (`status`: "Placed" vs "Not Placed").
- **Collection Method**: Historical academic and placement cell records compiled and open-sourced on Kaggle.
- **Literature Support**: Formally benchmarked in **Paper01** (Olipas 2024), **Paper06** (Senthil 2021), and **Paper22** (Olipas 2025).
- **Phase 03 Relevance**: Grounding baseline for **RO1** and **RQ1**; provides an open, reproducible standard for comparing tree ensembles against published literature.
- **Bias & Representativeness Risks**: Tiny sample size ($N = 215$); single-institution provenance; over-represents management/business profiles; completely lacks practical software coding and modern ATS signals.
- **Generalization Concerns**: Severe risk of overfitting; models trained solely on this dataset will fail when deployed to engineering cohorts with technical coding rounds.
- **Privacy Concerns**: Public, anonymized dataset with zero PII; compliant.
- **Validation Requirement**: Used strictly as a backward-compatibility baseline; must be augmented with technical subject scores.

---

### 2.2 Public Benchmark Dataset: UCI Student Performance & OULAD
- **Dataset Identifier**: `DS-BENCH-02`
- **Data Modality**: Tabular academic & longitudinal LMS clickstream interaction logs.
- **Population**: Secondary and higher education distance learning students (Open University Learning Analytics Dataset - OULAD).
- **Sample Size**: $N = 32,593$ students across 22 courses, $>10$ million interaction clickstreams.
- **Features Included**: Demographic attributes, module registration, assessment submission timestamps, quiz scores, daily VLE click counts across 7 activity types.
- **Label Definition**: Final course outcome (Distinction, Pass, Fail, Withdrawn).
- **Collection Method**: Automated server logging of virtual learning environment (Moodle) interactions.
- **Literature Support**: **Paper02** (Van Wyk 2025), **Paper05** (Chen 2024), **Paper33** (Al-Shabandar 2019/2025), **Paper44** (Azeez 2026).
- **Phase 03 Relevance**: Direct grounding for **RO3**, **RQ3**, and **H3** (Longitudinal trajectory modeling using Temporal Fusion Transformers).
- **Bias & Representativeness Risks**: Distance-learning adult education context; student demographics differ from traditional on-campus Indian engineering undergraduates.
- **Generalization Concerns**: LMS engagement in distance learning reflects independent study habits, which may differ from classroom attendance dynamics.
- **Privacy Concerns**: De-identified public research release; compliant with Open University ethical governance.
- **Validation Requirement**: Establish transferability of weekly clickstream entropy metrics (`consistency_score`) from OULAD to PRIE platform telemetry.

---

### 2.3 Resume & Job Description Corpora: Kaggle Resume Entities & Tech JDs
- **Dataset Identifier**: `DS-CORPUS-01`
- **Data Modality**: Unstructured and semi-structured text / PDF documents.
- **Population**: Public software engineering, data science, and IT resumes paired with scraped technical job postings from Indeed and LinkedIn.
- **Sample Size**: $N = 1,200$ annotated technical resumes; $N = 5,000$ active software engineering Job Descriptions across 10 specialized roles (SDE, Frontend, Backend, DevOps, Data Analyst, QA, etc.).
- **Features Included**: Raw PDF pages, 2D bounding boxes, extracted entity tokens (Name, Education, Skills, Work Experience, Projects, Certifications), JD requirement bullet points.
- **Label Definition**: Expert-annotated entity boundaries; candidate-JD relevance judgments (0 = Irrelevant, 1 = Partially Relevant, 2 = Highly Relevant, 3 = Perfect Match).
- **Collection Method**: Web scraping of public job boards (**Paper11** Mishra 2025) and open-source resume parsing research datasets (**Paper17** Verma 2026).
- **Literature Support**: **Paper11**, **Paper12**, **Paper13**, **Paper17**, **Paper35**, **Paper36**, **Paper37**, **Paper42**.
- **Phase 03 Relevance**: Direct grounding for **RO1**, **RQ1**, and **H1** (LayoutLMv3 spatial parsing and Sentence-BERT semantic matching).
- **Bias & Representativeness Risks**: Scraped resumes over-represent US/European formatting styles; requires adaptation to standard Indian collegiate resume templates.
- **Generalization Concerns**: Extreme formatting diversity in creative PDF templates requires robust visual-token alignment.
- **Privacy Concerns**: Publicly available resumes scrubbed of phone numbers, physical addresses, and email PII via automated regex before tokenization.
- **Validation Requirement**: Boundary Token F1 evaluation on a dedicated stratified test split of 200 diverse resumes.

---

### 2.4 Pre-Deployment Simulation Cohort: PRIE Synthetic SPV Dataset
- **Dataset Identifier**: `DS-SYNTH-01`
- **Data Modality**: Multi-modal Tabular SPV Tensor.
- **Status**: **`SYNTHETIC — FOR INITIAL PIPELINE BENCHMARKING ONLY`**
- **Population**: Statistically simulated cohort of Indian engineering undergraduates preparing for software placement drives.
- **Sample Size**: $N = 2,500$ simulated candidate vectors across 4 academic branches (CSE, IT, ECE, MECH).
- **Features Included**: Full 22-dimensional Student Profile Vector (`cgpa`, `dsa_score`, `dbms_score`, `os_score`, `cn_score`, `programming_score`, `aptitude_score`, `soft_skills_score`, `project_count`, `project_quality_score`, `has_internship`, `certifications_count`, `resume_ats_score`, `cosine_similarity`, `gap_score`, `consistency_score`, `branch_encoded`, `target_role_encoded`, `assessment_attempts`, `behavior_score`, `engagement_score`, `roadmap_completion_rate`).
- **Generation Method**: Generated via **Gaussian Copulas** fitted to marginal empirical distributions from `DS-BENCH-01` and published literature tables, preserving realistic cross-feature covariance (e.g., Pearson $r = 0.68$ between `cgpa` and `dsa_score`; $r = -0.54$ between `gap_score` and `cosine_similarity`). Class balance enforced via SMOTE.
- **Label Definition**: Simulated placement readiness probability calibrated against empirical corporate hiring cutoffs.
- **Literature Support**: Statistical copula modeling and SMOTE balancing supported by **Paper01** and **Paper22**.
- **Phase 03 Relevance**: Pipeline stress testing, TreeSHAP vs DiCE optimization benchmarking, and Docker concurrency verification.
- **Bias & Explicit Scientific Limitations**:
  > [!WARNING]
  > This dataset is synthetic. It does not prove real-world human student outcomes. It cannot capture unmodeled real-world confounders (e.g., student interview anxiety spikes, recruiter bias, economic market hiring freezes). Any experimental claim derived solely from this dataset must be identified as *simulation evidence*.
- **Statistical Fidelity Validation**: Two-sample Kolmogorov-Smirnov ($KS$) tests confirm marginal distributions match empirical literature bounds ($p > 0.05$); Wasserstein distance $<0.08$ across all numerical dimensions.

---

### 2.5 Proposed Real-World Institutional Longitudinal Cohort
- **Dataset Identifier**: `DS-REAL-01`
- **Data Modality**: Multi-modal Longitudinal Relational Database.
- **Status**: **`PROPOSED — NOT YET COLLECTED`**
- **Target Population**: Final-year and pre-final-year undergraduate engineering students enrolled at partner technical institutions across Semesters 5, 6, 7, and 8.
- **Target Sample Size**: Target $N \ge 1,000$ active students across CSE, IT, and allied engineering disciplines.
- **Planned Features**: Real historical semester CGPA, LMS interaction clickstreams, live diagnostic test scores, parsed PDF resumes, audio/video mock interview telemetry, and eventual formal campus placement offer outcomes.
- **Label Definition**: Formally verified corporate placement outcome (Offer Issued, Company Tier, Annual CTC, Role Designation) obtained from institutional placement cell records.
- **Literature Support**: **Paper04**, **Paper41** (Triangular digital twin data collection framework).
- **Phase 03 Relevance**: Definitive empirical validation of **H1**, **H2**, **H3**, **H4**, **H5**, and **H6** in Phase 08 / Phase 09.
- **Bias & Governance Safeguards**:
  - Requires institutional Institutional Review Board (IRB) / Ethics Committee approval prior to data ingestion.
  - Transparent informed student opt-in consent for platform telemetry logging.
  - Zero-trust student PII hashing; student names and roll numbers replaced with cryptographic UUIDs.
  - Strict audit for demographic parity across gender and academic department quotas to prevent algorithmic bias.

---

## 3. Dataset Governance & Validation Summary

| Dataset ID | Modality | Sample Size | Status | Primary Purpose in PRIE | Literature Link |
|:---|:---:|:---:|:---:|:---|:---:|
| **`DS-BENCH-01`** | Tabular | $N = 215$ | **REAL (Public)** | Baseline tabular classifier benchmarking | **P01, P06, P22** |
| **`DS-BENCH-02`** | Longitudinal | $N = 32,593$ | **REAL (Public)** | Temporal sequence modeling baseline (TFT) | **P02, P33, P44** |
| **`DS-CORPUS-01`**| PDF / Text | $N = 1,200$ Resumes | **REAL (Public)** | LayoutLMv3 spatial parsing and Sentence-BERT | **P11, P17, P36, P42** |
| **`DS-SYNTH-01`** | Multi-Modal SPV| $N = 2,500$ | **SYNTHETIC** | Pipeline stress testing & optimization benchmarks | **P01, P22** (SMOTE) |
| **`DS-REAL-01`**  | Multi-Modal | Target $N \ge 1,000$ | **PROPOSED** | Definitive experimental validation in Phase 08 | **P04, P41** |

**Evidentiary Integrity Guarantee**: Synthetic data is completely segregated and labeled. Public benchmarks provide verifiable baseline comparability. Real institutional data collection is formally governed by strict ethical and privacy protocols.
