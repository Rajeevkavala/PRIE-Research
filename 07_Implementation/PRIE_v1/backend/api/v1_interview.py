"""
PRIE v1 — REST API: Multimodal Mock Interview Coach (M05)
File: backend/api/v1_interview.py
"""

from __future__ import annotations

import shutil
import uuid
from pathlib import Path
from typing import Any, Dict, Optional

from fastapi import APIRouter, File, Form, HTTPException, UploadFile
from pydantic import BaseModel, Field

import config
from modules.m05_mock_interview import MultimodalMockInterviewCoach

router = APIRouter()
coach = MultimodalMockInterviewCoach()


class InterviewTextSubmitRequest(BaseModel):
    student_id: int = 1
    session_id: Optional[str] = None
    target_role: str = "Software Development Engineer"
    transcript_text: str
    duration_seconds: float = 30.0


@router.post("/process-session", response_model=Dict[str, Any])
async def process_session(
    student_id: int = Form(1),
    session_id: Optional[str] = Form(None),
    target_role: str = Form("Software Development Engineer"),
    file: UploadFile = File(...),
):
    """Upload recorded interview audio/video for multimodal analysis."""
    s_id = session_id or f"session_{uuid.uuid4().hex[:8]}"
    upload_dir = config.ROOT_DIR / "uploads" / "interviews"
    upload_dir.mkdir(parents=True, exist_ok=True)

    dest_path = upload_dir / f"{s_id}_{file.filename}"
    with open(dest_path, "wb") as buf:
        shutil.copyfileobj(file.file, buf)

    try:
        results = coach.process_interview_session(
            student_id=student_id,
            session_id=s_id,
            media_path=str(dest_path),
            target_role=target_role,
        )
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Interview analysis failed: {e}")


@router.post("/submit-text", response_model=Dict[str, Any])
async def submit_text_interview(request: InterviewTextSubmitRequest):
    """Submit simulated text response for speech linguistic diagnostics."""
    speech_res = coach.speech_analyzer.analyze_text(
        request.transcript_text, duration_seconds=request.duration_seconds
    )
    s_id = request.session_id or f"session_{uuid.uuid4().hex[:8]}"

    # Multimodal late fusion with baseline visual/acoustic
    audio_res = coach.audio_analyzer._default_acoustic_features(duration=request.duration_seconds)
    visual_res = coach.visual_analyzer._default_visual_features()

    overall_score = round(
        0.35 * audio_res["acoustic_delivery_score"] +
        0.35 * visual_res["visual_composure_score"] +
        0.30 * speech_res["semantic_delivery_score"],
        1
    )

    return {
        "session_id": s_id,
        "student_id": request.student_id,
        "overall_interview_score": overall_score,
        "spv_f20_behavior_score": round(overall_score / 100.0, 4),
        "speech_breakdown": speech_res,
        "acoustic_breakdown": audio_res,
        "visual_breakdown": visual_res,
        "epistemological_status": "ESTABLISHED_BY_RESEARCH (ASR Speech Diagnostics, DD-005)",
    }
