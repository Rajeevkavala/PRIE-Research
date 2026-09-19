# Master Cross-Paper Comparison Matrix (Phase 01 Corpus)

This document provides a comprehensive cross-paper comparison matrix across all **44 verified research papers** in the Phase 01 corpus, establishing the evidence baseline for the **ScholarCamp** ecosystem and the **Placement Readiness Intelligence Engine (PRIE)**.

> [!NOTE]
> All entries, metrics, dataset figures, and algorithm names are extracted strictly from the primary source PDF research notes.

---

## 1. Master Cross-Paper Comparison Table (44 Papers)

| Paper ID | Authors & Year | Domain / Module | Dataset / Cohort | Core Algorithm / Model | Key Performance Results | Explainability (XAI) | Primary Limitations Reported |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **Paper01** | Shikha Pachouly et al. (2026) | `01_Employability` | 1,378 student records | Ten distinct algorithms were benchm... | | Model | Accuracy | Precision | Recall ... | SHAP | - Cross-Sectional Design: Data was gathe... |
| **Paper04** | Ganesh Vasant Padole et al. (2024) | `01_Employability` | 420 student respondents (enrol... | Five supervised models and one unsu... | | Model | Accuracy (%) | Precision | Rec... | SHAP | - Geographic Focus: Data collection was ... |
| **Paper06** | Nesrine Mezhoudi et al. (2021) | `01_Employability` | Empirical cohort | The survey synthesizes and compares... | - Random Forest Yields Peak Accuracy: Wh... | SHAP | - Literature Boundary: Survey focused on... |
| **Paper07** | Nazia Azeem et al. (2021) | `01_Employability` | 386 student responses ($N = 38... | - Multiple Linear Regression (Ordin... | See detailed note | None | - Cross-Sectional Self-Reporting: Relies... |
| **Paper09** | Cherry D. Casuat et al. (2019) | `01_Employability` | 3,000 engineering student reco... | Three supervised classifiers were e... | | Algorithm | Accuracy (%) | Recall (%) ... | None | - Single Institutional Scope: The study ... |
| **Paper22** | Cris Norman P. Olipas* et al. (2026) | `01_Employability` | Empirical cohort | ### 1. Random Forest Classifier (Pr... | | Model | Mean Accuracy | Standard Devia... | SHAP | Not explicitly reported |
| **Paper24** | Tewa Promnuchanont (1) et al. (2026) | `01_Employability` | Empirical cohort | ### 1. Feature Selection Methods (T... | | Model | Accuracy (%) | Recall (%) | Pr... | SHAP | - Single-Institution Scope: Evaluated so... |
| **Paper08** | Yousuf Nasser Said Al Husaini et al. (2022) | `02_Prediction` | Empirical cohort | While the review focuses on feature... | See detailed note | None | - Temporal Boundary: Systematic search c... |
| **Paper10** | Student Project Team (Bachelor of Technology in Computer Science and Engineering) et al. (2022) | `02_Prediction` | Empirical cohort | The application implements four sup... | See detailed note | None | - Monograph Nature: Developed as an acad... |
| **Paper31** | Weikuan Jia et al. (2022) | `02_Prediction` | Empirical cohort | The paper categorizes and compares ... | See detailed note | None | 1. Computational Overhead of Swarm Wrapp... |
| **Paper33** | Raghad Al-Shabandar (Liverpool John Moores Univ.) et al. (2019) | `02_Prediction` | Empirical cohort | The authors train and tune five mac... | - Top Performer: Gradient Boosting Machi... | None | 1. MOOC-Specific Telemetry: Models were ... |
| **Paper18** | Wildan Hidayatulloh (1*) et al. (2026) | `03_XAI` | Approximately 650 records (130... | ### 1. Random Forest (Bagging Parad... | | Accuracy | 90.77% (0.9077) | 89.23% (0... | SHAP | - Contextual Generalizability: Dataset i... |
| **Paper19** | Ashphak Khan (1) et al. (2026) | `03_XAI` | Empirical cohort | ### 1. Primary Model: LightGBM (Lig... | - Mean Error: LightGBM achieved an MAE o... | SHAP | - State-Specific Scope: Validated exclus... |
| **Paper32** | Ramzi Talmoudi and Jamel Choukir et al. (2026) | `03_XAI` | Empirical cohort | Not reported | See detailed note | SHAP | 1. Single Database Limitation: Restricte... |
| **Paper34** | Neethu S Babu (Lecturer) et al. (2026) | `03_XAI` | Empirical cohort | The framework compares four machine... | ### Performance & Accuracy Range (Sectio... | SHAP | 1. Static Tabular Scope: Relies on struc... |
| **Paper11** | Dr Reeta Mishra (IILM University et al. (2025) | `04_ATS` | 500 job postings | - HTML Parsing Engine: BeautifulSou... | | Method | Total Listings Collected | Ti... | None | Not explicitly reported |
| **Paper12** | Mohammed Kashif (Student) and Parimal Kumar K R (Assistant Professor) et al. (2024) | `04_ATS` | Empirical cohort | - Information Extraction: | - Classification Precision: The Linear S... | SHAP | - Complex Layout Fragility: The system s... |
| **Paper17** | Kumkum Solanki (1) et al. (2026) | `04_ATS` | Empirical cohort | - Information Extraction: `spaCy` N... | - Notice: Specific multi-class confusion... | None | - Superficial Semantic Understanding: Ke... |
| **Paper36** | Snehal Suryawanshi et al. (2025) | `04_ATS` | Empirical cohort | 1. Text Extraction & NER: spaCy NLP... | - Resume Parsing Entity Extraction Accur... | None | 1. Failure on Image-Based / Scanned Resu... |
| **Paper37** | Dr. J. JayaPriya (Assistant Professor) et al. (2025) | `04_ATS` | Empirical cohort | The platform combines NLP libraries... | See detailed note | None | 1. Predefined Job Role Scope: Evaluation... |
| **Paper42** | Karthik Kapula (UiPath Solution Architect et al. (2025) | `04_ATS` | Empirical cohort | - Optical Character Recognition (OC... | - Data Entry Error Rate: Dropped from 10... | None | - Document Quality Dependency: Extractio... |
| **Paper03** | Prof. Jayshree Pawar et al. (2026) | `05_Mock_Interview` | Final-year engineering student... | 1. Aptitude Evaluation Algorithm: | See detailed note | SHAP | - Pilot Scope: Initial validation was co... |
| **Paper14** | Ms. Prajakta Prakash Koli et al. (2025) | `05_Mock_Interview` | Empirical cohort | The paper classifies and compares a... | | 3 | BERT-Based Semantic Evaluation for... | Rubric Feedback | - Acoustic Noise Vulnerability: Speech e... |
| **Paper15** | Shoaib Inamdar et al. (2025) | `05_Mock_Interview` | Empirical cohort | - Generative Question & Report Engi... | - Notice: Specific numerical benchmark t... | Rubric Feedback | - Lack of VR Integration: Does not curre... |
| **Paper27** | He Zhang (Penn State University) et al. (2025) | `05_Mock_Interview` | Empirical cohort | - Core LLM Engine: GPT-4o (OpenAI),... | 1. Cognitive Relief: Participants report... | None | 1. Simulated Interviewee Dynamics: Used ... |
| **Paper28** | Pooja Vachkal (Dept. of Computer Engg.) et al. (2026) | `05_Mock_Interview` | Empirical cohort | IndusAI coordinates several machine... | See detailed note | None | 1. English Language Restriction: Models ... |
| **Paper29** | Abdul Wahid et al. (2026) | `05_Mock_Interview` | Empirical cohort | The system coordinates specialized ... | See detailed note | None | 1. Lack of Non-Verbal Computer Vision: T... |
| **Paper30** | Dr. Vijayant Verma (Assistant Professor) et al. (2025) | `05_Mock_Interview` | Empirical cohort | The system incorporates several spe... | - Evaluation Accuracy: 95.45% accuracy i... | None | 1. Lack of Multimodal Vision: Does not t... |
| **Paper38** | Siddhi Kulkarni et al. (2026) | `05_Mock_Interview` | Not quantified with exact samp... | - Large Language Models (LLMs): Acc... | - Quantitative Benchmark Results: No num... | Rubric Feedback | - Text-Only Evaluation: The current syst... |
| **Paper20** | Jakub Swacha (1*) and Michał Gracel (1) et al. (2025) | `06_RAG` | Empirical cohort | The survey identifies the distribut... | | Domain Factual Accuracy | Human Expert... | Graph / Citation | - Search Query Language Constraint: Rest... |
| **Paper21** | Nisanth P et al. (2025) | `06_RAG` | Empirical cohort | ### 1. Embedding Model | - Re-Ranking Impact: Qualitative analysi... | None | - Static Knowledge Base: The vector inde... |
| **Paper23** | Venkatesh S. (1) et al. (2024) | `06_RAG` | Empirical cohort | ### 1. Vector Embedding Model | See detailed note | Graph / Citation | - Computational Power & Connectivity: Re... |
| **Paper40** | Yusza Reditya Murti (1) et al. (2025) | `06_RAG` | Empirical cohort | - Large Language Model (LLM): Pre-t... | - Overall TAM Acceptance: Overall mean s... | Graph / Citation | - Demonstration-Based Evaluation: Evalua... |
| **Paper13** | Saeed Ashrafi (1) et al. (2023) | `07_Recommendation` | 8,870 job postings | ### 1. Salary Classification Engine... | ### 1. Salary Classification Model Accur... | None | - Job Scope Focus: Primarily tested and ... |
| **Paper16** | Yaqian Zheng (1 et al. (2024) | `07_Recommendation` | Empirical cohort | ### 1. Proposed Algorithm: MACO (Mo... | | Dataset | RS (Mean) | IA (Mean) | GA (... | SHAP | - Computational Benchmark Datasets: Due ... |
| **Paper35** | Akshay Gugnani (IBM Research - AI) and Hemant Misra (Applied Research et al. (2020) | `07_Recommendation` | Empirical cohort | The paper integrates four distinct ... | - A@1 (First Recommendation Accuracy): | Graph / Citation | 1. Corpus Availability: Absence of publi... |
| **Paper43** | M. S. Rajeevan (1 et al. (2026) | `07_Recommendation` | Empirical cohort | - Sentence-BERT (SBERT): Sentence-T... | ### Information Overload Reduction by Qu... | Graph / Citation | - Limited Evaluation Scale: Evaluated ac... |
| **Paper02** | Olufunke E. Ajayi et al. (2026) | `08_Learning_Analytics` | Empirical cohort | The review documents the distributi... | See detailed note | SHAP | - Narrative Design: While guided by PRIS... |
| **Paper05** | Lim Seong Pek et al. (2026) | `08_Learning_Analytics` | Empirical cohort | - Bibliometric Mapping Software: VO... | See detailed note | None | - Single Database Scope: Literature sear... |
| **Paper44** | Dr Ansari Pulickal Abdul Azeez (1) et al. (2026) | `08_Learning_Analytics` | Empirical cohort | - Temporal Fusion Transformer (TFT)... | - Accuracy: 0.89 (89.5%) | SHAP | - Disciplinary Focus: Validated primaril... |
| **Paper25** | Nichoas X. Wang (Stellar Learning Technologies et al. (2025) | `09_Question_Generation` | Empirical cohort | The framework employs a coordinated... | See detailed note | Graph / Citation | 1. Occasional Difficulty Mismatch: A min... |
| **Paper26** | Halim Wildan Awalurahman et al. (2025) | `09_Question_Generation` | Empirical cohort | The review establishes an authorita... | See detailed note | None | 1. Quality Assessment Subjectivity: Qual... |
| **Paper39** | Ghader Kurdi (1) et al. (2020) | `09_Question_Generation` | Empirical cohort | The review categorizes generation a... | See detailed note | None | - Language Restriction: The review is li... |
| **Paper41** | Babureddy N S (1 et al. (2026) | `10_Digital_Twin` | **1,000 student records** alon... | - XGBoost Multiclass Classifier: Pr... | - Overall Accuracy: 94.5% (189 out of 20... | SHAP | - Survey Self-Report Bias: Portions of s... |
---

## 2. Synthesis of Thematic Module Representation

Across the 44 verified papers, research efforts distribute across ten functional modules:

1. **Employability & Career Readiness (`01_Employability/`)**: 7 papers (Paper 01, 04, 06, 07, 09, 22, 24). Focus on statistical classification of graduate placement outcomes, identifying skill gaps, and social support.
2. **Student Performance & Risk Prediction (`02_Prediction/`)**: 4 papers (Paper 08, 10, 31, 33). Focus on academic GPA prediction, feature selection metaheuristics, and early warning systems.
3. **Explainable Artificial Intelligence (`03_XAI/`)**: 4 papers (Paper 18, 19, 32, 34). Focus on SHAP/LIME post-hoc model interpretability, bibliometric mapping of XAI in HE, and institutional trust.
4. **Applicant Tracking Systems & Resume Parsing (`04_ATS/`)**: 5 papers (Paper 11, 12, 17, 36, 42). Focus on automated PDF parsing, web scraping, transformer NER, and intelligent document processing.
5. **Mock Interviews & Multimodal Feedback (`05_Mock_Interview/`)**: 7 papers (Paper 03, 14, 15, 27, 28, 29, 30, 38). Focus on speech prosody, facial expression tracking, follow-up interview generation, and rubric scoring.
6. **Retrieval-Augmented Generation & Chatbots (`06_RAG/`)**: 4 papers (Paper 20, 21, 23, 40). Focus on grounding LLMs on institutional courseware, vector databases, and student technology acceptance.
7. **Curriculum & Career Recommendation (`07_Recommendation/`)**: 4 papers (Paper 13, 16, 35, 43). Focus on implicit skill extraction, learning pathways, and Knowledge Graph discovery.
8. **Learning Analytics & Educational Mining (`08_Learning_Analytics/`)**: 3 papers (Paper 02, 05, 44). Focus on longitudinal clickstream sequences, Temporal Fusion Transformers, and reinforcement learning interventions.
9. **Automatic Question Generation (`09_Question_Generation/`)**: 3 papers (Paper 25, 26, 39). Focus on causal graphs, systematic literature reviews, and MCQ generation.
10. **Digital Twin Architectures (`10_Digital_Twin/`)**: 1 paper (Paper 41). Focus on multi-stakeholder Student–Faculty–Industry modeling and counterfactual simulation.

---

## 3. Critical Observations from the Comparative Baseline

- **Fragmented Point Solutions**: Nearly all existing systems target isolated functions (e.g., resume parsing alone, mock interviews alone, or grade prediction alone).
- **Single-Stakeholder Dominance**: Except for Paper 41 (Babureddy & Mathew 2026), systems focus solely on student attributes, ignoring faculty mentoring and employer hiring standards.
- **Absence of Closed-Loop Interventions**: Few systems bridge prediction to prescriptive intervention; Paper 44 is a notable exception demonstrating RCT-proven failure reduction.
