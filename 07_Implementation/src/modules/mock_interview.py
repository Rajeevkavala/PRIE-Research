"""
ScholarCamp - Placement Readiness Intelligence Engine (PRIE)
Module: Mock Interview Voice & Prosody Engine
File: modules/mock_interview.py

Implements an ethical, audio-first interview evaluation system combining:
1. Automatic Speech Recognition (ASR) with OpenAI Whisper.
2. Acoustic Prosody & Paralinguistic Signal Extraction via Librosa.
3. Verbal Fluency, Hesitation Ratio, and Filler Word Detection.
4. Technical Concept Keyword Coverage and Multi-Metric Interview Scoring.
"""

from __future__ import annotations

import json
import logging
import re
import warnings
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union

import librosa
import numpy as np
import soundfile as sf
import whisper

import config

logger = logging.getLogger("PRIE.MockInterview")

# Standard list of verbal fillers / crutches
DEFAULT_FILLER_WORDS: List[str] = [
    "um",
    "uh",
    "like",
    "you know",
    "basically",
    "actually",
    "sort of",
    "kind of",
    "i mean",
    "right",
    "you see",
]


class MockInterviewEvaluator:
    """
    Evaluates candidate spoken interview responses using OpenAI Whisper for ASR
    transcription and Librosa for paralinguistic acoustic prosody extraction.
    """

    # Class-level model cache to avoid reloading large binaries into memory
    _cached_models: Dict[str, whisper.Whisper] = {}

    def __init__(
        self,
        model_size: Optional[str] = None,
        filler_words: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize the MockInterviewEvaluator.

        Args:
            model_size: Whisper model size ("tiny", "base", "small"). Defaults to config.WHISPER_MODEL_SIZE.
            filler_words: Custom list of filler words or phrases to detect.
        """
        self.model_size: str = model_size or getattr(config, "WHISPER_MODEL_SIZE", "base")
        self.filler_words: List[str] = [w.lower().strip() for w in (filler_words or DEFAULT_FILLER_WORDS)]
        self._model: Optional[whisper.Whisper] = None

    def get_whisper_model(self) -> whisper.Whisper:
        """
        Retrieves or loads the CPU-optimized Whisper model instance from cache.
        """
        if self.model_size not in MockInterviewEvaluator._cached_models:
            logger.info("Loading OpenAI Whisper '%s' model on CPU...", self.model_size)
            model = whisper.load_model(self.model_size)
            MockInterviewEvaluator._cached_models[self.model_size] = model

        self._model = MockInterviewEvaluator._cached_models[self.model_size]
        return self._model

    def transcribe_audio(self, audio_path: Union[str, Path]) -> str:
        """
        Transcribes candidate speech into plain text using OpenAI Whisper.

        Args:
            audio_path: File system path to the audio recording (WAV, MP3, etc.)

        Returns:
            Clean, stripped transcript text.

        Raises:
            FileNotFoundError: If the specified audio file does not exist.
            ValueError: If the audio file is empty or corrupted.
        """
        path = Path(audio_path)
        if not path.exists():
            raise FileNotFoundError(f"Audio file not found: {path}")

        if path.stat().st_size == 0:
            raise ValueError(f"Audio file is empty (0 bytes): {path}")

        model = self.get_whisper_model()
        logger.debug("Executing Whisper transcription on %s", path)

        try:
            # Enforce fp16=False for standard CPU execution compatibility
            result = model.transcribe(str(path), fp16=False)
            transcript = str(result.get("text", "")).strip()
            return transcript
        except Exception as e:
            logger.error("Whisper transcription failed for %s: %s", path, e)
            raise ValueError(f"Failed to transcribe audio: {e}") from e

    def analyze_prosody(self, audio_path: Union[str, Path]) -> Dict[str, Any]:
        """
        Extracts paralinguistic acoustic features via Librosa signal processing:
        - Speaking Cadence / Tempo (BPM)
        - Fundamental Pitch Variability (std dev of f0 in Hz)
        - Vocal Projection Energy (RMS)
        - Silence Duration and Hesitation Ratio (top_db=25 threshold)

        Args:
            audio_path: File system path to the audio file.

        Returns:
            Dictionary containing extracted prosodic metrics.
        """
        path = Path(audio_path)
        if not path.exists():
            raise FileNotFoundError(f"Audio file not found: {path}")

        if path.stat().st_size == 0:
            raise ValueError(f"Audio file is empty: {path}")

        # Load audio at 16,000 Hz sample rate (standardized speech benchmark)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            y, sr = librosa.load(str(path), sr=16000)

        total_samples = len(y)
        total_duration = float(total_samples / sr) if sr > 0 else 0.0

        if total_duration < 0.2:
            return {
                "tempo_bpm": 0.0,
                "pitch_variability": 0.0,
                "vocal_energy": 0.0,
                "hesitation_ratio": 1.0,
                "duration_seconds": round(total_duration, 2),
                "spoken_duration_seconds": 0.0,
                "is_valid": False,
                "warning": "Audio recording too short (< 0.2s).",
            }

        # 1. Speaking Cadence / Tempo (BPM)
        try:
            onset_env = librosa.onset.onset_strength(y=y, sr=sr)
            try:
                import librosa.feature.rhythm as rhythm
                tempo_arr = rhythm.tempo(onset_envelope=onset_env, sr=sr)
            except (ImportError, AttributeError):
                tempo_arr = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

            tempo = float(np.atleast_1d(tempo_arr)[0])
        except Exception as e:
            logger.warning("Tempo extraction fallback due to error: %s", e)
            tempo = 120.0

        # 2. Fundamental Pitch Variability (σ_f0 in Hz) via piptrack
        try:
            pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
            # Filter non-silent voiced frames above 75th percentile of magnitude
            mag_thresh = float(np.percentile(magnitudes, 75))
            voiced_pitches = pitches[magnitudes > mag_thresh]
            # Exclude extreme unvoiced frequencies (human speech fundamental typically 50 - 500 Hz)
            valid_pitches = voiced_pitches[(voiced_pitches >= 50.0) & (voiced_pitches <= 500.0)]
            pitch_std = float(np.std(valid_pitches)) if len(valid_pitches) > 10 else 0.0
        except Exception as e:
            logger.warning("Pitch extraction fallback due to error: %s", e)
            pitch_std = 0.0

        # 3. Vocal Projection Energy (RMS)
        try:
            rms = librosa.feature.rms(y=y)
            mean_rms = float(np.mean(rms)) if len(rms) > 0 else 0.0
        except Exception as e:
            logger.warning("RMS extraction fallback due to error: %s", e)
            mean_rms = 0.0

        # 4. Silence Interval Detection & Hesitation Ratio (top_db=25)
        try:
            non_silent_intervals = librosa.effects.split(y, top_db=25)
            if len(non_silent_intervals) > 0:
                spoken_samples = sum(int(end - start) for start, end in non_silent_intervals)
                spoken_duration = float(spoken_samples / sr)
            else:
                spoken_duration = 0.0

            hesitation_ratio = max(
                0.0,
                min(1.0, (total_duration - spoken_duration) / total_duration),
            )
        except Exception as e:
            logger.warning("Silence detection fallback due to error: %s", e)
            spoken_duration = total_duration * 0.8
            hesitation_ratio = 0.20

        return {
            "tempo_bpm": round(float(tempo), 1),
            "pitch_variability": round(float(pitch_std), 2),
            "vocal_energy": round(float(mean_rms), 4),
            "hesitation_ratio": round(float(hesitation_ratio), 3),
            "duration_seconds": round(float(total_duration), 2),
            "spoken_duration_seconds": round(float(spoken_duration), 2),
            "is_valid": True,
        }

    def detect_filler_words(self, transcript: str) -> Dict[str, Any]:
        """
        Identifies filler words and computes overall filler density.

        Args:
            transcript: Transcribed speech text.

        Returns:
            Dictionary with total_fillers, filler_density, and itemized breakdown.
        """
        if not transcript or not transcript.strip():
            return {
                "total_fillers": 0,
                "filler_density": 0.0,
                "breakdown": {},
                "word_count": 0,
            }

        text_lower = transcript.lower()
        filler_breakdown: Dict[str, int] = {}
        total_fillers = 0

        for filler in self.filler_words:
            # Word-boundary matching to prevent false substring matches (e.g. 'um' in 'number')
            pattern = r"\b" + re.escape(filler) + r"\b"
            matches = len(re.findall(pattern, text_lower))
            if matches > 0:
                filler_breakdown[filler] = matches
                total_fillers += matches

        words = re.findall(r"\b\w+\b", text_lower)
        word_count = len(words)
        filler_density = (total_fillers / float(word_count)) if word_count > 0 else 0.0

        return {
            "total_fillers": total_fillers,
            "filler_density": round(float(filler_density), 3),
            "breakdown": filler_breakdown,
            "word_count": word_count,
        }

    def evaluate_keyword_coverage(
        self,
        transcript: str,
        expected_keywords: List[str],
    ) -> Dict[str, Any]:
        """
        Matches spoken response against expected technical concepts.

        Args:
            transcript: Transcribed candidate response.
            expected_keywords: List of target technical keywords/phrases.

        Returns:
            Dictionary with coverage score (0-100), matched list, and missing list.
        """
        if not expected_keywords:
            return {
                "coverage_score": 85.0,
                "matched_keywords": [],
                "missing_keywords": [],
                "total_expected": 0,
            }

        text_lower = transcript.lower()
        matched: List[str] = []
        missing: List[str] = []

        for kw in expected_keywords:
            kw_clean = kw.strip().lower()
            # Match exact or with common grammatical suffixes (s, es, ed, ing)
            pattern = r"\b" + re.escape(kw_clean) + r"(?:s|es|ed|ing)?\b"
            is_matched = bool(re.search(pattern, text_lower))

            # If not matched and keyword is plural, test singular root
            if not is_matched and kw_clean.endswith("s") and len(kw_clean) > 3:
                root = kw_clean[:-1]
                pattern_root = r"\b" + re.escape(root) + r"(?:s|es|ed|ing)?\b"
                is_matched = bool(re.search(pattern_root, text_lower))

            # Support hyphen and space interchangeability (e.g. hash map vs hash-map)
            if not is_matched and (" " in kw_clean or "-" in kw_clean):
                flexible_kw = re.escape(kw_clean).replace(r"\ ", r"[\s\-]+").replace(r"\-", r"[\s\-]+")
                flexible_pattern = r"\b" + flexible_kw + r"(?:s|es|ed|ing)?\b"
                is_matched = bool(re.search(flexible_pattern, text_lower))

            if is_matched:
                matched.append(kw)
            else:
                missing.append(kw)

        coverage_ratio = len(matched) / float(len(expected_keywords))
        coverage_score = round(coverage_ratio * 100.0, 1)

        return {
            "coverage_score": coverage_score,
            "matched_keywords": matched,
            "missing_keywords": missing,
            "total_expected": len(expected_keywords),
        }

    def compute_vocal_delivery_score(
        self,
        prosody: Dict[str, Any],
        fillers: Dict[str, Any],
    ) -> float:
        """
        Calculates Vocal Delivery Score on a [20.0, 100.0] scale.

        Deductions:
        - Cadence: -15 if tempo < 100 or tempo > 165 BPM.
        - Hesitation: -20 if hesitation ratio > 0.20 (20%).
        - Filler Density: -15 if filler density > 0.05 (5%).
        - Monotone: -10 if pitch variability < 15.0 Hz.
        """
        if not prosody.get("is_valid", True):
            return 30.0

        score = 100.0
        tempo = prosody.get("tempo_bpm", 120.0)
        hesitation = prosody.get("hesitation_ratio", 0.15)
        filler_density = fillers.get("filler_density", 0.0)
        pitch_std = prosody.get("pitch_variability", 25.0)

        # Tempo penalty (ideal conversational cadence: 100 - 165 BPM)
        min_tempo = getattr(config, "TEMPO_MIN_OPTIMAL", 100.0)
        max_tempo = getattr(config, "TEMPO_MAX_OPTIMAL", 165.0)
        if tempo < min_tempo or tempo > max_tempo:
            score -= 15.0

        # Hesitation penalty (ideal: <= 20% silence)
        max_hesitation = getattr(config, "HESITATION_MAX_OPTIMAL", 0.20)
        if hesitation > max_hesitation:
            score -= 20.0

        # Filler density penalty (ideal: <= 5%)
        max_filler = getattr(config, "FILLER_DENSITY_MAX_OPTIMAL", 0.05)
        if filler_density > max_filler:
            score -= 15.0

        # Monotone inflection penalty
        min_pitch = getattr(config, "PITCH_VARIABILITY_MIN_OPTIMAL", 15.0)
        if pitch_std < min_pitch:
            score -= 10.0

        # Clamp between 20.0 and 100.0
        return float(max(20.0, min(100.0, round(score, 1))))

    def generate_feedback_insights(
        self,
        prosody: Dict[str, Any],
        fillers: Dict[str, Any],
        keyword_eval: Dict[str, Any],
    ) -> List[str]:
        """
        Produces actionable pedagogical feedback points from acoustic & content diagnostics.
        """
        insights: List[str] = []

        # Content feedback
        coverage = keyword_eval.get("coverage_score", 0.0)
        missing = keyword_eval.get("missing_keywords", [])
        if coverage >= 80.0:
            insights.append("🎯 **Strong Technical Depth:** You articulated the foundational concepts and keywords thoroughly.")
        elif missing:
            sample_missing = ", ".join(f"`{k}`" for k in missing[:3])
            insights.append(f"⚠️ **Technical Gap:** Consider expanding on key technical concepts such as {sample_missing}.")

        # Cadence feedback
        tempo = prosody.get("tempo_bpm", 120.0)
        if tempo < 100.0:
            insights.append("⏱️ **Pacing:** Your speaking cadence was somewhat slow (< 100 BPM). Practice answering more fluidly.")
        elif tempo > 165.0:
            insights.append("⏱️ **Pacing:** Your speaking cadence was hurried (> 165 BPM). Slow down slightly to project calm authority.")
        else:
            insights.append("✅ **Cadence:** Your speaking pace was within the ideal professional interview range (100–165 BPM).")

        # Hesitation feedback
        hesitation = prosody.get("hesitation_ratio", 0.0)
        if hesitation > 0.25:
            insights.append(f"⏸️ **Pauses & Hesitation:** {int(hesitation * 100)}% of the response was silent intervals. Aim to structure your thoughts before speaking.")
        else:
            insights.append("✅ **Flow:** Natural continuity with low hesitation ratio.")

        # Filler words feedback
        total_fillers = fillers.get("total_fillers", 0)
        density = fillers.get("filler_density", 0.0)
        if density > 0.05:
            top_fillers = ", ".join(f"'{k}' ({v})" for k, v in fillers.get("breakdown", {}).items())
            insights.append(f"🗣️ **Verbal Crutches:** Detected {total_fillers} filler words ({top_fillers}). Replace filler sounds with brief, confident silence.")
        else:
            insights.append("✅ **Fluency:** Crisp verbal delivery with negligible filler word usage.")

        # Pitch variation
        pitch_std = prosody.get("pitch_variability", 25.0)
        if pitch_std < 15.0:
            insights.append("🎵 **Vocal Variety:** Your delivery was somewhat monotone. Inject vocal inflection to highlight key points.")

        return insights

    def evaluate_response(
        self,
        audio_path: Union[str, Path],
        expected_keywords: List[str],
    ) -> Dict[str, Any]:
        """
        Executes end-to-end mock interview evaluation:
        1. Whisper ASR Transcription.
        2. Librosa Prosody Analysis.
        3. Filler Word & Fluency Detection.
        4. Technical Concept Coverage Evaluation.
        5. Composite Scoring: 0.60 * Content + 0.40 * Delivery.

        Args:
            audio_path: Path to recorded speech audio.
            expected_keywords: List of target technical keywords.

        Returns:
            Dictionary containing transcripts, scores, breakdowns, and diagnostic feedback.
        """
        path = Path(audio_path)
        logger.info("Evaluating interview response audio: %s", path)

        # 1. Transcribe audio
        transcript = self.transcribe_audio(path)

        # 2. Analyze acoustic prosody
        prosody = self.analyze_prosody(path)

        # 3. Detect verbal fillers
        fillers = self.detect_filler_words(transcript)

        # 4. Evaluate keyword coverage
        keyword_eval = self.evaluate_keyword_coverage(transcript, expected_keywords)

        # 5. Compute delivery score
        delivery_score = self.compute_vocal_delivery_score(prosody, fillers)

        # 6. Formulate Overall Interview Score: 0.60 * Content + 0.40 * Delivery
        content_score = keyword_eval["coverage_score"]
        overall_score = round((0.60 * content_score) + (0.40 * delivery_score), 1)
        overall_score = max(0.0, min(100.0, overall_score))

        # 7. Generate diagnostic feedback
        feedback = self.generate_feedback_insights(prosody, fillers, keyword_eval)

        return {
            "transcript": transcript,
            "overall_score": overall_score,
            "technical_coverage_score": content_score,
            "vocal_delivery_score": delivery_score,
            "matched_keywords": keyword_eval["matched_keywords"],
            "missing_keywords": keyword_eval["missing_keywords"],
            "total_expected_keywords": keyword_eval["total_expected"],
            "prosody": prosody,
            "fillers": fillers,
            "feedback": feedback,
        }

    @staticmethod
    def load_scenarios() -> List[Dict[str, Any]]:
        """
        Loads curated interview scenarios from disk.
        """
        scenarios_path = getattr(config, "INTERVIEW_SCENARIOS_PATH", None)
        if scenarios_path and Path(scenarios_path).exists():
            with open(scenarios_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    @staticmethod
    def generate_synthetic_audio(
        output_path: Union[str, Path],
        duration_seconds: float = 3.0,
        frequency_hz: float = 220.0,
        sample_rate: int = 16000,
    ) -> Path:
        """
        Generates a synthetic sinusoidal audio WAV file for testing purposes.
        """
        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), endpoint=False)
        # Generate tone with subtle amplitude modulation
        waveform = 0.5 * np.sin(2 * np.pi * frequency_hz * t) * (0.8 + 0.2 * np.sin(2 * np.pi * 2 * t))
        sf.write(str(out_file), waveform.astype(np.float32), sample_rate)
        return out_file
