from __future__ import annotations

from fractions import Fraction
from itertools import combinations, product

from boundary_model.multichannel_identifiability import residual_equivalence_dimension
from boundary_model.observation_rank import (
    coordinate_anchor_rows,
    exact_matrix_rank,
    log_linear_identification,
    scalar_observation_rank_gain,
)


def det(matrix: tuple[tuple[int, ...], ...]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    if n == 1:
        return matrix[0][0]
    total = 0
    for j, value in enumerate(matrix[0]):
        sub = tuple(
            tuple(row[c] for c in range(n) if c != j)
            for row in matrix[1:]
        )
        total += ((-1) ** j) * value * det(sub)
    return total


def minor_rank_oracle(rows: tuple[tuple[int, ...], ...], columns: int) -> int:
    """Independent small-matrix rank oracle via non-zero minors."""
    if not rows:
        return 0
    max_size = min(len(rows), columns)
    for size in range(max_size, 0, -1):
        for row_ids in combinations(range(len(rows)), size):
            for col_ids in combinations(range(columns), size):
                minor = tuple(
                    tuple(rows[i][j] for j in col_ids)
                    for i in row_ids
                )
                if det(minor) != 0:
                    return size
    return 0


def test_exact_rank_matches_independent_minor_oracle_exhaustively_small():
    for columns in (1, 2, 3):
        pool = [
            row
            for row in product((-1, 0, 1), repeat=columns)
            if any(row)
        ]
        for n_rows in range(1, min(columns, 3) + 1):
            for rows in product(pool, repeat=n_rows):
                expected = minor_rank_oracle(rows, columns)
                assert exact_matrix_rank(rows, columns=columns) == expected


def test_coordinate_anchor_formula_is_a_corollary_of_rank_theorem():
    for channels in range(2, 8):
        indices = tuple(range(channels))
        for r in range(channels):
            for anchored in combinations(indices, r):
                rows = coordinate_anchor_rows(
                    channels=channels, anchored_indices=anchored
                )
                general = log_linear_identification(
                    channels=channels, extra_observation_rows=rows
                )
                special = residual_equivalence_dimension(
                    channels=channels, independent_anchors=r
                )
                assert general.observation_rank == r + 1
                assert general.residual_dimension == channels - 1 - r
                assert general.residual_dimension == special.residual_dimension
                assert general.point_identified == (r == channels - 1)


def test_candidate_reduces_dimension_iff_it_adds_row_rank():
    channels = 3
    existing = ((1, 0, 0),)

    # Net row (1,1,1) is implicit. These candidates lie in its span with the anchor.
    assert scalar_observation_rank_gain(
        channels=channels,
        existing_extra_rows=existing,
        candidate_row=(1, 0, 0),
    ) == 0
    assert scalar_observation_rank_gain(
        channels=channels,
        existing_extra_rows=existing,
        candidate_row=(2, 1, 1),
    ) == 0
    assert scalar_observation_rank_gain(
        channels=channels,
        existing_extra_rows=existing,
        candidate_row=(3, 0, 0),
    ) == 0

    # This candidate lies outside the current span and closes the final dimension.
    assert scalar_observation_rank_gain(
        channels=channels,
        existing_extra_rows=existing,
        candidate_row=(0, 1, 0),
    ) == 1
    after = log_linear_identification(
        channels=channels,
        extra_observation_rows=(*existing, (0, 1, 0)),
    )
    assert after.residual_dimension == 0
    assert after.point_identified


def test_duplicate_and_rescaled_measurements_do_not_buy_structural_identification():
    base = ((1, 0, 0, 0), (0, 1, 0, 0))
    original = log_linear_identification(channels=4, extra_observation_rows=base)
    assert original.residual_dimension == 1

    for candidate in (
        (1, 0, 0, 0),
        (2, 0, 0, 0),
        (1, 1, 1, 1),  # duplicate of the implicit net-product direction
        (2, 1, 1, 1),  # net + first anchor
        (1, -1, 0, 0),  # first anchor - second anchor
    ):
        assert scalar_observation_rank_gain(
            channels=4,
            existing_extra_rows=base,
            candidate_row=candidate,
        ) == 0

    assert scalar_observation_rank_gain(
        channels=4,
        existing_extra_rows=base,
        candidate_row=(0, 0, 1, 0),
    ) == 1


def test_point_identification_is_exactly_full_rank_on_exhaustive_row_subsets():
    for channels in (2, 3, 4):
        candidate_pool = [
            tuple(1 if j == i else 0 for j in range(channels))
            for i in range(channels)
        ]
        candidate_pool += [
            tuple(1 if j in pair else 0 for j in range(channels))
            for pair in combinations(range(channels), 2)
        ]
        for r in range(len(candidate_pool) + 1):
            # Keep the exhaustive family bounded for the 4-channel case.
            if channels == 4 and r > 4:
                break
            for chosen in combinations(candidate_pool, r):
                result = log_linear_identification(
                    channels=channels, extra_observation_rows=chosen
                )
                augmented = ((1,) * channels, *chosen)
                oracle_rank = minor_rank_oracle(augmented, channels)
                assert result.observation_rank == oracle_rank
                assert result.residual_dimension == channels - oracle_rank
                assert result.point_identified == (oracle_rank == channels)


def test_fraction_rows_are_handled_exactly():
    rows = (
        (Fraction(1, 2), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(1, 3), Fraction(0)),
    )
    result = log_linear_identification(channels=3, extra_observation_rows=rows)
    assert result.observation_rank == 3
    assert result.point_identified
