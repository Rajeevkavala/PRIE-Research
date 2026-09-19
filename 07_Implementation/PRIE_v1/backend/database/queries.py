"""
PRIE v1 — Parameterized SQL Query Library
File: backend/database/queries.py
"""

# ── Students ──────────────────────────────────────────────────────────────────
GET_STUDENT_BY_ID = "SELECT * FROM students WHERE student_id = ?"
GET_STUDENT_BY_EMAIL = "SELECT * FROM students WHERE email = ?"
GET_ALL_STUDENTS = "SELECT student_id, name, email, branch, cgpa, profile_completeness, is_admin, created_at FROM students ORDER BY created_at DESC"

INSERT_STUDENT = """
INSERT INTO students
  (name, email, password_hash, branch, cgpa, has_internship, internship_months,
   project_count, project_quality_score, certifications_count, target_role,
   skills_json, learning_style)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

UPDATE_STUDENT_PROFILE = """
UPDATE students SET
  name=?, branch=?, cgpa=?, has_internship=?, internship_months=?,
  project_count=?, project_quality_score=?, certifications_count=?,
  target_role=?, skills_json=?, learning_style=?,
  profile_completeness=?, updated_at=CURRENT_TIMESTAMP
WHERE student_id=?
"""

UPDATE_STUDENT_COMPLETENESS = """
UPDATE students SET profile_completeness=?, updated_at=CURRENT_TIMESTAMP
WHERE student_id=?
"""

# ── Companies ─────────────────────────────────────────────────────────────────
GET_ALL_COMPANIES = "SELECT * FROM companies ORDER BY company_name"
GET_COMPANY_BY_ID = "SELECT * FROM companies WHERE company_id = ?"
GET_COMPANY_BY_NAME = "SELECT * FROM companies WHERE company_name = ?"

INSERT_COMPANY = """
INSERT OR IGNORE INTO companies
  (company_name, tier, min_cgpa, max_backlogs, required_skills_json,
   tech_stack_json, prs_threshold, role_profiles_json, description)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# ── Resumes ───────────────────────────────────────────────────────────────────
GET_LATEST_RESUME = """
SELECT * FROM resumes WHERE student_id = ?
ORDER BY uploaded_at DESC LIMIT 1
"""

GET_ALL_RESUMES_FOR_STUDENT = "SELECT * FROM resumes WHERE student_id = ? ORDER BY uploaded_at DESC"

INSERT_RESUME = """
INSERT INTO resumes
  (student_id, file_path, extracted_text, extracted_skills_json,
   ats_score, cosine_similarity, keyword_coverage, target_jd_hash, layout_diagnostics_json)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# ── Assessments ───────────────────────────────────────────────────────────────
GET_STUDENT_ASSESSMENTS = """
SELECT * FROM assessments WHERE student_id = ? ORDER BY taken_at DESC
"""

GET_ASSESSMENTS_BY_TOPIC = """
SELECT * FROM assessments WHERE student_id = ? AND topic = ? ORDER BY taken_at DESC
"""

COUNT_ASSESSMENT_ATTEMPTS = """
SELECT COUNT(*) as cnt FROM assessments WHERE student_id = ?
"""

INSERT_ASSESSMENT = """
INSERT INTO assessments
  (student_id, question_id, topic, difficulty, is_correct, score, total_questions, time_taken_seconds)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

# ── Question Bank ─────────────────────────────────────────────────────────────
GET_QUESTIONS_BY_TOPIC = """
SELECT * FROM question_bank WHERE topic = ? ORDER BY RANDOM() LIMIT ?
"""

GET_QUESTIONS_BY_TOPIC_AND_DIFFICULTY = """
SELECT * FROM question_bank WHERE topic = ? AND difficulty = ? ORDER BY RANDOM() LIMIT ?
"""

GET_QUESTION_BY_ID = "SELECT * FROM question_bank WHERE question_id = ?"
COUNT_QUESTIONS = "SELECT COUNT(*) as cnt FROM question_bank WHERE topic = ?"

INSERT_QUESTION = """
INSERT OR IGNORE INTO question_bank
  (topic, difficulty, question_text, options_json, correct_option, explanation,
   item_difficulty_p, item_discrimination, concept_node_id, misconception_tag)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# ── SPV Snapshots ─────────────────────────────────────────────────────────────
GET_LATEST_SPV_SNAPSHOT = """
SELECT * FROM spv_snapshots WHERE student_id = ?
ORDER BY computed_at DESC LIMIT 1
"""

GET_SPV_HISTORY = """
SELECT * FROM spv_snapshots WHERE student_id = ?
ORDER BY computed_at DESC LIMIT ?
"""

INSERT_SPV_SNAPSHOT = """
INSERT INTO spv_snapshots
  (student_id, spv_version,
   f01_cgpa, f02_dsa_score, f03_dbms_score, f04_os_score, f05_cn_score,
   f06_programming_score, f07_aptitude_score, f08_soft_skills_score,
   f09_project_count, f10_project_quality_score, f11_has_internship,
   f12_certifications_count, f13_resume_ats_score, f14_cosine_similarity,
   f15_gap_score, f16_consistency_score, f17_branch_encoded,
   f18_target_role_encoded, f19_assessment_attempts, f20_behavior_score,
   f21_engagement_score, f22_roadmap_completion_rate,
   confidence_mask_json, readiness_probability, readiness_tier,
   shap_values_json, trigger_event)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# ── Learning Events (M11 Telemetry) ──────────────────────────────────────────
GET_RECENT_EVENTS = """
SELECT * FROM learning_events WHERE student_id = ?
AND event_time >= datetime('now', ?)
ORDER BY event_time DESC
"""

GET_EVENTS_BY_TYPE = """
SELECT * FROM learning_events WHERE student_id = ? AND event_type = ?
ORDER BY event_time DESC LIMIT ?
"""

INSERT_LEARNING_EVENT = """
INSERT INTO learning_events
  (student_id, event_type, event_detail, event_payload_json, duration_seconds)
VALUES (?, ?, ?, ?, ?)
"""

COUNT_ACTIVE_WEEKS = """
SELECT COUNT(DISTINCT strftime('%Y-%W', event_time)) as active_weeks
FROM learning_events
WHERE student_id = ? AND event_time >= datetime('now', '-42 days')
"""

# ── Roadmaps (M08) ────────────────────────────────────────────────────────────
GET_STUDENT_ROADMAP = """
SELECT * FROM roadmaps WHERE student_id = ? ORDER BY week_number
"""

GET_ROADMAP_WEEK = """
SELECT * FROM roadmaps WHERE student_id = ? AND week_number = ?
"""

COUNT_COMPLETED_MILESTONES = """
SELECT COUNT(*) as cnt FROM roadmaps WHERE student_id = ? AND status = 'completed'
"""

COUNT_TOTAL_MILESTONES = """
SELECT COUNT(*) as cnt FROM roadmaps WHERE student_id = ?
"""

INSERT_ROADMAP_WEEK = """
INSERT OR REPLACE INTO roadmaps
  (student_id, week_number, topics_json, resources_json, concept_nodes_json,
   status, target_features_json)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

UPDATE_ROADMAP_STATUS = """
UPDATE roadmaps SET status=?, completed_at=?
WHERE student_id=? AND week_number=?
"""

DELETE_STUDENT_ROADMAP = "DELETE FROM roadmaps WHERE student_id = ?"

# ── Skill Map ─────────────────────────────────────────────────────────────────
GET_SKILL_BY_NAME = "SELECT * FROM skill_map WHERE skill_name = ?"
GET_ALL_SKILLS = "SELECT * FROM skill_map ORDER BY category, skill_name"
INSERT_SKILL = """
INSERT OR IGNORE INTO skill_map
  (skill_name, category, level, baseline_weight, synonyms_json, related_topics_json)
VALUES (?, ?, ?, ?, ?, ?)
"""

# ── Recommendations ───────────────────────────────────────────────────────────
GET_RECOMMENDATIONS = """
SELECT * FROM recommendations WHERE student_id = ?
ORDER BY relevance_score DESC, recommended_at DESC
"""

INSERT_RECOMMENDATION = """
INSERT INTO recommendations
  (student_id, title, topic, resource_type, url, difficulty, platform, relevance_score, reason)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

UPDATE_RECOMMENDATION_COMPLETED = """
UPDATE recommendations SET is_completed=1, completed_at=CURRENT_TIMESTAMP
WHERE rec_id=? AND student_id=?
"""

# ── Mock Interviews (M05) ─────────────────────────────────────────────────────
GET_MOCK_INTERVIEWS_FOR_STUDENT = """
SELECT * FROM mock_interviews WHERE student_id = ? ORDER BY created_at DESC
"""

GET_LATEST_MOCK_INTERVIEW = """
SELECT * FROM mock_interviews WHERE student_id = ? ORDER BY created_at DESC LIMIT 1
"""

INSERT_MOCK_INTERVIEW = """
INSERT INTO mock_interviews
  (student_id, session_id, target_role, audio_metrics_json, video_metrics_json,
   transcript_text, fluency_score, technical_score, behavior_score,
   multimodal_composite_score, is_mock)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# ── Placement Predictions (M06) ───────────────────────────────────────────────
INSERT_PLACEMENT_PREDICTION = """
INSERT INTO placement_predictions
  (student_id, snapshot_id, model_id, model_version, readiness_probability,
   confidence_lower, confidence_upper, readiness_tier, is_mock)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

GET_LATEST_PREDICTION = """
SELECT * FROM placement_predictions WHERE student_id = ? ORDER BY predicted_at DESC LIMIT 1
"""

# ── Counterfactual Plans (M07) ────────────────────────────────────────────────
INSERT_COUNTERFACTUAL_PLAN = """
INSERT INTO counterfactual_plans
  (student_id, prediction_id, target_probability, counterfactual_vector_json,
   deltas_json, sparsity_l0, distance_l1, recourse_method, is_valid)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

GET_COUNTERFACTUAL_PLANS = """
SELECT * FROM counterfactual_plans WHERE student_id = ? ORDER BY created_at DESC
"""

