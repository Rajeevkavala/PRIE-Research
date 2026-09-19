# Paper 15 — Multimodal AI-Based Mock Interview System: Integrating Facial Expression Analysis, Speech Emotion Recognition, and NLP for Holistic Candidate Evaluation

## 1. Bibliographic Information

- **Paper ID**: Paper15
- **Full Title**: Multimodal AI-Based Mock Interview System: Integrating Facial Expression Analysis, Speech Emotion Recognition, and NLP for Holistic Candidate Evaluation
- **Authors**: Shoaib Inamdar, Abhijeet Panchal, Priyanka Kumbhar, Yogita Sontakke, and Asma Hannure
- **Institution**: Department of Computer Science, A G Patil Polytechnic Institute, Solapur, Maharashtra, India
- **Year**: 2025 (Published: November–December 2025)
- **Venue**: International Journal of Scientific Research and Engineering Development (IJSRED), Vol. 8, Issue 6, pp. 681–683
- **ISSN**: 2581-7175
- **PDF filename**: `Paper15_consortium2025multimodal.pdf`
- **PDF path**: `Papers/PDFs/Paper15_consortium2025multimodal.pdf`
- **Page count**: 3 pages (pp. 681–683)

> [!NOTE]
> **Corpus Reconciliation Note**: The legacy BibTeX file (`Paper15_consortium2025multimodal.bib`) cited an institutional pseudonym ("Advanced Innovation Consortium"). Inspection of the actual PDF confirms the true authors are Shoaib Inamdar, Abhijeet Panchal, Priyanka Kumbhar, Yogita Sontakke, and Asma Hannure from A G Patil Polytechnic Institute, Solapur.

---

## 2. Research Problem

Conventional interview preparation focuses disproportionately on static technical knowledge while neglecting non-verbal communication channels (such as facial micro-expressions, eye contact, speech tone, pitch modulation, and hesitation). These non-verbal cues strongly dictate human interviewer impressions. Existing automated AI interview tools are predominantly unimodal (evaluating text transcripts only) and fail to provide integrated, real-time feedback across emotional regulation, acoustic prosody, and verbal competence.

### Source Evidence
- **PDF Page**: Page 1 (p. 681), Abstract & Page 2 (p. 682), Section II "LITERATURE REVIEW".

---

## 3. Research Objectives

1. Design an accessible web-based mock interview platform that simulates realistic, multi-domain interviews without requiring human interviewers.
2. Integrate three distinct analytical pipelines into a unified scoring framework:
   - Deep learning-based Facial Expression Analysis (video stream).
   - Acoustic Speech Emotion Recognition (audio stream).
   - Natural Language Processing (NLP) answer content evaluation.
3. Leverage modern Generative AI (Google Gemini API) for dynamic, domain-specific interview question generation and automated performance report synthesis.
4. Implement a full-stack cloud architecture utilizing Next.js, Firebase, and Tailwind CSS for low-latency candidate assessment.

### Source Evidence
- **PDF Page**: Page 1 (p. 681), Abstract & Page 2 (p. 682), Section III "SYSTEM ARCHITECTURE AND METHODOLOGY".

---

## 4. Research Questions

Not explicitly stated in question format by the authors. The work is framed around architectural implementation and multimodal integration feasibility.

---

## 5. Dataset

As an architectural and system prototype paper, the authors did not publish a stand-alone empirical benchmark dataset:
- **Input Modality**: Real-time webcam video streams and microphone audio recordings collected from student users practicing interview sessions.
- **Domain Coverage**: Multi-domain question generation dynamically formulated across user-selected professional specializations.
- **Sample Count**: Not explicitly reported in quantitative participant numbers.

### Source Evidence
- **PDF Page**: Page 2 (p. 682), Section III "SYSTEM ARCHITECTURE AND METHODOLOGY".

---

## 6. Features

The system extracts three synchronous tiers of multimodal features:

### 1. Visual & Facial Modality
- Detected emotional expressions (confidence, nervousness, neutral, anxiety).
- Facial micro-expression changes during question response windows.

### 2. Acoustic & Speech Modality
- Vocal tone and pitch modulation.
- Speech fluency and cadence.
- Acoustic energy contours indicative of emotional arousal.

### 3. Verbal & Semantic Modality
- Technical answer correctness against domain concepts.
- Answer coherence, structure, and depth.
- Alignment with standard behavioral interview frameworks (e.g., STAR methodology principles).

### Source Evidence
- **PDF Page**: Page 2 (p. 682), Section III.

---

## 7. Data Preprocessing

1. **User Authentication & Session Setup**: Authenticating candidate profiles via Firebase Auth and storing historical session metadata.
2. **Audio/Video Stream Splitting**: Capturing synchronized audiovisual media from candidate webcams and routing audio to speech recognition and video to facial analysis.
3. **Speech Transcription**: Transcribing raw vocal audio streams into text transcripts for NLP processing.
4. **Facial Frame Extraction**: Sampling video frames for neural facial action unit and emotion classification.

### Source Evidence
- **PDF Page**: Page 2 (p. 682), Section III & Figure 1.

---

## 8. Algorithms and Models

- **Generative Question & Report Engine**: **Google Gemini API** (Large Language Model) used for zero-shot and few-shot generation of adaptive interview questions and synthesis of textual evaluation reports.
- **Facial Expression Recognition (FER)**: Deep learning computer vision models classifying video frames into affective states (confidence vs nervousness).
- **Speech Emotion Recognition (SER)**: Deep acoustic neural networks evaluating vocal tone, pitch, and fluency from raw audio.
- **Answer Content Evaluation**: NLP scoring pipelines assessing transcribed answer relevance, coherence, and keyword coverage.

### Source Evidence
- **PDF Page**: Page 2 (p. 682), Section III & Page 3 (p. 683), Section IV "CONCLUSION".

---

## 9. Architecture

The system is deployed as an integrated web application:
- **Frontend Layer**: Built using **Next.js** and styled with **Tailwind CSS**, providing real-time camera/microphone interfaces and dynamic evaluation dashboards.
- **Backend & Storage Layer**: **Firebase** providing secure user authentication, database persistence (Firestore), and cloud media storage for longitudinal progress tracking.
- **Generative AI Service**: Cloud connection to **Google Gemini API** for on-demand question synthesis and diagnostic summary generation.
- **Multimodal Evaluation Pipeline**: Tripartite pipeline processing video (Facial), audio (SER), and transcribed text (NLP).

### Source Evidence
- **PDF Page**: Page 2 (p. 682), "Fig 1. System workflow" & Page 3 (p. 683), Section IV.

---

## 10. Methodology

1. **Profile Initialization**: Candidate registers and selects desired career domain and experience tier.
2. **Dynamic Questioning**: Google Gemini generates customized, domain-specific interview prompts.
3. **Response Recording**: Candidate records video and audio responses directly in browser.
4. **Parallel Multimodal Processing**:
   - Video stream analyzed for facial affective states.
   - Audio stream analyzed for speech prosody, fluency, and tone.
   - Speech transcribed and evaluated for technical relevance and clarity.
5. **Score Synthesis & Feedback Delivery**: Scores across verbal, emotional, and prosodic metrics are merged into an actionable diagnostic report with improvement suggestions.
6. **Progress Tracking**: Results committed to Firebase for longitudinal readiness tracking.

### Source Evidence
- **PDF Page**: Page 2 (p. 682), Section III.

---

## 11. Experimental Setup

- **Frontend Framework**: Next.js.
- **Styling**: Tailwind CSS.
- **Backend & Cloud Services**: Firebase (Authentication, Storage, Firestore).
- **Foundation LLM**: Google Gemini API.
- **Deployment Modality**: Web browser-accessible client.

### Source Evidence
- **PDF Page**: Page 3 (p. 683), Section IV "CONCLUSION".

---

## 12. Evaluation Metrics

Evaluated conceptually across:
- **Candidate Confidence & Communication Scores**: Qualitative composite ratings tracking verbal delivery, fluency, and emotional poise.
- **Technical Accuracy & Answer Coherence**: Relevance scores measuring semantic alignment with expected domain knowledge.
- **System Accessibility & Latency**: Qualitative responsiveness in institutional deployment environments.

### Source Evidence
- **PDF Page**: Page 2 (p. 682), Section III & Page 3 (p. 683), Section IV.

---

## 13. Results

- **System Feasibility**: Demonstrates that modern web frameworks (Next.js) coupled with cloud serverless backends (Firebase) and commercial LLMs (Google Gemini API) can host real-time, low-cost multimodal mock interview simulations.
- **Candidate Impact**: Authors report that the multimodal feedback pipeline significantly enhanced candidate confidence and communication effectiveness compared to text-only alternatives.
- *Notice*: Specific numerical benchmark tables (e.g., accuracy percentages or F1-scores) are **not reported** in this 3-page system design paper.

### Source Evidence
- **PDF Page**: Page 3 (p. 683), Section IV "CONCLUSION".

---

## 14. Baselines

- **Traditional In-Person Coaching**: Costly, human-dependent interview preparation.
- **Unimodal Text-Only Mock Systems**: Systems that evaluate text answers without acoustic or non-verbal behavioral tracking.

### Source Evidence
- **PDF Page**: Page 1 (p. 681) & Page 2 (p. 682), Section II.

---

## 15. Ablation Study

Not reported.

---

## 16. Explainability

Multidimensional rubric feedback: The system provides explainable feedback by decomposing overall interview readiness into explicit, separate scoring dimensions (facial confidence score, speech fluency/prosody score, and technical content accuracy score), accompanied by Gemini-generated narrative tips.

### Source Evidence
- **PDF Page**: Page 2 (p. 682), Section III.

---

## 17. Main Findings

1. Integrating computer vision (facial analysis) and speech emotion recognition with textual NLP addresses the critical gap of non-verbal assessment in AI mock interviews.
2. Next.js, Firebase, and the Google Gemini API provide a viable, lightweight stack for building serverless interview simulators for educational institutions.
3. Providing separate feedback on delivery style (tone/expression) alongside technical correctness improves applicant self-awareness and confidence.

### Source Evidence
- **PDF Page**: Page 3 (p. 683), Section IV "CONCLUSION".

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Lack of VR Integration**: Does not currently support immersive virtual reality (VR) environments.
- **Monolingual Focus**: Primarily evaluated in English, lacking multilingual interview capabilities.
- **Industry Tailoring**: Domain-specific analytics require further customization for niche industry verticals.

### 18.2 Research Interpretation
- The paper is a brief 3-page system architecture note with unedited boilerplate text in the acknowledgment section (`"[Your Institution/University Name]"`), indicating an early conference/journal draft.
- No empirical quantitative performance numbers (WER, accuracy %, precision/recall) are reported for the facial expression or speech emotion models.

---

## 19. Future Work

Explicitly proposed by authors:
1. Virtual reality (VR) interview simulation integration.
2. Multilingual support to support non-native English speakers.
3. Enhanced industry-tailored rubrics and analytics.

### Source Evidence
- **PDF Page**: Page 3 (p. 683), Section IV "CONCLUSION".

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

- **Relevant Module**: **PRIE Interactive Mock Interview Simulator (Module 05)**.
- **Stack Alignment**: Validates the architectural synergy between modern full-stack web clients (Next.js/React), cloud database storage, and LLMs (Gemini) for real-time interview generation.
- **Critical Takeaway**: While the paper validates the architectural pattern, ScholarCamp must implement rigorous, quantitatively evaluated models (with verified WER, precision, and latency benchmarks) rather than relying solely on black-box external APIs.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Multimodal framework integrates facial, speech, and NLP | Tripartite analysis pipeline | PDF p. 2, Section III | Architecture |
| Google Gemini API for question generation | Dynamic prompt synthesis | PDF p. 2, Section III | Methodology |
| Next.js, Firebase, and Tailwind CSS tech stack | Implementation technologies | PDF p. 3, Section IV | Experimental setup |
| Future expansion to VR and multilingual support | Author's explicit roadmap | PDF p. 3, Section IV | Future work |
| Absence of empirical numerical benchmark tables | Verified by full-text inspection | PDF pp. 1–3 | Source verification |

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

**PARTIALLY VERIFIED** (Primary PDF read, architecture and stack verified; noted that quantitative empirical benchmark metrics were omitted by the authors in this 3-page design monograph).
