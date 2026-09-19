"""
Unit tests for Module M02: Resume ATS Intelligence Engine.
Tests text extraction, spatial bounding box extraction, multidimensional ATS scoring,
and explicit LayoutLMv3 pipeline status reporting.
"""

import json
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from modules.m02_resume_ats import ResumeATSEngine, LayoutLMv3ResumePipeline


@pytest.fixture
def sample_resume_text():
    return (
        "John Doe\n"
        "Email: john.doe@email.com | Phone: +1-555-0199 | GitHub: github.com/johndoe\n\n"
        "EDUCATION\n"
        "Bachelor of Technology in Computer Science and Engineering\n"
        "CGPA: 8.4 / 10.0 | 2021 - 2025\n\n"
        "TECHNICAL SKILLS\n"
        "Languages: Python, Java, JavaScript, C++, SQL\n"
        "Frameworks & Tools: FastAPI, React, Docker, Git, Linux, PostgreSQL\n"
        "Core Concepts: Data Structures, Algorithms, Object Oriented Programming, System Design\n\n"
        "EXPERIENCE\n"
        "Software Engineering Intern | ABC Tech Solutions | Summer 2024\n"
        "- Developed REST API endpoints using FastAPI and PostgreSQL, serving 5000+ daily requests.\n"
        "- Improved query execution latency by 35% through indexing and Redis caching.\n"
        "- Configured CI/CD automation pipelines using GitHub Actions and Docker.\n\n"
        "PROJECTS\n"
        "1. Distributed Task Queue: Implemented asynchronous task processing with Redis and Python.\n"
        "- Increased task throughput by 40% using thread-pool concurrency.\n"
        "2. Cloud Resume Analyzer: Built automated resume keyword parser with 92% extraction accuracy.\n\n"
        "CERTIFICATIONS\n"
        "- AWS Certified Cloud Practitioner\n"
        "- Meta Back-End Developer Professional Certificate\n"
    )


def test_compute_ats_score(sample_resume_text):
    """Test multidimensional ATS score calculation."""
    engine = ResumeATSEngine()
    result = engine.compute_ats_score(sample_resume_text, target_role="Software Development Engineer")

    assert "overall_ats_score" in result
    assert 0.0 <= result["overall_ats_score"] <= 100.0
    assert result["keyword_coverage_score"] > 0.0
    assert result["section_coverage_score"] > 0.0
    assert result["length_score"] > 0.0
    assert result["impact_metric_score"] > 0.0

    # Key sections should be recognized
    assert "education" in result["detected_sections"]
    assert "skills" in result["detected_sections"]
    assert "experience" in result["detected_sections"]
    assert "projects" in result["detected_sections"]
    assert "certifications" in result["detected_sections"]


def test_extract_skills(sample_resume_text):
    """Test recognized skill keyword taxonomy extraction."""
    engine = ResumeATSEngine()
    skills = engine.extract_skills(sample_resume_text)

    assert isinstance(skills, list)
    assert "python" in skills
    assert "fastapi" in skills
    assert "docker" in skills
    assert "sql" in skills
    assert "git" in skills


def test_cosine_similarity_empty():
    """Test cosine similarity graceful degradation on empty inputs."""
    engine = ResumeATSEngine()
    sim = engine.compute_cosine_similarity("", "Software Engineer JD")
    assert sim == 0.5


def test_layoutlmv3_pipeline_unavailability():
    """
    LayoutLMv3 without fine-tuned weights MUST explicitly declare MODEL NOT TRAINED,
    per scientific integrity rules.
    """
    pipeline = LayoutLMv3ResumePipeline(model_dir=Path("models/non_existent_layoutlm"))
    assert pipeline.is_trained is False

    mock_tokens = [
        {"text": "Education", "bbox": [100, 100, 200, 120], "page": 1},
        {"text": "Python", "bbox": [100, 150, 150, 170], "page": 1},
    ]
    res = pipeline.parse_spatial(mock_tokens)
    assert res["status"] == "MODEL NOT TRAINED"
    assert "PROPOSED_ARCHITECTURE" in res["epistemological_status"]
    assert "requires_fine_tuning" in res.get("note", "").lower() or "requires" in res.get("note", "").lower()
