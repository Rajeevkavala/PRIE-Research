"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Input Validation and Sanitization Service
File: utils/validators.py

Provides robust validation and sanitization primitives for student registration,
academic credential inputs, resume uploads, and user-submitted data.
Adheres to strict defensive programming and security best practices.
"""

from __future__ import annotations

import html
import re
from pathlib import Path
from typing import Any, Optional, Set, Tuple

import config

# RFC 5322 simplified email regex pattern with min 2-char TLD
EMAIL_REGEX: re.Pattern = re.compile(
    r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$"
)

# HTML Tag stripping pattern for text sanitization
HTML_TAG_REGEX: re.Pattern = re.compile(r"<[^>]*>")

# Allowed resume file extensions
DEFAULT_ALLOWED_EXTENSIONS: Set[str] = {".pdf", ".docx"}


def validate_email(email: Optional[str]) -> bool:
    """Validate email address against RFC 5322 standards.

    Args:
        email: Candidate email string.

    Returns:
        bool: True if email is non-empty, well-formed, and valid; False otherwise.
    """
    if not email or not isinstance(email, str):
        return False
    cleaned = email.strip()
    if len(cleaned) > 255:
        return False
    return bool(EMAIL_REGEX.match(cleaned))


def validate_password(password: Optional[str]) -> Tuple[bool, str]:
    """Validate password strength according to institutional security policy.

    Requirements:
    - Minimum length: 8 characters
    - Must contain at least one letter (a-z, A-Z)
    - Must contain at least one digit or special character

    Args:
        password: Plaintext password candidate.

    Returns:
        Tuple[bool, str]: (is_valid, validation_message)
    """
    if not password or not isinstance(password, str):
        return False, "Password cannot be empty."

    if len(password) < 8:
        return False, "Password must be at least 8 characters in length."

    if len(password) > 128:
        return False, "Password exceeds maximum allowable length of 128 characters."

    has_letter = any(c.isalpha() for c in password)
    has_digit_or_special = any(c.isdigit() or not c.isalnum() for c in password)

    if not has_letter:
        return False, "Password must contain at least one letter."

    if not has_digit_or_special:
        return False, "Password must contain at least one number or special character."

    return True, "Password meets all security criteria."


def validate_cgpa(cgpa: Any) -> Tuple[bool, float, str]:
    """Validate cumulative grade point average (CGPA).

    Academic scale: 0.0 to 10.0 inclusive.

    Args:
        cgpa: Numeric value or parseable string.

    Returns:
        Tuple[bool, float, str]: (is_valid, parsed_cgpa, error_message)
    """
    if cgpa is None:
        return False, 0.0, "CGPA value is required."

    try:
        val = float(cgpa)
    except (ValueError, TypeError):
        return False, 0.0, f"Invalid CGPA format: '{cgpa}'. Must be a floating-point number."

    if val < 0.0 or val > 10.0:
        return False, val, f"CGPA {val} is outside allowed academic bounds [0.0, 10.0]."

    return True, round(val, 2), "CGPA is valid."


def validate_backlogs(backlogs: Any) -> Tuple[bool, int, str]:
    """Validate active backlog count.

    Must be a non-negative integer (0 to 50).

    Args:
        backlogs: Integer value or parseable string.

    Returns:
        Tuple[bool, int, str]: (is_valid, parsed_backlogs, error_message)
    """
    if backlogs is None:
        return False, 0, "Backlogs value is required."

    try:
        val = int(backlogs)
    except (ValueError, TypeError):
        return False, 0, f"Invalid backlogs format: '{backlogs}'. Must be an integer."

    if val < 0:
        return False, val, f"Backlogs cannot be negative: {val}."

    if val > 50:
        return False, val, f"Backlog count {val} exceeds reasonable threshold."

    return True, val, "Backlogs count is valid."


def validate_name(name: Optional[str]) -> Tuple[bool, str]:
    """Validate student or user display name.

    Args:
        name: Name string.

    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    if not name or not isinstance(name, str):
        return False, "Name cannot be empty."

    cleaned = name.strip()
    if len(cleaned) < 2:
        return False, "Name must be at least 2 characters long."

    if len(cleaned) > 100:
        return False, "Name must not exceed 100 characters."

    return True, "Name is valid."


def validate_file_extension(
    filename: Optional[str],
    allowed_extensions: Optional[Set[str]] = None,
) -> bool:
    """Validate file extension against allowed whitelist.

    Args:
        filename: Name or path of candidate file.
        allowed_extensions: Set of allowed extensions with leading period.
                           Defaults to {'.pdf', '.docx'}.

    Returns:
        bool: True if extension is permitted; False otherwise.
    """
    if not filename or not isinstance(filename, str):
        return False

    allowed = allowed_extensions or DEFAULT_ALLOWED_EXTENSIONS
    suffix = Path(filename).suffix.lower()
    return suffix in {ext.lower() for ext in allowed}


def validate_file_size(
    file_bytes_len: int,
    max_bytes: int = config.MAX_UPLOAD_SIZE_BYTES,
) -> bool:
    """Validate uploaded file size against maximum allowable threshold.

    Args:
        file_bytes_len: Byte size of uploaded file payload.
        max_bytes: Maximum allowed byte size (default: 5 MB).

    Returns:
        bool: True if file size is strictly greater than 0 and <= max_bytes.
    """
    if not isinstance(file_bytes_len, int):
        return False
    return 0 < file_bytes_len <= max_bytes


def sanitize_text(text: Optional[str]) -> str:
    """Sanitize raw text input to prevent XSS and strip unwanted markup.

    Strips HTML tags, unescapes entities safely, and normalizes excessive whitespace.

    Args:
        text: Raw user-submitted string.

    Returns:
        str: Sanitized plain text string.
    """
    if not text or not isinstance(text, str):
        return ""

    # Strip HTML tags
    stripped = HTML_TAG_REGEX.sub(" ", text)
    # Unescape HTML entities
    unescaped = html.unescape(stripped)
    # Normalize contiguous whitespace
    normalized = re.sub(r"\s+", " ", unescaped)
    # Clean space before trailing punctuation marks
    cleaned = re.sub(r"\s+([.,!?:;])", r"\1", normalized).strip()
    return cleaned
