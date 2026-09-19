"""
PRIE v1 — Profile & SPV API Routes
File: backend/api/v1_profile.py
"""

from __future__ import annotations

import json, sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from api.v1_auth import get_current_student
from modules.m01_spv_aggregator import SPVAggregator
from database import db_manager, queries

router = APIRouter()


class ProfileUpdateRequest(BaseModel):
    name: Optional[str] = None
    branch: Optional[str] = None
    cgpa: Optional[float] = None
    has_internship: Optional[int] = None
    internship_months: Optional[int] = None
    project_count: Optional[int] = None
    project_quality_score: Optional[float] = None
    certifications_count: Optional[int] = None
    target_role: Optional[str] = None
    skills_json: Optional[str] = None
    learning_style: Optional[str] = None


@router.get("/me")
def get_profile(student_id: int = Depends(get_current_student)):
    row = db_manager.dict_row(db_manager.execute_single(queries.GET_STUDENT_BY_ID, (student_id,)))
    if not row:
        raise HTTPException(status_code=404, detail="Student not found")
    row.pop("password_hash", None)
    return row


@router.get("/spv")
def get_spv(student_id: int = Depends(get_current_student)):
    """GET /api/v1/profile/spv — Returns F01–F22 tensor + confidence mask + SPV version."""
    try:
        aggregator = SPVAggregator()
        return aggregator.get_feature_dict(student_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/update")
def update_profile(req: ProfileUpdateRequest, student_id: int = Depends(get_current_student)):
    row = db_manager.dict_row(db_manager.execute_single(queries.GET_STUDENT_BY_ID, (student_id,)))
    if not row:
        raise HTTPException(status_code=404, detail="Student not found")

    updated = {k: v for k, v in req.dict().items() if v is not None}

    db_manager.execute_update(
        queries.UPDATE_STUDENT_PROFILE,
        (
            updated.get("name", row["name"]),
            updated.get("branch", row["branch"]),
            updated.get("cgpa", row["cgpa"]),
            updated.get("has_internship", row["has_internship"]),
            updated.get("internship_months", row["internship_months"]),
            updated.get("project_count", row["project_count"]),
            updated.get("project_quality_score", row["project_quality_score"]),
            updated.get("certifications_count", row["certifications_count"]),
            updated.get("target_role", row["target_role"]),
            updated.get("skills_json", row["skills_json"]),
            updated.get("learning_style", row["learning_style"]),
            row.get("profile_completeness", 0.0),
            student_id,
        ),
    )
    return {"status": "updated", "student_id": student_id}
