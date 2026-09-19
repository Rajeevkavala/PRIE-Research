# Paper 28 — Smart AI Interviewer and Resume Analyzer (IndusAI)

## 1. Bibliographic Information

- **Paper ID**: Paper28
- **Full Title**: Smart AI Interviewer and Resume Analyzer
- **Authors**: Pooja Vachkal (Dept. of Computer Engg.), Vishal Chole, Gaurav Padol, Samarth Kawane, and Omkar Kasar
- **Institution**: Department of Computer Engineering, Jayawantrao Sawant College of Engineering (JSCOE), Hadapsar, Pune (Savitribai Phule Pune University), India
- **Year**: June 2026
- **Venue**: International Journal of Engineering Research & Technology (IJERT), Vol. 15, Issue 06, June 2026, pp. 1–4
- **ISSN**: 2278-0181 (Article ID: IJERTV15IS060994)
- **DOI**: Available via IJERT (https://www.ijert.org/)
- **PDF filename**: `Paper28_gupta2025indusai.pdf` (Note: filename reflects legacy bibtex tag `gupta2025indusai`; authentic PDF confirms authors Pooja Vachkal, Vishal Chole, Gaurav Padol, Samarth Kawane, and Omkar Kasar, IndusAI, IJERT June 2026)
- **PDF path**: `Papers/PDFs/Paper28_gupta2025indusai.pdf`
- **Page count**: 4 pages (pp. 1–4)

---

## 2. Research Problem

In increasingly competitive technical job markets, candidates face two major hurdles: (1) exiting employment interviews without objective, actionable feedback regarding their verbal fluency, acoustic prosody, answer relevance, and body language; and (2) having resumes silently rejected by Applicant Tracking Systems (ATS) due to formatting flaws or keyword misalignment before a human recruiter ever evaluates them.

### Source Evidence
- **Page**: PDF p. 1
- **Section**: Section I — Introduction

---

## 3. Research Objectives

The authors explicitly define their objectives:
1. To develop and deploy **IndusAI**, a unified web-based multimodal interview coaching and resume analysis system.
2. To extract and integrate speech transcripts, acoustic prosodic vectors, semantic content relevance, non-verbal posture/gaze metrics, and ATS keyword compliance into a single quantified **Confidence Score**.
3. To synthesize automated, downloadable PDF performance reports containing section radar charts and targeted improvement guidance for candidates.

### Source Evidence
- **Page**: PDF p. 1
- **Section**: Abstract & Section I

---

## 4. Research Questions

- *Not explicitly reported* (The paper presents an applied systems engineering architecture and workflow demonstration rather than numbered theoretical hypotheses).

---

## 5. Dataset

The system was evaluated as an integrated software artifact:
- **Corpus / Test Samples**: Tested across a diverse internal benchmark of candidate interview audio-video recordings (MP4, WebM, WAV, MP3) and resumes (PDF and DOCX formats).
- **Target Vocabulary**: Configurable job description keyword sets representing industry technical roles (e.g., Software Engineering, Data Science).
- **Acoustic / Speech Pretraining Corpora**: Whisper pre-trained on 680,000 hours of multilingual speech data; openSMILE baseline feature sets; Sentence-BERT pre-trained embeddings.
- **Availability**: Applied institutional engineering project developed at JSCOE, Savitribai Phule Pune University.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section II, Section III.A, Section VI

---

## 6. Features

The platform extracts five distinct feature categories:

### Speech & Acoustic Features
- **384-dimensional prosodic/spectral feature vector** via openSMILE (pitch variance, fundamental frequency contour, energy dynamics, tempo).
- **Filler-word density** (frequency of "um", "uh", "like") derived from Whisper word-level timestamps.
- **Speech rate**: Syllables-per-second rate.

### Semantic & Linguistic Features
- **Sentence-BERT dense embeddings**: Cosine similarity between candidate response vectors and domain expert reference answers.
- **BERT sentiment polarity & grammatical quality score**.

### Non-Verbal Behavioral Features (Optional Video Stream)
- **Gaze vectors & eye-contact ratio**: Extracted via MediaPipe Face Mesh.
- **Postural stability index & head pose**: Derived from MediaPipe Pose upper-body keypoints.

### Resume ATS Features
- **Keyword coverage ratio**: Proportion of target job-description tokens matched in resume body tokens.
- **Formatting compliance index**: Document structural integrity (heading labels, section hierarchy, font readability).

### Source Evidence
- **Page**: PDF p. 2
- **Section**: Section III (Subsections B, C, D, E)

---

## 7. Data Preprocessing

The ingestion pipeline executes multi-stream data preprocessing:
- **Audio Extraction**: FFmpeg asynchronously extracts raw WAV audio from video containers (MP4, WebM).
- **Document Text Extraction**: Resume parser strips formatting and extracts clean token lists and heading hierarchies from PDF/DOCX files.
- **Normalization**: Min-max normalization scaling all feature sub-scores into the continuous range $[0, 1]$.
- **Penalties Computation**: Calculation of deduction penalties ($P$) for excessive disfluency, severe gaze avoidance, or ATS structural violations.

### Source Evidence
- **Page**: PDF p. 2
- **Section**: Section III.F & Section IV.B

---

## 8. Algorithms and Models

IndusAI coordinates several machine learning and deep learning models across its analytics layer:
1. **Speech Recognition**: **OpenAI Whisper ASR** for automatic speech-to-text with word-level timestamps.
2. **Acoustic Modeling**: **openSMILE** extracting 384 acoustic and spectral features.
3. **Semantic Relevance**: **Sentence-BERT (SBERT)** using Siamese/triplet networks for sentence embedding cosine similarity against reference solutions.
4. **Sentiment / Quality**: Fine-tuned **BERT** for response sentiment polarity and grammatical fluency.
5. **Computer Vision / Pose**: **MediaPipe Face Mesh** and **MediaPipe Pose** for real-time facial landmark tracking, gaze orientation, and upper-body posture analysis.
6. **Composite Scoring Function**:
   $$C = 100 \times (w_1 S_v + w_2 S_f + w_3 S_c + w_4 S_{nv} - P)$$
   where $S_v$ = voice sub-score, $S_f$ = fluency/prosody, $S_c$ = content relevance, $S_{nv}$ = non-verbal behavior, $\sum w_i = 1$, and $P$ = penalty term.
   - Categorical thresholds:
     - **Highly Competent**: $C \ge 75$
     - **Satisfactory**: $50 \le C < 75$
     - **Requires Development**: $C < 50$

### Source Evidence
- **Page**: PDF p. 2
- **Section**: Section III.B, C, D, F

---

## 9. Architecture

The system is organized into a six-layer, loosely coupled modular architecture (Section IV):
1. **User Interface Layer**: Responsive web dashboard for file uploads, historical session tracking, and inline score visualizations.
2. **Media Ingestion Layer**: Asynchronous file validator and FFmpeg audio demuxer.
3. **Multimodal Analytics Layer**: Four concurrent workers (Whisper, openSMILE, BERT/SBERT, MediaPipe).
4. **Confidence Scoring Layer**: Weight matrix aggregator applying deduction penalties and outputting the scalar Confidence Score.
5. **Report Synthesis Layer**: Automated PDF template engine compiling radar charts, resume gaps, and actionable text recommendations.
6. **Extensibility & Scaling Layer**: Containerized stateless microservices prepared for horizontal cloud scaling.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section IV (Subsections A–F)

---

## 10. Methodology

1. **Candidate Ingestion**: User uploads resume (PDF/DOCX) and records/uploads an interview video session.
2. **Asynchronous Parallel Processing**: Audio is demuxed; speech, semantic content, facial gaze, and resume ATS compatibility are processed by independent analytics workers.
3. **Multi-Criteria Fusion**: Feature sub-scores are normalized and aggregated into the composite Confidence Score ($C$).
4. **Actionable Report Delivery**: Automated PDF rendering presents performance breakdown radar charts, flagged filler words, eye-contact percentages, and resume keyword recommendations.
5. **Functional Validation**: End-to-end testing verifying pipeline latency, interface responsiveness, and report generation accuracy.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section III & Section VI

---

## 11. Experimental Setup

- **Platform**: Web application deployed with Python microservices, FFmpeg media processing, and container orchestration.
- **Libraries / Frameworks**: PyTorch, Transformers (Hugging Face BERT / Sentence-BERT), OpenAI Whisper, openSMILE, Google MediaPipe, ReportLab / PDF template renderer.
- **Hardware / Deployment**: Cloud virtual server running containerized stateless analytics workers.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section III & Section IV

---

## 12. Evaluation Metrics

1. **Confidence Score ($C$)**: Continuous composite score on a $0–100$ scale.
2. **Competency Classification**: 3-class rating (Highly Competent, Satisfactory, Requires Development).
3. **Acoustic Sub-Scores**: Pitch variance, energy contour, speaking tempo, and syllables/second rate.
4. **Speech Fluency**: Filler-word density count.
5. **Semantic Similarity**: Cosine similarity score between candidate response and target answer vector.
6. **Visual Gaze Ratio**: Percentage of interview duration maintaining direct eye contact.
7. **Resume ATS Match Rate**: Percentage overlap of target job description keywords.

### Source Evidence
- **Page**: PDF p. 2
- **Section**: Section III.F

---

## 13. Results

### System Verification & Usability (Section VI)
- **Functional Validation**: Verified complete end-to-end execution of the four automated processing stages (audio extraction, Whisper speech-to-text, NLP keyword analysis, and question scoring).
- **Operational Interface**: Successfully deployed live UI workflows for file ingestion, real-time expression tracking, AI question presentation, and PDF report compilation (Figures 1 and 2).
- **Comparative Analysis (Table I)**:
  - *Conventional human mock interviews*: Costly, subjective, appointment-bounded, lack acoustic and ATS analysis.
  - *IndusAI*: 24/7 on-demand web access, automated Whisper + openSMILE acoustic scoring, MediaPipe gaze tracking, ATS simulation, and structured downloadable PDF reports.

### Source Evidence
- **Page**: PDF p. 3
- **Table / Figures**: Table I, Figure 1, Figure 2, Section VI text

---

## 14. Baselines

The authors explicitly benchmark IndusAI against traditional career preparation approaches in **Table I**:
1. **Conventional Human Coaching**: Human evaluators conducting manual mock interviews and recruiter resume reviews.
2. **Single-Modality Prep Apps**: Mobile apps restricted to voice recording or simple flashcard questions without multimodal fusion.

### Source Evidence
- **Page**: PDF p. 3
- **Table**: Table I ("Comparative Assessment: Conventional Methods vs. IndusAI")

---

## 15. Ablation Study

- *Not reported* (The paper presents an applied architectural framework rather than an empirical ablation of individual model weights).

---

## 16. Explainability

- **Diagnostic Visual Reports**: Rather than outputting an opaque score, the report synthesis layer visualizes performance along multi-axis radar charts (speech fluency, content depth, non-verbal confidence, resume ATS match).
- **Granular Error Attribution**: Highlights exact filler-word locations via Whisper timestamps and lists unfulfilled target keywords from the resume analysis.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section III.E & Section IV.E

---

## 17. Main Findings

1. Fusing speech recognition (Whisper), acoustic prosody (openSMILE), semantic matching (Sentence-BERT), vision tracking (MediaPipe), and ATS resume parsing inside a single web platform enables a comprehensive, objective assessment of job readiness.
2. Word-level timestamping from Whisper allows precise automated quantification of filler words without requiring human transcription.
3. Combining interview simulation and ATS resume evaluation in one workflow provides candidates with a cohesive roadmap for both securing interview shortlists and clearing subsequent interviews.

### Source Evidence
- **Page**: PDF pp. 2–4
- **Section**: Section III, Section V, Section VII

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
1. **English Language Restriction**: Models currently operate solely on English speech and English resumes.
2. **Static Reference Answers**: Content scoring relies on pre-configured reference answers rather than open-ended dynamic dialogue reasoning.
3. **Absence of Live Job Portal Sync**: Keyword matching is based on static uploaded job descriptions rather than real-time job board API telemetry.

### 18.2 Research Interpretation
- *Research interpretation — not stated by the original authors*: The paper focuses on system architecture and qualitative pipeline demonstration; it does not report formal machine learning accuracy benchmarks (e.g., ASR word error rate, classifier F1-scores) or large-cohort statistical validation.

### Source Evidence
- **Page**: PDF pp. 3–4
- **Section**: Section IV.F & Section VII

---

## 19. Future Work

Explicitly proposed by the authors:
1. Developing adaptive interview question generation personalized to candidate performance trajectories.
2. Multilingual resume parsing and acoustic analysis for non-English job markets.
3. Live job-portal API integration for dynamic keyword benchmarking.
4. Institutional analytics dashboard enabling placement officers to monitor cohort-level readiness trends across graduating batches.

### Source Evidence
- **Page**: PDF pp. 3–4
- **Section**: Section IV.F & Section VII

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

IndusAI serves as an immediate reference architecture for the integration of PRIE's **Mock Interview** and **ATS Resume Screening** engines:
1. **Dual-Pillar Integration (Resume + Interview)**: IndusAI provides an empirical precedent for evaluating resume ATS compatibility and interview performance within a single student profile, directly matching ScholarCamp's unified ecosystem.
2. **Technical Pipeline Reuse**: PRIE can adopt IndusAI's exact open-source stack: Whisper for word-level disfluency extraction, openSMILE for acoustic prosody, Sentence-BERT for semantic relevance, and MediaPipe for gaze and posture monitoring.
3. **Cohort-Level Institutional Analytics**: IndusAI's proposed future institutional dashboard mirrors PRIE's placement coordinator analytics module for monitoring department-wide placement readiness.

---

## 21. Evidence Table

| Finding / Fact | Evidence Statement from PDF | Source Location | Evidence Type |
|---|---|---|---|
| **System Overview** | "IndusAI, a web-based intelligent coaching system that automatically assesses interview performance through multimodal analysis of speech, language, and non-verbal behavior." | PDF p. 1, Abstract | Direct statement |
| **Acoustic & Speech Stack** | Whisper ASR for transcript with timestamps; openSMILE for 384-dimensional prosodic/spectral feature vector. | PDF p. 2, Section III.B | Methodology |
| **Semantic Matching** | Sentence-BERT encodes candidate and reference responses; cosine distance measures semantic relevance. | PDF p. 2, Section III.C | Methodology |
| **Non-Verbal Computer Vision** | MediaPipe face mesh and pose models extract gaze vectors and upper-body keypoints. | PDF p. 2, Section III.D | Methodology |
| **Scoring Formula** | $C = 100 \times (w_1 S_v + w_2 S_f + w_3 S_c + w_4 S_{nv} - P)$; thresholds at 75 and 50. | PDF p. 2, Section III.F | Formula / Result |
| **Conventional vs IndusAI** | Table I benchmarks conventional human coaching vs IndusAI 24/7 on-demand web architecture. | PDF p. 3, Table I | Table / Comparison |

---

## 22. Verification Checklist

- [x] PDF read (`Paper28_gupta2025indusai.pdf`, 4 pages)
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected (6-stage pipeline: ingestion, speech, semantics, vision, ATS, scoring)
- [x] Dataset verified (Multimodal interview media benchmark, resumes in PDF/DOCX)
- [x] Features verified (384 acoustic features, filler density, SBERT embeddings, MediaPipe gaze, ATS keywords)
- [x] Algorithms verified (Whisper, openSMILE, BERT, Sentence-BERT, MediaPipe)
- [x] Architecture inspected (6-layer architecture described in Section IV)
- [x] Experiments inspected (Operational verification, Figures 1 & 2, Table I)
- [x] Results verified (Formula $C$, threshold classifications 75/50, automated PDF report)
- [x] Limitations verified (English restriction, static reference answers, no live API sync)
- [x] Future work verified (Adaptive questions, multilingual parsing, cohort analytics)
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read in full; exact multi-stage pipeline, scoring formula from Section III.F, 6-layer architecture from Section IV, and Table I comparison verified directly from source text; legacy filename discrepancy documented).
