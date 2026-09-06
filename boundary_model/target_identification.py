"""Target-specific identification over an observational equivalence class.

Boundary owns structural identification, not downstream normative/report
licensing. A singleton target image is therefore reported as point-identified,
not as automatically publishable or actionable.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Generic, Iterable, TypeVar

W = TypeVar("W")
T = TypeVar("T")


def _unique_equal(values: Iterable[T]) -> tuple[T, ...]:
    unique: list[T] = []
    for value in values:
        if not any(value == old for old in unique):
            unique.append(value)
    return tuple(unique)


@dataclass(frozen=True)
class TargetIdentification(Generic[T]):
    compatible_world_count: int
    target_values: tuple[T, ...]

    @property
    def point_identified(self) -> bool:
        return len(self.target_values) == 1

    @property
    def unresolved(self) -> bool:
        return len(self.target_values) > 1

    @property
    def identified_value(self) -> T:
        if not self.point_identified:
            raise ValueError("target is not point-identified")
        return self.target_values[0]


def identify_target(
    compatible_worlds: Iterable[W],
    target: Callable[[W], T],
) -> TargetIdentification[T]:
    """Map the current compatible-world set through one declared target."""
    worlds = tuple(compatible_worlds)
    if not worlds:
        raise ValueError("compatible_worlds must be non-empty")
    values = _unique_equal(target(world) for world in worlds)
    return TargetIdentification(
        compatible_world_count=len(worlds),
        target_values=values,
    )


def claim_constant_on_equivalence_class(
    compatible_worlds: Iterable[W],
    target: Callable[[W], T],
) -> bool:
    return identify_target(compatible_worlds, target).point_identified
