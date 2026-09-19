# Paper 29 — AI Mock Interview: An Intelligent Voice-Driven Interview Simulation System using Gemini AI and Whisper

## 1. Bibliographic Information

- **Paper ID**: Paper29
- **Full Title**: AI Mock Interview: An Intelligent Voice-Driven Interview Simulation System using Gemini AI and Whisper
- **Authors**: Abdul Wahid, Aditya Jha, Meerhan Munshi, Sumit Sonwane, and Prof. Amit Chakrawarti (Head of Department, AIML)
- **Institution**: Department of Artificial Intelligence & Machine Learning, Dilkap Research Institute of Engineering and Management Studies (Affiliated with University of Mumbai), Village Mamdapur, Post-Neral, Tal: Karjat, Maharashtra, India - 410101
- **Year**: March 2026
- **Venue**: International Journal of Engineering Research & Technology (IJERT), Vol. 15, Issue 03, March 2026, pp. 1–4
- **ISSN**: 2278-0181 (Article ID: IJERTV15IS031282)
- **DOI**: Available via IJERT (https://www.ijert.org/)
- **PDF filename**: `Paper29_srinivasan2025aimock.pdf` (Note: filename reflects legacy bibtex tag `srinivasan2025aimock`; authentic PDF confirms authors Abdul Wahid, Aditya Jha, Meerhan Munshi, Sumit Sonwane, and Prof. Amit Chakrawarti, IJERT March 2026)
- **PDF path**: `Papers/PDFs/Paper29_srinivasan2025aimock.pdf`
- **Page count**: 4 pages (pp. 1–4)

---

## 2. Research Problem

Technical interview preparation for engineering students and early-career job seekers remains fragmented: coding platforms (e.g., LeetCode, HackerRank) evaluate algorithmic syntax but ignore verbal communication, behavioral dynamics, and open-ended design; peer mock interviews (e.g., Pramp) suffer from scheduling bottlenecks and non-expert evaluations; and enterprise platforms (e.g., HireVue) are inaccessible to individual learners. Candidates lack an integrated, low-cost platform that combines resume-aware technical questioning, voice interaction, automated feedback, and structured reporting.

### Source Evidence
- **Page**: PDF pp. 1–2
- **Section**: Section I — Introduction & Section III.A — Problem Statement

---

## 3. Research Objectives

The authors explicitly define their objectives:
1. To design and implement a voice-interactive technical interview simulation web application using Streamlit.
2. To extract and parse candidate PDF resume data to personalize question generation according to the candidate's skills, projects, and target technical domain.
3. To transcribe spoken candidate responses using OpenAI Whisper and conduct automated evaluation using Google Gemini across technical depth, communication skills, and problem-solving.
4. To automatically compile a multi-dimensional performance evaluation report and deliver it as a downloadable PDF using ReportLab.

### Source Evidence
- **Page**: PDF pp. 1–2
- **Section**: Abstract & Section III.B — Objectives

---

## 4. Research Questions

- *Not explicitly reported* (The paper presents an applied systems engineering architecture, software pipeline, and system validation rather than formal theoretical research questions).

---

## 5. Dataset / Supported Domains

The system was evaluated across six technical domains:
- **Supported Domains (6)**:
  1. Software Development
  2. Data Science
  3. Machine Learning
  4. Cloud Computing
  5. Cybersecurity
  6. Web Development
- **Test Ingestion**: Real-world student resumes in PDF format parsed via PyPDF2; spoken audio captured at 16 kHz (16-bit mono .wav).
- **Session Scale**: Standard dynamic interview sessions comprising 8 to 12 contextually evolving technical questions per candidate.
- **Availability**: Applied laboratory research project at the AIML Laboratory, Dilkap Research Institute of Engineering and Management Studies, University of Mumbai.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section III.C (Scope) & Section V.B (Interview Flow)

---

## 6. Features / Input Information

The system extracts and processes four input feature categories:

### Resume Features
- **Extracted Entities**: Technical skill tags, programming languages, academic degrees, project descriptions, and prior internship/work experience.

### Spoken Response Features
- **Audio Stream**: 16 kHz 16-bit mono audio samples captured via SoundDevice.
- **Transcribed Utterances**: Whisper ASR transcript text after disfluency removal and punctuation normalization.

### Technical & Conversational Signals
- **Technical Accuracy & Depth**: Domain correctness of explained concepts.
- **Communication Rating**: Structure, articulation clarity, and conciseness.
- **Problem-Solving Rating**: Systematic approach, edge-case consideration, and design reasoning.

### Performance Metadata
- **Domain Suitability**: Match percentage against the selected technical domain.
- **Upskilling Trajectory**: Specific identified weak topics and recommended learning resources.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section IV.B & Section V (Subsections A–E)

---

## 7. Data Preprocessing

- **PDF Resume Extraction**: PyPDF2 extracts body text; rule-based regex and prompt-formatting isolate educational history, skill keywords, and projects.
- **Audio Pipeline**: Real-time microphone input captured via `SoundDevice` and saved to temporary `.wav` files via `SoundFile`.
- **Text Normalization**: Whisper transcripts undergo filler-word filtering and punctuation normalization before injection into Gemini evaluation prompts.
- **Structured Schema Enforcement**: Evaluation prompts enforce strict JSON output formatting from Gemini (`overall_score`, `communication_rating`, `technical_depth`, `strengths`, `improvement_areas`, `problem_solving_rating`, `alternative_domains`).

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section IV.B, Section V.C, Section V.D

---

## 8. Algorithms and Models

The system coordinates specialized AI/NLP components (Table II):
1. **Generative LLM Engine**: **Google Gemini API** (`gemini-pro` / generative API) used for:
   - Dynamic resume-aware question generation (8–12 questions).
   - Real-time follow-up probe generation conditioned on previous candidate responses.
   - Comprehensive multi-criteria performance evaluation and domain suitability analysis.
2. **Automatic Speech Recognition (ASR)**: **OpenAI Whisper** (`load_model("base")`), balancing transcription speed and accuracy for interactive voice sessions at 16 kHz.
3. **Session State Tracking**: Streamlit in-memory session manager with optional SQLite backend for multi-session longitudinal progress tracking.
4. **Report Rendering Engine**: **ReportLab** dynamic PDF generation compiling radar charts, score badges, transcripts, and study guides.

### Source Evidence
- **Page**: PDF pp. 2–4
- **Section**: Section IV.B, Section V, Table II

---

## 9. Architecture

The system implements a five-module, linear-pipeline client-server architecture (Figure 1 & Section IV):
- **Ingestion Pipeline**: `Resume Upload (PDF)` + `Domain Selection` $\rightarrow$ `PyPDF2 Text Extraction` $\rightarrow$ `Structured Gemini Context Prompt`.
- **Conversational Interactive Loop**:
  $$\text{Gemini Question} \xrightarrow{\text{Voice Prompt}} \text{Candidate Speech} \xrightarrow{\text{SoundDevice}} \text{Whisper ASR} \xrightarrow{\text{Transcript}} \text{Session History} \xrightarrow{\text{Gemini Follow-up}} \dots$$
- **Evaluation & Synthesis Pipeline**: `Full Transcript (8–12 Turns)` $\rightarrow$ `Gemini JSON Evaluator` $\rightarrow$ `ReportLab Engine` $\rightarrow$ `Downloadable PDF Performance Report`.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section IV (Subsections A & B)

---

## 10. Methodology

1. **Profile Setup**: Candidate uploads PDF resume and selects one of 6 technical tracks.
2. **Resume-Conditioned Seed Question**: Gemini parses the resume and generates an opening question targeting a specific project or core technology listed by the candidate.
3. **Voice Interaction Loop**: Candidate answers verbally; SoundDevice records audio; Whisper transcribes the response.
4. **Adaptive Probing**: Gemini evaluates response adequacy and generates a progressive follow-up (e.g., asking for complexity trade-offs, architecture choices, or debugging strategies).
5. **JSON Evaluation**: Upon interview completion, the conversation history is passed to Gemini, returning structured numerical ratings and qualitative feedback.
6. **PDF Delivery**: ReportLab formats the data into a downloadable performance dossier.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section IV & Section V

---

## 11. Experimental Setup

- **Software Stack (Table II)**:
  - Language: Python 3.10+
  - Web UI: Streamlit
  - AI Generation & Evaluation: Google Gemini API
  - Speech Recognition: OpenAI Whisper (`base` model)
  - PDF Parsing: PyPDF2
  - Report Compilation: ReportLab
  - Audio I/O: SoundDevice & SoundFile
- **Hardware Requirements (Section VII.A)**: Intel Core i5 / AMD Ryzen 5 (4+ cores, 2.0 GHz+), 8 GB RAM (16 GB recommended), 500 MB temporary disk storage, standard microphone, broadband internet (10+ Mbps). Optional NVIDIA GPU for local Whisper acceleration.

### Source Evidence
- **Page**: PDF pp. 3–4
- **Section**: Section VII (A & B, Table II)

---

## 12. Evaluation Metrics

1. **Overall Score**: Scalar rating on a $0–100$ scale.
2. **Communication Rating**: Verbal clarity, structure, and articulation.
3. **Technical Depth Assessment**: Conceptual correctness, knowledge of edge cases, and design depth.
4. **Problem-Solving Rating**: Logical decomposition, analytical reasoning, and algorithmic structuring.
5. **Domain Suitability Index**: Percentage alignment with industry role expectations.
6. **Turn Count & Session Length**: Typical interview progression spanning 8–12 questions.

### Source Evidence
- **Page**: PDF pp. 2–3
- **Section**: Section IV.B.4 & Section V.D

---

## 13. Results

### System Verification & Comparative Benchmarking (Table I)
- **Feature Matrix Benchmark (Table I)**:
  - *HireVue*: Partial voice, non-resume-aware, automated feedback, no free student access, no instant downloadable PDF.
  - *Pramp*: Voice-based, non-resume-aware, human-only feedback, free, no PDF reporting.
  - *HackerRank*: Text/code only, non-resume-aware, code execution only, free, no PDF reporting.
  - *Proposed AI Mock Interview System*: Fully voice-based (Whisper), resume-personalized (Gemini), automated AI feedback (Gemini), downloadable PDF report (ReportLab), 100% free/learner accessible.
- **Operational Performance**: Stable transcription at 16 kHz using Whisper `base` model; reliable structured JSON response parsing from Gemini without regex breakage; automated multi-page PDF generation within seconds of session completion.

### Source Evidence
- **Page**: PDF pp. 2–4
- **Table / Sections**: Table I, Section V.C, Section VI, Section VIII

---

## 14. Baselines

The authors compare their system directly against commercial and community platforms in **Table I**:
1. **HireVue** (Enterprise video recruitment and assessment platform).
2. **Pramp** (Peer-to-peer live mock interview platform).
3. **HackerRank** (Automated online algorithmic assessment platform).
4. **LeetCode** (Online judge and coding challenge repository).

### Source Evidence
- **Page**: PDF p. 2
- **Section**: Section II.A & Table I

---

## 15. Ablation Study

- *Not reported* (System implementation paper focusing on end-to-end integration rather than component ablation).

---

## 16. Explainability

- The generated PDF report provides transparent rationales:
  - Itemized lists of specific candidate strengths and concrete improvement areas.
  - Domain suitability rationale explaining *why* a candidate scored high or low for a given track.
  - Curated upskilling recommendations linking identified weak topics to concrete learning resources.

### Source Evidence
- **Page**: PDF p. 3
- **Section**: Section V.E & Section VI

---

## 17. Main Findings

1. Combining Google Gemini for resume-aware prompt orchestration with OpenAI Whisper for local speech-to-text enables a completely responsive, voice-driven mock interview pipeline without expensive enterprise software.
2. Structured output prompting in Gemini (requesting a strict JSON schema) eliminates parsing failures and ensures consistent multi-metric scoring across technical depth, communication, and problem solving.
3. Automated ReportLab PDF compilation transforms ephemeral interview sessions into permanent, actionable study guides that students can review iteratively.

### Source Evidence
- **Page**: PDF pp. 2–4
- **Section**: Section IV, Section V, Section VIII

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
1. **Lack of Non-Verbal Computer Vision**: The current implementation is strictly voice-and-text; it lacks computer vision tracking for facial emotion, eye contact, and body posture.
2. **Absence of Real-Time Acoustic Prosody**: Relies on Whisper text transcription rather than raw acoustic signal analysis for tone or pitch variations.
3. **Technical Domain Scope**: Confined to 6 predefined technical tracks; behavioral and HR interview simulations are not yet supported.
4. **Cloud API Dependency**: Requires stable broadband internet connectivity for external Google Gemini API calls.

### 18.2 Research Interpretation
- *Research interpretation — not stated by the original authors*: The paper describes system implementation and functional testing; it does not present statistical reliability studies (e.g., inter-rater reliability between Gemini scores and human senior engineering interviewers) on a large student cohort.

### Source Evidence
- **Page**: PDF pp. 3–4
- **Section**: Section VII.A & Section VIII — Conclusion

---

## 19. Future Work

Explicitly proposed by the authors:
1. Incorporating real-time emotion and sentiment analysis for richer communication feedback.
2. Implementing adaptive difficulty calibration using reinforcement learning from historical candidate performance.
3. Expanding domain support to include behavioral and Human Resources (HR) interview simulations.
4. Developing a multimodal evaluation pipeline incorporating computer vision video analysis for posture, gaze, and non-verbal communication.

### Source Evidence
- **Page**: PDF p. 4
- **Section**: Section VIII — Conclusion

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

This paper provides immediate, practical implementation patterns for PRIE's **Mock Interview Engine**:
1. **Streamlit / Python Implementation Blueprint**: Demonstrates how to connect PyPDF2 resume parsing, SoundDevice microphone capture, Whisper `base` transcription, and Gemini prompt chains into a cohesive conversational loop.
2. **Complementary Modalities with IndusAI (Paper 28)**: While IndusAI focuses on openSMILE acoustic prosody and MediaPipe vision, Wahid et al. provide the exact Gemini prompt structure for adaptive technical follow-up questioning and structured JSON score outputs. PRIE can synthesize both approaches into a unified technical-multimodal interview engine.
3. **PDF Report Compilation**: Validates the utility of automated ReportLab PDF dossiers for candidate diagnostic remediation.

---

## 21. Evidence Table

| Finding / Fact | Evidence Statement from PDF | Source Location | Evidence Type |
|---|---|---|---|
| **System Overview** | "AI Mock Interview system, an advanced voice-interactive web application developed using Streamlit... integrates Google Gemini... and OpenAI Whisper." | PDF p. 1, Abstract | Direct statement |
| **Supported Tracks** | Six technical domains: Software Development, Data Science, Machine Learning, Cloud Computing, Cybersecurity, Web Development. | PDF p. 2, Section III.C | Scope / Specification |
| **ASR Configuration** | Audio sampled at 16 kHz (16-bit mono .wav); processed by `whisper.load_model("base")`. | PDF p. 3, Section V.C | Methodology |
| **Structured Output Mode** | Evaluation prompt requests strict JSON schema for overall score, communication, technical depth, strengths, and improvement areas. | PDF p. 3, Section V.D | Methodology |
| **Comparison with Existing** | Table I benchmarks HireVue, Pramp, HackerRank vs proposed system across 5 criteria. | PDF p. 2, Table I | Table / Benchmark |
| **Stated Future Work** | Video analysis for posture/eye contact, emotion/sentiment analysis, RL adaptive difficulty, HR interview simulation. | PDF p. 4, Section VIII | Author future work |

---

## 22. Verification Checklist

- [x] PDF read (`Paper29_srinivasan2025aimock.pdf`, 4 pages)
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected (Streamlit, PyPDF2, Whisper base, Gemini prompt chains, ReportLab)
- [x] Dataset verified (6 technical domains, PDF resumes, 16 kHz audio)
- [x] Features verified (Resume skills/projects, transcribed answers, technical depth, communication ratings)
- [x] Algorithms verified (Google Gemini API, OpenAI Whisper base model)
- [x] Architecture inspected (5-module pipeline, Section IV.B)
- [x] Experiments inspected (Table I comparison against HireVue, Pramp, HackerRank)
- [x] Results verified (8–12 turn flow, JSON output schema, automated PDF report)
- [x] Limitations verified (No video/vision, no acoustic prosody, cloud API dependency)
- [x] Future work verified (Video posture/gaze, RL difficulty calibration, HR domains)
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read in full; exact 5-module architecture, Table I comparison, software stack from Table II, and 6 technical domains verified directly from source text; legacy filename discrepancy documented).
