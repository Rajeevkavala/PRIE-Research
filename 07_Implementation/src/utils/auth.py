"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Security & Authentication Service
File: utils/auth.py

Implements salted bcrypt password hashing, credential verification, user registration,
and session lifecycle management for Streamlit multi-page routing.
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional, Tuple, Union

import bcrypt
import streamlit as st

import config
from database import queries
from database.db_manager import execute_insert, execute_single
from utils import validators

logger = logging.getLogger("PRIE.Auth")


def hash_password(plain_password: str) -> str:
    """Hash a plaintext password with a random salted bcrypt round.

    Args:
        plain_password: Cleartext password string.

    Returns:
        str: Bcrypt hash encoded as UTF-8 string.

    Raises:
        ValueError: If password is empty or invalid type.
    """
    if not plain_password or not isinstance(plain_password, str):
        raise ValueError("Password must be a non-empty string.")

    salt = bcrypt.gensalt(rounds=int(getattr(config, "BCRYPT_ROUNDS", 12)))
    hashed_bytes = bcrypt.hashpw(plain_password.encode("utf-8"), salt)
    return hashed_bytes.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plaintext password against its stored bcrypt hash.

    Args:
        plain_password: Cleartext password candidate.
        hashed_password: Stored bcrypt hash string.

    Returns:
        bool: True if candidate matches hash; False otherwise.
    """
    if not plain_password or not hashed_password:
        return False

    try:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"),
            hashed_password.encode("utf-8"),
        )
    except Exception as exc:
        logger.warning("Bcrypt verification failed due to format error: %s", exc)
        return False


def authenticate_user(
    email: str,
    plain_password: str,
    db_path: Optional[Union[str, Path]] = None,
) -> Optional[Dict[str, Any]]:
    """Authenticate student or administrator credentials against the database.

    Args:
        email: Candidate email address.
        plain_password: Candidate plaintext password.
        db_path: Optional explicit database file path.

    Returns:
        Optional[Dict[str, Any]]: User record dictionary if authentication succeeds;
                                 None otherwise. Password hash is redacted in result.
    """
    if not email or not plain_password:
        return None

    clean_email = email.strip().lower()
    user_row = execute_single(
        queries.GET_STUDENT_BY_EMAIL,
        (clean_email,),
        db_path=db_path,
    )

    if not user_row:
        logger.info("Authentication attempt failed: user not found (%s)", clean_email)
        return None

    user_dict = dict(user_row)
    stored_hash = user_dict.get("password_hash", "")

    if verify_password(plain_password, stored_hash):
        logger.info("Authentication successful: student_id=%s (%s)", user_dict["student_id"], clean_email)
        # Redact raw password hash before returning dictionary
        user_dict.pop("password_hash", None)
        return user_dict

    logger.warning("Authentication failed: invalid password for (%s)", clean_email)
    return None


def register_user(
    name: str,
    email: str,
    password: str,
    branch: str = "Computer Science",
    cgpa: float = 7.0,
    backlogs: int = 0,
    target_role: str = "Software Development Engineer",
    target_company_id: Optional[int] = None,
    learning_style: str = "practical",
    is_admin: int = 0,
    db_path: Optional[Union[str, Path]] = None,
) -> Tuple[bool, str, Optional[int]]:
    """Register a new student or admin account with validation and password hashing.

    Args:
        name: Full display name.
        email: Candidate email address.
        password: Plaintext password.
        branch: Academic engineering branch.
        cgpa: Academic CGPA (0.0 to 10.0).
        backlogs: Active backlogs count.
        target_role: Target career job profile.
        target_company_id: Target benchmark company ID.
        learning_style: Preferred learning modality.
        is_admin: 1 if administrator, 0 otherwise.
        db_path: Optional explicit database path.

    Returns:
        Tuple[bool, str, Optional[int]]: (success, message, created_student_id)
    """
    # 1. Validate inputs
    is_name_valid, name_msg = validators.validate_name(name)
    if not is_name_valid:
        return False, name_msg, None

    if not validators.validate_email(email):
        return False, "Invalid email address format.", None

    is_pwd_valid, pwd_msg = validators.validate_password(password)
    if not is_pwd_valid:
        return False, pwd_msg, None

    is_cgpa_valid, parsed_cgpa, cgpa_msg = validators.validate_cgpa(cgpa)
    if not is_cgpa_valid:
        return False, cgpa_msg, None

    is_backlogs_valid, parsed_backlogs, backlogs_msg = validators.validate_backlogs(backlogs)
    if not is_backlogs_valid:
        return False, backlogs_msg, None

    clean_email = email.strip().lower()
    clean_name = validators.sanitize_text(name)

    # 2. Check for duplicate email
    existing_user = execute_single(
        queries.GET_STUDENT_BY_EMAIL,
        (clean_email,),
        db_path=db_path,
    )
    if existing_user:
        return False, f"An account with email '{clean_email}' already exists.", None

    # 3. Hash password and insert record
    pwd_hash = hash_password(password)

    try:
        student_id = execute_insert(
            queries.CREATE_STUDENT,
            (
                clean_name,
                clean_email,
                pwd_hash,
                branch,
                parsed_cgpa,
                parsed_backlogs,
                "[]",  # skills_json
                target_role,
                target_company_id,
                learning_style,
                0.0,   # profile_completeness
                int(is_admin),
            ),
            db_path=db_path,
        )

        # Log registration learning event
        execute_insert(
            queries.INSERT_LEARNING_EVENT,
            (
                student_id,
                "registration",
                json.dumps({"name": clean_name, "email": clean_email}),
                "Student account registered successfully",
                0,
            ),
            db_path=db_path,
        )

        return True, "Registration successful.", student_id

    except Exception as exc:
        logger.error("Registration database insert error: %s", exc)
        return False, f"Database error during registration: {exc}", None


def login_user(user_dict: Dict[str, Any]) -> None:
    """Initialize Streamlit session state upon successful authentication.

    Args:
        user_dict: User profile dictionary from authenticate_user.
    """
    try:
        st.session_state["authenticated"] = True
        st.session_state["student_id"] = user_dict["student_id"]
        st.session_state["name"] = user_dict["name"]
        st.session_state["email"] = user_dict["email"]
        st.session_state["is_admin"] = bool(user_dict.get("is_admin", 0))
        st.session_state["user"] = dict(user_dict)
    except Exception as exc:
        logger.warning("Streamlit session_state not accessible: %s", exc)


def logout_user() -> None:
    """Clear Streamlit session authentication tokens and reset state."""
    try:
        for key in ["authenticated", "student_id", "name", "email", "is_admin", "user", "current_prs"]:
            if key in st.session_state:
                del st.session_state[key]
        st.session_state["authenticated"] = False
    except Exception as exc:
        logger.warning("Streamlit session_state not accessible during logout: %s", exc)


def is_authenticated() -> bool:
    """Check if active Streamlit session is authenticated.

    Returns:
        bool: True if authenticated session exists; False otherwise.
    """
    try:
        return bool(st.session_state.get("authenticated", False))
    except Exception:
        return False


def get_current_user() -> Optional[Dict[str, Any]]:
    """Retrieve active user dictionary from Streamlit session state.

    Returns:
        Optional[Dict[str, Any]]: User dictionary or None if unauthenticated.
    """
    try:
        if is_authenticated():
            return st.session_state.get("user")
        return None
    except Exception:
        return None


def require_auth(
    require_admin: bool = False,
    login_page: str = "pages/01_login.py",
) -> Optional[Dict[str, Any]]:
    """Page guard requiring active authentication to access protected routes.

    Redirects unauthenticated users to login page and halts execution.

    Args:
        require_admin: If True, halts if authenticated user is not an admin.
        login_page: Relative path to login page.

    Returns:
        Optional[Dict[str, Any]]: Current authenticated user record if authorized.
    """
    if not is_authenticated():
        try:
            st.warning("Please sign in to access this page.")
            st.switch_page(login_page)
        except Exception:
            pass
        st.stop()
        return None

    user = get_current_user() or {}
    if require_admin and not user.get("is_admin", False):
        try:
            st.error("Access denied: Administrative privileges required.")
        except Exception:
            pass
        st.stop()
        return None

    return user
