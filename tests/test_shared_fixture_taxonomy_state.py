"""Cross-repository target-state semantics on the existing shared fixture."""
from __future__ import annotations

import json
from pathlib import Path

from boundary_model.limitation_taxonomy_adapter import project_target_factorization
from boundary_model.target_factorization import audit_target_factorization


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "target_factorization_v1.json"


def _rows(case):
    columns = tuple(case["columns"])
    return tuple(dict(zip(columns, values)) for values in case["rows"])


def test_shared_factorization_fixture_maps_to_same_target_taxonomy_semantics():
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    assert data["contract_id"] == "boundary-mrod-target-factorization-v1"

    for case in data["cases"]:
        rows = _rows(case)
        audit = audit_target_factorization(rows, lambda row: row["O"], lambda row: row["T"])
        assert audit.factors_through_observation is bool(case["expected"]["factors"])
        projection = project_target_factorization(audit)
        target_states = {
            state
            for axis, state in projection.canonical_states
            if axis == "target_identification"
        }
        expected_state = (
            "target_identified_full_mechanism_ambiguous"
            if case["expected"]["factors"]
            else "target_unresolved"
        )
        assert target_states == {expected_state}, case["name"]
