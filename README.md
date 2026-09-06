# Boundary: identification limits of mechanistic evidence in ecology

This repository is the standalone research repository for **Paper A**, the boundary / mechanistic-evidence Perspective formerly developed inside `microdonta`.

## Scientific question

> What can the current observation map identify about mechanism in principle?

The paper separates **biological/mechanistic proximity** from **identification strength**. Measurements close to biological machinery can remain compatible with several competing mechanisms, while strategically chosen field measurements can sometimes eliminate mechanism ambiguity directly. The two properties are distinct; no monotone relation or statistical independence is assumed.

The target is a structural property of the observation map, not generic uncertainty. In particular:

```text
rejecting a null hypothesis      != identifying a unique mechanism
small residuals / perfect fit    != identifying a unique mechanism
more precise replication         != adding a new identification direction
identifying a causal contrast    != identifying a complete mechanism decomposition
```

These neighboring concepts remain scientifically valuable; they simply answer different questions. See `docs/observation_limits_scope_2026-09-06.md` for the scope audit.

## Quantitative spine

```text
mechanistic evidence needs an identification axis
→ observational equivalence under the declared observation map
→ exact log-linear residual dimension = k - rank(M)
→ a scalar observation helps iff it adds row rank
→ net-only multiplicative equivalence and k - 1 - r as a coordinate-anchor corollary
→ calibration-transport family 1/Gamma <= kappa <= Gamma
→ reference-invariant breakdown factor
→ channel-anchor and calibration-anchor design rules
→ joint-set reporting rule
```

For positive channels written on the log scale, exact log-linear observations define an observation matrix `M`. Conditional on compatibility, the structural unidentified dimension is

```text
k - rank(M).
```

A new scalar observation reduces that dimension if and only if its observation row lies outside the current row span. Duplicate, rescaled or more precise versions of an existing observation direction can improve statistical precision but do not change structural rank.

For the special declared product `W = prod_j F_j`, endpoint-only observation leaves `k-1` product-preserving degrees of freedom. `r` independent direct coordinate anchors leave `k-1-r`.

For the common two-channel proxy comparison, `kappa=q_1/q_0` is bounded symmetrically by `1/Gamma <= kappa <= Gamma`. Stable calibration (`Gamma=1`), finite partial identification, and unrestricted transport are one family. The canonical directional breakdown factor is `Gamma*=max(rho_hat,1/rho_hat)`.

## Interface to mrod

`boundary` characterizes the equivalence or identified set left by the **current** observation map. The separate `mrod` methods project takes unresolved mechanism distinctions plus a feasible candidate-observation vocabulary and asks which observation should be acquired next.

```text
boundary: current observation map -> unresolved equivalence set
mrod:     unresolved set + candidates -> next observation
```

The two repositories remain independent at runtime and for peer-review reproducibility.

## Repository layout

```text
boundary_model/   standalone identification-theory implementation
paper/            Perspective manuscript, proposal, audits and figure sources
tests/            theorem, submission and figure regression tests
```

## Reproduce

```bash
python -m pip install -e ".[dev]"
python paper/check_submission.py
python paper/make_mechanistic_evidence_axis_figure.py
python paper/make_multichannel_anchor_figure.py
python paper/make_boundary_identification_figure.py
pytest -q
```

## Separation from microdonta

`boundary` owns Paper A. `mrod` owns the separate observation-design methods paper. Neither repository should require the other at runtime or for peer-review reproducibility.
