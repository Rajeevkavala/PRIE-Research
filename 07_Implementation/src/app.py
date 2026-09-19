"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Main Application Entry Point & Navigation Router
File: app.py

Adheres to:
- Implementation Plan: 05_Streamlit_Implementation.md
- Streamlit 1.30+ Multi-Page st.Page & st.navigation architecture
- Chapter 09: System Implementation
"""

from __future__ import annotations

import streamlit as st
from utils.auth import get_current_user, is_authenticated, logout_user

# =============================================================================
# 1. Global Page Configuration
# =============================================================================
st.set_page_config(
    page_title="ScholarCamp | PRIE",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =============================================================================
# 2. Global CSS Injection — Modern Elevation, Typography & Badges
# =============================================================================
st.markdown(
    """
<style>
    /* Metric Card Styling */
    .metric-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        margin-bottom: 1rem;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    }
    
    /* Technical Skill Badges */
    .badge {
        display: inline-block;
        padding: 0.28rem 0.65rem;
        font-size: 0.82rem;
        font-weight: 600;
        border-radius: 9999px;
        background-color: #EFF6FF;
        color: #1D4ED8;
        border: 1px solid #DBEAFE;
        margin-right: 0.35rem;
        margin-bottom: 0.45rem;
    }
    .badge-success {
        background-color: #DCFCE7;
        color: #15803D;
        border-color: #BBF7D0;
    }
    .badge-warning {
        background-color: #FEF3C7;
        color: #B45309;
        border-color: #FDE68A;
    }
    .badge-danger {
        background-color: #FEE2E2;
        color: #B91C1C;
        border-color: #FECACA;
    }

    /* Status Pills */
    .status-pill {
        display: inline-block;
        padding: 0.2rem 0.5rem;
        font-size: 0.75rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        border-radius: 6px;
    }

    /* Sidebar Profile Card */
    .sidebar-profile {
        padding: 1rem;
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

# =============================================================================
# 3. Authentication & Role Detection
# =============================================================================
authenticated = is_authenticated()
user = get_current_user() or {}
is_admin = bool(st.session_state.get("is_admin", user.get("is_admin", False)))

# =============================================================================
# 4. Define Application Pages (Streamlit 1.30+ st.Page)
# =============================================================================
# Public Authentication Pages
login_page = st.Page("pages/01_login.py", title="Sign In", icon="🔐", default=(not authenticated))
register_page = st.Page("pages/02_register.py", title="Register", icon="📝")

# Protected Student Workspace Pages
dashboard_page = st.Page("pages/03_dashboard.py", title="Dashboard", icon="📊", default=(authenticated and not is_admin))
assessment_page = st.Page("pages/04_assessment.py", title="Adaptive Assessment", icon="✍️")
resume_page = st.Page("pages/05_resume.py", title="Resume & ATS", icon="📄")
roadmap_page = st.Page("pages/06_roadmap.py", title="Study Roadmap", icon="🗺️")
recommendations_page = st.Page("pages/07_recommendations.py", title="Recommendations", icon="💡")
company_page = st.Page("pages/08_company_readiness.py", title="Company Readiness", icon="🏢")
progress_page = st.Page("pages/09_progress.py", title="Progress Tracker", icon="📈")

# Protected Administration Page
admin_page = st.Page("pages/10_admin.py", title="Admin Cohort Analytics", icon="⚙️", default=(authenticated and is_admin))

# =============================================================================
# 5. Multi-Page Navigation Routing Logic
# =============================================================================
if not authenticated:
    # Public mode: only display Sign In and Registration
    pg = st.navigation({"Account Access": [login_page, register_page]})
else:
    # Protected mode: Student Workspace + Optional Faculty / Admin Portal
    nav_sections = {
        "Student Workspace": [
            dashboard_page,
            assessment_page,
            resume_page,
            roadmap_page,
            recommendations_page,
            company_page,
            progress_page,
        ]
    }
    if is_admin:
        nav_sections["Administration"] = [admin_page]

    pg = st.navigation(nav_sections)

    # Sidebar Header & User Profile
    with st.sidebar:
        st.markdown("### 🎓 ScholarCamp PRIE")
        st.caption("Placement Readiness Intelligence Engine")
        st.divider()

        user_name = st.session_state.get("name", user.get("name", "Student"))
        user_email = st.session_state.get("email", user.get("email", ""))
        user_role = "Administrator" if is_admin else user.get("target_role", "Engineering Candidate")

        st.markdown(
            f"""
        <div class="sidebar-profile">
            <div style="font-weight: 700; font-size: 0.95rem; color: #0F172A;">{user_name}</div>
            <div style="font-size: 0.8rem; color: #64748B;">{user_email}</div>
            <div style="margin-top: 0.4rem;">
                <span class="badge {'badge-warning' if is_admin else 'badge-success'}">{user_role}</span>
            </div>
        </div>
        """,
            unsafe_allow_html=True,
        )

        if st.button("🚪 Sign Out", use_container_width=True, type="secondary"):
            logout_user()
            st.rerun()

# =============================================================================
# 5. Execute Current Active Page
# =============================================================================
pg.run()
