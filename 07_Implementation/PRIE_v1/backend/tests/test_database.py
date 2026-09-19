"""
Unit tests for Database layer and 3NF integrity.
"""

import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from database import db_manager, queries


def test_db_connection():
    """Test thread-local SQLite connection and WAL mode."""
    conn = db_manager._get_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA journal_mode;")
    mode = cursor.fetchone()[0]
    assert mode.lower() == "wal"


def test_seed_student_exists():
    """Verify demo student exists and is properly populated."""
    row = db_manager.execute_single(queries.GET_STUDENT_BY_EMAIL, ("demo@scholarcamp.ai",))
    assert row is not None
    data = db_manager.dict_row(row)
    assert data["email"] == "demo@scholarcamp.ai"
    assert data["cgpa"] > 0.0


def test_question_bank_seeded():
    """Verify question bank has items across technical topics."""
    topics = ["dsa", "dbms", "os", "cn", "programming", "aptitude"]
    for t in topics:
        res = db_manager.execute_query(queries.GET_QUESTIONS_BY_TOPIC, (t, 5))
        assert len(res) > 0, f"Topic {t} has no questions seeded!"


def test_schema_includes_all_research_tables():
    """Verify all 17 research tables and indexes exist in the database."""
    db_manager.initialize_schema()
    conn = db_manager._get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = {row[0] for row in cursor.fetchall()}
    
    expected_tables = {
        "students", "companies", "resumes", "question_bank", "assessments",
        "spv_snapshots", "learning_events", "roadmaps", "skill_map", "recommendations",
        "mock_interviews", "placement_predictions", "counterfactual_plans",
        "rag_documents", "rag_chunks", "experiment_runs", "model_registry", "audit_logs",
    }
    missing = expected_tables - tables
    assert not missing, f"Missing database tables: {missing}"

