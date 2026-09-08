"""Internal projection of Boundary diagnostics into the shared action taxonomy.

This module does not alter the active Boundary Perspective or define a new
identification criterion.  It translates already-computed exact Boundary
results into the canonical state/action vocabulary shared with MROD.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Iterable

from .observation_rank import RankIdentificationResult
from .target_factorization import TargetFactorizationAudit


_TAXONOMY = Path(__file__).resolve().parents[1] / "docs" / "limitation_action_taxonomy_v1.json"


@dataclass(frozen=True)
class TaxonomySignal:
    axis: str
    state: str
    action: str
    source: str


@dataclass(frozen=True)
class BoundaryTaxonomyProjection:
    signals: tuple[TaxonomySignal, ...]
    certificates: tuple[str, ...]
    sources: tuple[str, ...]

    @property
    def canonical_actions(self) -> tuple[str, ...]:
        return tuple(dict.fromkeys(signal.action for signal in self.signals))

    @property
    def canonical_states(self) -> tuple[tuple[str, str], ...]:
        return tuple((signal.axis, signal.state) for signal in self.signals)


def _registry() -> dict[tuple[str, str], str]:
    data = json.loads(_TAXONOMY.read_text(encoding="utf-8"))
    if data.get("schema") != "limitation_action_taxonomy" or data.get("version") != "1.0":
        raise ValueError("unsupported limitation-action taxonomy contract")
    registry: dict[tuple[str, str], str] = {}
    for axis in data["axes"]:
        for item in axis["states"]:
            key = (axis["id"], item["state"])
            if key in registry:
                raise ValueError(f"duplicate taxonomy state {key!r}")
            registry[key] = item["action"]
    return registry


def _signal(axis: str, state: str, source: str) -> TaxonomySignal:
    try:
        action = _registry()[(axis, state)]
    except KeyError as exc:
        raise ValueError(f"state {(axis, state)!r} is absent from the canonical taxonomy") from exc
    return TaxonomySignal(axis, state, action, source)


def _projection(
    signals: Iterable[TaxonomySignal], *,
    certificates: Iterable[str] = (),
    sources: Iterable[str] = (),
) -> BoundaryTaxonomyProjection:
    unique: dict[tuple[str, str, str], TaxonomySignal] = {}
    for signal in signals:
        unique.setdefault((signal.axis, signal.state, signal.action), signal)
    return BoundaryTaxonomyProjection(
        tuple(unique.values()),
        tuple(dict.fromkeys(str(item) for item in certificates)),
        tuple(dict.fromkeys(str(item) for item in sources)),
    )


def project_target_factorization(
    audit: TargetFactorizationAudit,
) -> BoundaryTaxonomyProjection:
    """Project finite exact target-factorization status and conflict witnesses."""
    source = "target_factorization_audit"
    signals: list[TaxonomySignal] = []
    certificates: list[str] = []

    if audit.factors_through_observation:
        if all(len(fibre.world_indices) == 1 for fibre in audit.fibres):
            # On the supplied finite world set the observation identifies the full
            # represented world, not merely the declared target.
            signals.append(_signal("target_identification", "fully_resolved", source))
        else:
            signals.append(
                _signal(
                    "target_identification",
                    "target_identified_full_mechanism_ambiguous",
                    source,
                )
            )
            for fibre in audit.fibres:
                if len(fibre.world_indices) > 1:
                    certificates.append(
                        f"observation={fibre.observation!r} retains worlds={fibre.world_indices!r} "
                        f"with target={fibre.target_values[0]!r}"
                    )
    else:
        signals.extend(
            (
                _signal(
                    "observation_structure",
                    "current_target_collapsed_on_observation_fibre",
                    source,
                ),
                _signal("target_identification", "target_unresolved", source),
            )
        )
        for fibre in audit.fibres:
            if fibre.conflict_pair is not None:
                certificates.append(
                    f"observation={fibre.observation!r} conflict_pair={fibre.conflict_pair!r} "
                    f"target_values={fibre.target_values!r}"
                )

    return _projection(signals, certificates=certificates, sources=(source,))


def project_rank_identification(
    result: RankIdentificationResult,
) -> BoundaryTaxonomyProjection:
    """Project exact log-linear full-state rank identification."""
    source = "observation_rank_audit"
    if result.point_identified:
        signals = (_signal("target_identification", "fully_resolved", source),)
        certificates = (
            f"rank={result.observation_rank}=channels={result.channels}; residual_dimension=0",
        )
    else:
        signals = (
            _signal(
                "observation_structure",
                "current_target_collapsed_on_observation_fibre",
                source,
            ),
            _signal("target_identification", "target_unresolved", source),
        )
        certificates = (
            f"rank={result.observation_rank}; channels={result.channels}; "
            f"residual_dimension={result.residual_dimension}",
        )
    return _projection(signals, certificates=certificates, sources=(source,))


def project_scalar_rank_gain(
    gain: int,
    *,
    source: str = "scalar_observation_rank_gain",
) -> BoundaryTaxonomyProjection:
    """Project the exact scalar rank-gain screen for the active log-linear class."""
    if gain == 0:
        state = "candidate_determined_by_current_observation"
    elif gain == 1:
        state = "candidate_structurally_new"
    else:
        raise ValueError("scalar rank gain must be exactly 0 or 1")
    return _projection(
        (_signal("observation_structure", state, source),),
        certificates=(f"scalar_rank_gain={gain}",),
        sources=(source,),
    )


def combine_boundary_taxonomy_projections(
    *projections: BoundaryTaxonomyProjection,
) -> BoundaryTaxonomyProjection:
    """Union Boundary signals without imposing a severity or priority order."""
    return _projection(
        (signal for projection in projections for signal in projection.signals),
        certificates=(
            item for projection in projections for item in projection.certificates
        ),
        sources=(source for projection in projections for source in projection.sources),
    )


__all__ = [
    "TaxonomySignal",
    "BoundaryTaxonomyProjection",
    "project_target_factorization",
    "project_rank_identification",
    "project_scalar_rank_gain",
    "combine_boundary_taxonomy_projections",
]
