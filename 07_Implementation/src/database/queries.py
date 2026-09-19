"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Centralized SQL Query Registry
File: database/queries.py

Houses all parameterized SQL statement constants for PRIE. Isolating raw SQL
into immutable constants guarantees defense against SQL injection and decouples
business logic from persistence schemas.
"""

# =============================================================================
# 1. Student Profile Queries
# =============================================================================
GET_STUDENT_BY_ID: str = """
SELECT * FROM students WHERE student_id = ?;
"""

GET_STUDENT_BY_EMAIL: str = """
SELECT * FROM students WHERE email = ?;
"""

GET_ALL_STUDENTS: str = """
SELECT student_id, name, email, branch, cgpa, backlogs, target_role,
       target_company_id, profile_completeness, is_admin, created_at
FROM students
ORDER BY student_id ASC;
"""

COUNT_STUDENTS: str = """
SELECT COUNT(*) AS student_count FROM students WHERE is_admin = 0;
"""

CREATE_STUDENT: str = """
INSERT INTO students (
    name, email, password_hash, branch, cgpa, backlogs,
    skills_json, target_role, target_company_id, learning_style,
    profile_completeness, is_admin
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

UPDATE_STUDENT_PROFILE: str = """
UPDATE students
SET name = ?,
    branch = ?,
    cgpa = ?,
    backlogs = ?,
    skills_json = ?,
    internship_status = ?,
    internship_months = ?,
    target_role = ?,
    target_company_id = ?,
    learning_style = ?,
    profile_completeness = ?,
    certification_count = ?,
    project_count = ?,
    updated_at = CURRENT_TIMESTAMP
WHERE student_id = ?;
"""

UPDATE_STUDENT_COMPLETENESS: str = """
UPDATE students
SET profile_completeness = ?,
    updated_at = CURRENT_TIMESTAMP
WHERE student_id = ?;
"""

UPDATE_STUDENT_PASSWORD: str = """
UPDATE students
SET password_hash = ?,
    updated_at = CURRENT_TIMESTAMP
WHERE student_id = ?;
"""

DELETE_STUDENT_BY_ID: str = """
DELETE FROM students WHERE student_id = ?;
"""

# =============================================================================
# 2. Resumes Queries
# =============================================================================
GET_LATEST_RESUME: str = """
SELECT * FROM resumes
WHERE student_id = ?
ORDER BY uploaded_at DESC, resume_id DESC
LIMIT 1;
"""

GET_STUDENT_RESUMES: str = """
SELECT * FROM resumes
WHERE student_id = ?
ORDER BY uploaded_at DESC, resume_id DESC;
"""

INSERT_RESUME: str = """
INSERT INTO resumes (
    student_id, file_path, extracted_text, extracted_skills_json,
    ats_score, cosine_similarity, keyword_coverage, target_jd_hash
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?);
"""

GET_RESUME_BY_ID: str = """
SELECT * FROM resumes
WHERE resume_id = ?;
"""

UPDATE_RESUME_ANALYSIS: str = """
UPDATE resumes
SET ats_score = ?,
    cosine_similarity = ?,
    keyword_coverage = ?,
    extracted_skills_json = ?,
    extracted_text = COALESCE(?, extracted_text)
WHERE resume_id = ?;
"""

DELETE_RESUME_BY_ID: str = """
DELETE FROM resumes WHERE resume_id = ?;
"""

# =============================================================================
# 3. Assessment & Diagnostic Quiz Queries
# =============================================================================
GET_STUDENT_ASSESSMENTS: str = """
SELECT * FROM assessments
WHERE student_id = ?
ORDER BY taken_at DESC;
"""

GET_ASSESSMENT_AVERAGE_BY_STUDENT: str = """
SELECT AVG(CAST(score AS REAL) / total_questions) * 100.0 AS avg_percentage,
       COUNT(*) AS total_assessments
FROM assessments
WHERE student_id = ?;
"""

INSERT_ASSESSMENT: str = """
INSERT INTO assessments (
    student_id, question_id, topic, difficulty,
    score, total_questions, time_taken_minutes
)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""

# =============================================================================
# 4. Placement Readiness Score (PRS) History Queries
# =============================================================================
GET_LATEST_PRS: str = """
SELECT * FROM prs_history
WHERE student_id = ?
ORDER BY computed_at DESC
LIMIT 1;
"""

GET_PRS_TIMELINE: str = """
SELECT prs_id, student_id, COALESCE(prs_score, prs_value) AS prs_score,
       s_pred, s_skill, s_resume, s_behavior, c_norm, s_company, s_assessment,
       trigger_event, computed_at
FROM prs_history
WHERE student_id = ?
ORDER BY computed_at ASC;
"""

INSERT_PRS_RECORD: str = """
INSERT INTO prs_history (
    student_id, company_id, prs_score, prs_value,
    s_pred, s_skill, s_resume, s_behavior, c_norm, s_company, s_assessment,
    confidence_score, ci_lower, ci_upper, shap_values_json, trigger_event
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

# =============================================================================
# 5. Companies Benchmark Queries
# =============================================================================
GET_COMPANY_BY_ID: str = """
SELECT * FROM companies WHERE company_id = ?;
"""

GET_COMPANY_BY_NAME: str = """
SELECT * FROM companies WHERE company_name = ?;
"""

GET_ALL_COMPANIES: str = """
SELECT company_id, company_name, tier, min_cgpa, max_backlogs,
       required_skills_json, tech_stack_json, prs_threshold,
       role_profiles_json, description
FROM companies
ORDER BY prs_threshold DESC;
"""

INSERT_COMPANY: str = """
INSERT INTO companies (
    company_name, tier, min_cgpa, max_backlogs,
    required_skills_json, tech_stack_json, prs_threshold,
    role_profiles_json, description
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

# =============================================================================
# 6. Roadmaps Queries
# =============================================================================
GET_STUDENT_ROADMAP: str = """
SELECT * FROM roadmaps
WHERE student_id = ?
ORDER BY week_number ASC;
"""

INSERT_ROADMAP_WEEK: str = """
INSERT INTO roadmaps (student_id, week_number, topics_json, resources_json, status)
VALUES (?, ?, ?, ?, ?);
"""

UPDATE_ROADMAP_STATUS: str = """
UPDATE roadmaps
SET status = ?,
    completed_at = CASE WHEN ? = 'completed' THEN CURRENT_TIMESTAMP ELSE completed_at END,
    updated_at = CURRENT_TIMESTAMP
WHERE student_id = ? AND week_number = ?;
"""

DELETE_STUDENT_ROADMAP: str = """
DELETE FROM roadmaps WHERE student_id = ?;
"""

# =============================================================================
# 7. Recommendations Queries
# =============================================================================
GET_STUDENT_RECOMMENDATIONS: str = """
SELECT * FROM recommendations
WHERE student_id = ?
ORDER BY is_completed ASC, relevance_score DESC
LIMIT ?;
"""

INSERT_RECOMMENDATION: str = """
INSERT INTO recommendations (
    student_id, title, topic, resource_type, url,
    difficulty, platform, relevance_score, reason, is_completed
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
"""

MARK_RECOMMENDATION_COMPLETE: str = """
UPDATE recommendations
SET is_completed = 1,
    completed_at = CURRENT_TIMESTAMP
WHERE rec_id = ? AND student_id = ?;
"""

# =============================================================================
# 8. Learning Events Telemetry Queries
# =============================================================================
INSERT_LEARNING_EVENT: str = """
INSERT INTO learning_events (
    student_id, event_type, event_payload_json, event_detail, duration_minutes
)
VALUES (?, ?, ?, ?, ?);
"""

GET_STUDENT_EVENTS: str = """
SELECT * FROM learning_events
WHERE student_id = ?
ORDER BY event_time DESC, event_id DESC
LIMIT ?;
"""

COUNT_EVENTS_IN_DAYS: str = """
SELECT COUNT(*) AS event_count
FROM learning_events
WHERE student_id = ?
  AND event_time >= datetime('now', ? || ' days');
"""

# =============================================================================
# 9. Question Bank Queries
# =============================================================================
GET_QUESTIONS_BY_TOPIC_DIFFICULTY: str = """
SELECT * FROM question_bank
WHERE topic = ? AND difficulty = ?
ORDER BY RANDOM()
LIMIT ?;
"""

GET_QUESTION_BY_ID: str = """
SELECT * FROM question_bank WHERE question_id = ?;
"""

GET_RANDOM_QUESTIONS: str = """
SELECT * FROM question_bank
ORDER BY RANDOM()
LIMIT ?;
"""

INSERT_QUESTION: str = """
INSERT INTO question_bank (
    topic, difficulty, question_text, options_json,
    correct_option, explanation, created_by
)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""

GET_DISTINCT_TOPICS: str = """
SELECT DISTINCT topic FROM question_bank ORDER BY topic ASC;
"""

COUNT_QUESTIONS_BY_TOPIC: str = """
SELECT topic, difficulty, COUNT(*) AS count
FROM question_bank
GROUP BY topic, difficulty;
"""

GET_STUDENT_TOPIC_STATS: str = """
SELECT topic,
       COUNT(*) AS total_quizzes,
       SUM(score) AS total_score,
       SUM(total_questions) AS total_questions,
       ROUND(AVG(CAST(score AS REAL) / total_questions) * 100.0, 1) AS avg_accuracy,
       MAX(taken_at) AS last_taken_at
FROM assessments
WHERE student_id = ?
GROUP BY topic
ORDER BY avg_accuracy DESC;
"""

# =============================================================================
# 10. Skill Map / Taxonomy Queries
# =============================================================================
GET_ALL_SKILLS: str = """
SELECT * FROM skill_map ORDER BY category ASC, baseline_weight DESC;
"""

GET_SKILL_BY_NAME: str = """
SELECT * FROM skill_map WHERE LOWER(skill_name) = LOWER(?);
"""

SEARCH_SKILLS_BY_CATEGORY: str = """
SELECT * FROM skill_map WHERE category = ? ORDER BY baseline_weight DESC;
"""

INSERT_SKILL: str = """
INSERT INTO skill_map (
    skill_name, category, level, baseline_weight,
    synonyms_json, aliases_json, related_topics_json
)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""

COUNT_SKILLS: str = """
SELECT COUNT(*) AS skill_count FROM skill_map;
"""

# =============================================================================
# 11. Cohort Analytics & Administration Queries
# =============================================================================
GET_COHORT_PRS_LATEST: str = """
SELECT s.student_id, s.name, s.email, s.branch, s.cgpa, s.backlogs, s.target_role,
       c.company_name,
       p.prs_score, p.confidence_score, p.computed_at
FROM students s
LEFT JOIN (
    SELECT student_id, company_id, COALESCE(prs_score, prs_value) AS prs_score, confidence_score, computed_at,
           ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY computed_at DESC) as rn
    FROM prs_history
) p ON s.student_id = p.student_id AND p.rn = 1
LEFT JOIN companies c ON s.target_company_id = c.company_id
WHERE s.is_admin = 0
ORDER BY COALESCE(p.prs_score, 0) DESC;
"""

GET_BRANCH_READINESS_STATS: str = """
SELECT s.branch,
       COUNT(s.student_id) AS student_count,
       ROUND(AVG(s.cgpa), 2) AS avg_cgpa,
       ROUND(AVG(COALESCE(p.prs_score, 50.0)), 1) AS avg_prs
FROM students s
LEFT JOIN (
    SELECT student_id, COALESCE(prs_score, prs_value) AS prs_score,
           ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY computed_at DESC) as rn
    FROM prs_history
) p ON s.student_id = p.student_id AND p.rn = 1
WHERE s.is_admin = 0
GROUP BY s.branch
ORDER BY avg_prs DESC;
"""

GET_AT_RISK_STUDENTS: str = """
SELECT s.student_id, s.name, s.email, s.branch, s.cgpa, s.backlogs,
       COALESCE(p.prs_score, 0.0) AS prs_score,
       c.company_name
FROM students s
LEFT JOIN (
    SELECT student_id, COALESCE(prs_score, prs_value) AS prs_score,
           ROW_NUMBER() OVER (PARTITION BY student_id ORDER BY computed_at DESC) as rn
    FROM prs_history
) p ON s.student_id = p.student_id AND p.rn = 1
LEFT JOIN companies c ON s.target_company_id = c.company_id
WHERE s.is_admin = 0 AND (COALESCE(p.prs_score, 0.0) < 40.0 OR s.backlogs > 1)
ORDER BY prs_score ASC, s.backlogs DESC;
"""
