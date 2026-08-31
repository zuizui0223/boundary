# Boundary: identification limits of mechanistic evidence in ecology

This repository is the standalone research repository for **Paper A**, the boundary / mechanistic-evidence Perspective formerly developed inside `microdonta`.

## Scientific question

> What can the current observation map identify about mechanism in principle?

The paper separates **biological/mechanistic proximity** from **identification strength**. Measurements close to biological machinery can remain compatible with several competing mechanisms, while strategically chosen field measurements can sometimes eliminate mechanism ambiguity directly. The two properties are distinct; no monotone relation or statistical independence is assumed.

## Quantitative spine

```text
mechanistic evidence needs an identification axis
→ net-only multiplicative equivalence
→ k-channel residual dimension = k - 1 - r
→ calibration-transport family 1/Gamma <= kappa <= Gamma
→ reference-invariant breakdown factor
→ channel-anchor and calibration-anchor design rules
→ joint-set reporting rule
```

For a declared positive product `W = prod_j F_j`, endpoint-only observation leaves `k-1` product-preserving degrees of freedom. `r` independent direct channel anchors leave `k-1-r`.

For the common two-channel proxy comparison, `kappa=q_1/q_0` is bounded symmetrically by `1/Gamma <= kappa <= Gamma`. Stable calibration (`Gamma=1`), finite partial identification, and unrestricted transport are one family. The canonical directional breakdown factor is `Gamma*=max(rho_hat,1/rho_hat)`.

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

`boundary` owns Paper A. `microdonta` is being reduced to the separate observation-design methods paper. Neither repository should require the other at runtime or for peer-review reproducibility.
