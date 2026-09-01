from math import exp, isclose
from pathlib import Path

import pytest

from boundary_model.calibration_transport_family import breakdown_factor, symmetric_interval
from boundary_model.multichannel_identifiability import (
    log_gauge_basis,
    reconstruct_final_channel,
    residual_equivalence_dimension,
)

ROOT = Path(__file__).resolve().parents[1]


def test_dimension_rule_exhaustive_for_small_chains():
    for channels in range(2, 10):
        for anchors in range(channels):
            result = residual_equivalence_dimension(
                channels=channels, independent_anchors=anchors
            )
            assert result.residual_dimension == channels - 1 - anchors
            expected = (
                "point_identified"
                if anchors == channels - 1
                else "non_identified"
                if anchors == 0
                else "partially_identified"
            )
            assert result.identification == expected


def test_log_gauge_basis_preserves_product_for_every_basis_direction():
    values = [1.7, 2.3, 3.1, 4.9, 5.3]
    baseline = 1.0
    for value in values:
        baseline *= value

    for direction in log_gauge_basis(len(values)):
        shifted = [
            value * exp(0.37 * delta)
            for value, delta in zip(values, direction, strict=True)
        ]
        product = 1.0
        for value in shifted:
            product *= value
        assert isclose(product, baseline, rel_tol=1e-12)


def test_point_identification_reconstructs_only_after_k_minus_one_anchors():
    channels = [2.0, 3.0, 5.0, 7.0]
    net = 1.0
    for value in channels:
        net *= value
    reconstructed = reconstruct_final_channel(
        net_product=net, anchored_values=channels[:-1], channels=len(channels)
    )
    assert isclose(reconstructed, channels[-1])
    with pytest.raises(ValueError):
        reconstruct_final_channel(
            net_product=net, anchored_values=channels[:-2], channels=len(channels)
        )


def test_dimension_rule_rejects_invalid_anchor_counts():
    with pytest.raises(ValueError):
        residual_equivalence_dimension(channels=4, independent_anchors=-1)
    with pytest.raises(ValueError):
        residual_equivalence_dimension(channels=4, independent_anchors=4)


def test_breakdown_factor_is_reciprocal_reference_invariant_across_values():
    for ratio in (0.2, 0.5, 0.9, 1.0, 1.1, 2.0, 5.0):
        gamma, eta = breakdown_factor(ratio)
        gamma_rev, eta_rev = breakdown_factor(1.0 / ratio)
        assert isclose(gamma, gamma_rev)
        assert isclose(eta, eta_rev)
        interval = symmetric_interval(ratio, gamma=gamma)
        assert interval.lower <= 1.0 <= interval.upper


def test_introduction_keeps_joint_measurement_bottleneck_explicit():
    manuscript = (ROOT / "paper" / "manuscript.md").read_text(encoding="utf-8")
    introduction = manuscript.split("## 1. Introduction", 1)[1].split("## 2.", 1)[0]
    for phrase in (
        "joint-measurement bottleneck",
        "visitor identity",
        "effective service",
        "reproductive dependency",
        "not evaluable",
    ):
        assert phrase in introduction
