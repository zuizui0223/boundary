"""Synthetic Boundary diagnostics projected to the shared limitation taxonomy.

Run from repository root:
    python -m examples.limitation_taxonomy_adapter_report
"""
from __future__ import annotations

from dataclasses import asdict
import json

from boundary_model.limitation_taxonomy_adapter import (
    combine_boundary_taxonomy_projections,
    project_rank_identification,
    project_scalar_rank_gain,
    project_target_factorization,
)
from boundary_model.observation_rank import (
    log_linear_identification,
    scalar_observation_rank_gain,
)
from boundary_model.target_factorization import audit_target_factorization


def build_report() -> dict:
    conflict_worlds = (
        {"O": "same", "T": "pollination"},
        {"O": "same", "T": "abiotic"},
    )
    conflict = project_target_factorization(
        audit_target_factorization(
            conflict_worlds,
            lambda row: row["O"],
            lambda row: row["T"],
        )
    )

    question_resolved_worlds = (
        {"O": "same", "T": "pollination", "micro": 0},
        {"O": "same", "T": "pollination", "micro": 1},
    )
    question_resolved = project_target_factorization(
        audit_target_factorization(
            question_resolved_worlds,
            lambda row: row["O"],
            lambda row: row["T"],
        )
    )

    rank_state = project_rank_identification(log_linear_identification(channels=3))
    redundant = project_scalar_rank_gain(
        scalar_observation_rank_gain(channels=3, candidate_row=(1, 1, 1))
    )
    novel = project_scalar_rank_gain(
        scalar_observation_rank_gain(channels=3, candidate_row=(1, 0, 0))
    )
    combined = combine_boundary_taxonomy_projections(rank_state, novel)

    return {
        "data_kind": "synthetic_boundary_shared_taxonomy_projection",
        "scope": (
            "exact finite Boundary diagnostics projected to the shared taxonomy; "
            "not world-set exhaustiveness, causal identification or MROD information value"
        ),
        "target_conflict": asdict(conflict),
        "target_resolved_full_world_ambiguous": asdict(question_resolved),
        "log_linear_unresolved": asdict(rank_state),
        "redundant_candidate": asdict(redundant),
        "structurally_new_candidate": asdict(novel),
        "composed_boundary_state": asdict(combined),
    }


if __name__ == "__main__":
    print(json.dumps(build_report(), indent=2, allow_nan=False))
