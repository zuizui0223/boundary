from __future__ import annotations

import math

from boundary_model.observation_rank import exact_matrix_rank, log_linear_identification


ENDPOINT = (1, 1, 1)
VISITATION = (1, 0, 0)
NORMALIZED_ENDPOINT = (0, 1, 1)  # ENDPOINT - VISITATION
EFFECTIVENESS = (0, 1, 0)
NULL_DIRECTION = (0, 1, -1)


def dot(row, vector):
    return sum(a * b for a, b in zip(row, vector))


def test_data_rich_panel_has_rank_two_and_one_unidentified_direction():
    rows = (ENDPOINT, VISITATION, NORMALIZED_ENDPOINT)
    assert exact_matrix_rank(rows, columns=3) == 2

    # log_linear_identification inserts ENDPOINT implicitly, so pass the two
    # additional reported directions only.
    result = log_linear_identification(
        channels=3,
        extra_observation_rows=(VISITATION, NORMALIZED_ENDPOINT),
    )
    assert result.observation_rank == 2
    assert result.residual_dimension == 1
    assert not result.point_identified

    assert all(dot(row, NULL_DIRECTION) == 0 for row in rows)


def test_more_rows_inside_old_span_do_not_change_identification():
    # Duplicate visitation, a rescaled visitation metric, and an exact derived
    # endpoint+visitation combination remain in the same two-dimensional span.
    rows = (
        ENDPOINT,
        VISITATION,
        NORMALIZED_ENDPOINT,
        VISITATION,
        (2, 0, 0),
        (2, 1, 1),  # ENDPOINT + VISITATION
    )
    assert exact_matrix_rank(rows, columns=3) == 2


def test_direct_effectiveness_anchor_closes_the_last_dimension():
    rows = (ENDPOINT, VISITATION, NORMALIZED_ENDPOINT, EFFECTIVENESS)
    assert exact_matrix_rank(rows, columns=3) == 3

    result = log_linear_identification(
        channels=3,
        extra_observation_rows=(VISITATION, NORMALIZED_ENDPOINT, EFFECTIVENESS),
    )
    assert result.observation_rank == 3
    assert result.residual_dimension == 0
    assert result.point_identified


def test_two_numerical_mechanisms_are_observationally_equal_before_anchor():
    world_a = {"V": 10.0, "E": 0.4, "D": 0.5}
    world_b = {"V": 10.0, "E": 0.2, "D": 1.0}

    def record(world):
        W = world["V"] * world["E"] * world["D"]
        return {
            "V": world["V"],
            "W": W,
            "W_over_V": W / world["V"],
        }

    rec_a = record(world_a)
    rec_b = record(world_b)
    assert rec_a == rec_b == {"V": 10.0, "W": 2.0, "W_over_V": 0.2}

    # The targeted effectiveness measurement distinguishes the mechanisms.
    assert world_a["E"] != world_b["E"]

    # Once E is anchored, downstream dependency is uniquely recovered.
    for world in (world_a, world_b):
        W = world["V"] * world["E"] * world["D"]
        reconstructed_D = W / (world["V"] * world["E"])
        assert math.isclose(reconstructed_D, world["D"], rel_tol=0.0, abs_tol=1e-12)
