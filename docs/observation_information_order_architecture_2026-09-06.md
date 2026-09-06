# Observation-information order across REC, TNOA, Boundary and MROD

Status: **future cross-paper architecture note.** This document positions sister projects without changing the active Boundary Perspective, REC manuscript, TNOA Paper 1 or MROD submission claims.

## 1. Why these projects should not be merged conceptually

The projects all care about the gap between the biological world and scientific inference, but they expose different failure or repair points.

- **REC:** biological events or exposure opportunities may fail to enter the scientific record at all.
- **TNOA:** a rich entered record may be semantically collapsed into a coarser decision than the evidence licenses.
- **Boundary:** even after the current evidence record is fixed, distinct mechanism states may remain observationally equivalent under the declared observation map.
- **MROD:** when mechanism ambiguity remains, choose a feasible future observation by how much information it is expected to add about mechanism identity.

Boundary is therefore not a third information-loss operator parallel to REC and TNOA. It is a **diagnostic of non-injectivity** in the current mechanism-to-observation map. MROD is an **active refinement / repair layer** built after that diagnosis.

## 2. A common state-space notation

Let the full declared world state be

```text
Z = (theta, S, M),
```

where `S` is the mechanism variable of scientific interest, `theta` are biological or statistical parameters, and `M` collects measurement-side states such as observability, sensor geometry or nuisance conditions.

A primary physical measurement is

```text
Y = F(Z).
```

Let `K` denote whether an exposure enters the scientific record, `E` a rich retained evidence representation, and `c(E)` a later semantic coarsening. A downstream mechanism-facing observation map can therefore be written schematically as

```text
O = O_mech(E)
```

or, after coarsening,

```text
O_c = O_mech(c(E)).
```

The notation is schematic: the projects do not require one runtime pipeline or one shared implementation.

## 3. Information operations before Boundary

### 3.1 Optional reference refinement

The existing V3/reference-refinement theory considers adding a target-free reference `Q_ref` while retaining the primary observation. Under its declared conditions, the compatible measurement-state set can contract:

```text
M(Y,Q_ref) subseteq M(Y).
```

This is potentially information-adding. It is not REC and it does not by itself license a biological mechanism conclusion.

### 3.2 REC: support deletion before inference

REC starts from a gate-independent exposure universe `Omega` and tracks acquisition / registration / record-entry provenance. When `K=0` rows disappear from the entered record, the scientific problem is not merely semantic uncertainty among retained rows: exposure support and denominators can disappear.

REC therefore owns the question

> Which opportunities or events failed to become records, and what estimands are distorted by that selection?

This cannot generally be represented as a simple compatible-state expansion on one retained row because whole rows may be absent.

### 3.3 TNOA: semantic coarsening after entry

For a rich entered evidence state `E` and deterministic coarsening `c`, every world compatible with `E` is also compatible with its coarsening. Hence

```text
C(E) subseteq C(c(E)).
```

Semantic coarsening can preserve or enlarge the compatible-world set; it cannot create identification that was absent from the richer retained representation.

TNOA therefore owns the question

> What evidence state should be preserved, including unresolved states, before downstream ecological inference?

## 4. Boundary: diagnose mechanism equivalence after the observation map is declared

Let the current downstream observation map be

```text
O : Z -> Y_obs.
```

For exact observation `y`, define the compatible fibre

```text
A_0(y) = {z : O(z)=y and declared constraints hold}.
```

The mechanism-compatible set is its projection

```text
M_0(y) = pi_S(A_0(y)).
```

Two mechanism states are observationally equivalent relative to the declared map when the map does not separate the relevant worlds. In a deterministic formulation,

```text
s1 ~_O s2
```

when admissible states carrying `s1` and `s2` can produce the same current observation.

Boundary asks

> Which mechanism distinctions has the current observation map preserved, and which has it collapsed?

This is different from saying that a record was missed (REC), that a rich record was coarsened (TNOA), or that the model fits poorly. Exact fit can coexist with a non-singleton mechanism projection.

For the exact log-linear class in the active Boundary paper, the structural compatible dimension is

```text
k - rank(M_obs),
```

and a scalar candidate adds one structural direction iff its row lies outside the current observation row span.

## 5. MROD: choose a mechanism-targeted refinement

Suppose the current admissible region is `A_epsilon` and residual mechanism vector `S` is not resolved. A candidate future observation `Q` with a verified predictive partition has value

```text
V(Q) = I(S;Q | A_epsilon)/K.
```

Conditioning on a realised candidate outcome refines the current region:

```text
A_epsilon(q) subseteq A_epsilon,
```

but MROD values the refinement only to the extent that it reduces uncertainty in the **mechanism projection**, not merely the full latent state.

This produces the exact one-way interface already formalised between Boundary and MROD:

```text
Q already determined by current observation
    -> zero new mechanism information.

Q structurally new
    -/-> positive mechanism information.
```

A new observation can separate nuisance parameters while leaving `S` unchanged, so Boundary's rank screen does not replace MROD's information value.

## 6. Sensitivity propagation: identification robustness is not recommendation robustness

Boundary can generate a **family** of compatible sets indexed by a declared identification or transport assumption. Write the sensitivity index generically as `lambda`; examples include the calibration-transport factor `Gamma`, a bounded drift parameter, or another assumption that changes the identified set:

```text
lambda -> A_lambda -> pi_S(A_lambda).
```

Boundary asks whether a scientific conclusion survives that family. A directional breakdown factor such as `Gamma*` answers a question of the form

> Over what assumption range does the current conclusion remain identified in the same direction?

MROD asks a different downstream question. Once each admissible state under `lambda` has a mechanism projection and candidate predictive distribution, the same assumption family can induce a family of next-observation values

```text
V_lambda(Q) = I_lambda(S;Q | A_lambda)/K,
```

and therefore a family of recommended candidates

```text
B_lambda = argmax_Q V_lambda(Q).
```

Two robustness statements must not be conflated:

```text
identification robustness:
    the scientific conclusion is stable across lambda

recommendation robustness:
    the identity of the best next observation is stable across lambda
```

A conclusion can remain directionally robust while the most informative next observation changes, because different assumptions can redistribute the residual mechanism ambiguity without overturning the current directional conclusion. Conversely, the same next observation can remain optimal even while the identified conclusion becomes assumption-sensitive.

For a finite, predeclared sensitivity set `Lambda`, a simple reporting diagnostic is

```text
B_common = intersection_{lambda in Lambda} B_lambda.
```

A nonempty `B_common` means at least one ordinary MROD candidate is optimal throughout the declared assumption set. An empty `B_common` means the **next-observation recommendation itself** is assumption-sensitive. This is a reporting diagnostic, not a new robust-design objective; maximin, robust-EIG, model-averaging or regret criteria would add extra decision assumptions.

This creates a useful bridge between the active Boundary sensitivity logic and MROD without merging their papers:

```text
Boundary:
assumption family -> identified-set family -> conclusion breakdown

MROD:
same propagated family -> candidate-information family -> recommendation stability
```

For example, if a Boundary result states that a directional conclusion survives calibration drift up to a declared `Gamma`, a downstream MROD analysis can separately ask whether the same follow-up measurement is optimal throughout that tolerated drift range.

## 7. Full architecture and repair loop

A useful cross-project schematic is

```text
world / process state
    -> physical measurement (+ optional reference refinement)
    -> REC: acquisition / registration / record entry
    -> rich entered record
    -> TNOA: preserve target / nuisance / observability / unresolved evidence
    -> declared mechanism-facing observation map
    -> Boundary: diagnose residual mechanism equivalence
    -> MROD: choose next Q
    -> new physical measurement
    -> repeat the observation pipeline
```

The last arrow matters. An MROD candidate that is collected in the field still passes through a real observation process. If acquisition, observability, nuisance or semantic coarsening are material, the candidate predictive model should represent them rather than treating the desired scientific variable as automatically observed without error.

Thus MROD is not outside REC/TNOA. It is a downstream design decision whose chosen observation may loop back through those upstream evidence contracts.

## 8. Signed information view

The architecture contains operations of different signs and one diagnostic layer:

| Layer | Operation | Compatible-set effect |
|---|---|---|
| reference refinement | retain primary data + independent reference | can contract compatible measurement states |
| REC | entry selection | can delete exposure support / denominators |
| TNOA coarsening | map rich evidence to coarse state | can expand compatible worlds |
| Boundary | diagnose current observation map | no information operation; characterises remaining equivalence |
| MROD | acquire informative `Q` | expected contraction of mechanism uncertainty |

Do not force these effects into one additive information-loss number. They act on different objects and, for nonlinear ecological estimands, their consequences need not add.

## 9. Relation to proximate and ultimate explanation

The architecture does not require choosing between a deepest proximate measurement and a complete ultimate fitness analysis. A mechanism vocabulary can span links such as

```text
environment
-> interaction process
-> transfer / performance consequence
-> reproduction / demography
-> trait or population outcome.
```

Boundary diagnoses which links remain observationally interchangeable under the current evidence. MROD asks which feasible observation best separates those explanations. The most useful next measurement may therefore be an intermediate ecological link rather than the biologically deepest assay.

This is the practical bridge between proximate and ultimate explanation: identify the unresolved link, then measure where the competing explanations make different predictions.

## 10. Strong common principle

Across the projects, the common rule is not `collect more data` and not `always abstain`. It is:

> **Do not manufacture certainty by deleting unresolved structure. Preserve what was observed, retain provenance for what may be missing, diagnose what the current observation map cannot distinguish, and add information targeted to the unresolved scientific distinction.**

A compact sequence is

```text
preserve -> audit -> diagnose -> resolve
```

with each verb owned by a different evidence problem rather than one omnibus method.

## 11. Scope guard

This note does not claim:

- that every ecological project must use all four frameworks;
- that REC, TNOA, Boundary and MROD form one mandatory software pipeline;
- that information losses at different stages are additive;
- that MROD repairs missing records or semantic misclassification automatically;
- that observational mechanism discrimination substitutes for causal intervention when the estimand is causal;
- that a structurally new measurement necessarily has positive mechanism value;
- that conclusion robustness across an assumption family guarantees recommendation robustness;
- that the common-best reporting diagnostic replaces robust experimental-design methods.

The purpose is only to locate distinct questions in one information-order architecture so their claims do not overlap accidentally.
