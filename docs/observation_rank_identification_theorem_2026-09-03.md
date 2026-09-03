# Observation-rank identification theorem

Status: proof-backed extension of the multiplicative-chain identification result.

## Question

The existing `k-1-r` result assumes that the `r` added measurements are already known to be independent channel anchors. The stronger design question is:

> Given an arbitrary new measurement of a positive multiplicative chain, exactly when does it reduce mechanism ambiguity?

This cannot be answered from precision, biological proximity, replicate count, or the number of reported variables alone. It depends on whether the new observation cuts a direction that the existing observation map leaves free.

## Setup

Let positive channels be

\[
F=(F_1,\ldots,F_k),\qquad F_j>0,
\]

and write log channels

\[
x_j=\log F_j.
\]

The net product observation

\[
W=\prod_{j=1}^kF_j
\]

is the exact linear constraint

\[
\mathbf 1^\top x=\log W.
\]

Suppose additional exact log-linear observations have rows `a_1,...,a_m`, so the full observation matrix is

\[
M=
\begin{bmatrix}
\mathbf 1^\top\\
a_1^\top\\
\vdots\\
a_m^\top
\end{bmatrix}.
\]

For an observed value vector `y`, the compatible log-channel set is

\[
\mathcal C_y=\{x\in\mathbb R^k:Mx=y\}.
\]

The theorem concerns structural identification conditional on compatibility, not sampling uncertainty around `y`.

## Theorem R1 — exact residual-dimension criterion

Assume `C_y` is nonempty. Then

\[
\boxed{\dim(\mathcal C_y)=k-\operatorname{rank}(M).}
\]

Consequently, all `k` log channels, and hence all positive channels, are point identified if and only if

\[
\boxed{\operatorname{rank}(M)=k.}
\]

### Proof

Choose any compatible point `x_0` with `Mx_0=y`. Then

\[
Mx=y
\iff
M(x-x_0)=0.
\]

Therefore

\[
\mathcal C_y=x_0+\ker M.
\]

Translation does not change dimension, so

\[
\dim(\mathcal C_y)=\dim(\ker M).
\]

By rank-nullity for the linear map `M:R^k -> R^{m+1}`,

\[
\dim(\ker M)=k-\operatorname{rank}(M).
\]

The compatible set is a singleton exactly when its dimension is zero, equivalently when `rank(M)=k`. Exponentiation is one-to-one coordinatewise, so point identification of `x` is equivalent to point identification of `F`. ∎

## Theorem R2 — necessary and sufficient condition for one new scalar measurement to help

Let `M` be the current observation matrix and let a candidate scalar measurement have row `a^T`. Let

\[
M^+=\begin{bmatrix}M\\a^\top\end{bmatrix}.
\]

Then the candidate reduces the structural unidentified dimension if and only if

\[
\boxed{a\notin\operatorname{rowspan}(M).}
\]

For a scalar candidate, when it helps it reduces the residual dimension by exactly one.

### Proof

Appending one row changes row rank by either zero or one. It changes rank by zero exactly when the appended row lies in the current row span; otherwise it increases rank by one. By Theorem R1, residual dimension is `k-rank`. Therefore the residual dimension decreases iff `a` lies outside the current row span, and then it decreases by exactly one. ∎

## Corollary R2a — precision cannot repair a structurally invariant observation map

Any operation that changes only measurement precision while leaving the exact observation rows unchanged leaves `rowspan(M)` unchanged. Likewise:

- repeating an existing observation row;
- multiplying an existing row by a nonzero scalar;
- adding a reported variable that is an exact linear combination of existing rows;

cannot reduce structural unidentified dimension.

This is the precise sense in which more precise or more numerous observations can leave mechanism identification unchanged.

## Corollary R2b — the old `k-1-r` channel-anchor rule is a special case

Take the net row `1^T` and directly observe `r` distinct channel coordinates, with `0<=r<=k-1`. Their coordinate rows are `e_{i_1}^T,...,e_{i_r}^T`.

These `r+1` rows are linearly independent: if

\[
c_0\mathbf 1+\sum_{j=1}^rc_je_{i_j}=0,
\]

choose any unanchored coordinate, which exists because `r<=k-1`. Its component gives `c_0=0`; then each anchored coordinate gives `c_j=0`. Hence

\[
\operatorname{rank}(M)=r+1.
\]

Theorem R1 yields

\[
\boxed{\dim(\mathcal C_y)=k-1-r.}
\]

When `r=k-1`, rank is `k` and the final channel is recovered from the product.

Thus `k-1-r` is not an assumption or dimension-count definition: it follows from the general rank criterion plus independence of distinct coordinate anchors.

## Sharpness and minimal counterexamples

### Dependent candidate: one more measurement, zero identification gain

For `k=3`, suppose the current rows are

\[
(1,1,1),\qquad(1,0,0).
\]

The candidate row

\[
(2,1,1)=(1,1,1)+(1,0,0)
\]

is biologically a different reported quantity but lies in the current row span. Rank remains two and one unidentified direction remains.

### Independent candidate: one measurement closes the last dimension

With the same current rows, add `(0,1,0)`. This row is outside the current span, rank becomes three, and all three channels are point identified.

These two candidates have the same scalar output dimension. Their identification value differs only because one cuts a new equivalence direction.

## Design consequence

The correct design question is not

> how many additional measurements can be collected?

but

> which candidate observation rows are outside the span of the measurements already made?

For exact log-linear measurement architectures, the answer is complete:

\[
\boxed{\text{new identification information}\iff\text{rank gain}.}
\]

This theorem does not claim that every ecological observation is log-linear or that rank alone solves noisy nonlinear identification. It gives a necessary-and-sufficient design rule for the positive multiplicative/log-linear class already used by the paper, and it explains why biological detail or precision alone is not an identification axis.

## Executable obligations

`tests/test_observation_rank_theorem.py` must verify:

1. exact rank against an independent minor/determinant oracle on exhaustive small integer matrices;
2. residual dimension `k-rank(M)`;
3. point identification iff rank `k`;
4. duplicate/rescaled/linear-combination rows give zero rank gain;
5. outside-span rows give rank gain one;
6. the coordinate-anchor special case exactly recovers `k-1-r`;
7. sharp `k=3` dependent-versus-independent candidate witnesses.
