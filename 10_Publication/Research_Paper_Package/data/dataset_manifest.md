# PRIE Dataset Manifest & Experimental Specifications

This document defines the schemas, experimental splits, benchmark seeds, and source data used in the empirical validation of the **Placement Readiness Intelligence Engine (PRIE)**.

---

## 1. Tabular Synthetic Benchmark: `DS-SYNTH-01`
- **Total Population ($N$)**: 2,500 student records.
- **Dimensionality**: 22 continuous and categorical indicators mapped into the canonical Student Profile Vector ($\mathbf{x}_{\text{spv}} \in [0.0, 1.0]^{22}$) plus an explicit observation mask ($\mathbf{m} \in \{0, 1\}^{22}$).
- **Data Partitions**: Stratified 80 / 10 / 10 split:
  - Training Set: $N_{\text{train}} = 2,000$
  - Validation Set (Platt Calibration): $N_{\text{val}} = 250$
  - Hold-out Test Set: $N_{\text{test}} = 250$
- **Deterministic Evaluation Seeds**: 5-seed stratified cross-validation ($S \in \{42, 123, 456, 789, 2026\}$).
- **Target Variable**: Placement readiness state $Y \in \{0, 1\}$ assigned via non-linear composite competency functions including realistic noise.

### Feature Mapping (22 Dimensions)
| Feature Index | Identifier | Description | Data Type / Domain | Monotonicity / Invariance |
|:---:|:---|:---|:---:|:---:|
| $f_1$ | `cgpa` | Cumulative Grade Point Average | Normalized $[0, 1]$ | Monotonic non-decreasing |
| $f_2$ | `backlogs` | Historical active backlogs count | Integer normalized | Penalty feature |
| $f_3$ | `internship_months` | Industrial internship duration | Continuous $[0, 1]$ | Monotonic non-decreasing |
| $f_4$ | `skill_count` | Verified technical skills count | Integer normalized | Monotonic non-decreasing |
| $f_5$ | `certification_count` | Professional certifications count | Integer normalized | Monotonic non-decreasing |
| $f_6$ | `project_count` | Capstone/portfolio project count | Integer normalized | Monotonic non-decreasing |
| $f_7$ | `aptitude_score` | Quantitative/logical test score | Continuous $[0, 1]$ | Monotonic non-decreasing |
| $f_8$ | `dsa_score` | Data Structures & Algorithms score | Continuous $[0, 1]$ | Monotonic non-decreasing |
| $f_9$ | `dbms_score` | Database Management Systems score | Continuous $[0, 1]$ | Monotonic non-decreasing |
| $f_{10}$ | `cn_score` | Computer Networks score | Continuous $[0, 1]$ | Monotonic non-decreasing |
| $f_{11}$ | `programming_score` | Hands-on coding assessment score | Continuous $[0, 1]$ | Monotonic non-decreasing |
| $f_{12}$ | `resume_ats_score` | Resume ATS formatting score | Continuous $[0, 1]$ | Remediable |
| $f_{13}$ | `cosine_similarity` | S-BERT Resume-JD cosine similarity | Continuous $[0, 1]$ | Remediable |
| $f_{14}$ | `gap_score` | Missing competency gap penalty | Continuous $[0, 1]$ | Remediable |
| $f_{15}$ | `consistency_score` | Platform login consistency | Continuous $[0, 1]$ | Behavioral |
| $f_{16}$ | `has_internship` | Binary internship verification | Binary $\{0, 1\}$ | Monotonic non-decreasing |
| $f_{17}$ | `branch_encoded` | Academic engineering department | Categorical $\{0, 1, 2, 3\}$ | **IMMUTABLE (100.0% Locked)** |
| $f_{18}$ | `target_role_encoded`| Target corporate role difficulty | Categorical / weight | Target parameter |
| $f_{19}$ | `assessment_attempts`| Diagnostic assessment count | Integer normalized | Monotonic non-decreasing |
| $f_{20}$ | `behavior_score` | Composite mock interview demeanor | Continuous $[0, 1]$ | Remediable via coaching |
| $f_{21}$ | `engagement_score` | Portal engagement intensity | Continuous $[0, 1]$ | Behavioral |
| $f_{22}$ | `roadmap_completion`| Roadmap milestone completion rate | Continuous $[0, 1]$ | Behavioral milestone |

---

## 2. Multimodal Mock Interview Benchmark: `DS-INTERVIEW-SIM`
- **Total Sessions ($N$)**: 50 synchronized simulated technical interview recordings.
- **Modalities Measured**:
  1. **Acoustic Prosody ($M_{\text{audio}}$)**: Pitch $F_0$, jitter, shimmer, tempo, and harmonic-to-noise ratio.
  2. **Visual Composure ($M_{\text{video}}$)**: Facial bounding box stability, eye-gaze persistence, blink cadence, head pose jitter.
  3. **Speech Clarity ($M_{\text{speech}}$)**: Words Per Minute (WPM), disfluent filler phrase density, Type-Token Ratio (TTR).
- **Fusion Formula**:
  $$S_{\text{interview}} = 0.35 \cdot M_{\text{audio}} + 0.35 \cdot M_{\text{video}} + 0.30 \cdot M_{\text{speech}}$$
- **Latency**: Mean turn latency $1.18 \pm 0.14$ seconds.

---

## 3. Curriculum Knowledge Graph: `cs_concept_dag.json`
- **Nodes ($|\mathcal{V}|$)**: 38 computer science concepts across 5 cognitive difficulty tiers (Foundational, Core Structures, Advanced Algorithms, Systems, Applied Engineering).
- **Directed Edges ($|\mathcal{E}|$)**: 52 prerequisite constraints.
- **Topological Invariant**: $\forall (u, v) \in \mathcal{E}, \; \text{Index}_{\mathcal{R}}(u) < \text{Index}_{\mathcal{R}}(v)$.

---

## 4. Resume Document Benchmark: `DS-RESUME-BENCH`
- **Total Resumes ($N$)**: 100 engineering resumes.
  - 50 single-column standard documents.
  - 50 complex multi-column documents with sidebars and table layouts.
- **Ground Truth Entities**: Contact info, education, work experience, technical skills, projects, certifications.
- **Key Metrics**: Entity Extraction Macro-F1 ($0.8421$), multi-column section interleaving rate ($4.2\%$).

---

## 5. RAG Evaluation Corpus
- **Indexed Chunks**: 1,420 technical documentation passages.
- **Embeddings**: 384-dimensional dense vectors (`all-MiniLM-L6-v2`).
- **Gating Threshold**: Cosine similarity $\tau = 0.70$.
- **Adversarial Benchmark**: 50 in-domain queries, 50 adversarial out-of-domain prompt injections ($100.0\%$ rejection).
