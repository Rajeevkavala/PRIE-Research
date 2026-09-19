# Paper 38 — PrepWise: A Generative AI-Powered Personalized Interview Preparation and Multi-Dimensional Assessment Platform

## 1. Bibliographic Information

- **Paper ID**: Paper38
- **Full Title**: PrepWise: A Generative AI-Powered Personalized Interview Preparation and Multi-Dimensional Assessment Platform
- **Authors**: Siddhi Kulkarni, Mahesh Madane, Dinesh Garule, Amruta Kore (Computer Science and Engineering, MIT College of Railway Engineering and Research, Barshi, Maharashtra, India)
- **Year**: 2026 (March - April 2026)
- **Venue**: International Journal of Electrical Engineering and Ethics (IJEEE), Volume 9, Issue 2, pp. 1347–1352, ISSN: 2455-9771
- **DOI**: Not explicitly reported / None assigned by journal (Journal URL: http://www.ijeeejournal.org)
- **PDF filename**: `Paper38_pillai2026prepwise.pdf`
- **PDF path**: `Papers/PDFs/Paper38_pillai2026prepwise.pdf`
- **Page count**: 6 pages
- **Metadata Note / Discrepancy**: The PDF filename indicates `pillai2026prepwise`, but the actual printed authors on PDF p. 1 (p. 1347) are Siddhi Kulkarni, Mahesh Madane, Dinesh Garule, and Amruta Kore from MIT College of Railway Engineering and Research, Barshi, Maharashtra, India. There is no author named Pillai in the paper.

## 2. Research Problem

The authors explicitly address the inefficiencies in recruitment and interview preparation: candidates employ broad, generic preparation techniques that lack alignment with targeted roles and fail to provide realistic practice or feedback on essential soft skills (communication, logical reasoning, cultural fit). Concurrently, recruiters expend excessive hours manually screening applications that fail to reflect actual competencies due to a lack of objective, multi-dimensional assessment tools.

### Source Evidence
- PDF p. 1 (p. 1347), Abstract & Section I — Introduction.
- PDF p. 2 (p. 1348), Section 1.3 — Problem Definition and Objectives.

## 3. Research Objectives

1. Develop an intelligent, generative AI-powered ecosystem (PrepWise) that generates pertinent, role-specific interview questions by analyzing candidate resumes and target job positions.
2. Provide real-time constructive feedback and multi-dimensional candidate evaluation across technical proficiency, communication skills, and problem-solving abilities using structured rubrics.
3. Integrate intelligent resume-to-job matching, ATS-friendly resume generation, and a centralized administrative analytics dashboard for monitoring candidate progress and recruitment workflows.

### Source Evidence
- PDF p. 1 (p. 1347), Abstract.
- PDF p. 2 (p. 1348), Section 1.3 — Problem Definition and Objectives.

## 4. Research Questions

- *Not explicitly reported.* The paper follows an applied software engineering and system architecture format rather than formulating explicit research questions.

## 5. Dataset

- **Dataset Name**: Private candidate resumes and job role profiles created within the application.
- **Dataset Source**: Synthetic / user-entered test resumes and job descriptions generated during system evaluation.
- **Institution**: MIT College of Railway Engineering and Research, Barshi, Maharashtra, India.
- **Collection Period**: 2025–2026 testing phase.
- **Dataset Size**: Not quantified with exact sample numbers in the text.
- **Number of Samples**: Not explicitly reported (qualitative UI testing across multiple scenarios).
- **Classes**: Not applicable (system platform implementation).
- **Target Variable**: Candidate performance score, rubric dimension scores, and resume-to-job match percentage.
- **Real / Synthetic**: Synthetic and real test profiles created by authors.
- **Public / Private**: Private / Internal system database.
- **Train/Test Split**: Not applicable (no statistical ML training on static corpora; relies on pre-trained LLM API via zero-shot / prompt orchestration).

### Source Evidence
- PDF p. 1 (p. 1347), Abstract.
- PDF p. 3–5 (pp. 1349–1351), Section I — Results and Discussion.

## 6. Features

Input data handled by the platform components:

### Academic & Education
- Degree, institution, graduation year, academic performance details (PDF p. 3–4, Section 4).

### Skills & Technical
- Technical skills extracted from resumes, programming languages, tools, frameworks (PDF p. 4, Section 4 & 5).

### Resume & Career
- Work experience, project descriptions, resume text, target job role requirements (PDF p. 4, Section 4 & 5).

### Interview & Behavioral
- Textual responses to AI-generated interview questions (PDF p. 1–2).
- Candidate communication indicators, logical reasoning structure, and problem-solving steps (evaluated textually).

### Other / Administrative
- User profile data, interview metadata (date, duration, scores obtained, status) (PDF p. 3–5).

## 7. Data Preprocessing

- **Resume Parsing**: Structured extraction of user input and uploaded resume data into JSON entities (personal info, experience, education, skills, projects) (PDF p. 3–4, Section 4).
- **Resume-to-Job Matching**: Comparison of extracted resume tokens and skills against target job description requirements to calculate match percentages and identify missing skills (PDF p. 4, Section 5).
- **Prompt Engineering**: Dynamic structuring of resume contents and job role descriptions into structured prompts sent to the LLM API for question generation and rubric scoring (PDF p. 1–2).

## 8. Algorithms and Models

- **Large Language Models (LLMs)**: Accessed via the **OpenRouter API** to generate context-specific interview questions and perform rubric-based multi-dimensional scoring (PDF p. 1, Abstract). Specific model family (e.g., GPT-3.5/4, Claude, LLaMA) not specified beyond OpenRouter API routing.
- **ATS Resume Matcher**: Rule-based and keyword/semantic matching engine that computes:
  - Overall match percentage
  - Skill match, experience match, and keyword match
  - Gap analysis highlighting missing competencies (PDF p. 4, Section 5).
- **Relational Data Modeling**: Object-Relational Mapping (ORM) in Node.js connected to PostgreSQL for managing entities, history, and interview records (PDF p. 2, Modeling and Analysis - Model).

### Source Evidence
- PDF p. 1 (p. 1347), Abstract.
- PDF p. 2 (p. 1348), Section I — Modeling and Analysis.
- PDF p. 4 (p. 1350), Section 5 — Resume Matcher Interface.

## 9. Architecture

The system implements a classic **Model-View-Controller (MVC)** web architecture:
- **Frontend / View**: Built with **React**; interactive web application providing client dashboards (user welcome, performance trend charts), resume builder, resume matcher, interview management, and admin oversight interfaces (PDF p. 1, 2, 3; Figures 1–6).
- **Backend / Controller**: Built with **Node.js**; handles API requests, orchestrates business logic, dispatches prompts to the OpenRouter LLM API, and applies rubric evaluation logic (PDF p. 1, 2; Figure 1).
- **Data Layer / Model**: **PostgreSQL** database managed via an ORM to store user credentials, resumes, question sets, completed interview transcripts, and longitudinal score analytics (PDF p. 1, 2; Figure 1).
- **Architecture Diagram**: Figure 1 ("System Architecture") on PDF p. 3 (p. 1349) illustrates the multi-tier data flow between React client, Node.js backend, PostgreSQL, and OpenRouter AI services.

## 10. Methodology

1. **System Requirement & Domain Analysis**: Identifying recruitment bottlenecks and interview prep limitations.
2. **Platform Engineering**: Developing modular micro-tiers (React frontend, Node.js controller, PostgreSQL ORM model).
3. **AI Pipeline Integration**: Connecting OpenRouter API endpoints to dynamically generate questions tailored to candidate resumes and target job profiles.
4. **Rubric-Based Evaluation**: Scoring submitted text responses across three primary dimensions: Technical Proficiency, Communication Skills, and Problem-Solving Ability.
5. **Dashboard & Analytics Implementation**: Building candidate progress tracking and recruiter/admin management portals.
6. **Scenario Testing**: Qualitative validation through trial runs evaluating candidate flow, resume matching, and question relevancy.

## 11. Experimental Setup

- **Frontend Environment**: React web framework (PDF p. 1).
- **Backend Environment**: Node.js runtime environment (PDF p. 1).
- **Database**: PostgreSQL with Object-Relational Mapping (ORM) (PDF p. 1, 2).
- **AI Gateway**: OpenRouter API for Large Language Model invocation (PDF p. 1).
- **Hardware / Server Specifications**: *Not explicitly reported.*
- **Evaluation Methodology**: Qualitative functional validation across operational modules (Resume Builder, Resume Matcher, Interview Management, Admin Portal) (PDF p. 3–5).

## 12. Evaluation Metrics

- **Match Percentage (%)**: Overall match, skill match, experience match, and keyword match between candidate resume and job description (PDF p. 4, Section 5).
- **Multi-Dimensional Interview Scores**: Numerical rubric scores assigned to candidate responses (PDF p. 3–5).
- **Interview Metadata Metrics**: Total interviews completed, average performance score, best score, time spent, and average interview duration (PDF p. 4–5).
- *Statistical ML metrics (Accuracy, F1-score, Precision, Recall, BLEU/ROUGE)*: *Not reported.* The paper is an engineering deployment study without benchmark classification metrics.

## 13. Results

- **System Implementation & Operational Validation**: The platform demonstrated successful functional operation across multiple user and recruiter test scenarios (PDF p. 3, Section I - Results and Discussion):
  - Resume Builder successfully creates, previews, and exports ATS-friendly PDF resumes (PDF p. 4, Figure 4).
  - Resume Matcher successfully outputs percentage breakdown across skills, experience, and keywords alongside gap analysis (PDF p. 4, Figure 5).
  - Interview Management Module successfully records sessions, displays performance trends, and enables users to review feedback or resume incomplete sessions (PDF p. 3–4, Figures 2, 3, 6).
  - Admin Overview Dashboard successfully aggregates total users, active/completed interviews, and average duration (PDF p. 4–5, Figures 7, 8, 9, 10).
- **Quantitative Benchmark Results**: No numerical statistical accuracy benchmarks are reported; evaluation is based on end-to-end software functionality and operational walkthroughs.

## 14. Baselines

- **Traditional Preparation & Recruitment Methods**: Qualitative baseline consisting of generic interview question lists, unassisted human resume review, and manual recruitment screening (PDF p. 1, 2, 5).

## 15. Ablation Study

- *Not reported.*

## 16. Explainability

- **Rubric-Based Feedback**: The platform provides decomposed scoring across technical expertise, communication, and problem-solving, coupled with explicit qualitative strengths and weaknesses (PDF p. 2, 4, 5).
- **Resume Gap Analysis**: Visually highlights specific missing skills and unmatched keywords between the candidate resume and job description (PDF p. 4, Section 5).

## 17. Main Findings

1. A full-stack web application combining React, Node.js, PostgreSQL, and OpenRouter LLM APIs can effectively automate personalized interview question generation and multi-criteria evaluation.
2. Integrating resume parsing with ATS-oriented job matching allows candidates to directly identify skill deficiencies before entering simulated interviews.
3. Centralized admin dashboards provide recruiters with objective visibility into candidate preparation trends and assessment scores.

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Text-Only Evaluation**: The current system relies entirely on text-based interviews and text evaluations, which prevents the assessment of critical non-verbal and vocal communication aspects such as tone, vocal pitch, fluency, and visual confidence (PDF p. 5, Section Discussion).
- **Absence of Multimodal Cues**: Voice and video analysis are currently unaddressed in the deployed system (PDF p. 5, Section Discussion).

### 18.2 Research Interpretation
- **Academic Rigor & Template Artifacts**: The published article contains unedited boilerplate text from the IEEE conference template in the Conclusions section ("The version of this template is V2. Most of the formatting instructions in this document have been compiled by Causal Productions...") and dummy references from 1989–2002 that do not cite contemporary GenAI or interview literature.
- **Absence of Quantitative Evaluation**: The paper presents no empirical sample sizes, benchmark datasets, user study statistics, or validation metrics measuring scoring reliability or question quality.
- **Model Opacity**: The specific LLM backend accessed via OpenRouter is not named or evaluated against alternative foundation models.

## 19. Future Work

1. Integrating voice and audio processing to evaluate vocal tone, fluency, and speech confidence (PDF p. 5, Section Discussion).
2. Incorporating computer vision / video analysis to assess facial expressions, eye contact, and physical interview poise (PDF p. 5, Section Discussion).

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*
- **System Architecture Alignment**: PrepWise illustrates a practical, modular full-stack architecture (React, Node.js, PostgreSQL, LLM API gateway) for placement preparation, closely mirroring ScholarCamp's user-facing portal.
- **ATS and Interview Symbiosis**: Demonstrates how combining an ATS resume matcher with dynamic interview question generation creates a closed-loop readiness workflow where resume gaps directly inform interview questions.
- **Architectural Reference vs. Scientific Rigor**: While offering useful UI/UX workflows, the lack of empirical validation and the presence of template artifacts mean Paper 38 serves as an architectural case study rather than a validated algorithmic benchmark for PRIE.

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|---|---|---|---|
| Generative AI interview platform | PrepWise generates questions and multidimensional rubric scoring via OpenRouter LLM API | PDF p. 1, Abstract; p. 2, Section 1.2 | Methodology |
| Full-stack tech stack | Implemented with React frontend, Node.js backend, and PostgreSQL ORM model | PDF p. 1, Abstract; p. 2, Modeling & Analysis | Methodology |
| Resume matching & gap analysis | Matches resume with JD and outputs percentage match and missing skills | PDF p. 4, Section 5, Figure 5 | Experimental result |
| Admin and candidate dashboards | Centralized monitoring of interviews, average scores, and candidate management | PDF p. 3–5, Figures 2, 7–10 | Experimental result |
| Text-only limitation | System lacks voice and video analysis for assessing tone, confidence, and non-verbal cues | PDF p. 5, Discussion | Author discussion |
| Template boilerplate in paper | Conclusion and references consist of unedited IEEE LaTeX template placeholder text | PDF p. 5–6, Conclusions & References | Direct observation |

## 22. Verification Checklist

- [x] PDF read
- [x] Introduction inspected
- [x] Related work inspected (Note: template references present)
- [x] Methodology inspected
- [x] Dataset verified (Synthetic test profiles; private internal database)
- [x] Features verified
- [x] Algorithms verified (OpenRouter LLM API, ATS matcher, ORM)
- [x] Architecture inspected (Figure 1: React, Node.js, PostgreSQL, OpenRouter)
- [x] Experiments inspected (Functional UI walkthrough)
- [x] Results verified (Qualitative system deployment)
- [x] Limitations verified (Text-only restriction explicitly noted)
- [x] Future work verified (Voice and video analysis)
- [x] Evidence locations recorded

## 23. Verification Status

**PARTIALLY VERIFIED**
*(The software engineering implementation, UI modules, and architectural design are verified from the PDF text and figures; however, the published paper contains unedited IEEE template boilerplate in its conclusion and references, and reports no quantitative empirical evaluation or sample metrics.)*
