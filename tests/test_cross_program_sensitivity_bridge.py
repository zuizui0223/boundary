"""Scope guards for the future Boundary -> MROD sensitivity bridge."""
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCH = ROOT / "docs" / "observation_information_order_architecture_2026-09-06.md"
MANUSCRIPT = ROOT / "paper" / "manuscript.md"


def test_future_architecture_separates_conclusion_and_recommendation_robustness():
    text = ARCH.read_text(encoding="utf-8")
    for marker in (
        "## 6. Sensitivity propagation: identification robustness is not recommendation robustness",
        "identification robustness:",
        "recommendation robustness:",
        "B_common = intersection_{lambda in Lambda} B_lambda",
        "the **next-observation recommendation itself** is assumption-sensitive",
        "conclusion robustness across an assumption family guarantees recommendation robustness",
    ):
        assert marker in text, marker


def test_future_bridge_keeps_boundary_and_mrod_targets_distinct():
    text = ARCH.read_text(encoding="utf-8")
    assert "Boundary:\nassumption family -> identified-set family -> conclusion breakdown" in text
    assert "MROD:\nsame propagated family -> candidate-information family -> recommendation stability" in text
    assert "This is a reporting diagnostic, not a new robust-design objective" in text


def test_active_boundary_manuscript_does_not_absorb_future_mrod_diagnostic():
    text = MANUSCRIPT.read_text(encoding="utf-8")
    assert "B_common" not in text
    assert "recommendation robustness" not in text
