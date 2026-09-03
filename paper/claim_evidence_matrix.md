# Boundary Perspective claim–evidence matrix

This file is the stop rule against claim escalation. Every headline statement must map to literature, an exact theorem under a declared observation map, or an operational consequence of those results.

| Claim | Evidence role | Main support | Figure | Scope guard |
|---|---|---|---|---|
| Biological proximity and identification strength are distinct dimensions | Perspective synthesis | Ungerer 2008; Rudman 2018; Grace 2025; Smith 2020; Siegel & Dee 2025 | Fig. 1 | Do not claim statistical independence or a universal ecology-wide hierarchy |
| A proximal measurement can remain non-identifying | Conceptual consequence | identification definition + genomic literature | Fig. 1 | Conditional on declared competing mechanisms |
| A field measurement can strongly discriminate mechanisms | Conceptual/design consequence | Smith 2020; design logic | Fig. 1 | Do not claim field evidence is generally superior |
| For exact log-linear observations of a positive multiplicative chain, residual structural dimension is `k-rank(M)` | Exact necessary-and-sufficient theorem | `docs/observation_rank_identification_theorem_2026-09-03.md`, Theorem R1; exhaustive rank oracle | Fig. 2 / text | Exact log-linear observation class; sampling uncertainty is separate |
| A new scalar observation reduces structural ambiguity iff its row lies outside the current observation row span | Exact necessary-and-sufficient design theorem | Theorem R2 + `tests/test_observation_rank_theorem.py` | Fig. 2 / text | One exact scalar log-linear candidate; nonlinear/noisy candidates require their own observation map |
| Repeating, rescaling, or improving precision of an observation without changing the observation row span cannot reduce structural unidentified dimension | Exact corollary | R2a | text | Structural identification statement, not a claim that precision has no statistical value |
| Net-only `W=prod_j F_j` leaves `k-1` dimensions | Exact corollary | R1 with only the net row | Fig. 2 | Positive declared multiplicative endpoint map only |
| `r` distinct direct coordinate anchors leave `k-1-r` | Exact corollary | R2b; coordinate rows are proved independent with the net row | Fig. 2 | `0<=r<=k-1`; direct coordinate/ratio anchors only |
| Stable/bounded/unrestricted proxy transport are one family | Exact theorem | `1/Gamma <= kappa <= Gamma` | Fig. 3 | `Gamma` is external, not estimated from the same W/X data |
| `Gamma*=max(rho_hat,1/rho_hat)` is reference-invariant | Exact breakdown result | calibration-transport family | Fig. 3 | 34% is only the directional translation of the worked example |
| Channel marginals must not be combined independently | Exact joint-set consequence | `rho_F rho_E=rho_W` | Fig. 3 | Sampling uncertainty is a separate layer |
| Pollination has rate-by-effectiveness architecture | Ecological architecture | Rader; Ballantyne; Reynolds & Fenster | text | Community sum-of-products adds another allocation problem |
| Seed dispersal has Quantity × Quality architecture | Independent cross-domain architecture | Schupp, Jordano & Gómez 2010 | text | Do not imply identical biological channel semantics |

## Minimum publishable claim

Even if reviewers reject the broadest rhetoric, the paper still contains:

1. a literature-grounded distinction between mechanistic proximity and identification strength;
2. a necessary-and-sufficient rank criterion for exact log-linear identification, including the exact condition under which a new measurement reduces ambiguity;
3. `k-1-r` as a proved coordinate-anchor corollary rather than a dimension-count definition;
4. the symmetric calibration-transport family, sharp joint set and breakdown factor;
5. direct field-design and reporting consequences.

## Claim-escalation stop rule

Do not add a general statement to the Abstract, proposal or Discussion unless it is one of:

- directly supported by cited ecological literature;
- an exact theorem under a declared observation model;
- a transparent operational consequence of an exact result;
- explicitly labelled as a Perspective-level proposal rather than a universal theorem.
