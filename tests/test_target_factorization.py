"""Finite factorization, reconstruction and conflict-certificate obligations."""
from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import pytest

from boundary_model.target_factorization import audit_target_factorization

FIXTURE = Path(__file__).parent / "fixtures" / "target_factorization_v1.json"
FIXTURE_SHA256 = "d12478f3354170130a8ed11e0c019a0099f5dc942d4365195770619ae3f14841"


def _rows(case):
    return [dict(zip(case["columns"], values)) for values in case["rows"]]


def _pairwise_oracle(rows, observation):
    return all(observation(a) != observation(b) or a["T"] == b["T"]
               for a in rows for b in rows)


def test_shared_contract_fixture_is_versioned_and_pinned():
    assert sha256(FIXTURE.read_bytes()).hexdigest() == FIXTURE_SHA256
    assert json.loads(FIXTURE.read_text())["contract_id"] == "boundary-mrod-target-factorization-v1"


def test_shared_cases_reconstruct_or_return_same_observation_different_target():
    for case in json.loads(FIXTURE.read_text())["cases"]:
        rows = _rows(case)
        maps = [("current", lambda r: r["O"], case["expected"]["factors"])]
        maps.extend((name, lambda r, q=name: (r["O"], r[q]), expected)
                    for name, expected in case["expected"]["repairs"].items())
        for name, observation, expected in maps:
            report = audit_target_factorization(rows, observation, lambda r: r["T"])
            assert report.compatible_world_count == len(rows)
            assert report.factors_through_observation == expected, (case["name"], name)
            assert expected == _pairwise_oracle(rows, observation)
            if expected:
                reconstruction = report.reconstruction_map()
                assert all(reconstruction[observation(r)] == r["T"] for r in rows)
            else:
                with pytest.raises(ValueError, match="does not factor"):
                    report.reconstruction_map()
            for fibre in report.fibres:
                assert fibre.point_identified == (fibre.conflict_pair is None)
                if fibre.conflict_pair is not None:
                    a, b = (rows[i] for i in fibre.conflict_pair)
                    assert observation(a) == observation(b)
                    assert a["T"] != b["T"]


def test_exhaustive_binary_maps_and_repairs_on_four_worlds():
    worlds = tuple(range(4))
    maps = tuple(product((0, 1), repeat=4))
    for observed, target, candidate in product(maps, repeat=3):
        report = audit_target_factorization(
            worlds, lambda i: (observed[i], candidate[i]), lambda i: target[i])
        expected = all(observed[i] != observed[j] or candidate[i] != candidate[j]
                       or target[i] == target[j] for i in worlds for j in worlds)
        assert report.factors_through_observation == expected
        if expected:
            g = report.reconstruction_map()
            assert all(g[(observed[i], candidate[i])] == target[i] for i in worlds)


def test_one_resolved_fibre_is_not_global_identification():
    report = audit_target_factorization(
        [(0, 0), (0, 0), (1, 0), (1, 1)], lambda w: w[0], lambda w: w[1])
    assert report.fibres[0].point_identified
    assert report.unresolved_fibre_count == 1
    assert not report.factors_through_observation


def test_row_replication_cannot_remove_an_existing_conflict():
    rows = [(0, 0), (0, 1)]
    for count in (1, 10, 1000):
        report = audit_target_factorization(rows + [rows[0]] * count,
                                            lambda w: w[0], lambda w: w[1])
        assert not report.factors_through_observation


def test_empty_or_missing_values_are_not_identification():
    with pytest.raises(ValueError, match="non-empty"):
        audit_target_factorization([], lambda w: w, lambda w: w)
    for bad in (None, float("nan"), float("inf"), (0, float("nan")), [0]):
        with pytest.raises(ValueError):
            audit_target_factorization([0], lambda w: 0, lambda w: bad)
        with pytest.raises(ValueError):
            audit_target_factorization([0], lambda w: bad, lambda w: 0)


def test_maps_are_evaluated_once_per_world():
    calls = [0, 0]
    def observed(w):
        calls[0] += 1
        return w // 2
    def target(w):
        calls[1] += 1
        return w // 2
    report = audit_target_factorization(iter(range(4)), observed, target)
    assert report.reconstruction_map() == {0: 0, 1: 1}
    assert calls == [4, 4]
