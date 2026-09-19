"""
PRIE v1 — Adaptive Assessment API Routes
File: backend/api/v1_assessment.py
"""

from __future__ import annotations
import sys
from pathlib import Path
from typing import List, Optional
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from api.v1_auth import get_current_student
from modules.m03_adaptive_assessment import AdaptiveAssessmentEngine

router = APIRouter()
engine = AdaptiveAssessmentEngine()


class SessionHistory(BaseModel):
    history: List[dict] = []


class AnswerSubmit(BaseModel):
    question_id: int
    topic: str
    difficulty: str
    selected_option: str
    time_taken_seconds: float = 0.0


@router.get("/topics")
def get_topics():
    return {"topics": engine.get_topics()}


@router.post("/next-item/{topic}")
def next_question(topic: str, body: SessionHistory, student_id: int = Depends(get_current_student)):
    """POST /api/v1/assessment/next-item/{topic} — Get next adaptive question."""
    question = engine.get_next_question(student_id, topic, body.history)
    if not question:
        raise HTTPException(status_code=404, detail="No questions available for this topic")
    # Remove correct_option from response (don't leak answer)
    safe = {k: v for k, v in question.items() if k != "correct_option"}
    return safe


@router.post("/submit")
def submit_answer(body: AnswerSubmit, student_id: int = Depends(get_current_student)):
    """POST /api/v1/assessment/submit — Submit answer and get feedback."""
    try:
        result = engine.submit_answer(
            student_id, body.question_id, body.topic,
            body.difficulty, body.selected_option, body.time_taken_seconds,
        )
        mastery = engine.compute_topic_mastery(student_id, body.topic)
        result["topic_mastery"] = mastery
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/mastery/{topic}")
def get_mastery(topic: str, student_id: int = Depends(get_current_student)):
    mastery = engine.compute_topic_mastery(student_id, topic)
    return {"topic": topic, "mastery_score": mastery}
