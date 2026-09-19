# Paper 17 — ResuMatch: Resume Screening System Using AI

## 1. Bibliographic Information

- **Paper ID**: Paper17
- **Full Title**: ResuMatch: Resume Screening System Using AI
- **Authors**: Kumkum Solanki (1), Aditya Dorwal (2), Piyush Rai (3), Arpit Awasthi (4), and Mohammad Haris (5)
  - (1,2,3,4) Undergraduate Students, Department of Computer Science and Engineering, KCC Institute of Technology and Management, Greater Noida, India
  - (5) Assistant Professor, Department of Computer Science and Engineering, KCC Institute of Technology and Management, Greater Noida, India
- **Year**: 2026 (Published: January 2026)
- **Venue**: International Journal of Creative Research Thoughts (IJCRT), Vol. 14, Issue 1, pp. d736–d743
- **ISSN**: 2320-2882
- **Article ID**: IJCRT2601457
- **PDF filename**: `Paper17_verma2026resumatch.pdf`
- **PDF path**: `Papers/PDFs/Paper17_verma2026resumatch.pdf`
- **Page count**: 8 pages (pp. d736–d743)

> [!NOTE]
> **Corpus Reconciliation Note**: The legacy BibTeX file (`Paper17_verma2026resumatch.bib`) listed synthetic authors ("Verma, Sanjay and Mehta, Alok") and title modifier ("Resume Screening System Using AI and Dense Semantic Representations"). Inspection of the actual PDF confirms the true authors are Kumkum Solanki, Aditya Dorwal, Piyush Rai, Arpit Awasthi, and Mohammad Haris from KCC Institute of Technology and Management.

---

## 2. Research Problem

Applicant Tracking Systems (ATS) deployed by modern employers automatically filter out high proportions of qualified applicants who fail exact keyword matching or standard layout parsing. Job seekers face three primary hurdles:
1. Resumes lack strategic alignment with specific target job descriptions, causing automated ATS rejection.
2. Candidates cannot identify their exact skill deficits or missing keywords before applying.
3. Resumes often suffer from poor grammar, spelling errors, and formatting inconsistencies that diminish professional appeal during human review.

### Source Evidence
- **PDF Page**: Page 1 (p. d736), Abstract & Page 2 (p. d737), Section II "MOTIVATION".

---

## 3. Research Objectives

1. Develop **ResuMatch**, an integrated web-based platform for resume screening, ATS optimization, and candidate upskilling.
2. Implement automated document parsing to extract structured candidate entities (skills, education, work experience) from unstructured resumes.
3. Compute an objective **ATS Compatibility Score** using TF-IDF vectorization and cosine similarity against target job descriptions.
4. Design a skill gap analysis engine that surfaces missing domain keywords and recommends targeted online courses, project ideas, and alternative job roles.
5. Integrate automated grammatical and spelling error correction to refine document presentation.

### Source Evidence
- **PDF Page**: Page 1 (p. d736), Abstract & Page 2 (p. d737), Section III "OBJECTIVE".

---

## 4. Research Questions

Not explicitly formulated in question syntax. The study is structured around software engineering milestones, NLP pipeline design, and user dashboard integration.

---

## 5. Dataset

As an applied software engineering and system implementation paper, no public standalone benchmark dataset was released:
- **Input Corpus**: User-uploaded resumes (PDF/DOCX) paired with user-pasted job descriptions from recruitment portals.
- **Domain Coverage**: Software engineering, technical roles, and general professional domains.
- **Sample Count**: Not quantitatively reported in benchmark numbers.

### Source Evidence
- **PDF Page**: Page 4 (p. d739), Section VII & Page 6 (p. d741), Section IX "IMPLEMENTATION & RESULT".

---

## 6. Features

The system extracts and transforms several key resume and job description features:

### Candidate Attributes
- **Technical Skills**: Extracted programming languages, frameworks, developer tools, and libraries.
- **Soft Skills**: Communication, leadership, and collaboration descriptors.
- **Academic Qualifications**: Degree title, institutional affiliation, and completion dates.
- **Professional Experience**: Past job roles, company names, tenure, and bulleted project accomplishments.
- **Linguistic Markers**: Spelling accuracy, grammatical structure, and syntax.

### Job Description Attributes
- Core required competencies and prerequisite toolkits.
- Educational credentials and minimum experience thresholds.

### Source Evidence
- **PDF Page**: Page 4 (p. d739), Section VII & Page 5 (p. d740), Section VIII.

---

## 7. Data Preprocessing

1. **Text Normalization**: Stripping punctuation, whitespace normalization, and case standardization (lowercasing).
2. **Tokenization & Stopword Filtering**: Segmenting text into lexical tokens and removing non-discriminative stopwords via NLTK.
3. **Lemmatization**: Reducing words to base lemma forms using spaCy lemmatizers.
4. **Keyword Vectorization**: Transforming cleaned text into sparse numerical vectors via TF-IDF (Term Frequency-Inverse Document Frequency) and dense word embeddings.

### Source Evidence
- **PDF Page**: Page 4 (p. d739), Section VII & Page 6 (p. d741), Section IX.

---

## 8. Algorithms and Models

- **Information Extraction**: `spaCy` NLP pipeline for entity extraction and rule-based keyword matching.
- **Vector Space Representation**: `scikit-learn` `TfidfVectorizer` and dense word embeddings.
- **Similarity & Scoring Engine**: **Cosine Similarity** measuring angular distance between candidate resume vector $\vec{R}$ and job description vector $\vec{J}$:
  $$\text{ATS Score} = \cos(\vec{R}, \vec{J}) \times 100$$
- **Gap Detection & Recommender**: Rule-based set divergence identifying missing keywords, triggering curated mappings to project prompts, courses, and role pathways.
- **Linguistic Correction**: NLP spell-checking and grammar-correction heuristics.

### Source Evidence
- **PDF Page**: Page 4 (p. d739), Section VII; Page 6 (p. d741), Section IX.

---

## 9. Architecture

The ResuMatch architecture consists of four layered components (Figure 4, PDF p. 6):
1. **User Interface Layer**: Web browser dashboard allowing interactive upload of resumes and pasting of job descriptions.
2. **Parsing & Preprocessing Engine**: Ingests files, cleans text, and segments sections (education, skills, experience).
3. **Analytics & Computation Layer**:
   - TF-IDF / Embedding Vectorizer.
   - Cosine Similarity ATS scoring calculator.
   - Skill Gap Detector comparing resume tokens against job requirements.
   - Spelling and grammar analysis module.
4. **Recommendation & Presentation Layer**: Renders real-time ATS match percentage, lists of missing competencies, project recommendations, and suggested online courses.

### Source Evidence
- **PDF Page**: Pages 4–6 (pp. d739–d741), Figures 2, 3, and 4.

---

## 10. Methodology

1. **User Submission**: User inputs resume and target job description via web UI.
2. **Preprocessing**: Document cleaning, tokenization, stopword removal, and lemmatization.
3. **Feature Extraction**: Identifying technical skills, credentials, and experience.
4. **Vector Transformation**: Computing TF-IDF matrices across documents.
5. **Score Generation**: Calculating cosine similarity to determine ATS compatibility percentage.
6. **Gap Analysis & Guidance**: Identifying missing required keywords; recommending relevant project ideas and online learning resources.
7. **Linguistic Refinement**: Flagging grammatical and spelling errors for candidate correction.
8. **Dashboard Visualization**: Displaying the consolidated readiness report on the UI.

### Source Evidence
- **PDF Page**: Pages 4–5 (pp. d739–d740), Section VII & Section VIII.

---

## 11. Experimental Setup

- **Language & Platform**: Python, web application framework.
- **NLP & ML Libraries**: `NLTK`, `spaCy`, `scikit-learn`.
- **Vectorization**: TF-IDF and word embeddings.
- **Deployment**: Web-based candidate dashboard.

### Source Evidence
- **PDF Page**: Page 6 (p. d741), Section IX "IMPLEMENTATION & RESULT".

---

## 12. Evaluation Metrics

Evaluated operationally through functional system verification:
- **ATS Compatibility Score**: Normalized similarity percentage (0–100%).
- **Skill Gap Detection Coverage**: Ability to flag missing keywords present in job description.
- **Linguistic Error Rate**: Detection of spelling and grammatical inaccuracies.
- **System Responsiveness**: Fast turnaround time for real-time candidate feedback.

### Source Evidence
- **PDF Page**: Page 6 (p. d741), Section IX.

---

## 13. Results

- **System Implementation**: Successfully deployed an interactive web portal where candidates receive instant ATS match percentages, granular skill gap breakdowns, and personalized course/project recommendations.
- **Linguistic Polish**: Automated spell/grammar checks improved resume readability and professional tone prior to human recruiter inspection.
- *Notice*: Specific multi-class confusion matrices, precision/recall curves, or numerical benchmarking tables across test datasets are **not reported** in this applied engineering paper.

### Source Evidence
- **PDF Page**: Pages 6–7 (pp. d741–d742), Figures 5 & 6, Section IX & Section X.

---

## 14. Baselines

- **Commercial ATS Systems**: Opaque black-box enterprise applicant tracking systems that reject resumes without feedback.
- **Manual Proofreading**: Traditional self-editing or peer review of resumes.

### Source Evidence
- **PDF Page**: Page 2 (p. d737), Section II.

---

## 15. Ablation Study

Not reported.

---

## 16. Explainability

High operational explainability: Rather than treating the ATS score as an uninterpretable number, ResuMatch explicitly itemizes matched keywords, highlights missing technical terms, and provides clear, prescriptive upskilling recommendations.

### Source Evidence
- **PDF Page**: Page 5 (p. d740), Section VIII & Page 7 (p. d742), Figure 6.

---

## 17. Main Findings

1. Pairing TF-IDF cosine similarity scoring with an explicit missing-keyword diagnostic empowers students to optimize resumes proactively before submitting them to corporate ATS gateways.
2. Integrating language correction (spelling/grammar) alongside technical skill matching provides a more complete resume preparation experience.
3. Modular Python-based web architectures (NLTK, spaCy, scikit-learn) offer an effective, lightweight foundation for university-level placement screening tools.

### Source Evidence
- **PDF Page**: Page 7 (p. d742), Section X "CONCLUSION".

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Superficial Semantic Understanding**: Keyword-driven and TF-IDF methods risk penalizing candidates who describe competencies using valid synonyms not verbatim in the job posting.
- **Recruiter Feedback Absence**: The platform currently lacks a direct recruiter portal for feedback verification.
- **Static Upskilling Catalog**: Course and project recommendations are driven by predefined rule mappings rather than dynamic web scraping.

### 18.2 Research Interpretation
- The authors do not provide quantitative empirical performance metrics (e.g., precision, recall, or user test accuracy percentages) on a benchmark corpus.
- The system relies on classical bag-of-words / TF-IDF representations rather than contextual bi-encoders (e.g., Sentence-BERT).

---

## 19. Future Work

Explicitly proposed by authors:
1. Integration of advanced deep learning transformer models (e.g., BERT/RoBERTa) for contextual and semantic understanding.
2. Incorporating recruiter feedback loops and continuous profile tracking.
3. Expanding system functionality to include AI interview preparation support.
4. Real-time market analytics to dynamically update skill importance weights.

### Source Evidence
- **PDF Page**: Page 7 (p. d742), Section X "CONCLUSION".

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

- **Relevant Module**: **PRIE ATS & Resume Analysis Engine (Module 04)**.
- **Direct Alignment**: ResuMatch's three-part diagnostic (ATS Compatibility Score + Skill Gap Identification + Project/Course Remediation) mirrors the functional blueprint of ScholarCamp's resume module.
- **PRIE Architectural Extension**: ScholarCamp directly solves ResuMatch's acknowledged limitation by replacing TF-IDF with fine-tuned Sentence-BERT dense embeddings, allowing semantic matching that recognizes technical synonyms without requiring rigid verbatim keyword stuffing.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| TF-IDF and cosine similarity for ATS scoring | Implementation details | PDF p. 6, Section IX | Methodology |
| spaCy and NLTK pipeline for parsing | Library usage description | PDF p. 6, Section IX | Experimental setup |
| Tripartite workflow (ATS + Gap + Remediation) | Workflow diagram and text | PDF pp. 4–5, Figs. 2 & 3 | Architecture |
| Limitation: keyword matching lacks semantic nuance | Discussion of TF-IDF constraints | PDF p. 7, Section X | Author discussion |
| Future integration of BERT and transformer models | Explicit future roadmap | PDF p. 7, Section X | Future work |

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

**PARTIALLY VERIFIED** (Primary PDF read, architecture and technical stack verified; absence of empirical precision/recall benchmark numbers documented).
