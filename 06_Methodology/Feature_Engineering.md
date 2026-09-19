# Feature Engineering: Mathematical Derivations, Interaction Terms & Temporal Metrics

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `06_Methodology/Feature_Engineering.md`  
**Phase**: 06 — Research Methodology  
**Status**: Authoritative Feature Engineering Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`), Phase 05 (`05_PRIE_Architecture/`)  
**Date**: September 2026  

---

## 1. Feature Engineering Philosophy & Grounding

In alignment with Phase 04 Feature Traceability (`Feature_Traceability.md`), PRIE derives compound interaction and temporal features designed to capture latent candidate employability traits that raw academic transcripts fail to represent (`RG1`, `RG2`).

Every derived feature satisfies four strict scientific criteria:
1. **Mathematical Interpretability**: A rigorous formula defining the derivation.
2. **Zero Lookahead Leakage**: Computable strictly using historical telemetry available at inference time.
3. **Empirical Rationale**: Grounded in published educational data mining and recruitment literature.
4. **Invariant Mapping**: Feeds directly into the 22-dimensional Student Profile Vector (`F01`–`F22`).

---

## 2. Exhaustive Derivations of Engineered Features

---

### Derived Feature 1: Normalized Skill Deficit Metric (`F15: gap_score`)
- **Mathematical Formula**:
  $$	ext{gap\_score}(s, j) = rac{1}{\sum_{k} w_k} \sum_{k \in \mathcal{K}_j} w_k \cdot \max\Big( 0, \mathcal{R}_j(k) - \mathcal{C}_s(k) \Big)$$
  where:
  - $\mathcal{K}_j$ is the set of required technical competencies for target corporate role $j$.
  - $w_k$ is the market importance weight of skill $k$ derived from tech job descriptions.
  - $\mathcal{R}_j(k) \in [0.0, 1.0]$ is the minimum mastery threshold required by job role $j$.
  - $\mathcal{C}_s(k) \in [0.0, 1.0]$ is candidate $s$'s verified competency score in skill $k$.
- **Source Modalities**: Diagnostic Assessments (`M03`) + Resume Extraction (`M02`) + Corporate JDs.
- **Downstream Consumer**: Predictor (`M06`), XAI Engine (`M07`), Recommendation Engine (`M08`).
- **Literature Grounding**: Patel & Nair 2024 (`Paper04`), Tan 2024 (`Paper16`), Qin 2020 (`Paper35`).

---

### Derived Feature 2: Longitudinal Habit Persistence & Login Cadence (`F16: consistency_score`)
- **Mathematical Formula**:
  $$	ext{consistency\_score}(s) = \exp\Big( -\lambda \cdot 	ext{Var}( \Delta t_s ) \Big) 	imes \left( 1 - rac{	ext{Gaps}_{>7	ext{d}}(s)}{W_{	ext{total}}} ight)$$
  where:
  - $\Delta t_s$ is the inter-session login interval distribution (in days) across observation window $W_{	ext{total}}$.
  - $	ext{Var}(\Delta t_s)$ is the variance of inter-session login intervals (quantifying habit irregularity).
  - $	ext{Gaps}_{>7	ext{d}}$ is the count of unexcused multi-day inactivity gaps exceeding 7 days.
  - $\lambda$ is a decay sensitivity constant ($\lambda = 0.25$).
- **Source Modalities**: LMS Login Telemetry & Formative Practice Logs (`M11`).
- **Downstream Consumer**: Predictor (`M06`), Temporal Sequence Store (`M11`), Faculty Dashboard (`M12`).
- **Literature Grounding**: Van Wyk & Du Plessis 2025 (`Paper02`), Chen 2024 (`Paper05`), Al-Shabandar 2019 (`Paper33`).

---

### Derived Feature 3: Paralinguistic Delivery Composure (`F20: behavior_score`)
- **Mathematical Formula**:
  $$	ext{behavior\_score}(s) = 0.40 \cdot \Psi_{	ext{speech}}(s) + 0.35 \cdot \Omega_{	ext{gaze}}(s) + 0.25 \cdot \Phi_{	ext{head}}(s)$$
  where:
  - $\Psi_{	ext{speech}} = 	ext{clip}\left( 1.0 - rac{	ext{FillerWordCount}}{	ext{TotalWordCount}} 	imes 10, 0, 1 ight) 	imes 	ext{NormalPaceScore}$
  - $\Omega_{	ext{gaze}} = rac{1}{T} \sum_{t=1}^T \mathbb{I}\Big( |	heta_{	ext{gaze}}(t)| \le 15^\circ \Big)$ (Proportion of time maintaining forward eye contact).
  - $\Phi_{	ext{head}} = 1.0 - 	ext{clip}\left( 	ext{std}(	ext{head\_pitch}) + 	ext{std}(	ext{head\_yaw}), 0, 1 ight)$ (Head stability index).
- **Source Modalities**: Whisper STT Linguistic Transcript + Client MediaPipe Landmarks (`M05`).
- **Downstream Consumer**: Invariant SPV Aggregator (`M01`), Predictor (`M06`).
- **Literature Grounding**: Deshmukh 2025 (`Paper14`), Inamdar 2025 (`Paper15`), Amarnath 2025 (`Paper27`).

---

### Derived Feature 4: Composite Learning Engagement Intensity (`F21: engagement_score`)
- **Mathematical Formula**:
  $$	ext{engagement\_score}(s) = rac{1}{4} \left[ rac{\log(1 + T_{	ext{active}})}{\log(1 + T_{	ext{max}})} + rac{N_{	ext{quiz\_sub}}}{N_{	ext{quiz\_target}}} + rac{N_{	ext{code\_sub}}}{N_{	ext{code\_target}}} + \mathcal{H}_{	ext{interaction}}(s) ight]$$
  where:
  - $T_{	ext{active}}$ is total cumulative interactive platform duration in minutes.
  - $N_{	ext{quiz\_sub}}, N_{	ext{code\_sub}}$ are completed assessment volumes relative to cohort targets.
  - $\mathcal{H}_{	ext{interaction}}$ is normalized Shannon entropy across platform resource categories.
- **Source Modalities**: LMS Interaction Streams & Telemetry Rollup Worker (`M11`).
- **Downstream Consumer**: Predictor (`M06`), Digital Twin State Engine (`M12`).
- **Literature Grounding**: Azeez 2026 (`Paper44`), Chen 2024 (`Paper05`).

---

### Derived Feature 5: Dense Semantic Resume Alignment (`F14: cosine_similarity`)
- **Mathematical Formula**:
  $$	ext{cosine\_similarity}(s, j) = rac{\mathbf{e}_{	ext{resume}}^{(s)} \cdot \mathbf{e}_{	ext{jd}}^{(j)}}{\|\mathbf{e}_{	ext{resume}}^{(s)}\|_2 \|\mathbf{e}_{	ext{jd}}^{(j)}\|_2}$$
  where:
  - $\mathbf{e}_{	ext{resume}}^{(s)}$ is the 384-dimensional dense semantic embedding generated by `all-MiniLM-L6-v2` over parsed resume sections.
  - $\mathbf{e}_{	ext{jd}}^{(j)}$ is the 384-dimensional embedding of target corporate Job Description $j$.
- **Source Modalities**: ATS Parsing Engine (`M02`) via Sentence-BERT.
- **Downstream Consumer**: SPV Aggregator (`M01`), Predictor (`M06`).
- **Literature Grounding**: Mishra 2025 (`Paper11`), Roy 2024 (`Paper12`), Verma & Mehta 2026 (`Paper17`).
