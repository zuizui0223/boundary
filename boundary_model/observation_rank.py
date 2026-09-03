"""Exact rank criteria for log-linear identification in multiplicative chains.

For positive channels F_j, write x_j = log F_j.  Exact observations that are
linear in x constrain x to an affine space.  The structural unidentified
dimension is therefore the nullity of the observation matrix, not a function
of measurement precision alone.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence

Number = int | float | Fraction


@dataclass(frozen=True)
class RankIdentificationResult:
    channels: int
    observation_rank: int
    residual_dimension: int
    point_identified: bool


def _fraction(value: Number) -> Fraction:
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int):
        return Fraction(value)
    return Fraction(str(float(value)))


def _rows(rows: Iterable[Sequence[Number]], channels: int) -> list[list[Fraction]]:
    out: list[list[Fraction]] = []
    for row in rows:
        converted = [_fraction(v) for v in row]
        if len(converted) != channels:
            raise ValueError("every observation row must have length=channels")
        if all(v == 0 for v in converted):
            raise ValueError("zero observation rows carry no declared measurement")
        out.append(converted)
    return out


def exact_matrix_rank(rows: Iterable[Sequence[Number]], *, columns: int) -> int:
    """Return exact row rank by Fraction-valued Gaussian elimination."""
    if columns < 1:
        raise ValueError("columns must be positive")
    a = _rows(rows, columns)
    if not a:
        return 0

    rank = 0
    col = 0
    while rank < len(a) and col < columns:
        pivot = next((i for i in range(rank, len(a)) if a[i][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pivot_value = a[rank][col]
        a[rank] = [v / pivot_value for v in a[rank]]
        for i in range(len(a)):
            if i == rank or a[i][col] == 0:
                continue
            factor = a[i][col]
            a[i] = [u - factor * v for u, v in zip(a[i], a[rank])]
        rank += 1
        col += 1
    return rank


def log_linear_identification(
    *,
    channels: int,
    extra_observation_rows: Iterable[Sequence[Number]] = (),
) -> RankIdentificationResult:
    """Audit exact identification from net product plus extra log-linear rows.

    The net product contributes the row (1,...,1).  If M is the augmented
    observation matrix, the compatible log-channel set has dimension
    channels-rank(M), and all channels are point identified iff rank(M)=channels.
    """
    k = int(channels)
    if k < 2:
        raise ValueError("channels must be at least 2")
    extras = list(extra_observation_rows)
    rows: list[Sequence[Number]] = [[1] * k, *extras]
    rank = exact_matrix_rank(rows, columns=k)
    residual = k - rank
    return RankIdentificationResult(k, rank, residual, residual == 0)


def scalar_observation_rank_gain(
    *,
    channels: int,
    existing_extra_rows: Iterable[Sequence[Number]] = (),
    candidate_row: Sequence[Number],
) -> int:
    """Return 1 iff a scalar candidate adds a new identification direction.

    For one scalar row, rank can rise by at most one.  A gain of zero is exactly
    the condition that the candidate lies in the row span of the existing net
    and extra observations.
    """
    existing = list(existing_extra_rows)
    before = log_linear_identification(
        channels=channels, extra_observation_rows=existing
    ).observation_rank
    after = log_linear_identification(
        channels=channels,
        extra_observation_rows=[*existing, candidate_row],
    ).observation_rank
    gain = after - before
    if gain not in (0, 1):
        raise AssertionError("a scalar observation changed rank by more than one")
    return gain


def coordinate_anchor_rows(*, channels: int, anchored_indices: Iterable[int]) -> tuple[tuple[int, ...], ...]:
    """Return coordinate-measurement rows for distinct anchored channels."""
    k = int(channels)
    if k < 2:
        raise ValueError("channels must be at least 2")
    indices = tuple(int(i) for i in anchored_indices)
    if len(set(indices)) != len(indices):
        raise ValueError("anchored_indices must be distinct")
    if any(i < 0 or i >= k for i in indices):
        raise ValueError("anchor index out of range")
    rows = []
    for i in indices:
        row = [0] * k
        row[i] = 1
        rows.append(tuple(row))
    return tuple(rows)
