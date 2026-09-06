import pytest

from boundary_model.target_identification import (
    claim_constant_on_equivalence_class,
    identify_target,
)


def test_target_can_be_identified_without_unique_mechanism():
    worlds = (
        {"mechanism": "A", "effect_sign": 1},
        {"mechanism": "B", "effect_sign": 1},
        {"mechanism": "C", "effect_sign": 1},
    )
    result = identify_target(worlds, lambda w: w["effect_sign"])
    assert result.compatible_world_count == 3
    assert result.point_identified
    assert result.identified_value == 1


def test_target_remains_set_valued_when_compatible_worlds_disagree():
    worlds = (
        {"mechanism": "A", "effect_sign": 1},
        {"mechanism": "B", "effect_sign": -1},
    )
    result = identify_target(worlds, lambda w: w["effect_sign"])
    assert result.unresolved
    assert set(result.target_values) == {-1, 1}
    with pytest.raises(ValueError, match="not point-identified"):
        _ = result.identified_value


def test_empty_equivalence_class_is_invalid():
    with pytest.raises(ValueError, match="non-empty"):
        identify_target((), lambda w: w)


def test_boolean_helper_matches_singleton_image():
    worlds = (("A", "same"), ("B", "same"))
    assert claim_constant_on_equivalence_class(worlds, lambda w: w[1])
