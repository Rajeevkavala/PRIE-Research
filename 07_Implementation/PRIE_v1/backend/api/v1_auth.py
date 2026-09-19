"""
PRIE v1 — Authentication API Routes
File: backend/api/v1_auth.py
"""

from __future__ import annotations

import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, EmailStr

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config
from database import db_manager, queries

router = APIRouter()
security = HTTPBearer()


# ── JWT Helpers ───────────────────────────────────────────────────────────────
def _create_token(student_id: int, is_admin: bool = False) -> str:
    try:
        import jwt
        payload = {
            "sub":      str(student_id),
            "is_admin": is_admin,
            "exp":      datetime.utcnow() + timedelta(minutes=config.JWT_EXPIRE_MINUTES),
        }
        return jwt.encode(payload, config.SECRET_KEY, algorithm=config.JWT_ALGORITHM)
    except ImportError:
        # Fallback simple token
        return f"prie-{student_id}-token"


def _decode_token(token: str) -> dict:
    if token.startswith("prie-") and token.endswith("-token"):
        try:
            sid = int(token.split("-")[1])
            return {"sub": str(sid), "is_admin": False}
        except Exception:
            pass
    try:
        import jwt
        return jwt.decode(token, config.SECRET_KEY, algorithms=[config.JWT_ALGORITHM])
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


def get_current_student(credentials: HTTPAuthorizationCredentials = Depends(security)) -> int:
    payload = _decode_token(credentials.credentials)
    return int(payload["sub"])


def get_current_admin(credentials: HTTPAuthorizationCredentials = Depends(security)) -> int:
    payload = _decode_token(credentials.credentials)
    if not payload.get("is_admin"):
        raise HTTPException(status_code=403, detail="Admin access required")
    return int(payload["sub"])


# ── Schemas ───────────────────────────────────────────────────────────────────
class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    branch: str = "Computer Science"
    cgpa: float = 0.0
    target_role: str = "Software Development Engineer"
    learning_style: str = "practical"


class LoginRequest(BaseModel):
    email: str
    password: str


# ── Endpoints ─────────────────────────────────────────────────────────────────
@router.post("/register", status_code=201)
def register(req: RegisterRequest):
    # Check if email already exists
    existing = db_manager.execute_single(queries.GET_STUDENT_BY_EMAIL, (req.email,))
    if existing:
        raise HTTPException(status_code=409, detail="Email already registered")

    # Hash password
    try:
        import bcrypt
        hashed = bcrypt.hashpw(req.password.encode(), bcrypt.gensalt(rounds=config.BCRYPT_ROUNDS)).decode()
    except ImportError:
        import hashlib
        hashed = hashlib.sha256(req.password.encode()).hexdigest()

    student_id = db_manager.execute_insert(
        queries.INSERT_STUDENT,
        (
            req.name, req.email, hashed, req.branch, req.cgpa,
            0, 0, 0, 40.0, 0, req.target_role,
            "[]", req.learning_style,
        ),
    )

    token = _create_token(student_id, is_admin=False)
    return {
        "access_token": token,
        "token_type":   "bearer",
        "student_id":   student_id,
        "name":         req.name,
        "email":        req.email,
        "is_admin":     False,
    }


@router.post("/login")
def login(req: LoginRequest):
    row = db_manager.dict_row(db_manager.execute_single(queries.GET_STUDENT_BY_EMAIL, (req.email,)))
    if not row:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Verify password
    try:
        import bcrypt
        valid = bcrypt.checkpw(req.password.encode(), row["password_hash"].encode())
    except ImportError:
        import hashlib
        valid = (hashlib.sha256(req.password.encode()).hexdigest() == row["password_hash"])

    if not valid:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = _create_token(row["student_id"], is_admin=bool(row.get("is_admin")))
    return {
        "access_token": token,
        "token_type":   "bearer",
        "student_id":   row["student_id"],
        "name":         row["name"],
        "email":        row["email"],
        "is_admin":     bool(row.get("is_admin")),
    }
