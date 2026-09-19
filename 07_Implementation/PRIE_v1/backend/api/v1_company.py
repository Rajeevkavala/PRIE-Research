"""
PRIE v1 — REST API: Company Benchmark Matcher (M11)
File: backend/api/v1_company.py
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from fastapi import APIRouter
from pydantic import BaseModel, Field

from modules.m11_company_matcher import CompanyBenchmarkMatcher
from spv_version import SPV_FEATURE_NAMES

router = APIRouter()
matcher = CompanyBenchmarkMatcher()


class CompanyMatchRequest(BaseModel):
    student_cgpa: float = Field(7.5, ge=0.0, le=10.0)
    student_skills: List[str] = Field(default_factory=lambda: ["python", "sql", "git"])
    spv_dict: Optional[Dict[str, float]] = None
    company_name: Optional[str] = None


@router.get("/benchmarks", response_model=List[Dict[str, Any]])
async def list_company_benchmarks():
    """List all available enterprise benchmark criteria."""
    return matcher.companies


@router.post("/match", response_model=List[Dict[str, Any]])
async def evaluate_company_compatibility(request: CompanyMatchRequest):
    """Evaluate student profile against company benchmark standards."""
    spv = request.spv_dict or {f: 0.65 for f in SPV_FEATURE_NAMES}
    results = matcher.evaluate_student(
        student_cgpa=request.student_cgpa,
        student_skills=request.student_skills,
        spv_dict=spv,
        company_name=request.company_name,
    )
    return results
