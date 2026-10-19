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


def test_same_resolution_flag_does_not_imply_same_identified_target_image():
    # Finite counterexamples independent of MROD scoring or a model-fitting method.
    images = {
        "spec_a": {"pollination_only", "combined"},
        "spec_b": {"abiotic_only", "combined"},
    }
    assert {len(image) == 1 for image in images.values()} == {False}
    assert images["spec_a"] != images["spec_b"]

    point_images = {
        "spec_a": {"pollination_only"},
        "spec_b": {"abiotic_only"},
    }
    assert {len(image) == 1 for image in point_images.values()} == {True}
    assert point_images["spec_a"] != point_images["spec_b"]


def test_future_bridge_requires_identified_image_or_declared_contrast_evidence():
    text = ARCH.read_text(encoding="utf-8")
    for marker in (
        "Resolution-status invariance is not conclusion robustness",
        "I_lambda(y) = {tau(s) : (theta,s) in A_lambda(y)}",
        "r_lambda(y) = 1 if |I_lambda(y)|=1, otherwise 0",
        "compare the actual",
        "predeclared contrast functional",
        "resolved/unresolved",
    ):
        assert marker in text, marker

    # The future cross-paper clarification is not part of the active Perspective.
    manuscript = MANUSCRIPT.read_text(encoding="utf-8")
    assert "I_lambda(y)" not in manuscript
    assert "Resolution-status invariance" not in manuscript
