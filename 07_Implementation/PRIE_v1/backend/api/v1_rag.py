"""
PRIE v1 — REST API: Curriculum RAG Assistant (M09) & Bloom's AQG (M10)
File: backend/api/v1_rag.py
"""

from __future__ import annotations

from typing import Any, Dict, Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from modules.m09_rag_assistant import CurriculumRAGAssistant

router = APIRouter()
rag_assistant = CurriculumRAGAssistant()


class RAGQueryRequest(BaseModel):
    question: str = Field(..., description="Student curriculum query")
    top_k: int = Field(3, ge=1, le=10)
    threshold: float = Field(0.20, ge=0.0, le=1.0)


@router.post("/query", response_model=Dict[str, Any])
async def query_rag(request: RAGQueryRequest):
    """Query the curriculum knowledge base with grounding validation and citations."""
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    res = rag_assistant.answer(
        question=request.question,
        top_k=request.top_k,
        threshold=request.threshold,
    )
    return res
