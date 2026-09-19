# Paper 30 — AI-Powered Mock Interview System for Automated Skill Assessment

## 1. Bibliographic Information

- **Paper ID**: Paper30
- **Full Title**: AI-Powered Mock Interview System for Automated Skill Assessment
- **Authors**: Dr. Vijayant Verma (Assistant Professor), Rana Padwar, Apurva Chandrakar, Khushi Jaiswal, and Palak Mishra
- **Institution**: Department of Computer Science & Engineering, Bhilai Institute of Technology, Raipur, India
- **Year**: November 2025
- **Venue**: International Journal for Research in Applied Science & Engineering Technology (IJRASET), Volume 13, Issue XI, November 2025, pp. 2249–2255
- **ISSN**: 2321-9653 (ISRA Journal Impact Factor: 7.894)
- **DOI**: 10.22214/ijraset.2025.75636
- **PDF filename**: `Paper30_kulkarni2024aipowered.pdf` (Note: filename reflects legacy bibtex tag `kulkarni2024aipowered`; authentic PDF confirms authors Dr. Vijayant Verma et al., Bhilai Institute of Technology, Raipur, IJRASET November 2025)
- **PDF path**: `Papers/PDFs/Paper30_kulkarni2024aipowered.pdf`
- **Page count**: 7 pages (pp. 2249–2255)

---

## 2. Research Problem

Traditional face-to-face mock interview preparation in higher education institutions faces severe scalability and equity constraints: human faculty evaluators are constrained by limited availability, subjective judgment, and lack of standardized real-time scoring rubrics. Students frequently enter high-stakes placement interviews without prior objective practice or immediate feedback on technical communication and conceptual depth.

### Source Evidence
- **Page**: PDF p. 2 (p. 2249)
- **Section**: Abstract & Section I — Introduction

---

## 3. Research Objectives

The authors explicitly define their objectives:
1. To design, implement, and empirically validate an AI-powered virtual mock interview system built on a modern full-stack web architecture.
2. To integrate voice-enabled automatic speech recognition (ASR) with transformer-based natural language processing for automated semantic answer evaluation.
3. To deliver instantaneous, objective feedback loops and visual progress tracking that measurably accelerate candidate interview skill acquisition.

### Source Evidence
- **Page**: PDF pp. 2, 5 (pp. 2249, 2252)
- **Section**: Abstract & Section VIII — Conclusion

---

## 4. Research Questions

- *Not explicitly reported* (The paper presents an applied educational software architecture, experimental cohort trial, and system performance evaluation rather than numbered formal hypotheses).

---

## 5. Dataset / Experimental Cohort

- **Cohort Size**: **200 unique student interview sessions** conducted at the Department of Computer Science & Engineering, Bhilai Institute of Technology, Raipur.
- **Data Capture**: Spoken candidate responses recorded via browser-based voice capture and transcribed into timestamped text.
- **Reference Standard**: Predefined standard answer rubrics and domain benchmark responses curated across computer science and engineering topics.
- **Data Availability**: Academic institutional deployment for student placement preparation.

### Source Evidence
- **Page**: PDF p. 4 (p. 2251)
- **Section**: Section V.1 — Experimental Setup

---

## 6. Features / Input Streams

Input features extracted across the evaluation workflow:
- **Speech Audio Streams**: Spoken candidate audio captured in real time via the Web Speech API / Google Speech API.
- **Transcribed Responses**: Noise-filtered text transcript generated via ASR.
- **Key Terms & Domain Concepts**: Extracted technical keywords representing core domain competencies.
- **Sentence Embeddings**: Dense semantic vector representations of student responses and reference answers.
- **Session Metadata**: Unique session IDs, question timestamps, response revision histories, and duration.

### Source Evidence
- **Page**: PDF pp. 3–4 (pp. 2250–2251)
- **Section**: Section IV — Methodology

---

## 7. Data Preprocessing

The text and speech processing pipelines execute:
- **Audio Capture & ASR Transcription**: Speech-to-text conversion with silence trimming and audio segmentation.
- **NLP Text Cleansing**: Noise removal, lowercasing, tokenization, and stop-word filtering.
- **Feature Extraction**: Identifying technical entities and key terminology.
- **Semantic Representation**: Mapping clean text into dense sentence embedding spaces for semantic distance computation.

### Source Evidence
- **Page**: PDF pp. 3–4 (pp. 2250–2251)
- **Section**: Section IV — Methodology

---

## 8. Algorithms and Models

The system incorporates several specialized architectural and algorithmic components:
1. **Speech Recognition (ASR)**: **Web Speech API** / Google Speech API (with Mozilla DeepSpeech modular support) for real-time speech-to-text conversion.
2. **Semantic Similarity Engine**: Transformer-based sentence embedding models computing **Cosine Similarity** between candidate response vectors and expert reference vectors:
   $$\text{Similarity}(u, v) = \frac{u \cdot v}{\|u\| \|v\|}$$
3. **Automated Scoring Rubric**: Multi-metric evaluation combining semantic accuracy, relevance, and keyword coverage.
4. **Application Stack**: **MERN Stack** (MongoDB for document storage, Express.js backend API, React.js frontend interface, Node.js server runtime).

### Source Evidence
- **Page**: PDF pp. 3–5 (pp. 2250–2252)
- **Section**: Section III, Section IV, Section VIII

---

## 9. Architecture

The system implements a multi-tier modular architecture (Figure 1 & Figure 2):
- **Interface Layer (Frontend)**: React.js student console providing real-time voice prompts, speech feedback indicators, dynamic radar charts, and progress dashboards.
- **Application Layer (Backend)**: Node.js / Express.js REST server managing session IDs, authentication, and routing audio streams to NLP microservices.
- **Data Layer**: MongoDB database storing user profiles, interview history, rubrics, and detailed score breakdowns.
- **Evaluation Loop (Figure 2)**: Candidate Voice $\rightarrow$ ASR Engine $\rightarrow$ NLP Cleaning $\rightarrow$ Semantic Similarity Match $\rightarrow$ Rubric Scoring $\rightarrow$ Real-Time Dashboard Feedback.

### Source Evidence
- **Page**: PDF pp. 3–4 (pp. 2250–2251)
- **Figures**: Figure 1 ("System Design & Architecture"), Figure 2 ("Complete Workflow")

---

## 10. Methodology

1. **Session Initialization**: Student logs into the portal; a unique session ID is generated, and interview questions are loaded from the database.
2. **Voice Response Recording**: Student speaks response into browser; Web Speech API captures and transcribes audio in real time.
3. **Automated NLP Assessment**: Text is cleaned; sentence embeddings are generated; cosine similarity calculates semantic alignment with gold-standard answers.
4. **Scoring & Feedback Synthesis**: Scoring algorithms evaluate accuracy, relevance, and coverage, populating student strengths and weaknesses.
5. **Interactive Revision**: Student console displays immediate results, allowing candidates to review and revise answers interactively.
6. **Empirical Benchmarking**: Validation across 200 student trials assessing scoring consistency against human expert evaluators.

### Source Evidence
- **Page**: PDF pp. 3–4 (pp. 2250–2251)
- **Section**: Section IV & Section V

---

## 11. Experimental Setup

- **Platform Architecture**: MERN Stack (MongoDB, Express.js, React.js, Node.js).
- **Voice / NLP Frameworks**: Web Speech API, Google Speech API, Transformer Sentence Embeddings.
- **Evaluation Sample**: 200 unique student interview sessions.
- **Comparative Baseline**: Conventional manual human faculty interview evaluations.

### Source Evidence
- **Page**: PDF pp. 4–5 (pp. 2251–2252)
- **Section**: Section V & Section VIII

---

## 12. Evaluation Metrics

1. **Evaluation Accuracy**: Percentage of automated scores concordant with expert human evaluators (**95.45%**).
2. **Answer Quality Improvement**: Percentage increase in student answer quality over iterative sessions (**23%**).
3. **Self-Reported Confidence Boost**: Percentage of candidates reporting elevated interview confidence (**85%**).
4. **Feedback Latency**: System response time for scoring and feedback generation (**sub-second**).
5. **Assessment Time Reduction**: Reduction in overall time required per candidate evaluation compared to human panels.

### Source Evidence
- **Page**: PDF pp. 4–5 (pp. 2251–2252)
- **Section**: Section V.2 & Section VIII — Conclusion

---

## 13. Results

### Quantitative Results (Section VIII, PDF p. 5)
- **Evaluation Accuracy**: **95.45%** accuracy in automated response evaluation compared to expert faculty panels.
- **Answer Quality Gain**: Average answer quality increased by **23%** across repeated practice sessions.
- **Candidate Confidence Boost**: **85%** of participating students reported a measurable boost in interview readiness and confidence.
- **Feedback Latency**: Achieved **sub-second** latency for automated response scoring and feedback rendering.

### Qualitative Findings (Section V.3)
- Users highlighted high system usability, clarity of automated feedback, responsiveness across technical question types, and reduction in interview anxiety.

### Source Evidence
- **Page**: PDF pp. 4–5 (pp. 2251–2252)
- **Section**: Section V.2 & Section VIII text

---

## 14. Baselines

- **Manual Human Faculty Interview Panels**: Conventional face-to-face faculty mock interviews.
- **Static Form-Based Automated Systems**: Text-only quiz platforms lacking real-time speech interaction and semantic similarity scoring.

### Source Evidence
- **Page**: PDF p. 4 (p. 2251)
- **Section**: Section V.4 — Comparative Analysis with Existing Systems

---

## 15. Ablation Study

- *Not reported* (Empirical system evaluation paper focusing on cohort outcomes and accuracy benchmarks).

---

## 16. Explainability

- **Transparent Feedback Summaries**: The student console presents itemized feedback summaries breaking down why a score was assigned, pointing out missed key technical terms and suggesting concrete conceptual additions.
- **Visual Progress Tracking**: Real-time dashboards visualize longitudinal improvements across successive practice sessions.

### Source Evidence
- **Page**: PDF pp. 3–4 (pp. 2250–2251)
- **Section**: Section IV (Student Console) & Section V.3

---

## 17. Main Findings

1. An open-source MERN-stack architecture integrating Web Speech API and Transformer sentence embeddings achieves **95.45% evaluation accuracy** and **sub-second feedback latency**, proving that low-cost web systems can replace expensive commercial coaching.
2. Providing immediate, objective feedback loops drives measurable learning gains, producing a **23% average increase in technical answer quality** and an **85% student confidence boost** across 200 unique trials.
3. Voice-enabled interaction significantly increases interview realism compared to text-based chat tools, helping candidates overcome verbal articulation barriers.

### Source Evidence
- **Page**: PDF pp. 4–5 (pp. 2251–2252)
- **Section**: Section V & Section VIII

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
1. **Lack of Multimodal Vision**: Does not track non-verbal cues such as facial expressions, gaze, and body gestures.
2. **Speech Recognition Under Accents / Noise**: ASR models may exhibit transcription errors in noisy acoustic environments or with heavy regional accents.
3. **Complex Context Understanding**: Automated semantic similarity may misinterpret highly nuanced, open-ended, or metaphorical responses.
4. **Computational Infrastructure Demands**: Scaling transformer models in real-time across large concurrent student batches requires significant CPU/GPU server resources.
5. **Algorithmic Transparency & Privacy**: Demands strict student data protection and transparent scoring explanations.

### 18.2 Research Interpretation
- *Research interpretation — not stated by the original authors*: The gold-standard answer comparison is based on predefined reference answers; if a candidate proposes a novel, valid alternative architecture or programming paradigm not anticipated in the rubric, semantic similarity might underestimate response quality.

### Source Evidence
- **Page**: PDF pp. 4–5 (pp. 2251–2252)
- **Section**: Section VI — Challenges & Limitations

---

## 19. Future Work

Explicitly proposed by the authors:
1. Implementing multimodal analysis by integrating computer vision for facial expression and gesture recognition.
2. Developing adaptive personalized feedback mechanisms that adjust difficulty dynamically.
3. Expanding system applicability across multiple regional languages and non-engineering job domains.

### Source Evidence
- **Page**: PDF p. 5 (p. 2252)
- **Section**: Section VII — Future Scope

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

This paper provides empirical benchmarks and full-stack implementation details for PRIE's **Mock Interview System**:
1. **Benchmark Ground Truth**: Verma et al. establish empirical validation targets for PRIE: achieving $\ge 95\%$ scoring consistency with expert faculty and sub-second feedback latency.
2. **MERN Architecture Compatibility**: Demonstrates how a React-based student dashboard communicates with backend NLP workers for real-time interview assessment.
3. **Closing Identified Limitations**: Verma et al. note their system's lack of non-verbal vision and dynamic difficulty adjustment; PRIE addresses these exact limitations by integrating MediaPipe non-verbal tracking and adaptive question generation.

---

## 21. Evidence Table

| Finding / Fact | Evidence Statement from PDF | Source Location | Evidence Type |
|---|---|---|---|
| **System Overview** | "Al-powered virtual mock interview system. Leveraging the MERN stack, the system employs natural language processing, automatic speech recognition, and real-time feedback." | PDF p. 2, Abstract | Direct statement |
| **Experimental Sample** | "200 unique student interview sessions were utilized to evaluate the system." | PDF p. 4, Section V.1 | Experimental setup |
| **Evaluation Accuracy** | "Technical performance metrics including 95.45% evaluation accuracy and sub-second Feedback latency confirms the system's capability." | PDF p. 5, Section VIII | Experimental result |
| **Answer Quality Gain** | "23% average answer quality increase, while 85% reported confidence boost." | PDF p. 5, Section VIII | Experimental result |
| **Semantic Matching** | Predefined rubrics with NLP preprocessing and semantic similarity via sentence embeddings and cosine similarity. | PDF pp. 3–4, Section IV | Methodology |
| **Stated Future Scope** | Multimodal analysis via facial expressions/gestures, adaptive personalized feedback, and multi-language expansion. | PDF p. 5, Section VII | Author future work |

---

## 22. Verification Checklist

- [x] PDF read (`Paper30_kulkarni2024aipowered.pdf`, 7 pages)
- [x] Introduction inspected
- [x] Related work inspected
- [x] Methodology inspected (MERN stack, Web Speech API, sentence embeddings, cosine similarity)
- [x] Dataset verified (200 unique student sessions, Bit Raipur)
- [x] Features verified (Audio streams, transcripts, key terms, sentence embeddings)
- [x] Algorithms verified (Web Speech API, Transformer Sentence Embeddings, Cosine Similarity)
- [x] Architecture inspected (Figures 1 & 2 verified: MERN multi-tier architecture)
- [x] Experiments inspected (200 trials, expert panel comparison)
- [x] Results verified (95.45% accuracy, 23% quality gain, 85% confidence boost, sub-second latency)
- [x] Limitations verified (No vision, noise/accents, compute demands, algorithmic transparency)
- [x] Future work verified (Multimodal facial/gesture analysis, adaptive feedback, multi-language)
- [x] Evidence locations recorded

---

## 23. Verification Status

**VERIFIED** (Primary PDF read in full; exact 200-student trial from Section V.1, 95.45% accuracy and 23% answer quality gain from Section VIII, MERN architecture from Figures 1–2 verified directly from source text; legacy filename discrepancy documented).
