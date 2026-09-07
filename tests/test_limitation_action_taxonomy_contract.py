"""Cross-program limitation-to-action taxonomy scope and hash guards."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TAXONOMY = ROOT / "docs" / "limitation_action_taxonomy_v1.json"
NOTE = ROOT / "docs" / "limitation_action_taxonomy_2026-09-07.md"
ARCH = ROOT / "docs" / "observation_information_order_architecture_2026-09-06.md"
MANUSCRIPT = ROOT / "paper" / "manuscript.md"
EXPECTED_SHA256 = "d150182345b04a9606b0a1c09caa4ad2328c0f8bf5179a258beae537d0aa3432"


def test_machine_readable_taxonomy_has_frozen_cross_repo_hash_and_axes():
    raw = TAXONOMY.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_SHA256
    data = json.loads(raw)
    assert data["schema"] == "limitation_action_taxonomy"
    assert data["version"] == "1.0"
    assert "do_not_replace_the_vector_with_one_severity_score" in data["composition_rule"]
    assert {axis["id"] for axis in data["axes"]} == {
        "evidence_integrity",
        "observation_structure",
        "current_state_estimability",
        "target_identification",
        "candidate_prediction_coverage",
        "information_horizon",
        "specification_robustness",
        "resource_operational",
    }


def test_future_taxonomy_preserves_distinct_scientific_actions():
    text = NOTE.read_text(encoding="utf-8")
    for marker in (
        "state vector -> one or more licensed scientific actions",
        "target resolved with residual mechanism ambiguity",
        "use a non-myopic bundle / sequence design",
        "require an explicit meta-prior, max-cost or cost-regret rule before scalar ranking",
        "preserve what kind of limitation it is",
    ):
        assert marker in text, marker
    assert "preserve -> audit -> diagnose -> resolve" in text
    assert ARCH.exists()


def test_active_boundary_manuscript_does_not_absorb_future_taxonomy():
    text = MANUSCRIPT.read_text(encoding="utf-8")
    assert "limitation_action_taxonomy_v1" not in text
    assert "resource_operational" not in text
    assert "cost_preference_crosses_scenarios" not in text
