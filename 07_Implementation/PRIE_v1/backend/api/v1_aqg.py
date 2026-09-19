"""
PRIE v1 — REST API: Bloom's Taxonomy Automated Question Generation (M10)
File: backend/api/v1_aqg.py
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field

from modules.m10_aqg import AutomatedQuestionGenerator

router = APIRouter()
aqg_engine = AutomatedQuestionGenerator()


class AQGGenerateRequest(BaseModel):
    topic: str = "DSA"
    concept_node_id: Optional[str] = None
    difficulty: str = "Medium"
    bloom_level: str = "Apply"
    count: int = Field(3, ge=1, le=10)


@router.post("/generate", response_model=Dict[str, Any])
async def generate_questions(request: AQGGenerateRequest):
    """Generate or retrieve questions aligned to specific Bloom taxonomy levels."""
    res = aqg_engine.generate(
        topic=request.topic,
        concept_node_id=request.concept_node_id,
        difficulty=request.difficulty,
        bloom_level=request.bloom_level,
        count=request.count,
    )
    return res
