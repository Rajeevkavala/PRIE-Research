-- =============================================================================
-- PRIE v1 — Relational Database DDL Schema
-- File: backend/database/schema.sql
-- Standard: 3NF Compliant, SQLite 3 with WAL + Foreign Keys
--
-- Traceability:
--   Layer 5 (Data & Knowledge Layer): 05_PRIE_Architecture/System_Architecture.md
--   M01: SPV Aggregator, M03: Assessment, M08: Roadmap, M11: Telemetry
--
-- SPV Version: v1 (22 invariant dimensions F01–F22)
-- =============================================================================

PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;

-- -----------------------------------------------------------------------------
-- 1. Students Table — M01 source of academic & demographic data
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS students (
    student_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    name                 TEXT    NOT NULL,
    email                TEXT    NOT NULL UNIQUE,
    password_hash        TEXT    NOT NULL,
    -- F17: branch_encoded source (IMMUTABLE in DiCE per DD-003)
    branch               TEXT    NOT NULL DEFAULT 'Computer Science',
    -- F01: cgpa
    cgpa                 REAL    NOT NULL DEFAULT 0.0 CHECK (cgpa >= 0.0 AND cgpa <= 10.0),
    -- F11: has_internship source
    has_internship       INTEGER NOT NULL DEFAULT 0 CHECK (has_internship IN (0, 1)),
    internship_months    INTEGER NOT NULL DEFAULT 0 CHECK (internship_months >= 0),
    -- F09: project_count source
    project_count        INTEGER NOT NULL DEFAULT 0 CHECK (project_count >= 0),
    -- F10: project_quality_score source (heuristic, PROPOSED status)
    project_quality_score REAL   NOT NULL DEFAULT 40.0 CHECK (project_quality_score >= 0.0 AND project_quality_score <= 100.0),
    -- F12: certifications_count source
    certifications_count INTEGER NOT NULL DEFAULT 0 CHECK (certifications_count >= 0),
    -- F18: target_role_encoded source
    target_role          TEXT    NOT NULL DEFAULT 'Software Development Engineer',
    -- Auxiliary (not in primary 22-dim SPV)
    skills_json          TEXT    NOT NULL DEFAULT '[]',
    learning_style       TEXT    NOT NULL DEFAULT 'practical'
                         CHECK (learning_style IN ('visual', 'reading', 'practical', 'mixed')),
    profile_completeness REAL    NOT NULL DEFAULT 0.0
                         CHECK (profile_completeness >= 0.0 AND profile_completeness <= 100.0),
    is_admin             INTEGER NOT NULL DEFAULT 0 CHECK (is_admin IN (0, 1)),
    created_at           DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at           DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 2. Companies Table — M04 role taxonomy, M06 company alignment score
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS companies (
    company_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name         TEXT    NOT NULL UNIQUE,
    tier                 TEXT    NOT NULL CHECK (tier IN ('MAANG', 'Tier-1 Product', 'Tier-2 Product', 'Startup', 'Service-Based')),
    min_cgpa             REAL    NOT NULL DEFAULT 6.0 CHECK (min_cgpa >= 0.0 AND min_cgpa <= 10.0),
    max_backlogs         INTEGER NOT NULL DEFAULT 0,
    required_skills_json TEXT    NOT NULL DEFAULT '[]',
    tech_stack_json      TEXT    NOT NULL DEFAULT '[]',
    -- PRS threshold for "Ready" classification against this company
    prs_threshold        REAL    NOT NULL DEFAULT 0.65 CHECK (prs_threshold >= 0.0 AND prs_threshold <= 1.0),
    role_profiles_json   TEXT    NOT NULL DEFAULT '{}',
    description          TEXT    NOT NULL DEFAULT '',
    created_at           DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 3. Resumes Table — M02 ATS Intelligence (F13, F14 source)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS resumes (
    resume_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id           INTEGER NOT NULL,
    file_path            TEXT    NOT NULL,
    extracted_text       TEXT,
    extracted_skills_json TEXT   NOT NULL DEFAULT '[]',
    -- F13: resume_ats_score
    ats_score            REAL    NOT NULL DEFAULT 0.0 CHECK (ats_score >= 0.0 AND ats_score <= 100.0),
    -- F14: cosine_similarity
    cosine_similarity    REAL    NOT NULL DEFAULT 0.0 CHECK (cosine_similarity >= 0.0 AND cosine_similarity <= 1.0),
    keyword_coverage     REAL    NOT NULL DEFAULT 0.0 CHECK (keyword_coverage >= 0.0 AND keyword_coverage <= 1.0),
    target_jd_hash       TEXT,
    layout_diagnostics_json TEXT NOT NULL DEFAULT '{}',
    uploaded_at          DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 4. Question Bank Table — M03 & M10 (IRT-calibrated items)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS question_bank (
    question_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    -- Topic maps to SPV feature: dsa→F02, dbms→F03, os→F04, cn→F05, programming→F06, aptitude→F07
    topic                TEXT    NOT NULL,
    difficulty           TEXT    NOT NULL CHECK (difficulty IN ('Easy', 'Medium', 'Hard')),
    question_text        TEXT    NOT NULL,
    options_json         TEXT    NOT NULL,   -- JSON array of 4 options
    correct_option       TEXT    NOT NULL,
    explanation          TEXT,
    -- IRT psychometric fields (M03 requirement)
    item_difficulty_p    REAL    DEFAULT 0.50 CHECK (item_difficulty_p >= 0.0 AND item_difficulty_p <= 1.0),
    item_discrimination  REAL    DEFAULT 0.35 CHECK (item_discrimination >= 0.0 AND item_discrimination <= 1.0),
    -- M10 causal concept DAG node association
    concept_node_id      TEXT    DEFAULT NULL,
    misconception_tag    TEXT    DEFAULT NULL,
    created_at           DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 5. Assessments Table — M03 (F02–F07, F19 source)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS assessments (
    assessment_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id           INTEGER NOT NULL,
    question_id          INTEGER,
    topic                TEXT    NOT NULL,
    difficulty           TEXT    NOT NULL,
    is_correct           INTEGER NOT NULL DEFAULT 0 CHECK (is_correct IN (0, 1)),
    score                INTEGER NOT NULL DEFAULT 0 CHECK (score >= 0),
    total_questions      INTEGER NOT NULL DEFAULT 1 CHECK (total_questions > 0),
    time_taken_seconds   REAL    NOT NULL DEFAULT 0.0,
    taken_at             DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES question_bank(question_id) ON DELETE SET NULL
);

-- -----------------------------------------------------------------------------
-- 6. SPV Snapshots Table — M01 versioned SPV history (SPV-DB per architecture)
-- Supports longitudinal TFT Track-2 prediction in M06
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS spv_snapshots (
    snapshot_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id           INTEGER NOT NULL,
    spv_version          TEXT    NOT NULL DEFAULT 'v1',
    -- F01–F22 stored as individual columns for SQL query efficiency
    f01_cgpa             REAL    NOT NULL DEFAULT 0.0,
    f02_dsa_score        REAL    NOT NULL DEFAULT 0.0,
    f03_dbms_score       REAL    NOT NULL DEFAULT 0.0,
    f04_os_score         REAL    NOT NULL DEFAULT 0.0,
    f05_cn_score         REAL    NOT NULL DEFAULT 0.0,
    f06_programming_score REAL   NOT NULL DEFAULT 0.0,
    f07_aptitude_score   REAL    NOT NULL DEFAULT 0.0,
    f08_soft_skills_score REAL   NOT NULL DEFAULT 0.0,
    f09_project_count    REAL    NOT NULL DEFAULT 0.0,
    f10_project_quality_score REAL NOT NULL DEFAULT 0.0,
    f11_has_internship   REAL    NOT NULL DEFAULT 0.0,
    f12_certifications_count REAL NOT NULL DEFAULT 0.0,
    f13_resume_ats_score REAL    NOT NULL DEFAULT 0.0,
    f14_cosine_similarity REAL   NOT NULL DEFAULT 0.0,
    f15_gap_score        REAL    NOT NULL DEFAULT 0.0,
    f16_consistency_score REAL   NOT NULL DEFAULT 0.0,
    f17_branch_encoded   REAL    NOT NULL DEFAULT 0.0,
    f18_target_role_encoded REAL NOT NULL DEFAULT 0.0,
    f19_assessment_attempts REAL NOT NULL DEFAULT 0.0,
    f20_behavior_score   REAL    NOT NULL DEFAULT 0.0,
    f21_engagement_score REAL    NOT NULL DEFAULT 0.0,
    f22_roadmap_completion_rate REAL NOT NULL DEFAULT 0.0,
    -- Binary observation confidence mask (1=observed, 0=imputed)
    confidence_mask_json TEXT    NOT NULL DEFAULT '[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]',
    -- Placement prediction at this snapshot
    readiness_probability REAL   DEFAULT NULL CHECK (readiness_probability IS NULL OR (readiness_probability >= 0.0 AND readiness_probability <= 1.0)),
    readiness_tier        TEXT   DEFAULT NULL,
    shap_values_json      TEXT   DEFAULT '{}',
    trigger_event         TEXT   NOT NULL DEFAULT 'profile_update',
    computed_at           DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 7. Learning Events Table — M11 Behavioral Telemetry (F16, F19, F21 source)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS learning_events (
    event_id             INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id           INTEGER NOT NULL,
    -- Event types: login, quiz_attempt, code_run, resume_upload, roadmap_milestone, page_view
    event_type           TEXT    NOT NULL,
    event_detail         TEXT    NOT NULL DEFAULT '',
    event_payload_json   TEXT    NOT NULL DEFAULT '{}',
    duration_seconds     REAL    NOT NULL DEFAULT 0.0,
    event_time           DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 8. Roadmaps Table — M08 Personalized Learning Milestones (F22 source)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS roadmaps (
    roadmap_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id           INTEGER NOT NULL,
    week_number          INTEGER NOT NULL CHECK (week_number >= 1),
    topics_json          TEXT    NOT NULL DEFAULT '[]',
    resources_json       TEXT    NOT NULL DEFAULT '[]',
    concept_nodes_json   TEXT    NOT NULL DEFAULT '[]',  -- CS DAG node IDs
    status               TEXT    NOT NULL DEFAULT 'pending'
                         CHECK (status IN ('pending', 'in_progress', 'completed', 'skipped')),
    target_features_json TEXT    NOT NULL DEFAULT '[]',  -- SPV features this week improves
    generated_at         DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_at         DATETIME DEFAULT NULL,
    UNIQUE (student_id, week_number),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 9. Skill Map — Canonical Skill Taxonomy
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS skill_map (
    skill_id             INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name           TEXT    NOT NULL UNIQUE,
    category             TEXT    NOT NULL,
    level                TEXT    NOT NULL DEFAULT 'intermediate'
                         CHECK (level IN ('beginner', 'intermediate', 'advanced')),
    baseline_weight      REAL    NOT NULL DEFAULT 0.5 CHECK (baseline_weight >= 0.0 AND baseline_weight <= 1.0),
    synonyms_json        TEXT    NOT NULL DEFAULT '[]',
    related_topics_json  TEXT    NOT NULL DEFAULT '[]'
);

-- -----------------------------------------------------------------------------
-- 10. Recommendations Table — M08/M09 curated resources
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS recommendations (
    rec_id               INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id           INTEGER NOT NULL,
    title                TEXT    NOT NULL,
    topic                TEXT    NOT NULL,
    resource_type        TEXT    NOT NULL
                         CHECK (resource_type IN ('video', 'article', 'practice_problem', 'documentation', 'course')),
    url                  TEXT    NOT NULL,
    difficulty           TEXT    NOT NULL DEFAULT 'intermediate'
                         CHECK (difficulty IN ('beginner', 'intermediate', 'advanced')),
    platform             TEXT    NOT NULL DEFAULT 'Web',
    relevance_score      REAL    NOT NULL CHECK (relevance_score >= 0.0 AND relevance_score <= 1.0),
    reason               TEXT,
    is_completed         INTEGER NOT NULL DEFAULT 0 CHECK (is_completed IN (0, 1)),
    recommended_at       DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_at         DATETIME DEFAULT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 11. Mock Interviews Table — M05 Multimodal Interview Telemetry & Scoring
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS mock_interviews (
    interview_id               INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id                 INTEGER NOT NULL,
    session_id                 TEXT    NOT NULL UNIQUE,
    target_role                TEXT    NOT NULL DEFAULT 'Software Development Engineer',
    -- Acoustic Prosodic Metrics from Librosa (pitch, jitter, shimmer, tempo, pauses)
    audio_metrics_json         TEXT    NOT NULL DEFAULT '{}',
    -- Visual Telemetry from MediaPipe (Action Units, gaze stability, blink rate)
    video_metrics_json         TEXT    NOT NULL DEFAULT '{}',
    -- ASR Speech Transcript from Whisper
    transcript_text            TEXT    NOT NULL DEFAULT '',
    -- Component Scores (0.0 - 100.0)
    fluency_score              REAL    NOT NULL DEFAULT 0.0 CHECK (fluency_score >= 0.0 AND fluency_score <= 100.0),
    technical_score            REAL    NOT NULL DEFAULT 0.0 CHECK (technical_score >= 0.0 AND technical_score <= 100.0),
    -- F20: behavior_score source
    behavior_score             REAL    NOT NULL DEFAULT 0.0 CHECK (behavior_score >= 0.0 AND behavior_score <= 100.0),
    multimodal_composite_score REAL    NOT NULL DEFAULT 0.0 CHECK (multimodal_composite_score >= 0.0 AND multimodal_composite_score <= 100.0),
    is_mock                    INTEGER NOT NULL DEFAULT 0 CHECK (is_mock IN (0, 1)),
    created_at                 DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 12. Placement Predictions Table — M06 Predictor Audit Ledger
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS placement_predictions (
    prediction_id              INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id                 INTEGER NOT NULL,
    snapshot_id                INTEGER,
    model_id                   TEXT    NOT NULL DEFAULT 'prie-xgb-static-v1',
    model_version              TEXT    NOT NULL DEFAULT 'v1',
    readiness_probability      REAL    NOT NULL CHECK (readiness_probability >= 0.0 AND readiness_probability <= 1.0),
    confidence_lower           REAL    CHECK (confidence_lower IS NULL OR (confidence_lower >= 0.0 AND confidence_lower <= 1.0)),
    confidence_upper           REAL    CHECK (confidence_upper IS NULL OR (confidence_upper >= 0.0 AND confidence_upper <= 1.0)),
    readiness_tier             TEXT    NOT NULL CHECK (readiness_tier IN ('Ready', 'Needs Remediation', 'At-Risk')),
    is_mock                    INTEGER NOT NULL DEFAULT 0 CHECK (is_mock IN (0, 1)),
    predicted_at               DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (snapshot_id) REFERENCES spv_snapshots(snapshot_id) ON DELETE SET NULL
);

-- -----------------------------------------------------------------------------
-- 13. Counterfactual Plans Table — M07 Prescriptive XAI Recourse Ledger
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS counterfactual_plans (
    plan_id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id                 INTEGER NOT NULL,
    prediction_id              INTEGER,
    target_probability         REAL    NOT NULL DEFAULT 0.80,
    counterfactual_vector_json TEXT    NOT NULL,
    deltas_json                TEXT    NOT NULL,
    sparsity_l0                INTEGER NOT NULL DEFAULT 0 CHECK (sparsity_l0 >= 0),
    distance_l1                REAL    NOT NULL DEFAULT 0.0 CHECK (distance_l1 >= 0.0),
    recourse_method            TEXT    NOT NULL DEFAULT 'dice_optimization',
    is_valid                   INTEGER NOT NULL DEFAULT 1 CHECK (is_valid IN (0, 1)),
    created_at                 DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (prediction_id) REFERENCES placement_predictions(prediction_id) ON DELETE SET NULL
);

-- -----------------------------------------------------------------------------
-- 14. RAG Knowledge Documents & Chunks Table — M09 Placement RAG
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS rag_documents (
    doc_id                     INTEGER PRIMARY KEY AUTOINCREMENT,
    title                      TEXT    NOT NULL,
    source_type                TEXT    NOT NULL CHECK (source_type IN ('syllabus', 'policy', 'interview_guide', 'company_doc')),
    file_path                  TEXT    NOT NULL,
    file_hash                  TEXT    NOT NULL UNIQUE,
    chunk_count                INTEGER NOT NULL DEFAULT 0,
    created_at                 DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS rag_chunks (
    chunk_id                   INTEGER PRIMARY KEY AUTOINCREMENT,
    doc_id                     INTEGER NOT NULL,
    chunk_index                INTEGER NOT NULL,
    content                    TEXT    NOT NULL,
    embedding_id               TEXT,
    topic                      TEXT    NOT NULL DEFAULT 'general',
    FOREIGN KEY (doc_id) REFERENCES rag_documents(doc_id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 15. Experiment Runs Table — Phase 06 Research Empirical Provenance
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS experiment_runs (
    run_id                     TEXT PRIMARY KEY,
    experiment_id              TEXT    NOT NULL CHECK (experiment_id IN ('EXP-1', 'EXP-2', 'EXP-3', 'EXP-4', 'EXP-5', 'EXP-6')),
    seed                       INTEGER NOT NULL,
    dataset_id                 TEXT    NOT NULL,
    dataset_version            TEXT    NOT NULL DEFAULT '1.0',
    model_id                   TEXT    NOT NULL,
    model_version              TEXT    NOT NULL DEFAULT 'v1',
    config_json                TEXT    NOT NULL DEFAULT '{}',
    metrics_json               TEXT    NOT NULL DEFAULT '{}',
    runtime_seconds            REAL    NOT NULL DEFAULT 0.0,
    executed_by                TEXT    NOT NULL DEFAULT 'researcher',
    executed_at                DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 16. Model Registry Table — Provenance & Checksum Verification
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS model_registry (
    model_id                   TEXT PRIMARY KEY,
    model_version              TEXT    NOT NULL,
    architecture_name          TEXT    NOT NULL,
    artifact_path              TEXT    NOT NULL,
    sha256_checksum            TEXT    NOT NULL,
    feature_schema_version     TEXT    NOT NULL DEFAULT 'v1',
    dataset_provenance         TEXT    NOT NULL,
    random_seed                INTEGER NOT NULL DEFAULT 42,
    metrics_json               TEXT    NOT NULL DEFAULT '{}',
    is_production_ready        INTEGER NOT NULL DEFAULT 0 CHECK (is_production_ready IN (0, 1)),
    registered_at              DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 17. Audit Logs Table — Enterprise & Academic Traceability
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS audit_logs (
    log_id                     INTEGER PRIMARY KEY AUTOINCREMENT,
    event_type                 TEXT    NOT NULL,
    user_id                    INTEGER,
    module                     TEXT    NOT NULL,
    action                     TEXT    NOT NULL,
    details_json               TEXT    NOT NULL DEFAULT '{}',
    status                     TEXT    NOT NULL DEFAULT 'SUCCESS',
    created_at                 DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- Performance & Integrity Indexes
-- -----------------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_students_email ON students(email);
CREATE INDEX IF NOT EXISTS idx_students_branch ON students(branch);
CREATE INDEX IF NOT EXISTS idx_spv_student_time ON spv_snapshots(student_id, computed_at);
CREATE INDEX IF NOT EXISTS idx_assessments_student_topic ON assessments(student_id, topic);
CREATE INDEX IF NOT EXISTS idx_learning_events_student_time ON learning_events(student_id, event_time);
CREATE INDEX IF NOT EXISTS idx_interviews_student_time ON mock_interviews(student_id, created_at);
CREATE INDEX IF NOT EXISTS idx_predictions_student_time ON placement_predictions(student_id, predicted_at);
CREATE INDEX IF NOT EXISTS idx_counterfactuals_student_time ON counterfactual_plans(student_id, created_at);
CREATE INDEX IF NOT EXISTS idx_experiments_id_seed ON experiment_runs(experiment_id, seed);
CREATE INDEX IF NOT EXISTS idx_rag_chunks_doc ON rag_chunks(doc_id);
