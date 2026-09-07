# Limitation-to-action taxonomy across the observation-information architecture

Status: **future cross-program architecture / claim-ceiling contract**. This document does not modify the active Boundary Perspective, MROD MEE manuscript, REC manuscript or TNOA paper claims.

Machine-readable contract: `docs/limitation_action_taxonomy_v1.json`  
Canonical SHA-256: `d150182345b04a9606b0a1c09caa4ad2328c0f8bf5179a258beae537d0aa3432`

## 1. Do not compress different limitations into one severity score

The architecture now has enough distinct failure and repair modes that one scalar `limitation score` would recreate the semantic coarsening the programme is trying to avoid. The reporting object is therefore a **state vector**, not a ladder from weak to severe:

```text
L = (
  evidence integrity,
  observation structure,
  current-state estimability,
  target identification,
  candidate prediction coverage,
  information horizon,
  specification robustness,
  resource / operational state
).
```

Several coordinates can be active simultaneously. For example, a best next observation can be identified while field budget is exhausted; a question-relative target can be identified while microscopic mechanism ambiguity remains; all singleton candidates can have zero immediate information while a joint bundle has positive information.

The correct output is therefore

```text
state vector -> one or more licensed scientific actions
```

rather than

```text
state vector -> one generic limitation label.
```

## 2. Axes and scientific actions

| Axis | Typical states | Action when limited |
|---|---|---|
| evidence integrity | record support uncertain; semantic coarsening present | audit record entry / denominator; restore or retain richer evidence state |
| observation structure | candidate determined by current observation; structurally new | drop exact redundant candidates; evaluate mechanism-target information for structurally new candidates rather than assuming value |
| current-state estimability | current admissible state estimable / non-estimable | repair or re-estimate the current admissible region before ranking observations |
| target identification | fully resolved; target resolved with residual mechanism ambiguity; unresolved; assumption-sensitive | stop at the declared target when appropriate, retain residual ambiguity, or report identified set / breakdown range |
| candidate prediction coverage | none declared; none estimable; partial; complete | expand candidate vocabulary, identify predictive outcome models, or restrict claims to provisional ranking among estimable candidates |
| information horizon | positive singleton; singleton-zero joint unaudited; singleton-zero joint positive; joint zero | measure the immediate best candidate, audit bundles, use non-myopic design, or redesign the observation vocabulary |
| specification robustness | conclusion/recommendation stable or sensitive | report conclusion and recommendation sensitivity separately; do not invent one robust optimum |
| resource / operational | budget exhausted; adaptive information gain; expected-cost saving; cost preferences cross scenarios | retain the epistemic recommendation, report operational savings separately, or declare an additional cost decision rule before scalar cost ranking |

The machine-readable JSON contains the normative state/action labels used for cross-repository regression tests.

## 3. Relation to Boundary

Boundary primarily determines the `observation_structure` and `target_identification` coordinates. For a target `T=tau(S)`, the target can be identified even while the full mechanism world is not. Under an assumption family, Boundary can additionally report an identified-set or breakdown range.

Boundary must not infer downstream actionability from structural novelty alone:

```text
candidate structurally new
-/->
positive mechanism-target information.
```

Nor should a structural impossibility result be promoted beyond its stated observation map or assumption family.

## 4. Relation to MROD

MROD owns most downstream coordinates after the current admissible region exists. Its existing limitation-to-action prototype already distinguishes current-state estimability, target versus full resolution, predictive coverage, singleton information, bundle information, budget state and recommendation stability.

Subsequent internal audits extend the same logic without changing the MEE mainline:

- replication audits distinguish finite-sample gains from observation-law floors;
- repeat-versus-switch audits compare another repeat with a different observation and with the remaining repeat-only information ceiling;
- calibration audits separate fixed calibration sensitivity from unknown calibration state;
- routing audits separate direct target information from information used to choose a later assay;
- expected-cost audits separate target-information advantage from operational measurement savings;
- cost-tie and scenario-tradeoff audits prevent those operational quantities from being misread as an expected-cost optimum.

These are **coordinates and claim ceilings**, not a mandate to combine all objectives in one optimizer.

## 5. Action composition examples

### Prediction-limited and budget-limited

If the current region is estimable but some candidate outcome models are missing and current field budget is also exhausted, report both:

```text
prediction action: identify candidate outcome models
resource action: report budget limit
```

Do not relabel the state as zero information.

### Target resolved but full mechanism ambiguous

If `T=tau(S)` is constant on the current observation fibre while `S` is not,

```text
scientific action: stop for the declared question
reporting action: retain residual out-of-target mechanism ambiguity.
```

Do not demand deeper molecular resolution unless those distinctions belong to the question target.

### Singleton zero but bundle positive

If all validated singleton values are zero but joint candidate information is positive,

```text
scientific action: use a non-myopic bundle / sequence design.
```

Do not call the candidate vocabulary information-limited.

### Recommendation stable but conclusion sensitive

If a Boundary conclusion changes across an assumption family but the same MROD candidate remains best,

```text
report conclusion breakdown
AND
report stable follow-up observation.
```

The two robustness statements are not collapsed.

### Expected-cost preference crosses scenarios

If two information-equivalent trees exchange which calibration/weight scenario they are cheaper in,

```text
report the scenario-wise cost vector
AND
require an explicit meta-prior, max-cost or cost-regret rule before scalar ranking.
```

Do not silently average scenarios.

## 6. Relation to the existing cross-paper architecture

This taxonomy refines the compact sequence

```text
preserve -> audit -> diagnose -> resolve
```

from `observation_information_order_architecture_2026-09-06.md` without replacing it.

- REC/TNOA primarily determine whether the evidence entering downstream inference is support-complete enough and semantically rich enough for the intended question.
- Boundary diagnoses which scientific distinctions survive the current observation map.
- MROD diagnoses whether a feasible observation can resolve the remaining distinction and what kind of acquisition problem remains.

The taxonomy is therefore an **interface contract among questions**, not one omnibus statistical method.

## 7. Scope guard

This taxonomy does not claim that:

- every project must traverse every axis;
- the axes are statistically independent;
- actions from different axes can be added into one utility without additional assumptions;
- expected information, causal value, financial cost and biological importance share a common natural unit;
- a listed action is globally optimal outside its declared model and candidate family;
- a resource or prediction limitation is evidence for biological absence;
- MROD repairs upstream record deletion or semantic coarsening automatically;
- cost-aware, robust, goal-oriented or non-myopic experimental design is invented here.

Its purpose is narrower: **when a limitation is found, preserve what kind of limitation it is, state what inference it blocks, and name the next scientific action without manufacturing certainty.**
