# Paper 03 — Preplyte: An Integrated AI-Powered Placement Preparation and Simulation Platform for Student and Institutions

## 1. Bibliographic Information

- **Paper ID**: Paper03
- **Full Title**: Preplyte: An Integrated AI-Powered Placement Preparation and Simulation Platform for Student and Institutions
- **Authors**: Prof. Jayshree Pawar, Swaranjith Satyanarayana Gudelli, Shravan Vijay Chavan, Sarvesh Balasaheb Bhoite
- **Affiliation**: Department of Information Technology, Vasantdada Patil Pratishthan’s College of Engineering and Visual Arts, Sion, Mumbai, Maharashtra, India
- **Year**: 2026 (Published January 29, 2026; cataloged under 2025 in earlier bib)
- **Venue**: International Journal of Latest Technology in Engineering, Management & Applied Science (IJLTEMAS)
- **Volume / Issue / Pages**: Volume XV, Issue I, January 2026, pp. 489–496
- **DOI**: [10.51583/IJLTEMAS.2026.150100044](https://doi.org/10.51583/IJLTEMAS.2026.150100044)
- **PDF filename**: `Paper03_sharma2025preplyte.pdf`
- **PDF path**: `01_Research_Foundation/Papers/PDFs/Paper03_sharma2025preplyte.pdf`
- **Page count**: 8 pages

---

## 2. Research Problem

Campus placement preparation is traditionally fragmented across disconnected tools: students use one platform for aptitude tests, another for competitive coding, third-party sites for resume formatting, and informal practice for interviews. This fragmentation causes cognitive overload, unorganized preparation, lack of continuous tracking, and an unrealistic simulation of actual company hiring drives. Additionally, university placement cells lack unified institutional dashboards to monitor preparation progress, diagnose skill gaps, and schedule proactive interventions.

### Source Evidence
- **Page**: PDF p. 489–490 (PDF pp. 1–2)
- **Section**: Section 1 (Introduction), Problem Statement

---

## 3. Research Objectives

The authors explicitly define five research objectives:
1. Design and develop an integrated, user-centric placement preparation platform resolving fragmentation limitations.
2. Implement automated assessment and feedback mechanisms for aptitude tests, coding evaluations, mock interviews, and resume analysis.
3. Simulate end-to-end campus recruitment drives by modeling company-specific hiring workflows.
4. Provide institutional analytical dashboards enabling placement officers and faculty to track student progress and cohort performance.
5. Evaluate platform efficacy in enhancing student technical skills, interview confidence, and placement readiness through pilot deployment.

### Source Evidence
- **Page**: PDF p. 490 (PDF p. 2)
- **Section**: Research Goals and Objectives

---

## 4. Research Questions

Not explicitly formulated as numbered research questions; framed as the five core research objectives above.

---

## 5. Dataset

- **Dataset name**: Institutional Pilot Evaluation Cohort (Vasantdada Patil Pratishthan's College of Engineering)
- **Dataset source**: Internal student and faculty usage logs during campus placement training
- **Institution**: Department of Information Technology, Vasantdada Patil Pratishthan’s College of Engineering and Visual Arts, Sion, Mumbai, India
- **Collection period**: Academic Year 2025–2026 placement preparation cycle
- **Dataset size**: Final-year engineering student cohort (pilot group) and placement faculty
- **Number of samples**: Qualitative and platform usage logs across final-year engineering students (exact sample size not explicitly quantified in the pilot summary)
- **Classes**: Placement-ready vs. In-preparation
- **Target variable**: Normalized composite readiness score and module scores (Aptitude, Coding, Interview, Resume)
- **Real / synthetic**: Real institutional user interactions
- **Public / private**: Private institutional deployment
- **Train/test split**: Not applicable (system design and pilot validation study)

### Source Evidence
- **Page**: PDF p. 494 (PDF p. 6)
- **Section**: Section 5 (Evaluation and Validation)

---

## 6. Features

The platform captures multi-modal student performance features across four core modules:

### Academic & Aptitude
- Quantitative aptitude accuracy percentage
- Logical reasoning score
- Verbal ability score
- Time taken per question (latency metric)

### Coding Skills
- Code compilation correctness
- Number of test cases passed (edge cases, boundary cases)
- Execution time and memory consumption
- Submission retry count

### Resume & ATS
- Resume keyword density matching target job descriptions
- Section completeness (Education, Projects, Skills, Experience)
- Format compliance and parseability score via spaCy NLP

### Interview & Behavioral
- Voice response completeness
- Technical question response accuracy
- Resume-aligned project explanations

### Source Evidence
- **Page**: PDF p. 492–494 (PDF pp. 4–6)
- **Section**: Section 4 (Student Workflow and Algorithm Integration)

---

## 7. Data Preprocessing

- **Resume Parsing & Information Extraction**: PDF and DOCX text extraction, tokenization, stop-word removal, and Named Entity Recognition (NER) using spaCy to isolate skills, education, and experience entities.
- **Score Normalization**: Linear min-max scaling of aptitude, coding execution times, and interview scores to a uniform [0, 100] scale for multi-attribute ranking.
- **Test Case Validation**: Input sanitization and automated execution sandboxing for submitted student code.

### Source Evidence
- **Page**: PDF p. 492–493 (PDF pp. 4–5)
- **Section**: Section 3 (System Architecture), Section 4 (Aptitude and Coding Evaluation Algorithm)

---

## 8. Algorithms and Models

1. **Aptitude Evaluation Algorithm**:
   - Role: Automated scoring of multiple-choice assessments
   - Mathematical formula: $\text{Score} = \left(\frac{\text{Correct Answers}}{\text{Total Questions}}\right) \times 100$
   - Combines accuracy metrics with time-per-question metrics to generate speed-accuracy diagnostic profiles.
2. **Coding Test Execution Engine (Online Judge)**:
   - Role: Sandboxed compilation and test case execution
   - Logic: Executes code against hidden test cases checking logic, syntax, edge cases, and runtime constraints.
3. **Resume Analysis & ATS Scoring Engine**:
   - Role: Applicant Tracking System parsing and scoring
   - Method: Natural Language Processing (NLP) implemented with spaCy / Scikit-learn to extract skills and match them with target job descriptions.
4. **Leaderboard and Ranking Algorithm**:
   - Role: Dynamic multi-criteria student ranking
   - Logic: Weighted aggregation of normalized aptitude, coding, interview, and resume scores to compute an overall cohort standing.
5. **AI-Driven Mock Interview Generator**:
   - Role: Conversational interview simulation
   - Method: Contextual question generation based on student resume profile and chosen target company job specifications.

### Source Evidence
- **Page**: PDF p. 492–494 (PDF pp. 4–6)
- **Section**: Section 3, Section 4

---

## 9. Architecture

The Preplyte system is structured into a classic 3-tier enterprise web architecture:
1. **Presentation Layer (Frontend)**: Developed in HTML5, CSS3, JavaScript, React / Angular. Delivers student dashboards, online coding editors, resume builders, and simulated interview screens.
2. **Application Layer (Backend)**: Built with Node.js / Python (Flask / Django). Coordinates business logic, executes online judge sandboxing, runs NLP resume parsing pipelines, and generates feedback analytics.
3. **Data Layer (Database)**: MySQL / MongoDB storing user credentials, question repositories, code submissions, parsed resume JSONs, and test score histories.

### Source Evidence
- **Page**: PDF p. 491–492 (PDF pp. 3–4)
- **Figure**: Overall System Architecture diagram (PDF p. 492)

---

## 10. Methodology

1. Requirements analysis through literature review of existing commercial and open-source placement preparation tools.
2. Design of an integrated modular architecture combining ATS resume scanning, aptitude assessment, coding judge, and mock interviews.
3. Implementation of full-stack prototype using React, Node.js/Python, and spaCy.
4. Deployment of pilot study with final-year engineering students and placement cell coordinators.
5. Qualitative and observational evaluation of platform utility, preparation efficiency, and user confidence.

### Source Evidence
- **Page**: PDF p. 491–494 (PDF pp. 3–6)
- **Section**: Section 3, 4, 5

---

## 11. Experimental Setup

- **Development Stack**: React frontend, Node.js/Python backend, MySQL/MongoDB database, spaCy NLP library.
- **Deployment Context**: Campus network at Vasantdada Patil Pratishthan’s College of Engineering and Visual Arts, Mumbai.

### Source Evidence
- **Page**: PDF p. 492 (PDF p. 4)
- **Section**: Section 3 (Architecture)

---

## 12. Evaluation Metrics

- Platform Usability & Satisfaction (qualitative feedback from students and faculty)
- Aptitude Scoring Accuracy: Formula-based scoring percentage
- Code Correctness: Test cases passed ratio
- Resume ATS Compatibility Score (0–100 scale based on keyword and formatting match)

### Source Evidence
- **Page**: PDF p. 493–494 (PDF pp. 5–6)
- **Section**: Section 4, Section 5

---

## 13. Results

- **Integration Success**: Demonstrated that integrating aptitude, coding, ATS resume scanning, and interview preparation into a unified platform eliminates tool switching and enables centralized progress monitoring.
- **Pilot Feedback**: Final-year engineering students reported improved preparation structure and confidence; placement cell faculty validated that institutional dashboards provided actionable visibility into cohort strengths and weaknesses.
- **Workflow Simulation**: Validated the feasibility of company-specific hiring drive simulation (Aptitude Round -> Coding Round -> Technical Interview -> HR Interview).

### Source Evidence
- **Page**: PDF p. 494 (PDF p. 6)
- **Section**: Section 5 (Evaluation and Validation)

---

## 14. Baselines

The system is contrasted with existing fragmented standalone tools: LeetCode/HackerRank (coding only), commercial ATS checkers (resume only), and generic video mock interview tools (e.g., platforms using external APIs described by Gomez et al. and IJIRT).

---

## 15. Ablation Study

Not reported (system prototype architecture and pilot implementation study).

---

## 16. Explainability

Explainability is operationalized as **diagnostic feedback loops** rather than mathematical post-hoc XAI (like SHAP):
- Detailed breakdown of test case failures in coding tests.
- Keyword gap analysis in ATS resume scanning (highlighting missing competencies relative to job descriptions).
- Speed vs. accuracy analysis in aptitude testing.

### Source Evidence
- **Page**: PDF p. 493–494 (PDF pp. 5–6)
- **Section**: Final Feedback and Analytics Loop

---

## 17. Main Findings

1. **Unified Preparation Enhances Student Coherence**: Single-portal placement ecosystems significantly reduce student preparation anxiety and streamline tracking compared to fragmented tools.
2. **Company-Specific Workflows are Critical**: Generic practice is less effective than replicating specific hiring round structures of major recruiters.
3. **Faculty Oversight Bridges Interventions**: Institutional dashboards allow college placement cells to intervene before companies arrive on campus.

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Pilot Scope**: Initial validation was conducted as a preliminary pilot in a single institution; large-scale cross-institutional empirical benchmarks were not reported.
- **API Cost & Complexity**: Video/speech interview integrations involve third-party API dependencies that raise scalability and cost considerations.
- **Conversational Flexibility**: Automated mock interview dialogs require further adaptation to handle unpredictable student responses.

### 18.2 Research Interpretation
- *Research team interpretation*: The paper presents an engineering design and prototype architecture with qualitative pilot findings; it does not report formal statistical benchmarking, p-values, or controlled A/B test effect sizes.

---

## 19. Future Work

Explicitly proposed by the authors:
1. **Roadmap-Based Skill Certification**: Provide structured step-by-step learning roadmaps with completion certificates to validate abilities.
2. **AI-Assisted Placement Prediction Engine**: Implement predictive modeling to evaluate student progress and predict placement probability before campus drives.
3. **Dedicated Mentor & Recruiter Dashboards**: Expand the platform to allow direct corporate recruiter interaction and alumni mentorship tracking.

### Source Evidence
- **Page**: PDF p. 495 (PDF p. 7)
- **Section**: Section 6 (Future Scope)

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **Relevant PRIE Module**: `05_Mock_Interview`, `04_ATS`, and `01_Employability`.
- **Architectural Link**: Directly mirrors ScholarCamp’s architectural vision of an integrated ecosystem combining ATS resume scanning, coding analytics, mock interviews, and placement prediction.
- **PRIE Novelty Distinction**: Preplyte identified "AI-assisted Placement Prediction" as future work; PRIE implements this core predictive engine directly, linking it with Explainable AI (SHAP) and multi-agent interview simulations.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Integrated Architecture | 3-tier architecture (Presentation, Application, Data Layer) | PDF p. 492, Section 3 | Figure / Architecture |
| Formula for Aptitude Scoring | Score = (Correct Answers / Total Questions) * 100 | PDF p. 493, Section 4 | Methodology |
| NLP Resume Engine | spaCy / Scikit-learn applied for ATS parsing and keyword extraction | PDF p. 492, Section 3 | Direct statement |
| Pilot Cohort Validation | Preliminary validation with final-year engineering students & faculty | PDF p. 494, Section 5 | Experimental result |
| Proposed Future Prediction | Authors explicitly list AI placement prediction as an unbuilt future enhancement | PDF p. 495, Section 6 | Author discussion |

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

**VERIFIED** (Fully verified from primary PDF source: `Paper03_sharma2025preplyte.pdf`, 8 pages).
