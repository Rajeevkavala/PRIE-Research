-- =============================================================================
-- ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
-- Relational Database DDL Schema (3NF Compliant)
-- Persistence Tier: SQLite 3 with Write-Ahead Logging & Foreign Keys
-- File: database/schema.sql
-- =============================================================================

PRAGMA foreign_keys = ON;

-- -----------------------------------------------------------------------------
-- 1. Students Table
-- Stores academic credentials, baseline profiles, and platform flags.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS students (
    student_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    name                TEXT NOT NULL,
    email               TEXT NOT NULL UNIQUE,
    password_hash       TEXT NOT NULL,
    branch              TEXT NOT NULL,
    cgpa                REAL NOT NULL CHECK (cgpa >= 0.0 AND cgpa <= 10.0),
    backlogs            INTEGER NOT NULL DEFAULT 0 CHECK (backlogs >= 0),
    skills_json         TEXT DEFAULT '[]',
    internship_status   TEXT DEFAULT 'None' CHECK (internship_status IN ('None', 'Completed', 'Ongoing')),
    internship_months   INTEGER DEFAULT 0 CHECK (internship_months >= 0),
    target_role         TEXT NOT NULL DEFAULT 'Software Development Engineer',
    target_company_id   INTEGER,
    learning_style      TEXT DEFAULT 'practical' CHECK (learning_style IN ('visual', 'reading', 'practical', 'mixed')),
    profile_completeness REAL DEFAULT 0.0 CHECK (profile_completeness >= 0.0 AND profile_completeness <= 100.0),
    certification_count INTEGER DEFAULT 0 CHECK (certification_count >= 0),
    project_count       INTEGER DEFAULT 0 CHECK (project_count >= 0),
    is_admin            INTEGER DEFAULT 0 CHECK (is_admin IN (0, 1)),
    created_at          DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at          DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (target_company_id) REFERENCES companies(company_id) ON DELETE SET NULL
);

-- -----------------------------------------------------------------------------
-- 2. Companies Table
-- Benchmark profiles, hiring criteria, and skill demand distributions.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS companies (
    company_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name        TEXT NOT NULL UNIQUE,
    tier                TEXT NOT NULL CHECK (tier IN ('Tier-1 Product', 'Tier-2 Product', 'Startup', 'Service-Based', 'Tier-1', 'Tier-2', 'Tier-3', 'MAANG')),
    min_cgpa            REAL NOT NULL DEFAULT 6.0 CHECK (min_cgpa >= 0.0 AND min_cgpa <= 10.0),
    max_backlogs        INTEGER NOT NULL DEFAULT 0 CHECK (max_backlogs >= 0),
    required_skills_json TEXT NOT NULL DEFAULT '[]',
    tech_stack_json     TEXT DEFAULT '[]',
    prs_threshold       REAL NOT NULL DEFAULT 0.65 CHECK (prs_threshold >= 0.0 AND prs_threshold <= 1.0),
    role_profiles_json  TEXT DEFAULT '{}',
    description         TEXT DEFAULT '',
    created_at          DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 3. Resumes Table
-- Student resume artifacts, extracted text, ATS and NLP similarity metrics.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS resumes (
    resume_id           INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id          INTEGER NOT NULL,
    file_path           TEXT NOT NULL,
    extracted_text      TEXT,
    extracted_skills_json TEXT DEFAULT '[]',
    ats_score           REAL DEFAULT 0.0 CHECK (ats_score >= 0.0 AND ats_score <= 100.0),
    cosine_similarity   REAL DEFAULT 0.0 CHECK (cosine_similarity >= 0.0 AND cosine_similarity <= 1.0),
    keyword_coverage    REAL DEFAULT 0.0 CHECK (keyword_coverage >= 0.0 AND keyword_coverage <= 1.0),
    target_jd_hash      TEXT,
    uploaded_at         DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 4. Question Bank Table
-- Curated technical assessment items with Bloom's taxonomy difficulties.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS question_bank (
    question_id         INTEGER PRIMARY KEY AUTOINCREMENT,
    topic               TEXT NOT NULL,
    difficulty          TEXT NOT NULL CHECK (difficulty IN ('Easy', 'Medium', 'Hard', 'easy', 'medium', 'hard')),
    question_text       TEXT NOT NULL,
    options_json        TEXT NOT NULL,
    correct_option      TEXT NOT NULL,
    explanation         TEXT,
    created_by          INTEGER,
    created_at          DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES students(student_id) ON DELETE SET NULL
);

-- -----------------------------------------------------------------------------
-- 5. Assessments Table
-- Assessment sessions, quiz attempts, scores, and completion times.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS assessments (
    assessment_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id          INTEGER NOT NULL,
    question_id         INTEGER,
    topic               TEXT NOT NULL,
    difficulty          TEXT NOT NULL,
    score               INTEGER NOT NULL CHECK (score >= 0),
    total_questions     INTEGER NOT NULL CHECK (total_questions > 0),
    time_taken_minutes  REAL DEFAULT 0.0 CHECK (time_taken_minutes >= 0.0),
    taken_at            DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES question_bank(question_id) ON DELETE SET NULL
);

-- -----------------------------------------------------------------------------
-- 6. Placement Readiness Score History (PRS History)
-- Longitudinal record of composite readiness scores and TreeSHAP values.
-- Supports dual column access (prs_score and prs_value) for seamless integration.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS prs_history (
    prs_id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id              INTEGER NOT NULL,
    company_id              INTEGER,
    prs_score               REAL CHECK (prs_score IS NULL OR (prs_score >= 0.0 AND prs_score <= 100.0)),
    prs_value               REAL CHECK (prs_value IS NULL OR (prs_value >= 0.0 AND prs_value <= 100.0)),
    s_pred                  REAL DEFAULT 0.0 CHECK (s_pred >= 0.0 AND s_pred <= 1.0),
    s_skill                 REAL DEFAULT 0.0 CHECK (s_skill >= 0.0 AND s_skill <= 1.0),
    s_resume                REAL DEFAULT 0.0 CHECK (s_resume >= 0.0 AND s_resume <= 1.0),
    s_behavior              REAL DEFAULT 0.0 CHECK (s_behavior >= 0.0 AND s_behavior <= 1.0),
    c_norm                  REAL DEFAULT 0.0 CHECK (c_norm >= 0.0 AND c_norm <= 1.0),
    s_company               REAL DEFAULT 0.0 CHECK (s_company >= 0.0 AND s_company <= 1.0),
    s_assessment            REAL DEFAULT 0.0 CHECK (s_assessment >= 0.0 AND s_assessment <= 1.0),
    confidence_score        REAL DEFAULT 0.0 CHECK (confidence_score >= 0.0 AND confidence_score <= 1.0),
    ci_lower                REAL DEFAULT 0.0 CHECK (ci_lower >= 0.0 AND ci_lower <= 1.0),
    ci_upper                REAL DEFAULT 1.0 CHECK (ci_upper >= 0.0 AND ci_upper <= 1.0),
    shap_values_json        TEXT DEFAULT '{}',
    trigger_event           TEXT NOT NULL DEFAULT 'manual',
    computed_at             DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (company_id) REFERENCES companies(company_id) ON DELETE SET NULL
);

-- Trigger to synchronize prs_score and prs_value
CREATE TRIGGER IF NOT EXISTS trg_prs_history_sync_insert
AFTER INSERT ON prs_history
BEGIN
    UPDATE prs_history
    SET prs_score = COALESCE(NEW.prs_score, NEW.prs_value, 0.0),
        prs_value = COALESCE(NEW.prs_value, NEW.prs_score, 0.0)
    WHERE prs_id = NEW.prs_id AND (prs_score IS NULL OR prs_value IS NULL);
END;

-- -----------------------------------------------------------------------------
-- 7. Roadmaps Table
-- Prescriptive multi-week study roadmaps with granular topic progress.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS roadmaps (
    roadmap_id          INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id          INTEGER NOT NULL,
    week_number         INTEGER NOT NULL CHECK (week_number >= 1),
    topics_json         TEXT NOT NULL DEFAULT '[]',
    resources_json      TEXT NOT NULL DEFAULT '[]',
    status              TEXT DEFAULT 'pending' CHECK (status IN ('pending', 'in_progress', 'completed', 'skipped')),
    generated_at        DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at          DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_at        DATETIME,
    UNIQUE(student_id, week_number),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 8. Recommendations Table
-- Curated learning recommendations ranked by content relevance score.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS recommendations (
    rec_id              INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id          INTEGER NOT NULL,
    title               TEXT NOT NULL,
    topic               TEXT NOT NULL,
    resource_type       TEXT NOT NULL CHECK (resource_type IN ('video', 'article', 'practice_problem', 'problem_set', 'documentation', 'course')),
    url                 TEXT NOT NULL,
    difficulty          TEXT DEFAULT 'intermediate' CHECK (difficulty IN ('beginner', 'intermediate', 'advanced')),
    platform            TEXT DEFAULT 'Web',
    relevance_score     REAL NOT NULL CHECK (relevance_score >= 0.0 AND relevance_score <= 1.0),
    reason              TEXT,
    is_completed        INTEGER DEFAULT 0 CHECK (is_completed IN (0, 1)),
    recommended_at      DATETIME DEFAULT CURRENT_TIMESTAMP,
    completed_at        DATETIME,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 9. Learning Events (Telemetry Log) Table
-- Granular clickstream and session logs for behavioral modeling.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS learning_events (
    event_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id          INTEGER NOT NULL,
    event_type          TEXT NOT NULL,
    event_payload_json  TEXT DEFAULT '{}',
    event_detail        TEXT DEFAULT '',
    duration_minutes    INTEGER DEFAULT 0 CHECK (duration_minutes >= 0),
    event_time          DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE
);

-- -----------------------------------------------------------------------------
-- 10. Skill Map / Taxonomy Table
-- Canonical 500+ skill taxonomy with synonyms, weights, and categories.
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS skill_map (
    skill_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    skill_name          TEXT NOT NULL UNIQUE,
    category            TEXT NOT NULL,
    level               TEXT DEFAULT 'intermediate' CHECK (level IN ('beginner', 'intermediate', 'advanced')),
    baseline_weight     REAL DEFAULT 0.5 CHECK (baseline_weight >= 0.0 AND baseline_weight <= 1.0),
    synonyms_json       TEXT DEFAULT '[]',
    aliases_json        TEXT DEFAULT '[]',
    related_topics_json TEXT DEFAULT '[]'
);
