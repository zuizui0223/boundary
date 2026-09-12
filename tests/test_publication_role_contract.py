from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "paper" / "BOUNDARY_ROLE_CONTRACT_2026-09-12.json"
ROUTE = ROOT / "paper" / "PUBLICATION_ROUTE_2026-09-11.md"
PROPOSAL = ROOT / "paper" / "ecology_letters_proposal.md"
EMAIL = ROOT / "paper" / "ecology_letters_proposal_email.md"

WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[-'’][A-Za-z0-9]+)*")


def _load() -> dict:
    return json.loads(CONTRACT.read_text(encoding="utf-8"))


def test_boundary_remains_independent_c1_owner() -> None:
    contract = _load()
    assert contract["repository"] == "zuizui0223/boundary"
    assert contract["submission_unit"] == "C1"
    assert contract["status"] == "independent-owner-parked-conditional"
    assert contract["target"] == "Ecology Letters Perspective"
    assert contract["machine_blockers"] == 0
    ownership = " ".join(contract["exclusive_scientific_ownership"])
    assert "k-rank(M)" in ownership
    assert "row span" in ownership
    assert "breakdown factor" in ownership


def test_c2_can_use_only_geometry_exemplar_without_ownership_transfer() -> None:
    contract = _load()
    c2 = contract["c2_interface"]
    assert c2["allowed_role"] == "geometry exemplar only"
    assert "existing observation direction" in c2["allowed_claim"]
    forbidden = " ".join(c2["forbidden_transfer"])
    assert "k-rank(M)" in forbidden
    assert "Gamma/kappa" in forbidden
    assert "anchor-ladder" in forbidden


def test_ced_is_downstream_reportability_not_boundary_owner() -> None:
    contract = _load()
    ced = contract["ced_interface"]
    assert ced["repository"] == "zuizui0223/ced"
    assert ced["ownership_transfer"] is False
    assert "target-safe reportability" in ced["ced_owns"]
    assert "structural identification geometry" in ced["boundary_retains"]
    route = ROUTE.read_text(encoding="utf-8")
    assert "CED is **not** the home of Boundary's identification geometry" in route
    assert "There is no theorem-ownership transfer" in route


def test_ecology_letters_proposal_surface_matches_live_gate() -> None:
    contract = _load()
    rules = contract["live_ecology_letters_rules_checked_2026_09_12"]
    assert rules["proposal_max_words"] == 300
    assert rules["proposal_first_required"] is True
    assert rules["full_manuscript_without_invitation_or_approved_proposal_considered"] is False
    assert set(rules["proposal_email_recipients"]) == {
        "ecolets@cefe.cnrs.fr",
        "ecolets2@cefe.cnrs.fr",
    }
    assert rules["novelty_expectation"] == "same expectation for novelty as a Letter"

    proposal = PROPOSAL.read_text(encoding="utf-8")
    body = proposal.split("## Proposal", 1)[1]
    assert len(WORD_RE.findall(body)) <= 300

    email = EMAIL.read_text(encoding="utf-8")
    assert "ecolets@cefe.cnrs.fr" in email
    assert "ecolets2@cefe.cnrs.fr" in email


def test_activation_is_strategy_gate_not_science_gate() -> None:
    contract = _load()
    assert "C2 is declined or judged too broad" in contract["activation_rule"]
    assert contract["machine_blockers"] == 0
    assert any("activated" in item for item in contract["human_gates_before_activation_or_send"])
    assert "Do not move Boundary theorems into C2 or CED" in contract["stop_rule"]
