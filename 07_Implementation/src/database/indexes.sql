-- =============================================================================
-- ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
-- High-Performance B-Tree Indexing Strategy
-- Guarantees O(log n) query execution and sub-second retrieval latency
-- File: database/indexes.sql
-- =============================================================================

-- Students Indexes
CREATE UNIQUE INDEX IF NOT EXISTS idx_students_email ON students(email);
CREATE INDEX IF NOT EXISTS idx_students_target_company ON students(target_company_id);

-- Assessments Indexes
CREATE INDEX IF NOT EXISTS idx_assessments_student ON assessments(student_id);
CREATE INDEX IF NOT EXISTS idx_assessments_topic ON assessments(topic);

-- Resumes Indexes
CREATE INDEX IF NOT EXISTS idx_resumes_student ON resumes(student_id);

-- PRS History Indexes
CREATE INDEX IF NOT EXISTS idx_prs_student ON prs_history(student_id);
CREATE INDEX IF NOT EXISTS idx_prs_student_time ON prs_history(student_id, computed_at DESC);

-- Roadmaps Indexes
CREATE INDEX IF NOT EXISTS idx_roadmaps_student ON roadmaps(student_id);
CREATE INDEX IF NOT EXISTS idx_roadmaps_student_week ON roadmaps(student_id, week_number);

-- Recommendations Indexes
CREATE INDEX IF NOT EXISTS idx_recommendations_student ON recommendations(student_id, relevance_score DESC);

-- Learning Events Telemetry Indexes
CREATE INDEX IF NOT EXISTS idx_learning_events_student ON learning_events(student_id);
CREATE INDEX IF NOT EXISTS idx_learning_events_student_time ON learning_events(student_id, event_time DESC);
CREATE INDEX IF NOT EXISTS idx_learning_events_type ON learning_events(event_type);

-- Question Bank Indexes
CREATE INDEX IF NOT EXISTS idx_questions_topic_diff ON question_bank(topic, difficulty);
CREATE UNIQUE INDEX IF NOT EXISTS idx_questions_text ON question_bank(question_text);

-- Skill Map Indexes
CREATE INDEX IF NOT EXISTS idx_skills_name ON skill_map(skill_name);
CREATE INDEX IF NOT EXISTS idx_skills_category ON skill_map(category);
