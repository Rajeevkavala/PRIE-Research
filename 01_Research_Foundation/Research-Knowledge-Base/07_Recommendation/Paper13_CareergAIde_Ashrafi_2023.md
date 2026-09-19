# Paper 13 — Efficient Resume-Based Re-Education for Career Recommendation in Rapidly Evolving Job Markets (Career-gAIde)

## 1. Bibliographic Information

- **Paper ID**: Paper13
- **Full Title**: Efficient resume based re-education for career recommendation in rapidly evolving job markets
- **Framework Name**: **Career-gAIde**
- **Authors**: Saeed Ashrafi (1), Babak Majidi (1), Ehsan Akhtarkavan (1), and Seyed Hossein Razavi Hajiagha (2)
  - (1) Department of Computer Engineering, Khatam University, Tehran, Iran
  - (2) Department of Management, Khatam University, Tehran, Iran
- **Corresponding Author**: Babak Majidi (`b.majidi@khatam.ac.ir`)
- **Year**: 2023 (Accepted in IEEE Access, 2023; DOI registered)
- **Venue**: IEEE Access, Vol. 11, pp. 1–20 (Author's Accepted Version)
- **DOI**: 10.1109/ACCESS.2023.3329576
- **PDF filename**: `Paper13_zhang2023careergai.pdf`
- **PDF path**: `Papers/PDFs/Paper13_zhang2023careergai.pdf`
- **Page count**: 20 pages

> [!NOTE]
> **Corpus Reconciliation Note**: The legacy BibTeX file (`Paper13_zhang2023careergai.bib`) listed synthetic authors ("Zhang, Yong and Wang, Xiang and Liu, Jian") and venue ("IEEE Transactions on Learning Technologies"). Inspection of the actual PDF confirms the true authors are Saeed Ashrafi, Babak Majidi, Ehsan Akhtarkavan, and Seyed Hossein Razavi Hajiagha from Khatam University, published in IEEE Access (DOI: 10.1109/ACCESS.2023.3329576).

---

## 2. Research Problem

The rapid disruption of global labor markets by pandemic-induced structural shifts and the rise of Generative AI (e.g., GPT-based automation) has caused large-scale, permanent job losses, particularly in low-skilled and routine knowledge roles. Traditional career counseling and static education systems cannot keep pace with rapidly changing workforce demands. To prevent long-term unemployment and support business recovery, there is an urgent need for an automated, intelligent framework capable of parsing individual resumes, recommending viable high-salary career transitions, diagnosing skill deficits, and dynamically generating personalized rapid re-education pathways.

### Source Evidence
- **PDF Page**: Page 1, Abstract & Section I "INTRODUCTION".

---

## 3. Research Objectives

1. Design **Career-gAIde**, an AI-driven framework for large-scale work-skill re-education and career path recommendation.
2. Formulate automated resume processing and skill extraction pipelines using customized Natural Language Processing (NLP).
3. Train Convolutional Neural Network (CNN) architectures (CNN-Random, CNN-Static, CNN-Non-Static) for salary range prediction to guide career upgrades.
4. Implement vector-space similarity metrics (Jaccard and $\phi$ correlation coefficient) to match job opportunities, extract required skills, and diagnose candidate skill deficiencies.
5. Integrate educational resource recommendation (Google Books and Amazon review datasets) to provide concrete learning materials for acquired skill deficits.
6. Empirically benchmark Career-gAIde against state-of-the-art career pathfinding frameworks (CaPaR and ResuMatcher).

### Source Evidence
- **PDF Page**: Page 1, Abstract & pp. 2–3, Section I and Section II.

---

## 4. Research Questions

Not explicitly stated in numbered question syntax; structured around modular architectural goals:
- Can deep convolutional networks accurately predict salary bands from job descriptions?
- How accurately can set-theoretic and statistical correlation metrics ($\phi$ coefficient vs Jaccard) identify required skills and candidate skill deficiencies?
- Does an end-to-end framework integrating salary estimation, skill gap analysis, and educational resource recommendation outperform single-focus baselines like CaPaR?

---

## 5. Dataset

The study incorporates four interconnected datasets:

### 1. Job Opportunity Dataset (Table III & IV)
- **Dataset Name**: Job Opportunity Dataset
- **Number of Samples**: 8,870 job postings
- **Format / Language**: JSON format / English
- **Features Extracted**: Job Title, Job Description (skills, degrees, experience), Job Rate/Salary (hourly, daily, monthly, annual)

### 2. Job Seeker Resume Dataset (Table V)
- **Dataset Name**: Resume Dataset
- **Format**: Real-world job seeker resumes
- **Features Extracted**: Resume Title, Summary (work experience, skills, education)

### 3. Educational Resources Dataset — Google Books (Table VI)
- **Dataset Source**: Google Books API
- **Features Extracted**: `title`, `description`, `authors`, `publisher`, `imUrl` (cover image URL)

### 4. Educational Resources Dataset — Amazon Books (Table VII & VIII)
- **Dataset Source**: Amazon Product & Review Dataset
- **Book Fields**: `asin`, `title`, `description`, `price` (USD), `imUrl`
- **Review Fields**: `reviewerID`, `asin`, `summary`, `overall` (rating score), `helpful` (usefulness score)

### Source Evidence
- **PDF Page**: Pages 6–7, Tables III, IV, V, VI, VII, VIII.

---

## 6. Features

### Job Market & Candidate Features
- **Job Attributes**: Job Title, Required Skills, Degree Requirements, Years of Experience, Salary Rate.
- **Resume Attributes**: Candidate Title, Work Experience Summary, Extracted Skills, Academic Background.
- **Educational Resource Attributes**: Book Title, Technical Description, Publisher, Book Price, User Review Summary, Review Helpfulness Rating.

### Source Evidence
- **PDF Page**: Pages 6–7, Section "DATASET" and Tables IV–VIII.

---

## 7. Data Preprocessing

1. **HTML & URL Sanitization**: Regex filtering of HTML tags, URLs, and non-text artifacts from web-scraped postings.
2. **Tokenization & Case Normalization**: Splitting text into token sequences and converting to uniform lowercase.
3. **Punctuation & Stopword Removal**: Eliminating common English stopwords and non-alphanumeric punctuation.
4. **Stemming**: Applying Porter/Snowball stemmers so morphological variants share identical roots.
5. **Part-of-Speech (POS) Tagging & NER**: Identifying technical competency noun phrases and named entities.
6. **Vocabulary & Embedding Matrix**: Generating word-level feature representations with randomly initialized and pre-trained embedding vectors.

### Source Evidence
- **PDF Page**: Pages 7–8, Section "DATA PREPROCESSING".

---

## 8. Algorithms and Models

### 1. Salary Classification Engine (CNNs)
- **Architecture**: Text-CNN with 1D convolution across text sequences.
- **Variants Evaluated**:
  - **CNN-Random**: Randomly initialized embeddings tuned during training.
  - **CNN-Static**: Pre-trained Word2Vec embeddings kept static.
  - **CNN-Non-Static**: Pre-trained Word2Vec fine-tuned during backpropagation.
- **Hyperparameters**: Filter sizes = 16, 17, 18; Number of filters = 32; Dense layer dimension = 300; Embedding dimension = 100; Epochs = 20.

### 2. Skill Matching & Deficiency Diagnosis
- **Jaccard Similarity Coefficient**: Set intersection over union between candidate skills ($S_{cand}$) and job requirements ($S_{job}$).
- **$\phi$ (Phi) Correlation Coefficient**: Binary contingency correlation metric measuring co-occurrence and divergence of candidate skills against target role profiles.

### 3. Educational Path Recommendation
- Content-based filtering using TF-IDF and review helpfulness weighting applied to Amazon and Google Books corpora.

### Source Evidence
- **PDF Page**: Pages 8–11, Section "MODEL ARCHITECTURE" and Table IX.

---

## 9. Architecture

The Career-gAIde framework comprises five coordinated modules:
1. **Resume Processing & Parsing Module**: Ingests resumes, applies NLP (tokenization, POS, NER), and generates candidate skill profiles.
2. **Salary Predictor & Career Upgrade Module**: CNN-based salary estimation categorizing postings into compensation brackets, ensuring recommended roles represent financial advancement.
3. **Job Recommendation Engine**: Evaluates applicant profile against 8,870 postings via Jaccard and $\phi$ similarity.
4. **Skill Deficiency Diagnostic Module**: Compares candidate skill set against recommended job requirements to identify missing competencies.
5. **Re-Education & Learning Resource Recommender**: Maps missing skills to educational books from Google Books and Amazon, ranking by review ratings and helpfulness.

### Source Evidence
- **PDF Page**: Pages 4–6, Figure 1 (Framework Architecture) and Figure 2.

---

## 10. Methodology

1. **Data Ingestion**: Parsing 8,870 job postings and candidate resumes into structured tabular records.
2. **Text Representation**: Constructing Bag-of-Words (BoW) with stemming and dense embedding matrices.
3. **Salary Model Training**: Training CNN models to classify compensation tiers from job descriptions.
4. **Candidate Job Matching**: Recommending upwardly mobile jobs matching existing candidate qualifications.
5. **Deficiency Diagnosis**: Computing missing skill vectors using $\phi$ correlation and Jaccard metrics.
6. **Courseware Retrieval**: Querying book catalogs for diagnosed skill gaps and ranking candidates by review metrics.
7. **Empirical Benchmarking**: Comparing Career-gAIde against CaPaR and ResuMatcher across precision, recall, and feature completeness.

### Source Evidence
- **PDF Page**: Pages 6–15, Sections III, IV, and V.

---

## 11. Experimental Setup

- **Framework**: Python, PyTorch / TensorFlow for CNN training.
- **Embedding Dim**: 100; Dense Hidden: 300; Filters: 32; Epochs: 20.
- **Evaluation Splits**: Cross-validation on 8,870 job postings.
- **Hardware**: GPU-accelerated computing environment (not further specified).

### Source Evidence
- **PDF Page**: Page 11, Table IX.

---

## 12. Evaluation Metrics

- **Classification Accuracy (%)**: For salary prediction CNNs.
- **Precision**: For job offer recommendation and skill extraction.
- **Recall**: For identifying required skills and diagnosed skill deficits.
- **F1-Score**: Harmonic mean of precision and recall.

### Source Evidence
- **PDF Page**: Page 11, Equation (11) & Tables IX, X, XII, XIII.

---

## 13. Results

### 1. Salary Classification Model Accuracy (Table IX)
- **CNN-Random (BoW with stemming, single-region size 18)**: **70.70%** accuracy (best configuration).
- **CNN-Random (BoW without stemming, single-region)**: **69.67%** accuracy.
- **CNN-Random (Multi-region sizes 16–18, with stemming)**: **66.40%** accuracy.
- **CNN-Random (Multi-region sizes 16–18, without stemming)**: **65.78%** accuracy.

### 2. Job Offer Recommendation (Table X & XI)
- **Career-gAIde ($\phi$ coefficient)**: **Precision = 0.67 (67%)**.
- **Career-gAIde (Jaccard similarity)**: **Precision = 0.65 (65%)**.
- *Comparison with CaPaR*: CaPaR achieved 0.73 precision on IT-only roles, but Career-gAIde accommodates multi-domain roles, salary constraints, and experience levels.

### 3. Job Skill Requirement Extraction (Table XII)
- **$\phi$ coefficient**: **Precision = 0.82**, **Recall = 0.84**, **F1-Score = 0.83**.
- **Jaccard similarity**: **Precision = 0.79**, **Recall = 0.81**, **F1-Score = 0.80**.

### 4. Diagnosis of Skill Deficiencies (Table XIII & XIV)
- **$\phi$ coefficient**: **Precision = 0.77**, **Recall = 0.79**, **F1-Score = 0.78**.
- **Jaccard similarity**: **Precision = 0.74**, **Recall = 0.76**, **F1-Score = 0.75**.
- **Benchmarking vs CaPaR (Table XIV)**:
  - **Career-gAIde Recall**: **0.79 (79%)**
  - **CaPaR Recall**: **0.65 (65%)**
  - *Improvement*: Career-gAIde exhibits a **+14 percentage point gain** in detecting missing skills over CaPaR.

### 5. Architectural Comparison (Table XV)
Career-gAIde uniquely supports multi-domain coverage, salary estimation, required skill recommendation, skill deficiency diagnosis, and personalized learning path recommendation simultaneously.

### Source Evidence
- **PDF Page**: Pages 11–14, Tables IX, X, XI, XII, XIII, XIV, XV.

---

## 14. Baselines

1. **CaPaR System (Career Pathfinder)**: Resume-based job and skill recommendation system (achieved 0.65 recall on skill deficiency vs 0.79 for Career-gAIde).
2. **ResuMatcher**: Information retrieval-based resume matching system utilizing TF-IDF and ontology matching.

### Source Evidence
- **PDF Page**: Pages 12–14, Tables XI, XIV, XV.

---

## 15. Ablation Study

Reported in Table IX through systematic ablation of:
- Embedding initialization (Random vs Static vs Non-Static).
- Stemming (BoW with stemming vs BoW raw).
- Filter region structures (single region size 18 vs multi-region sizes 16–18).
*Finding*: Single-region CNN with stemmed BoW and randomly initialized embeddings yielded highest salary accuracy (70.70%).

### Source Evidence
- **PDF Page**: Page 11, Table IX.

---

## 16. Explainability

The framework achieves operational explainability through its transparent deficiency diagnostic: rather than recommending a job as an opaque score, it explicitly outputs the $\phi$ contingency matrix showing which specific competencies the candidate lacks and links them directly to educational resources.

### Source Evidence
- **PDF Page**: Pages 12–13, Section "Evaluation of the diagnosis of skill deficiencies".

---

## 17. Main Findings

1. Deep CNNs can classify salary ranges from unstructured job descriptions with ~71% accuracy, allowing recommender systems to target career advancement.
2. The $\phi$ correlation coefficient consistently outperforms Jaccard similarity across precision, recall, and F1 in both skill requirement extraction (F1: 0.83 vs 0.80) and skill gap diagnosis (F1: 0.78 vs 0.75).
3. In diagnosing skill deficiencies, Career-gAIde significantly outperforms CaPaR (Recall: 79% vs 65%).
4. Coupling skill gap identification with concrete learning materials (e.g., book catalog retrieval) closes the loop from candidate assessment to actionable remediation.

### Source Evidence
- **PDF Page**: Page 1, Abstract; pp. 11–14, Tables IX–XIV; p. 15, Section V "CONCLUSION".

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Job Scope Focus**: Primarily tested and validated on software engineering and IT job markets.
- **Resource Modality**: Educational resource recommendation currently restricted to books (Google Books, Amazon) rather than multimedia or interactive online courses.
- **Computational Overhead**: Training deep neural networks for large-scale multi-class salary classification requires substantial compute.

### 18.2 Research Interpretation
- Salary classification accuracy capped at 70.70%, indicating that salary is influenced by external variables (location, equity, undisclosed perks) not fully captured in job descriptions.
- The evaluation of candidate satisfaction with recommended educational books is based on historical ratings rather than longitudinal pre/post intervention testing.

---

## 19. Future Work

Explicitly proposed by authors:
1. Extending the framework to non-technical, multi-disciplinary job markets.
2. Integrating online video courses, MOOC platforms (Coursera, edX), and interactive coding tutorials into the educational recommendation engine.
3. Incorporating Transformer-based foundational language models (e.g., modern BERT/GPT architectures) to enhance semantic nuance in job descriptions.

### Source Evidence
- **PDF Page**: Page 15, Section V "CONCLUSION".

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

- **Relevant Module**: **PRIE Learning Pathway Recommendation & Upskilling Engine (Module 07)**.
- **Direct Theoretical Contribution**: The $\phi$-coefficient skill deficiency diagnosis formula and multi-tier matching pipeline directly inform PRIE's skill gap remediation module.
- **Novel Integration Opportunity**: ScholarCamp extends Career-gAIde by replacing static book recommendations with dynamic, multi-modal micro-learning paths and hands-on coding challenges.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Best salary classification accuracy = 70.70% | CNN-Random, BoW + stemming, filter size 18 | PDF p. 11, Table IX | Experimental result |
| Skill deficiency diagnosis recall = 0.79 | $\phi$ coefficient achieves Recall=0.79, Prec=0.77 | PDF p. 13, Table XIII | Experimental result |
| Career-gAIde outperforms CaPaR by 14% recall | 0.79 (Career-gAIde) vs 0.65 (CaPaR) | PDF p. 13, Table XIV | Experimental result |
| Job offer recommendation precision = 0.67 | $\phi$ coefficient precision = 0.67, Jaccard = 0.65 | PDF p. 12, Table X | Experimental result |
| Dataset规模: 8,870 job postings | JSON format, English language specifications | PDF p. 6, Table III | Dataset |

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

**VERIFIED** (Primary PDF read, exact experimental numbers verified across Tables IX–XV, author correction from legacy BibTeX documented).
