"""Identification geometry for positive multiplicative ecological chains."""
from __future__ import annotations

from dataclasses import dataclass
from math import prod
from typing import Iterable, Literal, Sequence

IdentificationState = Literal["non_identified", "partially_identified", "point_identified"]

@dataclass(frozen=True)
class ChannelAnchorDimension:
    channels: int
    independent_anchors: int
    residual_dimension: int
    identification: IdentificationState

def _validate_channels(channels: int) -> int:
    k = int(channels)
    if k < 2:
        raise ValueError("channels must be at least 2")
    return k

def residual_equivalence_dimension(*, channels: int, independent_anchors: int = 0) -> ChannelAnchorDimension:
    k = _validate_channels(channels)
    r = int(independent_anchors)
    if r < 0 or r > k - 1:
        raise ValueError("independent_anchors must satisfy 0 <= r <= channels-1")
    dimension = k - 1 - r
    identification: IdentificationState
    if dimension == 0:
        identification = "point_identified"
    elif r == 0:
        identification = "non_identified"
    else:
        identification = "partially_identified"
    return ChannelAnchorDimension(k, r, dimension, identification)

def log_gauge_basis(channels: int) -> tuple[tuple[float, ...], ...]:
    k = _validate_channels(channels)
    rows = []
    for j in range(k - 1):
        row = [0.0] * k
        row[j] = 1.0
        row[-1] = -1.0
        rows.append(tuple(row))
    return tuple(rows)

def residual_product(*, net_product: float, anchored_values: Iterable[float]) -> float:
    total = float(net_product)
    if total <= 0:
        raise ValueError("net_product must be strictly positive")
    anchors = [float(v) for v in anchored_values]
    if any(v <= 0 for v in anchors):
        raise ValueError("anchored_values must be strictly positive")
    return total / (prod(anchors) if anchors else 1.0)

def reconstruct_final_channel(*, net_product: float, anchored_values: Sequence[float], channels: int) -> float:
    k = _validate_channels(channels)
    if len(anchored_values) != k - 1:
        raise ValueError("exactly channels-1 anchored values are required")
    return residual_product(net_product=net_product, anchored_values=anchored_values)

def channel_ratio_dimension(*, channels: int, observed_channel_ratios: int = 0) -> ChannelAnchorDimension:
    return residual_equivalence_dimension(channels=channels, independent_anchors=observed_channel_ratios)
