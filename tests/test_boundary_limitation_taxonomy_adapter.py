from pathlib import Path

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


def _states(projection):
    return set(projection.canonical_states)


def _actions(projection):
    return set(projection.canonical_actions)


def test_conflicting_target_on_one_observation_fibre_projects_structural_collapse():
    worlds = (
        {"O": "same", "T": "pollination"},
        {"O": "same", "T": "abiotic"},
    )
    audit = audit_target_factorization(worlds, lambda row: row["O"], lambda row: row["T"])
    projection = project_target_factorization(audit)
    assert ("observation_structure", "current_target_collapsed_on_observation_fibre") in _states(
        projection
    )
    assert ("target_identification", "target_unresolved") in _states(projection)
    assert "proceed_to_identification_or_repair_diagnosis" in _actions(projection)
    assert "proceed_to_candidate_design" in _actions(projection)
    assert any("conflict_pair" in certificate for certificate in projection.certificates)


def test_target_can_be_identified_while_full_world_remains_ambiguous():
    worlds = (
        {"O": "same", "T": "pollination", "micro": 0},
        {"O": "same", "T": "pollination", "micro": 1},
    )
    audit = audit_target_factorization(worlds, lambda row: row["O"], lambda row: row["T"])
    projection = project_target_factorization(audit)
    assert (
        "target_identification",
        "target_identified_full_mechanism_ambiguous",
    ) in _states(projection)
    assert "stop_declared_target_resolved_report_residual_ambiguity" in _actions(projection)
    assert any("retains worlds" in certificate for certificate in projection.certificates)


def test_injective_observation_on_supplied_worlds_projects_full_resolution():
    worlds = (
        {"O": "left", "T": "pollination"},
        {"O": "right", "T": "abiotic"},
    )
    audit = audit_target_factorization(worlds, lambda row: row["O"], lambda row: row["T"])
    projection = project_target_factorization(audit)
    assert ("target_identification", "fully_resolved") in _states(projection)
    assert "stop_fully_resolved" in _actions(projection)


def test_log_linear_rank_projects_full_state_identification_or_residual_collapse():
    unresolved = project_rank_identification(log_linear_identification(channels=3))
    assert ("target_identification", "target_unresolved") in _states(unresolved)
    assert ("observation_structure", "current_target_collapsed_on_observation_fibre") in _states(
        unresolved
    )

    resolved = project_rank_identification(
        log_linear_identification(
            channels=3,
            extra_observation_rows=((1, 0, 0), (0, 1, 0)),
        )
    )
    assert ("target_identification", "fully_resolved") in _states(resolved)


def test_scalar_rank_gain_maps_redundant_and_structurally_new_candidates():
    redundant_gain = scalar_observation_rank_gain(
        channels=3,
        candidate_row=(1, 1, 1),
    )
    redundant = project_scalar_rank_gain(redundant_gain)
    assert redundant_gain == 0
    assert (
        "observation_structure",
        "candidate_determined_by_current_observation",
    ) in _states(redundant)
    assert "drop_as_structurally_zero_value_for_current_contrast" in _actions(redundant)

    new_gain = scalar_observation_rank_gain(
        channels=3,
        candidate_row=(1, 0, 0),
    )
    novel = project_scalar_rank_gain(new_gain)
    assert new_gain == 1
    assert ("observation_structure", "candidate_structurally_new") in _states(novel)
    assert "evaluate_mechanism_target_information_not_structural_novelty_alone" in _actions(novel)


def test_projection_composition_preserves_multiple_boundary_coordinates():
    unresolved = project_rank_identification(log_linear_identification(channels=3))
    novel = project_scalar_rank_gain(1)
    combined = combine_boundary_taxonomy_projections(unresolved, novel)
    assert ("target_identification", "target_unresolved") in _states(combined)
    assert ("observation_structure", "candidate_structurally_new") in _states(combined)
    assert len(combined.certificates) >= 2


def test_adapter_remains_internal_and_off_active_manuscript():
    root = Path(__file__).resolve().parents[1]
    manuscript = (root / "paper" / "manuscript.md").read_text(encoding="utf-8")
    init_path = root / "boundary_model" / "__init__.py"
    if init_path.exists():
        assert "limitation_taxonomy_adapter" not in init_path.read_text(encoding="utf-8")
    assert "limitation_taxonomy_adapter" not in manuscript
