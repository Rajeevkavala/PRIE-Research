# Paper 14 — Review Paper on AI-Driven Mock Interview System Using NLP and Multinomial Performance Analysis

## 1. Bibliographic Information

- **Paper ID**: Paper14
- **Full Title**: REVIEW PAPER ON AI-DRIVEN MOCK INTERVIEW SYSTEM USING NLP AND MULTINOMIAL PERFORMANCE ANALYSIS
- **Authors**: Ms. Prajakta Prakash Koli, Ms. Srushti Satish Sagare, Mr. Shivam Sunil Ingale, and Mr. Aniket Ajay Mulik
- **Institution**: Department of Artificial Intelligence and Machine Learning (AIML), Adarsh Institute of Technology and Research Centre (AITRC), Vita, Maharashtra, India
- **Year**: 2025 (Published: December 2025)
- **Venue**: Journal of Advance and Future Research (JAAFR), Vol. 3, Issue 12, pp. 378–382
- **ISSN**: 2984-889X
- **Article ID**: JAAFR2512043
- **PDF filename**: `Paper14_deshmukh2025review.pdf`
- **PDF path**: `Papers/PDFs/Paper14_deshmukh2025review.pdf`
- **Page count**: 5 pages (pp. 378–382)

> [!NOTE]
> **Corpus Reconciliation Note**: The legacy BibTeX file (`Paper14_deshmukh2025review.bib`) listed synthetic authors ("Deshmukh, Anand and Kulkarni, Pradeep") and venue ("Journal of Advanced Applied Scientific Research"). Inspection of the actual PDF confirms the true authors are Prajakta Prakash Koli, Srushti Satish Sagare, Shivam Sunil Ingale, and Aniket Ajay Mulik from AITRC Vita, published in *Journal of Advance and Future Research (JAAFR)*.

---

## 2. Research Problem

Traditional face-to-face mock interviews require experienced industry recruiters, making them costly, resource-intensive, and difficult for academic institutions to organize frequently at scale. Consequently, university graduates face real-world placement drives without sufficient interactive practice, leading to low self-confidence, unrefined communication, poor body language, and difficulty structuring technical answers. Existing automated tools predominantly analyze isolated single-modality signals (text-only keyword matching) without capturing the multifaceted nature of interviews (spoken prosody, hesitation, emotional regulation, and semantic depth).

### Source Evidence
- **PDF Page**: Page 1 (p. 378), Section "INTRODUCTION".

---

## 3. Research Objectives

1. Conduct a systematic literature review synthesizing the evolution of AI-driven interview coaching across NLP, Speech Emotion Recognition (SER), and computer vision.
2. Evaluate 18 foundational research works (2020–2025) covering text evaluation, transformer question generation, speech sentiment, multimodal fusion, and conversational LLMs.
3. Formulate an enhanced multimodal architectural framework integrating Automatic Speech Recognition (ASR), transformer-based semantic evaluation (BERT/LLMs), acoustic emotion detection (CNN-LSTM), and adaptive question sequencing.
4. Establish design requirements for deploying accessible, low-latency, virtual interview coaches in higher education placement cells.

### Source Evidence
- **PDF Page**: Page 1 (p. 378), Section "INTRODUCTION"; Page 4 (p. 381), Section "CONCLUSION".

---

## 4. Research Questions

Not explicitly reported in numbered question syntax. The review is guided by architectural objectives:
- How do transformer-based semantic scoring models (BERT/SBERT) compare with classical keyword/TF-IDF models in scoring technical interview responses?
- What acoustic features (pitch, pause duration, speech rate) best capture candidate confidence and hesitation?
- How can multimodal signals (text, audio, non-verbal cues) be fused to deliver holistic, actionable interview feedback?

---

## 5. Dataset

As a systematic state-of-the-art review and conceptual architecture paper, no primary empirical dataset was collected by the authors. The paper synthesizes findings across 18 peer-reviewed research papers and benchmarking studies:
- **Corpus Analyzed**: 18 empirical and review studies (detailed in Sections 2.1 through 2.18).
- **Subject Domains Covered in Analyzed Systems**: Technical interview topics (Python, DBMS, Machine Learning, Data Structures) and Human Resources (HR behavioral questions).

### Source Evidence
- **PDF Page**: Pages 2–4 (pp. 379–381), Sections 2.1–2.18 and Comparative Table.

---

## 6. Features

The review synthesizes the key input and evaluation feature modalities identified across contemporary AI interview systems:

### Verbal & Textual Features
- Keyword match ratio and technical terminology coverage.
- Semantic sentence embeddings (BERT / Sentence-BERT similarity against ideal reference answers).
- Grammatical correctness and lexical diversity.

### Audio & Prosodic Features
- Fundamental frequency / pitch variation ($\Delta F_0$).
- Articulation rate and speaking speed (words per minute).
- Pause duration, silence ratio, and hesitation markers ("um", "uh").
- Acoustic tone and Speech Emotion Recognition (SER: confidence, calmness, nervousness, panic).

### Visual & Non-Verbal Features (Multimodal Extensions)
- Eye-contact stability and gaze tracking.
- Facial action units and micro-expressions.
- Head movement, nodding, and upper-body posture.

### Source Evidence
- **PDF Page**: Pages 2–3 (pp. 379–380), Sections 2.3, 2.4, 2.7, 2.8, 2.14, and 2.17.

---

## 7. Data Preprocessing

Synthesized across reviewed systems:
1. **Audio Ingestion & Denoising**: Noise cancellation and acoustic normalization to eliminate ambient background disturbances.
2. **Speech-to-Text Transcription**: Utilizing Transformer Automatic Speech Recognition (ASR) to handle varied accents, speech rates, and domain jargon.
3. **Text Cleaning & Tokenization**: Punctuation filtering, lowercasing, and subword tokenization for transformer encoders.
4. **Prosodic Feature Extraction**: Extracting MFCCs (Mel-Frequency Cepstral Coefficients), energy contours, and pitch contours from raw audio waveforms.

### Source Evidence
- **PDF Page**: Page 2 (p. 379), Section 2.4; Page 3 (p. 380), Section 2.16.

---

## 8. Algorithms and Models

The paper classifies and compares algorithms across four functional pipelines:
1. **Automatic Speech Recognition (ASR)**: Transformer-based ASR models (e.g., Whisper, Conformer) for high-accuracy spoken response transcription.
2. **Natural Language Evaluation**:
   - Classical: TF-IDF, CountVectorizer, and Naive Bayes / SVM (critiqued for lacking contextual comprehension).
   - Modern: BERT, Sentence-BERT (SBERT), and Generative LLMs (GPT-3.5/GPT-4) for semantic similarity against reference answers.
3. **Question Generation**: T5 (Text-to-Text Transfer Transformer) and prompt-engineered LLMs generating domain-specific technical and behavioral questions.
4. **Speech Emotion Recognition (SER)**: Deep learning hybrid architectures (CNN, LSTM, CNN-LSTM, CRNN) classifying acoustic spectrograms into emotional states (confidence vs nervousness).
5. **Adaptive Flow Control**: Reinforcement Learning (RL) agents dynamically adjusting follow-up question difficulty based on prior candidate performance.

### Source Evidence
- **PDF Page**: Pages 2–4 (pp. 379–381), Sections 2.1, 2.2, 2.3, 2.5, 2.10, 2.11, 2.18.

---

## 9. Architecture

The paper proposes an integrated multimodal mock interview workflow (Figure on PDF p. 2):
1. **Candidate Interface**: Web/video interface capturing audio, video, and text streams.
2. **Question Dispatcher**: Dynamic question generator (T5 / LLM) selecting prompts based on student domain and difficulty tier.
3. **Multimodal Analysis Engine**:
   - *Speech Engine*: ASR transcription + CNN-LSTM emotion and prosody analyzer.
   - *NLP Engine*: SBERT semantic similarity + keyword density checker.
   - *Computer Vision Engine*: Facial micro-expression and gaze tracker.
4. **Scoring & Performance Synthesis**: Multinomial scoring module combining semantic relevance, fluency, confidence, and posture.
5. **Feedback Generator**: Diagnostic dashboard presenting rubric breakdown, detected speech filler counts, and personalized improvement tips.

### Source Evidence
- **PDF Page**: Page 2 (p. 379), "Fig : Workflow diagram" & Section "LITERATURE REVIEW".

---

## 10. Methodology

As a literature review, the methodology comprises:
1. Identifying operational pain points in conventional manual interview preparation.
2. Formulating search queries across academic repositories (IEEE Xplore, MDPI, Springer, arXiv, Elsevier, ACM).
3. Analyzing 18 key papers across architectural dimensions: question generation, answer scoring, speech analysis, and multimodal integration.
4. Synthesizing findings into a comparative research matrix (Table on p. 4).
5. Proposing an end-to-end multimodal architecture overcoming current single-modality limitations.

### Source Evidence
- **PDF Page**: Pages 1–4 (pp. 378–381).

---

## 11. Experimental Setup

Not applicable (review paper). The authors synthesize experimental setups reported in literature: transformer ASR, PyTorch deep learning models for SER, and BERT embeddings.

---

## 12. Evaluation Metrics

The paper synthesizes metrics utilized across the reviewed literature:
- **Speech Emotion & ASR**: Word Error Rate (WER), Classification Accuracy (%), F1-Score across emotional states.
- **Answer Evaluation**: Semantic Cosine Similarity (BERT score), Correlation with Human Interviewer Ratings ($r$), Precision, Recall, BLEU/ROUGE for question generation.
- **Fluency & Confidence**: Speaking rate (words per minute), Pause frequency, Articulation index.

### Source Evidence
- **PDF Page**: Pages 2–4 (pp. 379–381).

---

## 13. Results

### Comparative Literature Synthesis Matrix (PDF p. 4, p. 381)

| Sr. No. | Research Paper Focus | Representative Study | Core Findings & Technological Role |
|:---:|:---|:---|:---|
| **1** | Intelligent Virtual Interviewing Using NLP | Sharma et al. (2021) | Evaluated text answers with TF-IDF and keyword matching; demonstrated feasibility but lacked deep semantic comprehension; established need for transformers. |
| **2** | Automatic Question Generation Using Transformer | Zhang et al. (2022) | Proposed T5-based model generating context-aware, adaptive interview questions; significantly outperformed template/rule-based generators. |
| **3** | BERT-Based Semantic Evaluation for Interviews | Singh et al. (2024) | Employed BERT / SBERT embeddings to grade answers on contextual meaning rather than surface keywords; high correlation with human domain experts. |
| **4** | Speech Emotion Recognition for Interviews | Latif et al. (2020) | Reviewed deep learning SER architectures; proved acoustic tone is critical for measuring confidence and nervousness. |
| **5** | Multimodal Assessment (Text + Audio) | Kim & Lee (2023) | Combined acoustic cues (pitch, pauses) with NLP; achieved superior assessment reliability over unimodal systems, but noted susceptibility to acoustic noise. |
| **6** | LLM Conversational Agents for Professional Training | Ouyang et al. (2023) | Demonstrated GPT-based agents simulate interactive multi-turn dialogue and generate instant feedback; identified prompt-injection and consistency challenges. |

### Source Evidence
- **PDF Page**: Page 4 (p. 381), Summary Table.

---

## 14. Baselines

- **Single-Modality Keyword Systems**: Systems evaluating interviews solely using exact keyword matching or bag-of-words without considering speech acoustics or semantics.
- **Traditional In-Person Human Mock Interviews**: High-cost, low-frequency human evaluations.

### Source Evidence
- **PDF Page**: Page 1 (p. 378) & Page 4 (p. 381).

---

## 15. Ablation Study

Not reported (review paper).

---

## 16. Explainability

The authors highlight the necessity of transparent scoring rubrics: rather than assigning a monolithic score, the system must provide granular, interpretable breakdowns across technical accuracy, vocabulary, speech rate, pause ratios, and confidence levels.

### Source Evidence
- **PDF Page**: Page 1 (p. 378) & Page 4 (p. 381), Section "CONCLUSION".

---

## 17. Main Findings

1. Text-only keyword evaluation is inadequate for open-ended technical interviews; dense transformer embeddings (BERT/SBERT) are necessary to capture semantic equivalence and synonyms.
2. Acoustic prosodic analysis (speech rate, pitch stability, pause frequency) correlates strongly with candidate confidence and nervousness.
3. Multimodal fusion (combining verbal text, audio prosody, and facial tracking) consistently achieves higher scoring validity than any single modality in isolation.
4. Generative transformers (T5, LLMs) enable dynamic, context-aware question sequencing and multi-turn conversational follow-ups.

### Source Evidence
- **PDF Page**: Pages 2–4 (pp. 379–381), Sections 2.1–2.18 & Section "CONCLUSION".

---

## 18. Limitations

### 18.1 Explicitly Stated by Authors
- **Acoustic Noise Vulnerability**: Speech emotion and prosodic models degrade significantly in noisy home/classroom environments.
- **LLM Consistency & Bias**: Generative language models occasionally exhibit hallucinations, response variability, and subtle demographic biases.
- **Computational Demands**: Real-time simultaneous processing of video streams, ASR, and transformer embeddings requires substantial edge or server hardware.

### 18.2 Research Interpretation
- As a review paper, it does not present independent empirical benchmarks or open-source software implementations.
- The reference list contains generic venue labels (e.g., "[1] IEEE (2023)", "[2] MDPI (2024)") without full citation metadata.

---

## 19. Future Work

Explicitly proposed by authors:
1. Integrating non-verbal behavioral tracking (gaze stability, posture, gesture analysis) using lightweight computer vision models.
2. Developing noise-robust speech emotion recognition pipelines.
3. Fine-tuning domain-specialized open-source LLMs to ensure factual consistency in evaluating niche engineering disciplines.
4. Deploying campus-wide pilot implementations across university training institutes.

### Source Evidence
- **PDF Page**: Page 4 (p. 381), Section "CONCLUSION".

---

## 20. ScholarCamp / PRIE Relevance

*Research interpretation — not stated by the original authors.*

- **Relevant Module**: **PRIE Interactive Mock Interview Simulator (Module 05)**.
- **Theoretical Contribution**: The 18-paper literature survey provides a comprehensive taxonomy justifying PRIE's planned multimodal architecture (combining Whisper ASR, SBERT semantic scoring, and audio/facial confidence analytics).
- **Architecture Validation**: Confirms that transitioning from keyword matching to transformer semantic similarity is an established requirement in modern placement intelligence research.

---

## 21. Evidence Table

| Finding | Evidence | Source Location | Evidence Type |
|:---|:---|:---|:---|
| Semantic scoring superior to keyword matching | Singh et al. (2024) review | PDF p. 2, Section 2.5 & p. 4, Table | Literature finding |
| Acoustic features indicate confidence | Latif et al. (2020) & Rani et al. (2023) review | PDF p. 2, Sections 2.3 & 2.7 | Literature finding |
| Multimodal fusion improves scoring accuracy | Fernandes et al. (2023) & Mahdavian et al. (2022) | PDF p. 3, Sections 2.8 & 2.14 | Literature finding |
| T5 and LLMs for adaptive question generation | Zhang et al. (2022) & Ouyang et al. (2023) | PDF p. 2, Sections 2.2 & 2.6 | Literature finding |
| RL for adaptive question sequencing | Sharma et al. (2024) | PDF p. 3, Section 2.18 | Literature finding |

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

**VERIFIED** (Primary PDF read, 18 reviewed studies verified, author and venue discrepancies from legacy BibTeX documented).
