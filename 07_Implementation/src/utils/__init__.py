"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Utilities Package Initializer

Contains cross-cutting helper functions:
- auth: Bcrypt hashing, token verification, session protection
- validators: Input sanitization, email regex, file type checks
- text_processing: PDF/DOCX extractors, text cleaning
- feature_engineering: 22-feature vector scaling, encoding
- visualization: Plotly charts (radar, gauge, waterfall)
"""

from utils.auth import (
    authenticate_user,
    get_current_user,
    hash_password,
    is_authenticated,
    login_user,
    logout_user,
    register_user,
    require_auth,
    verify_password,
)
from utils.text_processing import (
    build_skill_regex_pattern,
    extract_document_text,
    extract_text_from_docx,
    extract_text_from_pdf,
    normalize_technical_text,
)
from utils.validators import (
    sanitize_text,
    validate_backlogs,
    validate_cgpa,
    validate_email,
    validate_file_extension,
    validate_file_size,
    validate_name,
    validate_password,
)
from utils.visualization import (
    create_branch_comparison_chart,
    create_cohort_distribution_chart,
    create_component_radar,
    create_prs_gauge,
    create_prs_history_chart,
    create_shap_waterfall,
    create_skill_gap_chart,
)

__all__ = [
    "authenticate_user",
    "get_current_user",
    "hash_password",
    "is_authenticated",
    "login_user",
    "logout_user",
    "register_user",
    "require_auth",
    "verify_password",
    "sanitize_text",
    "validate_backlogs",
    "validate_cgpa",
    "validate_email",
    "validate_file_extension",
    "validate_file_size",
    "validate_name",
    "validate_password",
    "extract_text_from_pdf",
    "extract_text_from_docx",
    "extract_document_text",
    "normalize_technical_text",
    "build_skill_regex_pattern",
    "create_prs_gauge",
    "create_component_radar",
    "create_shap_waterfall",
    "create_skill_gap_chart",
    "create_prs_history_chart",
    "create_cohort_distribution_chart",
    "create_branch_comparison_chart",
]
