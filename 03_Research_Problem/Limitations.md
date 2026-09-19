# Research Limitations & Systematic Vulnerabilities

**Project**: ScholarCamp — AI-Powered Placement Preparation and Career Acceleration Platform  
**Core System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `03_Research_Problem/Limitations.md`  
**Corpus Foundation**: `01_Research_Foundation/` (44 Verified Primary Papers, 71 Processed Documents)  
**Cross-Analysis Foundation**: `02_Cross_Analysis/` (20 Authoritative Synthesis Documents)  
**Master Evidence Ledger**: `03_Research_Problem/PHASE_03_EVIDENCE_LEDGER.md`  
**Parent Scope & Assumptions**: `03_Research_Problem/Scope.md`, `03_Research_Problem/Assumptions.md`  
**Date**: September 2026  
**Status**: Authoritative Limitations Disclosure  

---

## 1. Epistemological Stance on Research Limitations

A foundational tenet of the ScholarCamp / PRIE research methodology is absolute intellectual transparency. In strict compliance with Phase 03 directives, **no limitation is disguised as a strength or minimized through rhetorical framing**. 

Every machine learning model, educational dataset, computational pipeline, and evaluation framework operates within defined mathematical and operational boundaries. Documenting these vulnerabilities candidly is essential for preventing algorithmic bias, establishing valid research claims, and setting defensible boundaries for future investigation.

Limitations are systematically classified into seven (7) distinct epistemological tiers:

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            RESEARCH LIMITATION TIERS                             │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 1. Literature Limitations (Gaps and Systemic Blind Spots in Corpus)              │
│ 2. Dataset Limitations (Sample Volumes, Representativeness & Class Imbalance)    │
│ 3. Methodological Limitations (Algorithmic Trade-offs & Theoretical Bounds)      │
│ 4. PRIE Research System Limitations (Engineering Complexities & Bottlenecks)     │
│ 5. Evaluation Limitations (Proxy Metrics & Ground-Truth Subjectivity)            │
│ 6. Generalization Limitations (Cross-Institutional & Disciplinary Boundaries)   │
│ 7. Deployment & Operational Limitations (Compute, Latency & API Dependencies)    │
└──────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Tier 1: Literature Limitations

1. **Systemic Architectural Siloing**: 95.5% of published systems (42 of 44 studies) address only single, isolated sub-problems [EVID-P03-045]. Consequently, there is an acute scarcity of published empirical benchmarks evaluating end-to-end multi-agent educational digital twins, forcing this research to synthesize baselines from adjacent, un-integrated sub-fields.
2. **Prevalence of Incomplete Prototypes**: Multiple published systems in the literature represent early student pilot projects or partial conference monographs (e.g., P10, P30, P38). In particular, P38 (PrepWise) contains unedited template boilerplate in its published conclusion and lacks quantitative metrics, limiting its utility as an authoritative baseline.
3. **Absence of Standardized Educational Benchmarks**: Unlike computer vision (ImageNet) or NLP (GLUE), educational placement readiness lacks a standardized, publicly accessible multi-modal benchmark dataset. Most published studies rely on private, non-replicable institutional databases [P02, P04, P06, P09, P18, P28, P41].

---

## 3. Tier 2: Dataset Limitations

1. **Small Cohort Vulnerabilities**: 14 out of 44 studies in the corpus (31.8%) rely on datasets with fewer than 1,000 student instances (e.g., P01 with N=215; P03 with N=65; P27 with N=48; P38 with N=150) [EVID-P03-001, EVID-P03-003, EVID-P03-027]. Models trained on such small cohorts risk severe sample variance and institutional overfitting.
2. **Severe Class Imbalance**: In real-world educational institutions, negative outcomes (academic failure, course dropouts, or unplaced candidates in top institutions) represent small minorities (15% to 28% of records) [P02, P05, P09, P44]. Despite synthetic oversampling (SMOTE) or cost-sensitive weighting, models remain susceptible to false negatives on borderline candidates.
3. **Self-Selection & Reporting Bias**: Student portfolio data (such as self-reported LinkedIn profiles, uploaded resumes, and voluntary mock interview participation) exhibits self-selection bias: highly motivated students participate more frequently than disengaged students, skewing training distributions [P07, P24].
4. **Historical Data Drift**: Student academic records and corporate hiring standards from 2019–2022 reflect a different macroeconomic hiring environment than post-2024 technology markets, creating temporal concept drift in historical training data [P31, P35].

---

## 4. Tier 3: Methodological Limitations

1. **Inability to Predict Sudden External Shocks**: Machine learning models and Temporal Fusion Transformers cannot predict unobserved external life events (such as sudden family medical crises, acute psychological burnout, financial shocks, or personal emergencies) that suddenly disrupt an otherwise high-performing student's placement outcome [P10].
2. **Macroeconomic Market Independence**: Machine learning classifiers predict placement readiness relative to historical standards, but cannot model sudden macroeconomic tech hiring freezes, mass industry layoffs, or corporate recruitment budget cancellations [P06]. A fully "placement-ready" student may remain unplaced during an industry-wide recession.
3. **Algorithmic Accuracy vs Opacity Trade-Off**: While Gradient Boosted Tree Ensembles (CatBoost) natively handle categorical features, deep tabular neural architectures (such as 5-layer MLPs in P34) require 4x more training time for negligible accuracy gains (+0.8%) while introducing severe black-box opacity that resists intuitive stakeholder explanation.
4. **Counterfactual Optimization Latency**: While distance-constrained counterfactual algorithms (DiCE) generate actionable recourses, counterfactual optimization over 22-dimensional mixed-integer feature spaces requires 1.8 to 2.4 seconds per candidate [P19], making real-time interactive parameter scrubbing computationally expensive.

---

## 5. Tier 4: PRIE Research System Limitations

1. **Multi-Subsystem Coordination Overhead**: Synchronizing four heterogeneous AI subsystems (LayoutLMv3 ATS, WebRTC interview streaming, Docker code execution, and Neo4j graph traversal) introduces significant integration complexity and microservice orchestration latency [P41].
2. **WebAssembly Video Processing Hardware Dependency**: Executing MediaPipe 3D FaceMesh landmark tracking entirely within the client's web browser offloads server compute, but relies on the student's local laptop CPU/GPU. Older hardware or unaccelerated browser configurations may experience frame rate drops below 20 FPS, reducing facial action unit extraction fidelity [P03, P14].
3. **Audio Noise & Acoustic Vulnerabilities**: Real-time acoustic prosody extraction via openSMILE (pitch jitter, shimmer, pause duration) is sensitive to poor-quality built-in laptop microphones, ambient room reverberation, and background household noise, which can artificially distort candidate composure scores [P03, P14].
4. **Code Sandboxing Execution Limits**: To prevent denial-of-service and malicious execution on host servers, the Docker container sandbox enforces strict execution timeouts ($\le 3.5$s) and memory caps ($\le 256$MB). Valid candidate solutions utilizing computationally intensive algorithms or large test fixtures may experience false timeout rejections [P28].

---

## 6. Tier 5: Evaluation Limitations

1. **Subjectivity of Human Panel Ground Truth**: Evaluating communication clarity, interview confidence, and behavioral composure relies on human recruiter scoring rubrics. Even with standardized rubrics, human evaluators exhibit subjective variation and unconscious cognitive biases (e.g., regional accent bias, halo effects) [P15, P27].
2. **Proxy Nature of Automated RAG Triad**: While automated RAG Triad metrics (Faithfulness, Answer Relevancy) provide scalable evaluation of academic advising, they serve as computational proxies and cannot fully substitute for continuous Subject Matter Expert pedagogical audits [P20].
3. **Lack of Multi-Year Longitudinal Career Tracking**: Due to academic research timelines, the evaluation of PRIE is bounded by the undergraduate placement season (Year 4). The system cannot evaluate long-term career outcomes (such as 3-year promotion velocity, job retention, or mid-career transitions).

---

## 7. Tier 6: Generalization Limitations

1. **Disciplinary Confinement to Technical Disciplines**: The PRIE architecture is explicitly engineered for Computer Science, Information Technology, and Software Engineering roles where technical coding, algorithmic problems, and structured technical resumes dominate. It cannot be generalized to non-technical disciplines (e.g., Fine Arts, Humanities, Clinical Medicine, or Law) without fundamental restructuring of assessment rubrics, knowledge graphs, and execution sandboxes.
2. **Institutional Tier Transferability**: A model calibrated on Tier-1 institutions (where 90% of students achieve campus placement in high-paying product firms) cannot be naively transferred to Tier-3 regional colleges without domain adaptation and recalibration of baseline feature weights [P07, P24].
3. **Language and Linguistic Boundaries**: The current conversational interview core, resume parsing pipeline, and question generation engines operate exclusively in English. Candidate evaluation in multilingual or regional vernacular contexts (e.g., Hindi, Tamil, Spanish, Bahasa) remains outside current capabilities [P24, P28].

---

## 8. Tier 7: Deployment & Operational Limitations

1. **Cloud Foundation API Dependency & Latency Spikes**: The real-time conversational interview bot relies on cloud-hosted foundation model APIs (Google Gemini 1.5 Flash). External cloud network latency spikes, regional API outages, or unexpected vendor token pricing modifications represent operational risks beyond institutional control [P23, P29].
2. **On-Premise GPU Infrastructure Requirements**: While local 4-bit quantized open-weights models (LLaMA-3-8B in P21) eliminate external API fees and protect student privacy, running on-premise inference requires institutions to invest in dedicated GPU servers (e.g., NVIDIA RTX 4060 or A10G), which may exceed the budget of under-resourced regional engineering colleges.
3. **Regulatory and Compliance Overhead**: Maintaining continuous compliance with regional data protection statutes (POPIA in South Africa, GDPR in Europe, DPDP in India) requires institutional data officers, regular cryptographic key rotations, and audited log purges, adding administrative overhead to campus IT teams [P02].

---

## 9. Limitations Summary Matrix

| Limitation Tier | Primary Vulnerability | Direct Impact / Severity | Literature Evidence Grounding |
|:---|:---|:---:|:---:|
| **Literature** | 95.5% single-module fragmentation in published studies | High | Cross-Paper Synthesis, P01–P44 |
| **Dataset** | Small sample sizes (N < 1,000 in 31.8% of studies) | High | P01, P03, P27, P38 |
| **Methodological** | Inability to predict sudden external personal shocks | Medium | P10 (Rajesh et al.) |
| **System Engineering** | Latency vs security trade-offs in Docker code compilation | Medium | P28 (Vachkal et al. IndusAI) |
| **Evaluation** | Recruiter panel subjectivity in communication scoring | Medium | P15, P27 (Inamdar, Zhang) |
| **Generalization** | Confinement to CS/IT software engineering disciplines | High | Scope Specification, P13, P28 |
| **Deployment** | Cloud API latency spikes & on-premise GPU cost | Medium | P21, P23, P29 |
