"""Finite, deterministic target-factorization audit (internal cross-paper aid).

A certificate concerns exactly the supplied worlds and maps, not unenumerated
worlds, sampling confidence, causal interventions, or publication licensing.
No probability weights are used: a low-probability compatible world still counts.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from numbers import Real
from typing import Callable, Generic, Hashable, Iterable, TypeVar

from .target_identification import identify_target

W = TypeVar("W")
O = TypeVar("O", bound=Hashable)
T = TypeVar("T", bound=Hashable)


def _check_label(value: Hashable) -> None:
    """Require explicit, hashable labels with ordinary equality semantics."""
    if value is None:
        raise ValueError("missing values are not identified target/observation labels")
    if isinstance(value, tuple):
        for part in value:
            _check_label(part)
    elif isinstance(value, Real) and not math.isfinite(value):
        raise ValueError("non-finite values are not valid labels")
    try:
        hash(value)
    except TypeError as exc:
        raise ValueError("observation and target labels must be hashable") from exc


@dataclass(frozen=True)
class TargetFibre(Generic[O, T]):
    observation: O
    world_indices: tuple[int, ...]
    target_values: tuple[T, ...]
    # Global zero-based indices: same observation, different target values.
    conflict_pair: tuple[int, int] | None

    @property
    def point_identified(self) -> bool:
        return len(self.target_values) == 1


@dataclass(frozen=True)
class TargetFactorizationAudit(Generic[O, T]):
    compatible_world_count: int
    fibres: tuple[TargetFibre[O, T], ...]

    @property
    def factors_through_observation(self) -> bool:
        return bool(self.fibres) and all(f.point_identified for f in self.fibres)

    @property
    def unresolved_fibre_count(self) -> int:
        return sum(not f.point_identified for f in self.fibres)

    def reconstruction_map(self) -> dict[O, T]:
        """Return g on the observed image only; refuse a partial global map."""
        if not self.factors_through_observation:
            raise ValueError("target does not factor through this observation map")
        return {f.observation: f.target_values[0] for f in self.fibres}


def audit_target_factorization(
    compatible_worlds: Iterable[W],
    observation: Callable[[W], O],
    target: Callable[[W], T],
) -> TargetFactorizationAudit[O, T]:
    """Test T=g(O) on a nonempty finite domain and retain conflict certificates.

    Each map is evaluated once per world. World multiplicities are retained but
    cannot remove a conflicting target value. Empty input is not identification.
    Labels must be nonmissing hashable scalars/tuples with stable equality; encode
    an explicit observation category with a string rather than a missing value.
    """
    worlds = tuple(compatible_worlds)
    if not worlds:
        raise ValueError("compatible_worlds must be non-empty")
    groups: dict[O, list[int]] = {}
    targets: list[T] = []
    for index, world in enumerate(worlds):
        observed, target_value = observation(world), target(world)
        _check_label(observed)
        _check_label(target_value)
        groups.setdefault(observed, []).append(index)
        targets.append(target_value)

    fibres: list[TargetFibre[O, T]] = []
    for observed, indices in groups.items():
        image = identify_target(indices, lambda i: targets[i])
        first = indices[0]
        conflict = next(
            ((first, i) for i in indices[1:] if targets[i] != targets[first]),
            None,
        )
        fibres.append(TargetFibre(
            observation=observed,
            world_indices=tuple(indices),
            target_values=image.target_values,
            conflict_pair=conflict,
        ))
    return TargetFactorizationAudit(len(worlds), tuple(fibres))
