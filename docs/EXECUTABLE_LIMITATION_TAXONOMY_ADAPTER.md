# Executable Boundary projection into the shared limitation-to-action taxonomy

Status: **internal cross-program architecture adapter**. This does not change the active Boundary Perspective, figures or theorem claims.

Boundary and MROD store the same canonical taxonomy JSON. The purpose of `boundary_model/limitation_taxonomy_adapter.py` is narrower than introducing a new inference layer: it translates exact Boundary diagnostics that already exist into that shared state/action vocabulary.

## 1. Target-factorization projection

For a finite declared world set, `audit_target_factorization` checks whether the scientific target factors through the observation map.

If one observation fibre contains different target values,

```text
O(w1)=O(w2)
but T(w1)!=T(w2),
```

the adapter emits both

```text
observation_structure = current_target_collapsed_on_observation_fibre
target_identification = target_unresolved.
```

The conflict-pair certificate is retained. The taxonomy does not replace that witness.

If the target is constant on every fibre but at least one fibre still contains multiple represented worlds, the adapter emits

```text
target_identification = target_identified_full_mechanism_ambiguous.
```

This is the exact question-relative case: the declared question is answered even though finer mechanism/world distinctions remain.

If every observation fibre is a singleton on the supplied finite world set, the full represented world is identified by the observation and the adapter emits

```text
target_identification = fully_resolved.
```

All statements remain conditional on the supplied finite domain and maps.

## 2. Exact log-linear rank projection

For the active positive log-linear class, `log_linear_identification` returns the exact row rank and residual dimension.

```text
residual_dimension > 0
    -> current_target_collapsed_on_observation_fibre
    -> target_unresolved

residual_dimension = 0
    -> fully_resolved
```

Here the target is the full declared log-channel state, so point identification of the state is licensed by full rank.

## 3. Candidate structural screen

`scalar_observation_rank_gain` is projected as

```text
rank gain 0
    -> candidate_determined_by_current_observation
    -> drop_as_structurally_zero_value_for_current_contrast

rank gain 1
    -> candidate_structurally_new
    -> evaluate_mechanism_target_information_not_structural_novelty_alone.
```

The second action is deliberately not `measure this candidate`. Structural novelty can split nuisance variation without resolving the mechanism contrast of interest. MROD owns that downstream value calculation.

## 4. Composition without severity

Boundary signals are compositional. A current system can be simultaneously

- target unresolved under the present observation map; and
- equipped with a structurally new candidate observation.

The adapter returns both coordinates. It does not turn them into one severity score or infer MROD information value.

## 5. Ownership boundary

This adapter does not infer:

- REC record-entry support;
- TNOA semantic-coarsening status;
- MROD candidate predictive coverage;
- mutual-information value;
- non-myopic bundle information;
- operational cost or budget state.

Those belong to other axes or repositories. The shared taxonomy provides the common vocabulary; it does not create a monolithic runtime pipeline.

## 6. Scope guard

The adapter does not establish that:

- the finite world set is exhaustive;
- observational target identification substitutes for causal intervention;
- full rank in the active log-linear class proves identification for arbitrary nonlinear models;
- structural rank gain guarantees positive mechanism information;
- a target-resolved fibre has no finer biological ambiguity;
- any canonical action is globally optimal outside its declared assumptions.

Its purpose is only to make existing Boundary diagnostics interoperable with the same limitation/action state vector already used by MROD extensions.
