"""
Unit tests for Module M09 (Curriculum RAG) and Module M10 (Bloom's AQG).
Verifies dense retrieval grounding, citations, hallucination safeguards,
and Bloom taxonomy cognitive question generation.
"""

import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from modules.m09_rag_assistant import CurriculumRAGAssistant
from modules.m10_aqg import AutomatedQuestionGenerator


def test_rag_grounded_query():
    """Verify RAG retrieves verified curriculum context and includes citations."""
    assistant = CurriculumRAGAssistant()
    res = assistant.answer("What is relational normalization and what are ACID transactions in DBMS?")

    assert res["is_grounded"] is True
    assert res["retrieval_score"] > 0.15
    assert len(res["citations"]) > 0
    assert "DBMS" in res["response"] or "database" in res["response"].lower()
    assert "assembled_context" in res


def test_rag_ungrounded_safeguard():
    """Verify RAG identifies out-of-domain query and does not fabricate grounded response."""
    assistant = CurriculumRAGAssistant()
    # Query completely unrelated to curriculum
    res = assistant.answer("What is the recipe for baking chocolate chip cookies with almond flour?")

    assert res["is_grounded"] is False
    assert len(res["citations"]) == 0
    assert "No verified syllabus" in res["response"]


def test_aqg_bloom_taxonomy():
    """Verify AQG generates items tagged with Bloom cognitive taxonomy levels."""
    aqg = AutomatedQuestionGenerator()
    res = aqg.generate(topic="DSA", difficulty="Medium", bloom_level="Analyze", count=2)

    assert "questions" in res
    assert len(res["questions"]) > 0
    for q in res["questions"]:
        assert "question_id" in q
        assert "question_text" in q
        assert "options" in q
        assert "correct_option" in q
        assert "explanation" in q
        assert "bloom_level" in q
