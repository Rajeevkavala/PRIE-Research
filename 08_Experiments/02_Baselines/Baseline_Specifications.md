# Authoritative Baseline Specifications
**Project**: ScholarCamp / PRIE  
**Phase**: Phase 08 — Experiments  

## 1. Classification Baselines (EXP-01)
- **BL-01: Logistic Regression**: Scikit-Learn `LogisticRegression(max_iter=1000, C=1.0, penalty='l2', solver='lbfgs', random_state=seed)`. Operating on standardized canonical 22D SPV.
- **BL-02: Random Forest**: Scikit-Learn `RandomForestClassifier(n_estimators=100, max_depth=10, min_samples_split=5, class_weight='balanced', random_state=seed, n_jobs=-1)`.

## 2. ATS Parsing Baselines (EXP-04)
- **BL-ATS-01: Flat Regex Keyword Extractor**: Linear text parser concatenating tokens across columns using standard regex boundaries without coordinate information.

## 3. Mock Interview Baselines (EXP-03)
- **BL-INT-01: Audio-Only Prosody**: Librosa acoustic pipeline alone ($F_0$, jitter, shimmer).
- **BL-INT-02: Video-Only Composure**: OpenCV visual tracking alone (eye contact, head pose).
- **BL-INT-03: Speech-Only Clarity**: Faster-Whisper ASR alone (WPM, filler rate).

## 4. Roadmap Scheduling Baselines (EXP-05)
- **BL-DAG-01: Randomized Milestone Ordering**: Permutation shuffle of curriculum topics without dependency constraint enforcement.

## 5. Curriculum RAG Baselines (EXP-06)
- **BL-RAG-01: Zero-Shot LLM Generation**: Unconstrained prompt execution with zero document retrieval and zero cosine hallucination gating.
