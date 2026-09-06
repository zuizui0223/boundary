# Structural observation limits: scope and neighboring concepts

Status: conceptual audit for the active Boundary Perspective.

## Core object

The paper is about a property of an observation map, not about generic uncertainty.

Let `m` denote a declared mechanism state and `O` the current observation map. Two mechanism states are observationally equivalent under `O` when the map cannot distinguish them. In deterministic form,

```text
m1 ~_O m2  iff  O(m1) = O(m2).
```

In a stochastic formulation the corresponding condition is equality of the observational distributions relevant to the declared inference. The paper's positive multiplicative/log-linear results give an exact instance: the compatible mechanism set is an affine class whose dimension is the nullity of the observation matrix.

The scientific limitation is therefore not merely that a variable was not measured. It is that the current observation map collapses biologically different states onto the same observable record.

## What this is not

### 1. Not a null-hypothesis problem

A null test asks whether a particular null statement can be rejected. Rejecting `H0` can establish that an effect or pattern is inconsistent with that null while leaving several non-null mechanisms compatible with the same observation.

```text
reject H0  !=  identify which non-null mechanism generated the observation
```

Boundary concerns the second problem.

### 2. Not residual error or goodness of fit

Residuals and discrepancy measure how closely a fitted prediction matches observed data. Mechanism ambiguity can remain even at exact fit. If two mechanism states lie on the same observation-equivalence orbit, both can have zero discrepancy while differing biologically.

```text
perfect fit  !=  unique mechanism decomposition
```

The word `residual` in `residual structural dimension` refers to dimensions left unidentified after applying observation constraints, not regression residuals.

### 3. Not sampling uncertainty

Replicates, larger sample size and higher precision can reduce sampling variance. They do not necessarily change structural identification. In the exact log-linear class, repeating, rescaling or measuring more precisely along an existing observation row leaves its row span unchanged and therefore leaves structural nullity unchanged.

```text
more observations of the same identification direction
can improve precision without adding an identification direction
```

This is a structural statement, not a claim that replication has no statistical value.

### 4. Not the same as counterfactual causal identification

Counterfactual causal inference asks what an outcome would be under an intervention or alternative exposure, under its own identification assumptions. That estimand can be scientifically decisive without uniquely decomposing all biological mechanisms that produce it. Conversely, two candidate mechanisms can sometimes be separated by a feasible observational measurement when they make different observational predictions, without estimating a full intervention effect.

```text
identify a causal contrast  !=  identify a complete mechanism decomposition
```

Boundary is complementary to causal inference. It asks whether the observation map distinguishes the declared mechanism alternatives; it does not claim that observational discrimination substitutes for intervention when the scientific estimand itself is causal.

## Exact result already implemented

For positive channels `F_j`, write `x_j=log F_j`. If exact log-linear observations define matrix `M`, then the compatible set is

```text
C_y = {x : Mx = y}
```

and, conditional on compatibility,

```text
dim(C_y) = k - rank(M).
```

A new scalar observation with row `a^T` reduces structural ambiguity if and only if

```text
a not in rowspan(M).
```

For one scalar observation the gain is exactly one rank unit when it helps and zero otherwise. This is implemented in `boundary_model/observation_rank.py` and independently tested against determinant/minor rank calculations in `tests/test_observation_rank_theorem.py`.

## Why this matters for ecological limitations sections

A conventional limitation statement often says that fitness, molecular state, an intermediate process or another expensive quantity was not measured. That may be true, but it does not yet diagnose the inferential limitation. The more informative sequence is:

```text
declare the mechanism alternatives
-> declare the observation map
-> characterize the equivalence set left by that map
-> separate structural ambiguity from sampling uncertainty and model misfit
-> identify which new observation direction would actually cut the equivalence set
```

The first four steps belong to Boundary. Ranking feasible candidate observations by how much residual mechanism ambiguity they are expected to remove belongs to the separate `mrod` project.

## Interface to mrod

Boundary and mrod should meet at a clean interface:

```text
Boundary:
current observation map
-> observational-equivalence / identified set
-> unresolved distinctions

mrod:
unresolved distinctions + candidate observation vocabulary
-> information value of each candidate
-> next observation
```

Boundary may prove that a candidate adds a new identification direction in a restricted exact class. It should not become a general sequential candidate-ranking framework. Conversely, mrod should take residual ambiguity as an input object rather than rebranding generic null testing, residual analysis or causal-effect estimation as mechanism resolution.

## Claim guard

Use the strong wording only under the declared scope:

> Increasing replication or precision cannot repair a structurally invariant observation map.

Do not shorten this to `more data never help`. New data can help when they change the observation map, constrain a previously free direction, calibrate a proxy, reduce sampling error enough to distinguish approximate predictions, or support assumptions required by a causal estimand.
