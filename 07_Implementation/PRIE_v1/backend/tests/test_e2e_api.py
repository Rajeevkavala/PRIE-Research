"""
Comprehensive End-to-End Test Suite for All PRIE v1 REST API Endpoints.
File: backend/tests/test_e2e_api.py

Tests every endpoint sequentially using FastAPI TestClient / requests:
  - Auth: Register & Login
  - Profile: Get Profile, Get 22D SPV, Update Profile
  - Predict: Placement Readiness Inference & Bootstrap CI
  - Explain: Prescriptive XAI, TreeSHAP, Recourse Directives
  - Roadmap: Active Roadmap, Generate A* DAG, Complete Week Milestone
  - Assessment: Topics, IRT Next Item, Submit Answer, Topic Mastery
"""

import json
import pytest
from fastapi.testclient import TestClient
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from main import app

client = TestClient(app)

# Global test state
test_state = {
    "token": None,
    "student_id": None,
    "new_email": "tester_e2e@scholarcamp.ai",
}


def test_01_health_and_root():
    """Verify system health and metadata."""
    res = client.get("/api/health")
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "healthy"
    assert data["spv_version"] == "v1"
    assert data["dimension"] == 22

    res_root = client.get("/")
    assert res_root.status_code == 200


def test_02_auth_login_demo_user():
    """Verify login with seeded demo credentials."""
    payload = {
        "email": "demo@scholarcamp.ai",
        "password": "password123",
    }
    res = client.post("/api/v1/auth/login", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    assert data["email"] == "demo@scholarcamp.ai"
    test_state["token"] = data["access_token"]
    test_state["student_id"] = data["student_id"]


def test_03_auth_register_new_user():
    """Verify student registration with full profile payload."""
    import time
    unique_email = f"e2e_{int(time.time())}@scholarcamp.ai"
    payload = {
        "name": "Pooja Hegde",
        "email": unique_email,
        "password": "securepassword123",
        "branch": "Information Technology",
        "cgpa": 8.75,
        "has_internship": 1,
        "internship_months": 4,
        "project_count": 4,
        "certifications_count": 2,
        "target_role": "Backend Engineer",
        "skills_json": json.dumps(["Python", "PostgreSQL", "FastAPI"]),
        "learning_style": "visual"
    }
    res = client.post("/api/v1/auth/register", json=payload)
    assert res.status_code == 201
    data = res.json()
    assert "access_token" in data
    assert data["name"] == "Pooja Hegde"


def test_04_profile_me():
    """Verify GET /api/v1/profile/me."""
    headers = {"Authorization": f"Bearer {test_state['token']}"}
    res = client.get("/api/v1/profile/me", headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert data["email"] == "demo@scholarcamp.ai"
    assert "password_hash" not in data
    assert data["cgpa"] > 0.0


def test_05_profile_spv_canonical_22d():
    """Verify GET /api/v1/profile/spv returns 22 dimensions with confidence mask."""
    headers = {"Authorization": f"Bearer {test_state['token']}"}
    res = client.get("/api/v1/profile/spv", headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert data["spv_version"] == "v1"
    assert len(data["features"]) == 22
    assert len(data["confidence_mask"]) == 22
    assert len(data["normalized_vector"]) == 22


def test_06_profile_update():
    """Verify PUT /api/v1/profile/update."""
    headers = {"Authorization": f"Bearer {test_state['token']}"}
    payload = {
        "project_count": 5,
        "project_quality_score": 82.5,
        "certifications_count": 3
    }
    res = client.put("/api/v1/profile/update", headers=headers, json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "updated"


def test_07_predict_readiness():
    """Verify POST /api/v1/predict/readiness."""
    headers = {"Authorization": f"Bearer {test_state['token']}"}
    res = client.post("/api/v1/predict/readiness", headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert "probability" in data
    assert 0.0 <= data["probability"] <= 1.0
    assert data["readiness_tier"] in ["Ready", "Needs Remediation", "At-Risk"]
    assert "confidence_interval" in data
    assert len(data["confidence_interval"]) == 2


def test_08_explain_prescribe():
    """Verify POST /api/v1/explain/prescribe with TreeSHAP and counterfactuals."""
    headers = {"Authorization": f"Bearer {test_state['token']}"}
    res = client.post("/api/v1/explain/prescribe", headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert "prediction" in data
    assert "explanation" in data
    assert "counterfactual" in data
    assert "narrative" in data
    assert "deficit_ranking" in data


def test_09_roadmap_active_and_generate():
    """Verify GET /api/v1/roadmap/active and POST /api/v1/roadmap/generate."""
    headers = {"Authorization": f"Bearer {test_state['token']}"}
    gen_res = client.post("/api/v1/roadmap/generate", headers=headers)
    assert gen_res.status_code == 200
    gen_data = gen_res.json()
    assert gen_data["total_weeks"] > 0

    get_res = client.get("/api/v1/roadmap/active", headers=headers)
    assert get_res.status_code == 200
    active_data = get_res.json()
    assert len(active_data["weeks"]) > 0


def test_10_roadmap_complete_week():
    """Verify POST /api/v1/roadmap/complete/{week_number}."""
    headers = {"Authorization": f"Bearer {test_state['token']}"}
    res = client.post("/api/v1/roadmap/complete/1", headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert data["status"] == "completed"
    assert data["week"] == 1


def test_11_assessment_topics():
    """Verify GET /api/v1/assessment/topics."""
    headers = {"Authorization": f"Bearer {test_state['token']}"}
    res = client.get("/api/v1/assessment/topics", headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert "topics" in data
    assert any("dsa" in t.lower() for t in data["topics"])


def test_12_assessment_next_item_and_submit():
    """Verify POST /api/v1/assessment/next-item/{topic} and submit."""
    headers = {"Authorization": f"Bearer {test_state['token']}"}
    res_q = client.post("/api/v1/assessment/next-item/dsa", headers=headers, json={"history": []})
    assert res_q.status_code == 200
    q = res_q.json()
    assert "question_id" in q
    assert "question_text" in q
    assert "correct_option" not in q  # Must not leak answer

    # Submit answer
    options = json.loads(q["options_json"])
    submit_payload = {
        "question_id": q["question_id"],
        "topic": "dsa",
        "difficulty": q["difficulty"],
        "selected_option": options[0],
        "time_taken_seconds": 12.5
    }
    res_sub = client.post("/api/v1/assessment/submit", headers=headers, json=submit_payload)
    assert res_sub.status_code == 200
    sub_data = res_sub.json()
    assert "is_correct" in sub_data
    assert "topic_mastery" in sub_data


def test_13_assessment_mastery():
    """Verify GET /api/v1/assessment/mastery/{topic}."""
    headers = {"Authorization": f"Bearer {test_state['token']}"}
    res = client.get("/api/v1/assessment/mastery/dsa", headers=headers)
    assert res.status_code == 200
    data = res.json()
    assert data["topic"] == "dsa"
    assert "mastery_score" in data


def test_14_resume_analyze_text():
    """Verify POST /api/v1/resume/analyze-text."""
    payload = {
        "resume_text": "Experienced Python and FastAPI backend developer with PostgreSQL and Docker expertise. Built REST APIs.",
        "target_role": "Software Development Engineer"
    }
    res = client.post("/api/v1/resume/analyze-text", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "ats_score" in data
    assert 0.0 <= data["ats_score"] <= 100.0
    assert "extracted_skills" in data
    assert "python" in data["extracted_skills"]


def test_15_interview_submit_text():
    """Verify POST /api/v1/interview/submit-text."""
    payload = {
        "student_id": test_state.get("student_id") or 1,
        "transcript_text": "In this problem, I used a binary search tree to optimize the lookup complexity to logarithmic time.",
        "duration_seconds": 15.0
    }
    res = client.post("/api/v1/interview/submit-text", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "overall_interview_score" in data
    assert "spv_f20_behavior_score" in data
    assert 0.0 <= data["spv_f20_behavior_score"] <= 1.0


def test_16_rag_curriculum_query():
    """Verify POST /api/v1/rag/query."""
    payload = {
        "question": "What are the core ACID transactional properties in relational database systems?",
        "top_k": 2
    }
    res = client.post("/api/v1/rag/query", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["is_grounded"] is True
    assert len(data["citations"]) > 0


def test_17_aqg_generate_bloom_questions():
    """Verify POST /api/v1/aqg/generate."""
    payload = {
        "topic": "DSA",
        "difficulty": "Medium",
        "bloom_level": "Analyze",
        "count": 2
    }
    res = client.post("/api/v1/aqg/generate", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "questions" in data
    assert len(data["questions"]) > 0
    assert data["questions"][0]["bloom_level"] == "Analyze"


def test_18_company_benchmarks_and_match():
    """Verify GET /api/v1/company/benchmarks and POST /api/v1/company/match."""
    res_b = client.get("/api/v1/company/benchmarks")
    assert res_b.status_code == 200
    benchmarks = res_b.json()
    assert len(benchmarks) > 0

    match_payload = {
        "student_cgpa": 8.5,
        "student_skills": ["python", "data structures", "sql", "git"],
    }
    res_m = client.post("/api/v1/company/match", json=match_payload)
    assert res_m.status_code == 200
    matches = res_m.json()
    assert len(matches) > 0
    assert "overall_compatibility_score" in matches[0]


def test_19_digital_twin_what_if_and_sensitivity():
    """Verify POST /api/v1/twin/simulate and POST /api/v1/twin/sensitivity."""
    valid_spv = [0.75] * 22
    sim_payload = {
        "spv_vector": valid_spv,
        "perturbations": {"dsa_score": 0.15, "project_quality_score": 0.20}
    }
    res_sim = client.post("/api/v1/twin/simulate", json=sim_payload)
    assert res_sim.status_code == 200
    sim_data = res_sim.json()
    assert "readiness_probability_delta" in sim_data
    assert "scientific_integrity_disclaimer" in sim_data

    # Sensitivity matrix
    sens_payload = {"spv_vector": valid_spv, "step_size": 0.10}
    res_sens = client.post("/api/v1/twin/sensitivity", json=sens_payload)
    assert res_sens.status_code == 200
    matrix = res_sens.json()
    assert len(matrix) > 0


def test_20_experiments_list_and_results():
    """Verify GET /api/v1/experiments/list and GET /api/v1/experiments/{exp_id}/results."""
    res_list = client.get("/api/v1/experiments/list")
    assert res_list.status_code == 200
    exps = res_list.json()
    assert len(exps) == 6
    exp1_status = next(e for e in exps if e["id"] == "EXP-1")
    assert exp1_status["status"] == "EXECUTED"

    res_exp1 = client.get("/api/v1/experiments/EXP-1/results")
    assert res_exp1.status_code == 200
    exp1_data = res_exp1.json()
    assert "run_metadata" in exp1_data
    assert "raw_metrics" in exp1_data

