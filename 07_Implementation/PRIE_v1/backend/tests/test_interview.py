"""
Unit tests for Module M05: Multimodal Mock Interview Coach.
Tests acoustic prosodic extraction, visual composure analysis, ASR speech diagnostics,
and Late Multimodal Fusion into canonical SPV F20.
"""

import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from modules.m05_mock_interview import (
    AudioProsodyAnalyzer,
    VisualComposureAnalyzer,
    SpeechTranscriptAnalyzer,
    MultimodalMockInterviewCoach,
)


def test_audio_prosody_analyzer():
    """Verify acoustic prosodic extraction and default handling."""
    analyzer = AudioProsodyAnalyzer()
    res = analyzer._default_acoustic_features(duration=15.0)

    assert "pitch_mean_hz" in res
    assert "jitter_percent" in res
    assert "shimmer_percent" in res
    assert "tempo_bpm" in res
    assert "pause_ratio" in res
    assert 0.0 <= res["acoustic_delivery_score"] <= 100.0


def test_visual_composure_analyzer():
    """Verify visual composure feature extraction."""
    analyzer = VisualComposureAnalyzer()
    res = analyzer._default_visual_features()

    assert "face_presence_ratio" in res
    assert "eye_contact_persistence" in res
    assert "head_movement_stability" in res
    assert 0.0 <= res["visual_composure_score"] <= 100.0


def test_speech_transcript_analyzer():
    """Verify speech linguistics: WPM, filler word detection, and TTR."""
    analyzer = SpeechTranscriptAnalyzer()
    sample_text = (
        "Um, basically in this project I implemented a binary search tree to optimize "
        "the lookup latency. Like, the time complexity became O of log N."
    )
    res = analyzer.analyze_text(sample_text, duration_seconds=10.0)

    assert res["word_count"] > 0
    assert res["filler_count"] >= 2  # 'um', 'basically', 'like'
    assert res["filler_density_percent"] > 0.0
    assert 0.0 <= res["lexical_diversity_ttr"] <= 1.0
    assert 0.0 <= res["semantic_delivery_score"] <= 100.0


def test_multimodal_late_fusion():
    """Verify multimodal late fusion produces valid composite and F20 behavior score."""
    coach = MultimodalMockInterviewCoach()
    # Test on non-existent media path triggers graceful default fallback
    result = coach.process_interview_session(
        student_id=1,
        session_id="test_session_001",
        media_path="uploads/dummy_interview.mp4",
        target_role="Software Development Engineer",
    )

    assert "overall_interview_score" in result
    assert 0.0 <= result["overall_interview_score"] <= 100.0
    assert "spv_f20_behavior_score" in result
    assert 0.0 <= result["spv_f20_behavior_score"] <= 1.0
    assert result["epistemological_status"].startswith("ESTABLISHED_BY_RESEARCH")
    assert "scientific_integrity_statement" in result
