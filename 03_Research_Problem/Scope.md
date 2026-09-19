# Research Scope & Boundary Specifications

**Project**: ScholarCamp — AI-Powered Placement Preparation and Career Acceleration Platform  
**Core System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `03_Research_Problem/Scope.md`  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers, 71 Processed Documents)  
**Cross-Analysis Foundation**: `02_Cross_Analysis/` (20 Authoritative Synthesis Documents)  
**Master Evidence Ledger**: `03_Research_Problem/PHASE_03_EVIDENCE_LEDGER.md`  
**Parent Problem Statement**: `03_Research_Problem/Problem_Statement.md`  
**Date**: September 2026  
**Status**: Authoritative Scope Specification  

---

## 1. Scope Formulation Principles

To maintain scientific rigor, methodological feasibility, and engineering containment, the scope of the ScholarCamp / PRIE research project is explicitly defined and strictly bounded. In accordance with Phase 03 directives:
1. **Evidence-Grounded Boundaries**: The scope aligns with the technological, empirical, and institutional realities substantiated by the 44-paper verified corpus.
2. **Defensive Containment**: Unnecessary expansion into generic education technology (e.g., broad K-12 schooling, non-technical degree programs, or speculative VR/metaverse interfaces) is explicitly excluded.
3. **Explicit Dual-Classification**: Every research dimension is categorized under either **INCLUDED SCOPE** or **EXPLICIT EXCLUSIONS**.

---

## 2. Granular Inclusions Across Research Dimensions

### 2.1 Included Research Problems
- Architectural and functional fragmentation across career readiness point solutions (`CG1`).
- The descriptive-to-prescriptive divide in educational explainable AI (`CG2`).
- Point-in-time retrospective modeling bias versus continuous longitudinal state tracking (`CG3`).
- Spatial layout destruction and Named Entity Recognition degradation in multi-column resume parsing (`CG4`).
- Conversational turn latency ($>1.5$s) and modality disconnection in multimodal technical mock interviews (`CG5`).
- Prerequisite-blind recommendation and hallucinated academic guidance in campus advising (`CG6`).
- Superficial Bloom's Level 1–2 factual recall dominance and distractor ambiguity in automated assessment generation (`CG7`).
- Human stakeholder validation deficits and regulatory privacy non-compliance in educational AI (`CG8`).

### 2.2 Included Student Population
- Undergraduate engineering and technology students (B.Tech / B.E. / B.S. in Computer Science, Information Technology, Electronics & Communication, and Data Science).
- Primary demographic focus: Students in their pre-final (Year 3) and final (Year 4) years actively preparing for corporate campus placements and off-campus software recruitment.
- Institutional focus: Tier-1, Tier-2, and Tier-3 accredited engineering colleges in emerging and transitional higher education markets (primarily India, Southeast Asia, and South Africa, reflecting P01, P04, P06, P07, P09, P22, P24, P41).

### 2.3 Included Readiness Dimensions
- **Technical & Algorithmic Competence**: Data structures, algorithms, runtime complexity, object-oriented design, database queries, and system architectures.
- **Applied Coding & Software Engineering**: Problem-solving velocity, clean code syntax, Abstract Syntax Tree (AST) structure, unit test pass rates, and GitHub repository maturity.
- **Communication & Verbal Fluency**: Articulation clarity, speaking pace (words per minute), pause-to-speech ratio, filler-word frequency, and acoustic pitch variability ($F_0$).
- **Non-Verbal Composure**: Sustained eye contact ratio, head pose stability (yaw/pitch/roll), and emotional composure under technical questioning.
- **Academic Progression & Engagement**: Semester GPA trajectories, credit completion velocity, LMS portal clickstream momentum, and assignment submission punctuality.

### 2.4 Included PRIE Subsystems & Components
- **Spatial ATS Engine**: LayoutLMv3 spatial vision-language document parser + SBERT-BM25 hybrid Reciprocal Rank Fusion matcher + Doc2Vec implicit skill miner.
- **Multimodal Mock Interview Engine**: WebRTC bidirectional audio streaming gateway + Gemini 1.5 Flash conversational core + openSMILE real-time acoustic prosody extractor + MediaPipe 3D FaceMesh WebAssembly tracker.
- **Isolated Code Execution Sandbox**: Ephemeral rootless Docker containers with cgroup resource bounding, read-only root filesystems, and zero network egress.
- **Adaptive Question Generation (AQG) Engine**: Neo4j Causal Concept DAG + Bloom's Levels 3–5 fine-tuned LLaMA-3 model + dual-agent distractor rationale verifier.
- **Placement Digital Twin & Dynamic Analytics**: 22-dimensional continuous latent state vector + Temporal Fusion Transformer (TFT) multi-horizon forecaster + CatBoost tabular outcome classifier.
- **Prescriptive XAI Engine**: Distance-constrained DiCE counterfactual optimization bounded by weekly cognitive load ($\le 15$ hrs/week) + TreeSHAP global mentor plots.
- **Private Syllabus RAG Tutor**: Local 4-bit quantized LLaMA-3 + ChromaDB vector store + Cohere cross-encoder re-ranker evaluated via the RAG Triad.
- **Ethical Privacy Shield**: Cryptographic tokenized data anonymization + role-based access control complying with POPIA and GDPR mandates.

### 2.5 Included Data Modalities
- **Tabular Data**: Longitudinal academic records, grade point averages, entrance ranks, and institutional demographic variables.
- **Unstructured Text**: PDF/DOCX resume documents, job description text, lecture slide transcripts, syllabus curriculum documents, and code commit messages.
- **Audio Signals**: Real-time microphone audio streams processed into 16kHz PCM chunks for Whisper ASR transcription and 88 openSMILE acoustic prosody features.
- **Video & Visual Data**: 2D PDF document bounding box coordinates; 468 3D facial mesh landmarks and eye-gaze vectors extracted via client-side WebAssembly.
- **Graph & Relational Data**: Neo4j property graph nodes and edges representing course prerequisite hierarchies, competency taxonomies, and multi-stakeholder interactions.
- **Temporal Sequences**: Multi-horizon weekly clickstream logs, problem-solving timestamps, and time-decayed assessment scores.

### 2.6 Included Prediction Tasks
- Binary Campus Placement Likelihood ($\text{Placed} \in \{0, 1\}$).
- Multi-Tier Placement Compensation Banding (e.g., Core Product Engineering vs. Service IT vs. Elite Tier-1).
- Multi-Horizon Early Academic & Placement Risk Forecasting at Week 3, Week 6, and Week 12 of a semester.
- Real-world placement offer simulation fidelity within the Triangular Digital Twin.

### 2.7 Included Recommendation Tasks
- Topological course and elective path optimization via Multi-Objective Ant Colony Optimization (MACO) over Neo4j prerequisite DAGs.
- Personalized skill gap remediation pathways linking candidate resume deficits to specific micro-learning modules.
- Dynamic assessment recommendations routing student mock interview weaknesses into targeted adaptive quizzes.

### 2.8 Included Explainability & Diagnostic Frameworks
- Prescriptive, distance-constrained DiCE counterfactuals generating student-facing "what-if" action cards.
- Game-theoretic TreeSHAP feature attribution generating global summary plots and dependency charts for institutional faculty mentors.
- Temporal self-attention weight heatmaps from Temporal Fusion Transformers identifying exact weeks of student engagement divergence.

### 2.9 Included Evaluation Protocols
- Computational Machine Learning Metrics: Macro-F1, Precision-Recall AUC (PR-AUC), ROC-AUC, 10-fold cross-validation.
- Information Retrieval Metrics: Mean Reciprocal Rank (MRR@10), Precision@K, NDCG@10.
- Psychometric & Natural Language Metrics: Item Difficulty ($p$), Item Discrimination ($D$), RAG Triad (Faithfulness, Relevancy, Groundedness).
- Systems Engineering Metrics: Conversational turn latency (ms), frame processing rate (FPS), container execution turnaround (s).
- Human-in-the-Loop Usability: System Usability Scale (SUS), Pearson/Spearman recruiter rubric correlation, randomized task completion trials.

---

## 3. Explicit Exclusions (Out of Scope)

To prevent mission creep and maintain scientific containment, the following domains, technologies, and tasks are strictly **EXCLUDED** from the ScholarCamp / PRIE research project:

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             EXPLICIT RESEARCH EXCLUSIONS                         │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ Category                      │ Excluded Scope & Operational Boundaries          │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 1. Student Populations        │ Non-engineering disciplines (Arts, Humanities,   │
│                               │ Medicine, Law); K-12 primary/secondary schooling;│
│                               │ Executive corporate MBA retraining.              │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 2. Hardware Environments      │ Ultra-low-power microcontrollers; legacy feature │
│                               │ phones; offline edge IoT devices (CG10).         │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 3. XR / Metaverse Modalities  │ Virtual Reality (VR) headsets; immersive 3D      │
│                               │ avatars; tactile haptic sensory feedback.        │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 4. Autonomous Replacement     │ Autonomous replacement of university placement   │
│                               │ cells, faculty advisors, or corporate HR panels  │
│                               │ without human-in-the-loop oversight (CG9).       │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 5. Macroeconomic Modeling     │ Forecasting global recession cycles, currency    │
│                               │ fluctuations, or international visa policies.    │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 6. Psychological Diagnostics  │ Clinical diagnostic evaluation of major mental   │
│                               │ health disorders or deep psychopathology.        │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 7. Proprietary Core Sandboxing│ Deploying untrusted candidate code directly on   │
│                               │ host bare-metal servers without Docker.          │
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

1. **Non-Technical & Non-Engineering Disciplines**: Excludes degree programs where technical coding, algorithmic problem-solving, and formal prerequisite graphs do not govern hiring (e.g., Fine Arts, Literature, Clinical Medicine, Nursing, Law).
2. **K-12 and Primary Education**: Excludes pediatric learning analytics, high school standardized college entrance coaching, and gamified childhood tutoring.
3. **Hardware-Constrained Microcontroller Deployments**: Excludes running transformer models locally on smartwatches, embedded IoT microcontrollers, or non-smartphone devices lacking modern web browsers.
4. **Immersive Virtual Reality (VR) & Metaverse Hardware**: Excludes Oculus/Apple Vision Pro head-mounted displays, spatial 3D avatar rendering, and biometric EEG/GSR electrodes in production (retaining pure standard webcams and microphones).
5. **Fully Autonomous University Replacement**: Explicitly excludes autonomous student grading, automated hiring rejection without human recruiter review, or replacing human academic advising offices.
6. **Macroeconomic Market Forecasting**: Excludes attempting to predict geopolitical hiring freezes, corporate layoffs, stock market shifts, or national labor policy legislation.
7. **Clinical Psychological Diagnostics**: Excludes clinical diagnosis of severe clinical depression, ADHD, or generalized anxiety disorders, restricting psychometric evaluation strictly to situational interview stress and speech fluency.

---

## 4. Scope Summary Matrix

| Research Dimension | In-Scope Inclusion | Out-of-Scope Exclusion | Literature Evidence Grounding |
|:---|:---|:---|:---:|
| **Target Population** | Undergraduate Engineering (CS/IT/ECE) | Arts, Humanities, Medical, K-12 | P01, P04, P06, P07, P09, P22 |
| **Document Processing**| LayoutLMv3 spatial 2D parsing + SBERT-BM25 | Flat linear regex/TF-IDF scrapers | P12, P17, P42 |
| **Interview Coaching** | WebRTC voice + MediaPipe vision + Docker code | VR avatars, EEG electrodes | P03, P14, P15, P28, P29 |
| **Predictive Modeling**| Dynamic Temporal Fusion Transformers + CatBoost| Static single-point CGPA regression | P08, P22, P44 |
| **Explainable AI** | Distance-constrained DiCE counterfactuals | Unconstrained DiCE, pure descriptive SHAP| P02, P18, P19, P32 |
| **Question Generation**| Bloom's Levels 3–5 on Neo4j Causal DAGs | Bloom's Level 1–2 ungrounded recall | P25, P26, P39 |
| **Governance & Ethics**| POPIA / GDPR cryptographic tokenization | Plaintext logging of biometric audio/video| P02, P40, P41 |
