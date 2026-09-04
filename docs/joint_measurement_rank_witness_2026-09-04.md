# Joint-measurement rank witness — pollination-style three-channel design

Status: exact synthetic design witness under the manuscript's declared positive multiplicative/log-linear class. This is **not** a natural-data validation.

## Question

The observation-rank theorem says that a new measurement helps structural identification if and only if its observation row lies outside the current row span. The remaining presentation risk is that this sounds like rank-nullity detached from field design.

The pollination motivation gives a concrete joint-measurement question:

> Can a study accumulate several biologically meaningful quantities about visitation and reproduction and still gain **zero** mechanism-identification dimension until per-visit effectiveness is measured directly?

## Declared three-channel chain

Let

- `V > 0` = interaction quantity / visitation;
- `E > 0` = per-visit effectiveness;
- `D > 0` = downstream reproductive dependency / conversion;
- `W = V E D` = endpoint reproductive output attributable to the declared chain.

In log coordinates

`x = (log V, log E, log D)`.

The endpoint observation is row

`w = (1,1,1)`.

A direct visitation measurement is

`v = (1,0,0)`.

A commonly reported derived contrast such as endpoint output normalized by visitation,

`W/V = E D`,

has row

`n = (0,1,1) = w - v`.

This quantity is biologically interpretable, but if it is computed from the already observed endpoint and visitation records, it is **not a new independent measurement direction**.

## Panel A — a data-richer record with no rank gain

Take

```
M_A = [
  [1,1,1],   # endpoint W
  [1,0,0],   # visitation V
  [0,1,1],   # derived W/V
]
```

Because the third row equals the first minus the second,

`rank(M_A)=2`.

For `k=3`, the residual structural dimension is therefore

`3 - rank(M_A) = 1`.

Adding exact repeats of visitation, a rescaled visitation index, or additional derived quantities formed from these same rows leaves the row span unchanged. The record can become longer and numerically more precise while the `E` versus `D` allocation remains structurally unresolved.

The remaining null direction can be written explicitly as

`h=(0,1,-1)`.

For any real `t`,

`x(t)=x_0+t h`

changes effectiveness and dependency in opposite directions while preserving every row of `M_A`. Thus two genuinely different mechanism allocations generate the same declared data-rich record.

## Panel B — one targeted effectiveness measurement closes the chain

Now measure per-visit effectiveness directly:

`e = (0,1,0)`.

The augmented matrix is

```
M_B = [
  [1,1,1],
  [1,0,0],
  [0,1,1],
  [0,1,0],
]
```

and

`rank(M_B)=3`.

The residual dimension becomes zero. `V` is measured directly, `E` is measured directly, and `D` is recovered from the endpoint product.

The identification change is therefore

```
more rows within old span:  rank 2 -> 2, residual dim 1 -> 1
one targeted E anchor:      rank 2 -> 3, residual dim 1 -> 0
```

## Numerical mechanism pair

Choose one compatible baseline mechanism

`(V,E,D)=(10,0.4,0.5)`

so that

`W=2` and `W/V=0.2`.

A different mechanism allocation

`(V,E,D)=(10,0.2,1.0)`

has the same endpoint and normalized endpoint:

- `W=10*0.4*0.5=2` and `10*0.2*1.0=2`;
- `W/V=0.2` in both cases;
- visitation is `10` in both cases.

Thus the pre-effectiveness record cannot distinguish the two mechanisms.

Once `E` is measured, the two worlds separate immediately (`0.4` versus `0.2`), and `D` follows from `D=W/(VE)`.

This is the concrete contradiction witness behind the rank statement: a claim that the original data-rich record identifies the effectiveness/dependency mechanism would assign different latent decompositions to two worlds that are identical under every declared observation.

## What this witness does and does not show

It shows, exactly and numerically, that:

1. biologically meaningful derived variables can add **zero** structural rank;
2. repeated/precise measurement along an existing observation span does not remove the remaining mechanism direction;
3. a single targeted channel measurement outside that span can close the last unidentified dimension;
4. `not evaluable` is the appropriate mechanism-level output before that discriminating measurement is available.

It does **not** show that real pollination systems obey this three-factor chain exactly, that `E` is always the best field measurement, or that visitor identity/community data are unimportant. The witness is a design translation of the exact theorem for studies that declare this quantity-by-quality-by-dependency architecture.

## Executable obligations

`tests/test_joint_measurement_rank_witness.py` must verify:

- exact ranks `2` and `3` for Panels A/B;
- explicit null direction `h=(0,1,-1)` for Panel A;
- duplicate/rescaled/derived rows leave rank unchanged;
- direct effectiveness row closes the residual dimension;
- the two numerical mechanism allocations produce identical pre-anchor observations and different effectiveness values;
- downstream dependency is uniquely reconstructed after the effectiveness anchor.
