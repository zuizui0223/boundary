"""Standalone theory for ecological identification boundaries."""

from .multichannel_identifiability import (
    ChannelAnchorDimension,
    channel_ratio_dimension,
    log_gauge_basis,
    reconstruct_final_channel,
    residual_equivalence_dimension,
    residual_product,
)
from .observation_rank import (
    RankIdentificationResult,
    coordinate_anchor_rows,
    exact_matrix_rank,
    log_linear_identification,
    scalar_observation_rank_gain,
)
from .calibration_transport_family import (
    AnchorLadderStep,
    SymmetricCalibrationBound,
    SymmetricIdentifiedInterval,
    anchor_ladder,
    breakdown_factor,
    identify_with_observed_kappa,
    observed_kappa,
    symmetric_interval,
)

__all__ = [
    "AnchorLadderStep",
    "ChannelAnchorDimension",
    "RankIdentificationResult",
    "SymmetricCalibrationBound",
    "SymmetricIdentifiedInterval",
    "anchor_ladder",
    "breakdown_factor",
    "channel_ratio_dimension",
    "coordinate_anchor_rows",
    "exact_matrix_rank",
    "identify_with_observed_kappa",
    "log_gauge_basis",
    "log_linear_identification",
    "observed_kappa",
    "reconstruct_final_channel",
    "residual_equivalence_dimension",
    "residual_product",
    "scalar_observation_rank_gain",
    "symmetric_interval",
]
