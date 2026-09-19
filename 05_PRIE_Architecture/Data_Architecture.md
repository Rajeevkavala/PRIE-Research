# Data Architecture: Logical Entities, Relationships & Data Governance

**Project**: ScholarCamp — AI-Powered Placement Readiness Ecosystem  
**Core Research System**: PRIE — Placement Readiness Intelligence Engine  
**Document**: `05_PRIE_Architecture/Data_Architecture.md`  
**Phase**: 05 — PRIE Architecture  
**Status**: Authoritative Logical Data Architecture Specification  
**Corpus Grounding**: Phase 01 (`01_Research_Foundation/`), Phase 02 (`02_Cross_Analysis/`), Phase 03 (`03_Research_Problem/`), Phase 04 (`04_Research_Evidence/`)  
**Date**: September 2026  

---

## 1. Architectural Scope & Logical Data Philosophy

The Data Architecture defines the logical entities, semantic relationships, lifecycles, and data protection boundaries governing PRIE.

**Methodological Boundary Notice**:
In accordance with Section 28, Phase 05 defines the **Logical Data Architecture**. Final physical database DDLs, SQL migration scripts, indexing strategies, and table partitioning are reserved for **Phase 07 (Implementation)**.

**Core Data Governance Principles**:
1. **Entity Justification**: Only data entities scientifically required by the M01–M12 module architecture are defined. Zero arbitrary entities are introduced.
2. **Data Minimization & Ephemerality**: In strict compliance with `DD-005` and `DD-011`, raw audio and video streams are completely ephemeral; **no raw media files are permanently persisted**.
3. **Temporal Immutability**: Historical SPV feature snapshots are append-only to support longitudinal forecasting without look-ahead data leakage.

---

## 2. Logical Entity-Relationship Overview

```
┌──────────────┐ 1      * ┌───────────────────────────┐ 1       * ┌───────────────────────────┐
│   Student    ├─────────►│   StudentProfileVector    ├──────────►│        Prediction         │
│              │          │  (22-Dim Tensor Snapshots)│           │  (Track 1 & Track 2 TFT)  │
└──────┬───────┘          └─────────────┬─────────────┘           └─────────────┬─────────────┘
       │ 1                               │ 1                                     │ 1
       │                                 │                                       │
       ▼ *                               ▼ *                                     ▼ 1
┌──────────────┐          ┌───────────────────────────┐           ┌───────────────────────────┐
│AcademicRecord│          │         SkillGap          │           │        Explanation        │
│(SIS Transcr) │          │(Weighted Euclidean Vector)│           │ (TreeSHAP Attrib & DiCE)  │
└──────────────┘          └─────────────┬─────────────┘           └─────────────┬─────────────┘
                                        │ 1                                     │ 1
                                        ▼ 1                                     ▼ 1
                          ┌───────────────────────────┐ 1       * ┌───────────────────────────┐
                          │      Recommendation       ├──────────►│          Roadmap          │
                          │   (Topological Path)      │           │(Sprints & Verified Milest)│
                          └───────────────────────────┘           └─────────────┬─────────────┘
                                                                                │ 1
                                                                                ▼ *
┌──────────────┐ 1      * ┌───────────────────────────┐ 1       * ┌───────────────────────────┐
│    Resume    ├─────────►│      ResumeAnalysis       │           │        Assessment         │
│(Encrypted Doc│          │ (LayoutLMv3 Bbox & SBERT) │           │ (Diagnostic Quizzes)      │
└──────────────┘          └───────────────────────────┘           └─────────────┬─────────────┘
                                                                                │ 1
┌──────────────┐ 1      * ┌───────────────────────────┐                         ▼ *
│  Interview   ├─────────►│     InterviewAnalysis     │           ┌───────────────────────────┐
│(Session Meta)│          │ (Whisper Text & Telemetry)│           │      QuestionAttempt      │
└──────────────┘          └───────────────────────────┘           │  (Misconception Distractor│
                                                                  └───────────────────────────┘
```

---

## 3. Detailed Logical Entity Specifications

---

### 1. `Student`
- **Purpose**: Represents the core human candidate entity within the educational institution.
- **Key Fields**: `student_id` (UUID, PK), `institution_id` (UUID), `department_code` (Enum: CS, IT, ECE), `enrollment_year` (Int), `created_at` (Timestamp).
- **Relationships**: 1-to-many with `StudentProfileVector`, `AcademicRecord`, `Resume`, `Interview`, `Roadmap`.
- **Source**: University Student Information System (SIS) onboarding sync.
- **Lifecycle**: Active throughout enrollment (Years 1–4); archived upon graduation.
- **Sensitivity**: High (Student PII; strictly isolated under FERPA/POPIA).
- **Retention**: Retained for 5 academic years post-graduation for institutional accreditation.

---

### 2. `StudentProfileVector`
- **Purpose**: Versioned, immutable snapshot of the 22-dimensional feature tensor representing student placement readiness at discrete observation epochs.
- **Key Fields**: `spv_id` (UUID, PK), `student_id` (UUID, FK), `epoch_timestamp` (Timestamp), `F01_cgpa` through `F22_roadmap_completion_rate` (Floats), `confidence_mask` (Bitmask[22]).
- **Relationships**: Many-to-1 with `Student`; 1-to-many with `Prediction`.
- **Source**: Aggregated and compiled by `M01` (`CMP-INT-SPV`).
- **Lifecycle**: Immutable append-only historical log.
- **Sensitivity**: Medium (Academic and technical telemetry metrics).
- **Retention**: Retained indefinitely as anonymized research benchmark data.

---

### 3. `AcademicRecord`
- **Purpose**: Course-by-course transcript grades, credits, and semester milestones.
- **Key Fields**: `record_id` (UUID, PK), `student_id` (UUID, FK), `semester` (Int: 1–8), `course_code` (Str), `course_title` (Str), `grade_points` (Float), `is_core_cs` (Bool).
- **Relationships**: Many-to-1 with `Student`.
- **Source**: University SIS registrar export.
- **Lifecycle**: Updated at the end of each academic semester.
- **Sensitivity**: High (Official educational transcript).
- **Retention**: Permanent registrar record.

---

### 4. `Skill`
- **Purpose**: Standardized competency entity in the Computer Science domain taxonomy.
- **Key Fields**: `skill_id` (Str, PK), `name` (Str), `category` (Enum: Language, Framework, System, Theory), `parent_concept_node` (Str, FK to Concept DAG).
- **Relationships**: Many-to-many with `ResumeAnalysis`, `JobDescription`, `Roadmap`.
- **Source**: Curated from CS Curricula (ACM/IEEE) and corporate job descriptions.
- **Lifecycle**: Managed by curriculum administrators.
- **Sensitivity**: Non-sensitive public technical ontology.
- **Retention**: Indefinite.

---

### 5. `Resume`
- **Purpose**: Metadata and storage pointer for uploaded candidate resume documents.
- **Key Fields**: `resume_id` (UUID, PK), `student_id` (UUID, FK), `storage_uri` (Str, encrypted storage pointer), `file_hash_sha256` (Str), `upload_timestamp` (Timestamp).
- **Relationships**: Many-to-1 with `Student`; 1-to-1 with `ResumeAnalysis`.
- **Source**: Candidate upload via `UI-DOC`.
- **Lifecycle**: Uploaded, parsed, and overwritten when candidate uploads an updated revision.
- **Sensitivity**: High (Candidate personal resume).
- **Retention**: Stored encrypted; automatically purged 180 days post-graduation upon student request.

---

### 6. `ResumeAnalysis`
- **Purpose**: Output of LayoutLMv3 spatial parsing and Sentence-BERT semantic matching (`M02`).
- **Key Fields**: `analysis_id` (UUID, PK), `resume_id` (UUID, FK), `f13_ats_score` (Float), `f14_cosine_similarity` (Float), `extracted_skills` (List[String]), `bounding_boxes_json` (JSON), `layout_type` (Enum: SingleColumn, MultiColumn).
- **Relationships**: 1-to-1 with `Resume`.
- **Source**: Generated by `M02` (`CMP-INT-ATS`).
- **Lifecycle**: Generated asynchronously upon resume upload.
- **Sensitivity**: Medium (Parsed skills and project descriptions).
- **Retention**: Tied to `Resume` lifecycle.

---

### 7. `JobDescription`
- **Purpose**: Target corporate employment opportunity and competency requirements profile.
- **Key Fields**: `jd_id` (UUID, PK), `company_name` (Str), `role_title` (Str), `role_tier_encoded` (Float, `F18`), `required_skills` (List[String]), `min_cgpa` (Float), `dense_embedding` (Vector[384]).
- **Relationships**: 1-to-many with `SkillGap`.
- **Source**: Placement Cell upload or campus recruitment portal.
- **Lifecycle**: Active during the specific recruitment drive window.
- **Sensitivity**: Low (Corporate job description).
- **Retention**: Retained for historical placement analytics.

---

### 8. `Interview`
- **Purpose**: Session metadata tracking an interactive mock technical interview instance (`M05`).
- **Key Fields**: `session_id` (UUID, PK), `student_id` (UUID, FK), `target_role` (Str), `session_start` (Timestamp), `session_end` (Timestamp), `completion_status` (Enum: Completed, Aborted).
- **Relationships**: Many-to-1 with `Student`; 1-to-1 with `InterviewAnalysis`.
- **Source**: Created upon WebSocket handshake initialization (`UI-INT`).
- **Lifecycle**: Ephemeral during session; metadata persisted upon session close.
- **Sensitivity**: Medium.
- **Retention**: **Zero storage of raw audio/video**; session metadata kept for 1 year.

---

### 9. `InterviewAnalysis`
- **Purpose**: Granular linguistic, paralinguistic, and coding evaluation metrics derived from an interview (`M05`).
- **Key Fields**: `analysis_id` (UUID, PK), `session_id` (UUID, FK), `turn_taking_latency_mean_ms` (Float), `f20_behavior_score` (Float), `speech_pause_ratio` (Float), `filler_frequency` (Float), `f06_programming_score` (Float), `transcript_text` (Text, PII scrubbed).
- **Relationships**: 1-to-1 with `Interview`.
- **Source**: Computed by `M05` perceivers and Docker sandbox runner.
- **Lifecycle**: Immutable post-interview evaluation report.
- **Sensitivity**: High (Evaluative paralinguistic data; protected under `DD-011`).
- **Retention**: Retained during active student enrollment; purged upon graduation.

---

### 10. `Assessment`
- **Purpose**: Formative diagnostic assessment or practice quiz session (`M03`).
- **Key Fields**: `assessment_id` (UUID, PK), `student_id` (UUID, FK), `subject_area` (Enum: DSA, OS, DBMS, Networks), `score_percentage` (Float), `duration_seconds` (Int), `completed_at` (Timestamp).
- **Relationships**: Many-to-1 with `Student`; 1-to-many with `QuestionAttempt`.
- **Source**: `M03` adaptive testing engine.
- **Lifecycle**: Created upon quiz initiation; finalized upon submission.
- **Sensitivity**: Low (Internal practice assessment).
- **Retention**: Indefinite for educational data mining.

---

### 11. `LearningEvent`
- **Purpose**: Granular, millisecond-precision behavioral telemetry log (`M11`).
- **Key Fields**: `event_id` (UUID, PK), `student_id` (UUID, FK), `event_type` (Enum: Login, PageView, QuizSubmit, CodeRun, HintClick), `payload_json` (JSON), `timestamp` (Timestamp).
- **Relationships**: Many-to-1 with `Student`.
- **Source**: Client browser event streaming via Redis.
- **Lifecycle**: Streamed in real-time to TimescaleDB hyper-tables.
- **Sensitivity**: Medium (User clickstream telemetry).
- **Retention**: Raw events kept for 90 days; rolled up into weekly aggregates thereafter.

---

### 12. `Prediction`
- **Purpose**: Inferred placement probability and multi-horizon trajectory output (`M06`).
- **Key Fields**: `prediction_id` (UUID, PK), `spv_id` (UUID, FK), `model_version` (Str), `p_ready` (Float), `readiness_tier` (Enum: Ready, NeedsRemediation, AtRisk), `tft_p50_6month` (Float), `computed_at` (Timestamp).
- **Relationships**: Many-to-1 with `StudentProfileVector`; 1-to-1 with `Explanation`.
- **Source**: `M06` Dual-Track prediction engine.
- **Lifecycle**: Generated on SPV recalculation.
- **Sensitivity**: Medium (Advisory evaluation score).
- **Retention**: Retained for longitudinal cohort analysis.

---

### 13. `Explanation`
- **Purpose**: Descriptive TreeSHAP feature attributions and DiCE prescriptive counterfactual recourse (`M07`).
- **Key Fields**: `explanation_id` (UUID, PK), `prediction_id` (UUID, FK), `shap_attributions_json` (JSON), `counterfactual_target_spv` (JSON), `proximity_L1` (Float), `sparsity_L0` (Int).
- **Relationships**: 1-to-1 with `Prediction`; 1-to-1 with `Recommendation`.
- **Source**: `M07` Prescriptive Explainability Engine.
- **Lifecycle**: Generated following a Tier 2/3 prediction.
- **Sensitivity**: Low.
- **Retention**: Tied to `Prediction` record.

---

### 14. `SkillGap`
- **Purpose**: Mathematically quantified deficit between candidate profile and target role (`M04`).
- **Key Fields**: `gap_id` (UUID, PK), `spv_id` (UUID, FK), `jd_id` (UUID, FK), `f15_gap_score` (Float), `missing_skills_json` (JSON), `euclidean_distance` (Float).
- **Relationships**: Many-to-1 with `StudentProfileVector`; many-to-1 with `JobDescription`.
- **Source**: `M04` Skill Gap Analysis Engine.
- **Lifecycle**: Recomputed on profile or role change.
- **Sensitivity**: Low.
- **Retention**: Dynamic state cache.

---

### 15. `Recommendation`
- **Purpose**: Optimal topological path across the Computer Science Concept DAG (`M08`).
- **Key Fields**: `recommendation_id` (UUID, PK), `gap_id` (UUID, FK), `ordered_concept_nodes` (List[String]), `total_estimated_hours` (Float).
- **Relationships**: 1-to-1 with `SkillGap`; 1-to-1 with `Roadmap`.
- **Source**: `M08` $A^*$ graph search engine.
- **Lifecycle**: Generated when skill gaps are diagnosed.
- **Sensitivity**: Low.
- **Retention**: Ephemeral transition state.

---

### 16. `Roadmap`
- **Purpose**: Active, milestone-based personalized learning curriculum (`M08`).
- **Key Fields**: `roadmap_id` (UUID, PK), `student_id` (UUID, FK), `recommendation_id` (UUID, FK), `target_role` (Str), `status` (Enum: Active, Completed, Abandoned), `sprints_json` (JSON), `progress_ratio` (Float, `F22`).
- **Relationships**: Many-to-1 with `Student`; 1-to-many with `Assessment`.
- **Source**: Synthesized by `M08`.
- **Lifecycle**: Persists and mutates as student verifies milestones.
- **Sensitivity**: Low.
- **Retention**: Retained throughout academic enrollment.

---

### 17. `Question`
- **Purpose**: Validated multiple-choice diagnostic item anchored to the CS Concept DAG (`M10`).
- **Key Fields**: `question_id` (UUID, PK), `concept_node` (Str), `stem_text` (Text), `correct_key` (Text), `distractors_json` (JSON mapping distractors to causal misconception branches), `difficulty_p` (Float), `discrimination_DI` (Float).
- **Relationships**: Many-to-1 with Concept DAG; 1-to-many with `QuestionAttempt`.
- **Source**: Generated by `M10` and validated via psychometric filters.
- **Lifecycle**: Persistent item bank asset.
- **Sensitivity**: High (Assessment item security; encrypted at rest).
- **Retention**: Permanent question bank asset.

---

### 18. `QuestionAttempt`
- **Purpose**: Specific examinee interaction with a diagnostic assessment question (`M03`).
- **Key Fields**: `attempt_id` (UUID, PK), `assessment_id` (UUID, FK), `question_id` (UUID, FK), `selected_option` (Str), `is_correct` (Bool), `latency_seconds` (Float), `diagnosed_misconception` (Str, Nullable).
- **Relationships**: Many-to-1 with `Assessment`; many-to-1 with `Question`.
- **Source**: Client submission via `UI-STU`.
- **Lifecycle**: Immutable attempt log.
- **Sensitivity**: Low.
- **Retention**: Indefinite for Classical Test Theory recalibration.

---

### 19. `ModelVersion`
- **Purpose**: Governance registry entity tracking deployed machine learning artifacts (`REG-MDL`).
- **Key Fields**: `model_id` (Str, PK), `architecture_family` (Enum: XGBoost, TFT, LayoutLMv3, SBERT, Whisper), `artifact_uri` (Str), `training_dataset_id` (Str), `validation_metric_score` (Float), `deployed_at` (Timestamp).
- **Relationships**: 1-to-many with `Prediction`.
- **Source**: Automated ML training pipeline.
- **Lifecycle**: Immutable versioned release.
- **Sensitivity**: Low.
- **Retention**: Permanent audit provenance.

---

### 20. `ExperimentReference`
- **Purpose**: Epistemological mapping linking runtime model evaluations to Phase 04 pre-experimental protocols (`EXP-1` to `EXP-6`).
- **Key Fields**: `exp_id` (Str, PK: EXP-1 to EXP-6), `target_hypothesis` (Str: H1 to H6), `baseline_model_id` (Str), `experimental_model_id` (Str), `evaluation_metric` (Str), `statistical_test` (Str).
- **Relationships**: Linked to `ModelVersion`.
- **Source**: Codified from Phase 04 `Experimental_Decisions.md`.
- **Lifecycle**: Static research governance metadata.
- **Sensitivity**: Non-sensitive scientific documentation.
- **Retention**: Permanent project record.

---

## 4. Entity Sensitivity & Regulatory Retention Matrix

| Logical Entity | Sensitivity Level | Legal / Privacy Framework | Storage Engine | Retention Policy |
|:---|:---:|:---|:---|:---|
| **`Student`** | High | FERPA / POPIA | PostgreSQL (Encrypted) | 5 Years post-graduation |
| **`StudentProfileVector`** | Medium | Institutional Privacy | TimescaleDB | Indefinite (Anonymized) |
| **`AcademicRecord`** | High | Registrar Regulations | PostgreSQL (ACID) | Permanent Institutional |
| **`Resume`** | High | Candidate Personal Data| Object Store (AES-256) | Purge on candidate request |
| **`ResumeAnalysis`** | Medium | Internal Skill Vector | ChromaDB / SQL | 180 Days post-graduation |
| **`Interview`** | Medium | Session Metadata | PostgreSQL | 1 Academic Year |
| **`InterviewAnalysis`** | High | Biometric Paralinguistics| TimescaleDB | Enrollment Duration Only |
| **`Raw Audio/Video`** | **Critical** | **POPIA / FERPA Zero-Trust**| **IN-MEMORY ONLY** | **ZERO RETENTION (DD-005, DD-011)**|
| **`LearningEvent`** | Medium | User Clickstream | TimescaleDB | 90 Days (Raw) -> Rollup |
| **`Question`** | High | Academic Integrity | PostgreSQL (Encrypted) | Permanent Bank Asset |
| **`ModelVersion`** | Low | MLOps Provenance | Model Registry | Permanent Audit Trail |
