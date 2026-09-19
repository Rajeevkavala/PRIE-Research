"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Module: Visualizations & Plotly Chart Generators
File: utils/visualization.py

Provides production-grade Plotly interactive data visualizations adhering strictly to:
- Chapter 05: PRIE Mathematical Framework & Visual Dashboards
- Chapter 09: Streamlit System Implementation (Section 9.3)
- Implementation Plan: 05_Streamlit_Implementation.md
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union
import plotly.graph_objects as go
import plotly.express as px


def create_prs_gauge(
    prs_score: float,
    ci_lower: Optional[float] = None,
    ci_upper: Optional[float] = None,
) -> go.Figure:
    """Create a semi-circular speedometer gauge for Composite PRS.

    Args:
        prs_score: Composite Placement Readiness Score in [0.0, 100.0].
        ci_lower: Optional lower bound of 95% bootstrap confidence interval.
        ci_upper: Optional upper bound of 95% bootstrap confidence interval.

    Returns:
        go.Figure: Configured Plotly Indicator figure.
    """
    score = float(max(0.0, min(100.0, prs_score)))

    # Qualitative tier coloring for active gauge needle/bar
    if score < 30.0:
        bar_color = "#DC2626"  # Red (Critical)
    elif score < 50.0:
        bar_color = "#F59E0B"  # Amber (Low)
    elif score < 65.0:
        bar_color = "#EAB308"  # Yellow (Moderate)
    elif score < 80.0:
        bar_color = "#0284C7"  # Sky Blue (Good)
    elif score < 90.0:
        bar_color = "#2563EB"  # Royal Blue (High)
    else:
        bar_color = "#16A34A"  # Emerald Green (Excellent)

    subtitle_text = "Placement Readiness Index"
    if ci_lower is not None and ci_upper is not None:
        subtitle_text += f"<br><span style='font-size:12px;color:#64748B;'>95% CI: [{ci_lower:.1f}%, {ci_upper:.1f}%]</span>"

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": "", "font": {"size": 42, "color": "#0F172A", "family": "Inter, sans-serif"}},
            domain={"x": [0, 1], "y": [0, 1]},
            title={
                "text": subtitle_text,
                "font": {"size": 16, "color": "#334155", "family": "Inter, sans-serif"},
            },
            gauge={
                "axis": {
                    "range": [0, 100],
                    "tickwidth": 1.5,
                    "tickcolor": "#94A3B8",
                    "tickvals": [0, 30, 50, 65, 80, 100],
                    "ticktext": ["0", "30", "50", "65", "80", "100"],
                },
                "bar": {"color": bar_color, "thickness": 0.28},
                "bgcolor": "white",
                "borderwidth": 1,
                "bordercolor": "#E2E8F0",
                "steps": [
                    {"range": [0, 30], "color": "#FEE2E2"},    # Critical (Soft Red)
                    {"range": [30, 50], "color": "#FEF3C7"},   # Low (Soft Amber)
                    {"range": [50, 65], "color": "#FEF9C3"},   # Moderate (Soft Yellow)
                    {"range": [65, 80], "color": "#E0F2FE"},   # Good (Soft Light Blue)
                    {"range": [80, 100], "color": "#DCFCE7"},  # High/Ready (Soft Green)
                ],
                "threshold": {
                    "line": {"color": "#059669", "width": 4},
                    "thickness": 0.8,
                    "value": 85.0,
                },
            },
        )
    )

    fig.update_layout(
        height=270,
        margin=dict(l=24, r=24, t=48, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


def create_component_radar(components: Dict[str, float]) -> go.Figure:
    """Create a 7-axis radar chart showing normalized sub-score proficiencies.

    Dimensions:
        - ML Placement Prediction (s_pred)
        - Skill Coverage (s_skill)
        - Resume ATS Alignment (s_resume)
        - Learning Behavior (s_behavior)
        - Study Consistency (c_norm)
        - Target Company Alignment (s_company)
        - Diagnostic Assessment (s_assessment)

    Args:
        components: Dictionary containing component scores (either [0.0, 1.0] or [0, 100]).

    Returns:
        go.Figure: Configured Plotly Scatterpolar figure.
    """
    categories = [
        "ML Prediction",
        "Skill Coverage",
        "Resume ATS",
        "Behavior",
        "Consistency",
        "Company Fit",
        "Assessment",
    ]

    def _normalize_val(val: Any) -> float:
        if val is None:
            return 50.0
        fval = float(val)
        # If passed as [0.0, 1.0], scale to 100
        if 0.0 <= fval <= 1.0 and fval != 0.0:
            return round(fval * 100.0, 1)
        return round(max(0.0, min(100.0, fval)), 1)

    vals = [
        _normalize_val(components.get("s_pred", components.get("predictive", 0.5))),
        _normalize_val(components.get("s_skill", components.get("skill_coverage", 0.5))),
        _normalize_val(components.get("s_resume", components.get("resume", 0.5))),
        _normalize_val(components.get("s_behavior", components.get("behavior", 0.5))),
        _normalize_val(components.get("c_norm", components.get("consistency", 0.5))),
        _normalize_val(components.get("s_company", components.get("company_alignment", 0.5))),
        _normalize_val(components.get("s_assessment", components.get("assessment", 0.5))),
    ]

    # Close the radar loop
    closed_categories = categories + [categories[0]]
    closed_vals = vals + [vals[0]]

    fig = go.Figure(
        go.Scatterpolar(
            r=closed_vals,
            theta=closed_categories,
            fill="toself",
            fillcolor="rgba(37, 99, 235, 0.22)",
            line=dict(color="#2563EB", width=2.5),
            marker=dict(size=6, color="#1D4ED8"),
            name="Current Competency",
        )
    )

    # Add benchmark reference loop (e.g. 75% target readiness)
    benchmark_vals = [75.0] * len(closed_categories)
    fig.add_trace(
        go.Scatterpolar(
            r=benchmark_vals,
            theta=closed_categories,
            mode="lines",
            line=dict(color="#94A3B8", width=1.5, dash="dash"),
            name="Tier-1 Benchmark (75%)",
        )
    )

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(size=10, color="#64748B"),
                gridcolor="#E2E8F0",
            ),
            angularaxis=dict(
                tickfont=dict(size=12, color="#1E293B", family="Inter, sans-serif"),
                gridcolor="#E2E8F0",
            ),
        ),
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        height=320,
        margin=dict(l=48, r=48, t=28, b=36),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


def create_shap_waterfall(
    shap_values: Dict[str, float],
    top_n: int = 8,
) -> go.Figure:
    """Create horizontal bar chart representing local SHAP feature attributions.

    Args:
        shap_values: Dictionary mapping feature column names to SHAP attribution floats.
        top_n: Number of top diagnostic contributors to display.

    Returns:
        go.Figure: Configured Plotly Bar figure.
    """
    if not shap_values:
        shap_values = {"academic_cgpa": 0.12, "skill_match_ratio": 0.08, "coding_score": 0.05}

    sorted_items = sorted(shap_values.items(), key=lambda x: abs(x[1]), reverse=True)[:top_n]
    
    # Reverse so largest impact appears at the top of the horizontal bar chart
    features = [k.replace("_", " ").title() for k, _ in reversed(sorted_items)]
    values = [round(v, 4) for _, v in reversed(sorted_items)]
    colors = ["#16A34A" if v >= 0 else "#DC2626" for v in values]

    fig = go.Figure(
        go.Bar(
            x=values,
            y=features,
            orientation="h",
            marker=dict(color=colors, line=dict(color="rgba(0,0,0,0.08)", width=1)),
            text=[f"{v:+.3f}" for v in values],
            textposition="auto",
            textfont=dict(color="#FFFFFF", size=11, family="Inter, sans-serif"),
        )
    )

    fig.update_layout(
        title={
            "text": "TreeSHAP Local Feature Attributions (Strengths & Drags)",
            "font": {"size": 15, "color": "#1E293B", "family": "Inter, sans-serif"},
        },
        xaxis=dict(
            title="Marginal Contribution to Placement Probability",
            zeroline=True,
            zerolinecolor="#94A3B8",
            zerolinewidth=1.5,
            gridcolor="#F1F5F9",
        ),
        yaxis=dict(gridcolor="rgba(0,0,0,0)"),
        height=320,
        margin=dict(l=20, r=20, t=44, b=24),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


def create_skill_gap_chart(
    gap_vector: Dict[str, float],
    top_n: int = 10,
) -> go.Figure:
    """Create horizontal bar chart showing skill gaps against target company profile.

    Args:
        gap_vector: Dictionary mapping skill names to gap magnitude in [0.0, 1.0].
        top_n: Maximum skills to display.

    Returns:
        go.Figure: Configured Plotly Bar figure.
    """
    if not gap_vector:
        return go.Figure()

    def _extract_val(val: Any) -> float:
        if isinstance(val, dict):
            return float(val.get("priority", val.get("gap", val.get("weight", 0.0))))
        try:
            return float(val)
        except (ValueError, TypeError):
            return 0.0

    # Sort descending by gap magnitude
    sorted_gaps = sorted(gap_vector.items(), key=lambda x: _extract_val(x[1]), reverse=True)[:top_n]
    skills = [s for s, _ in reversed(sorted_gaps)]
    gaps = [round(_extract_val(g) * 100.0, 1) for _, g in reversed(sorted_gaps)]

    # Colors: high gap = crimson red, medium = amber, low = green
    colors = []
    for g in gaps:
        if g > 60.0:
            colors.append("#EF4444")
        elif g > 30.0:
            colors.append("#F59E0B")
        else:
            colors.append("#10B981")

    fig = go.Figure(
        go.Bar(
            x=gaps,
            y=skills,
            orientation="h",
            marker=dict(color=colors),
            text=[f"{g:.1f}% Deficit" for g in gaps],
            textposition="outside",
            textfont=dict(size=11, color="#334155"),
        )
    )

    fig.update_layout(
        title={"text": "Target Enterprise Skill Deficits", "font": {"size": 15, "color": "#1E293B"}},
        xaxis=dict(title="Skill Gap Severity (%)", range=[0, 115], gridcolor="#F1F5F9"),
        yaxis=dict(gridcolor="rgba(0,0,0,0)"),
        height=320,
        margin=dict(l=20, r=30, t=44, b=24),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


def create_prs_history_chart(
    prs_records: List[Dict[str, Any]],
) -> go.Figure:
    """Create longitudinal line chart tracking historical PRS over time.

    Args:
        prs_records: List of dictionaries from prs_history table sorted by computed_at ASC.

    Returns:
        go.Figure: Configured Plotly Scatter line chart.
    """
    if not prs_records:
        fig = go.Figure()
        fig.update_layout(
            title="No Historical Readiness Records Yet",
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            height=300,
        )
        return fig

    dates = [r.get("computed_at", f"Session {i+1}") for i, r in enumerate(prs_records)]
    prs_vals = [float(r.get("prs_score", r.get("prs_value", 0.0))) for r in prs_records]
    ci_lowers = [float(r.get("ci_lower", 0.0)) * (100.0 if float(r.get("ci_lower", 0.0)) <= 1.0 else 1.0) for r in prs_records]
    ci_uppers = [float(r.get("ci_upper", 0.0)) * (100.0 if float(r.get("ci_upper", 0.0)) <= 1.0 else 1.0) for r in prs_records]

    fig = go.Figure()

    # Add Upper Confidence Band
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=ci_uppers,
            mode="lines",
            line=dict(width=0),
            showlegend=False,
            hoverinfo="skip",
        )
    )

    # Add Lower Confidence Band with fill
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=ci_lowers,
            mode="lines",
            line=dict(width=0),
            fill="tonexty",
            fillcolor="rgba(37, 99, 235, 0.12)",
            name="95% Confidence Interval",
        )
    )

    # Main PRS Trajectory line
    fig.add_trace(
        go.Scatter(
            x=dates,
            y=prs_vals,
            mode="lines+markers",
            name="Composite PRS",
            line=dict(color="#2563EB", width=3),
            marker=dict(size=8, color="#1D4ED8"),
            text=[f"PRS: {v:.1f}" for v in prs_vals],
            hovertemplate="%{x}<br><b>PRS: %{y:.1f}</b><extra></extra>",
        )
    )

    # Target readiness threshold reference line
    fig.add_hline(
        y=80.0,
        line_dash="dot",
        line_color="#16A34A",
        annotation_text="Tier-1 Placement Bar (80.0)",
        annotation_position="bottom right",
    )

    fig.update_layout(
        title={"text": "Longitudinal Placement Readiness Trajectory", "font": {"size": 16, "color": "#1E293B"}},
        xaxis=dict(title="Assessment & Telemetry Milestones", gridcolor="#F1F5F9"),
        yaxis=dict(title="Readiness Score (0-100)", range=[0, 105], gridcolor="#F1F5F9"),
        hovermode="x unified",
        height=340,
        margin=dict(l=24, r=24, t=44, b=24),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    )
    return fig


def create_cohort_distribution_chart(
    cohort_records: List[Dict[str, Any]],
) -> go.Figure:
    """Create cohort score distribution histogram for faculty/admin portal.

    Args:
        cohort_records: List of dictionaries with student PRS scores.

    Returns:
        go.Figure: Configured Plotly Histogram figure.
    """
    if not cohort_records:
        return go.Figure()

    prs_scores = [
        float(r["prs_score"])
        for r in cohort_records
        if r.get("prs_score") is not None
    ]

    if not prs_scores:
        prs_scores = [55.0, 68.0, 72.0, 84.0, 42.0, 61.0, 88.0, 77.0, 39.0, 91.0]

    fig = go.Figure(
        go.Histogram(
            x=prs_scores,
            xbins=dict(start=0, end=100, size=10),
            marker=dict(
                color="#3B82F6",
                line=dict(color="#1D4ED8", width=1.5),
            ),
            opacity=0.85,
            name="Students",
        )
    )

    # Add vertical mean line
    mean_prs = sum(prs_scores) / len(prs_scores)
    fig.add_vline(
        x=mean_prs,
        line_dash="dash",
        line_color="#DC2626",
        annotation_text=f"Cohort Mean ({mean_prs:.1f})",
        annotation_position="top left",
    )

    fig.update_layout(
        title={"text": "Cohort Placement Readiness Score (PRS) Distribution", "font": {"size": 16, "color": "#1E293B"}},
        xaxis=dict(title="PRS Score Bins (Deciles)", range=[0, 100], tickvals=list(range(0, 101, 10)), gridcolor="#F1F5F9"),
        yaxis=dict(title="Student Headcount", gridcolor="#F1F5F9"),
        height=320,
        margin=dict(l=24, r=24, t=44, b=24),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig


def create_branch_comparison_chart(
    branch_stats: List[Dict[str, Any]],
) -> go.Figure:
    """Create comparative bar chart of average PRS across academic engineering branches.

    Args:
        branch_stats: List of dicts with 'branch' and 'avg_prs'.

    Returns:
        go.Figure: Configured Plotly Bar figure.
    """
    if not branch_stats:
        return go.Figure()

    branches = [b.get("branch", "Unknown") for b in branch_stats]
    averages = [round(float(b.get("avg_prs", 0.0)), 1) for b in branch_stats]

    fig = go.Figure(
        go.Bar(
            x=branches,
            y=averages,
            marker=dict(color="#0284C7", line=dict(color="#0369A1", width=1.2)),
            text=[f"{v:.1f}" for v in averages],
            textposition="auto",
        )
    )

    fig.update_layout(
        title={"text": "Branch-wise Average Placement Readiness", "font": {"size": 15, "color": "#1E293B"}},
        xaxis=dict(title="Academic Branch"),
        yaxis=dict(title="Average PRS (0-100)", range=[0, 100], gridcolor="#F1F5F9"),
        height=320,
        margin=dict(l=24, r=24, t=44, b=24),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    return fig
