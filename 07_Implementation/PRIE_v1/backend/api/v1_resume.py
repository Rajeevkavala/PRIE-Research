"""
PRIE v1 — REST API: Resume ATS & Spatial Extraction
File: backend/api/v1_resume.py
"""

from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel, Field

import config
from modules.m02_resume_ats import ResumeATSEngine

router = APIRouter()
ats_engine = ResumeATSEngine()


class ResumeAnalysisResponse(BaseModel):
    ats_score: float = Field(..., description="Overall ATS score in [0, 100]")
    ats_breakdown: Dict[str, Any]
    cosine_similarity: float
    extracted_skills: list[str]
    spatial_token_count: int
    layoutlmv3_status: str
    layoutlmv3_details: Dict[str, Any]
    methodology_baseline: str


class ATSQueryRequest(BaseModel):
    resume_text: str
    target_role: str = "Software Development Engineer"
    jd_text: Optional[str] = ""


@router.post("/analyze-text", response_model=Dict[str, Any])
async def analyze_text(request: ATSQueryRequest):
    """Analyze resume plain text directly without file upload."""
    if not request.resume_text.strip():
        raise HTTPException(status_code=400, detail="Resume text cannot be empty.")

    breakdown = ats_engine.compute_ats_score(request.resume_text, target_role=request.target_role)
    skills = ats_engine.extract_skills(request.resume_text)
    sim = ats_engine.compute_cosine_similarity(request.resume_text, request.jd_text or "")

    return {
        "ats_score": breakdown["overall_ats_score"],
        "ats_breakdown": breakdown,
        "cosine_similarity": sim,
        "extracted_skills": skills,
        "layoutlmv3_status": "MODEL NOT TRAINED (Text mode active)",
    }


@router.post("/upload", response_model=ResumeAnalysisResponse)
async def upload_resume(
    student_id: int = Form(1),
    target_role: str = Form("Software Development Engineer"),
    jd_text: str = Form(""),
    file: UploadFile = File(...),
):
    """Upload PDF/DOCX resume for spatial extraction and ATS scoring."""
    suffix = Path(file.filename or "").suffix.lower()
    if suffix not in (".pdf", ".docx", ".doc"):
        raise HTTPException(status_code=400, detail="Only PDF and DOCX formats supported.")

    upload_dir = config.UPLOAD_DIR
    upload_dir.mkdir(parents=True, exist_ok=True)
    dest_path = upload_dir / f"student_{student_id}_{int(Path(file.filename).stat().st_mtime if Path(file.filename).exists() else 0)}_{file.filename}"

    with open(dest_path, "wb") as buf:
        shutil.copyfileobj(file.file, buf)

    try:
        res = ats_engine.analyze_resume(
            student_id=student_id,
            file_path=str(dest_path),
            target_role=target_role,
            jd_text=jd_text,
        )
        return res
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process resume: {e}")
