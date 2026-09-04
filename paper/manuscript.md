# Mechanistic evidence needs an identification axis: measurement boundaries in ecological chains

## Abstract

Ecological research uses *mechanistic* for several legitimate forms of evidence, including measurements close to biological machinery and observations that discriminate among competing process explanations. We argue that biological proximity and mechanism identification are different properties. A proximal measurement can remain compatible with several competing mechanisms, whereas a simple field observation can be strongly discriminating when it excludes alternatives. We make this distinction exact for recurring multiplicative ecological measurements. For `W=prod_j F_j`, net-only observations leave a `k-1` dimensional product-preserving equivalence class; `r` independent channel anchors leave `k-1-r` unresolved dimensions. In the common proxy case `W_i=F_iE_i`, `X_i=q_iF_i`, stable, bounded and unrestricted proxy transport form one family under `1/Gamma <= q_1/q_0 <= Gamma`. Finite `Gamma` yields a sharp joint identified set and a reference-invariant breakdown factor, while direct calibration creates a separate 0/1/2 anchor ladder. The resulting principle is that biological proximity and identification strength should be treated as distinct dimensions of mechanistic evidence.

## 1. Introduction

Ecologists seek mechanisms, not only patterns. Yet *mechanistic* has several legitimate uses across process-based ecology, causal-mechanistic explanation, and causal inference (Smith et al. 2020; Grace et al. 2025; Siegel & Dee 2025; Correia et al. 2025). Measurements taken close to biological machinery—physiology, gene expression, genomic variation or molecular interactions—are naturally described as mechanistically proximal. Ecological genomics, for example, has explicitly been motivated by identifying genetic mechanisms underlying organismal responses to natural environments, and genomic data can deepen mechanistic understanding of ecological and eco-evolutionary change (Ungerer et al. 2008; Rudman et al. 2018). This aspiration is compatible with a second question: does a measurement actually distinguish the mechanisms relevant to the inference?

The distinction matters whenever several mechanisms can generate the same observation. A molecular profile may be biologically close to the relevant machinery yet remain compatible with multiple upstream explanations. Conversely, a field-level measurement can be strong mechanistic evidence if explicit competing mechanisms make different predictions for it. We therefore propose two distinct dimensions for ecological evidence: **biological measurement level or proximity**, and **identification strength**—non-identifying, partially identifying or point-identifying relative to declared competing mechanisms (Figure 1). No monotone relation between these dimensions is assumed.

> **Mechanistic evidence should be evaluated by what it identifies, not by biological measurement level alone.**

This principle does not imply that molecular scale is irrelevant, that genomics is non-mechanistic, or that all field observations are equally informative. Molecular and genomic measurements can provide causal perturbations, physical constraints and close access to biological machinery. The narrower claim is that none of these properties alone guarantees identification among the particular competing mechanisms under study. Likewise, field observations need not remain merely descriptive when their observation map separates explicit alternatives.

We formalise this distinction using a recurring ecological measurement architecture in which several positive biological stages combine multiplicatively. Pollination provides a concrete example. At visitor type `m`, effective contribution can be written as `S_m = V_m E_m`, where `V_m` is interaction quantity, such as visitation rate, and `E_m` is per-interaction effectiveness. Community service then aggregates those contributions as `S=sum_m V_mE_m`. Pollination studies explicitly distinguish visitation or quantity from per-visit effectiveness, and combine them when estimating pollinator importance or service (Rader et al. 2012; Reynolds & Fenster 2008; Ballantyne et al. 2017). Network degree, visitor abundance or visitation alone may therefore describe or proxy the quantity side of this architecture, but they are not effective service unless the effectiveness term is fixed or otherwise known. Seed dispersal supplies an independent quantity-by-quality architecture in which effectiveness is likewise defined by the product of quantity and quality (Schupp et al. 2010).

The same logic appears in longer ecological measurement chains. A study may wish to connect change in a visitor community to effective service, dependency or reproductive assurance, and finally a demographic or trait response. Observing only an endpoint does not, by itself, identify which unobserved intermediate stage changed. If a declared endpoint factorises as a product of positive stages, the number of unresolved stages has a precise structural meaning.

This is also a practical **joint-measurement bottleneck**, not only an algebraic one. A data-rich field system may resolve plant state, visitor identity, community composition and realised interaction structure yet still fail to identify the mechanism linking community change to reproduction if per-visit effectiveness and reproductive dependency are not measured on the same inferential chain. Visitor identity is not effective service; effective service is not reproductive dependency; and an endpoint reproductive contrast does not reveal which missing link changed. More generally, causal mediation and mechanism-oriented ecological designs require measurements of the intermediary quantities that distinguish the process claims being made (Correia et al. 2025; Grace et al. 2025). When the measurements required to distinguish the declared alternatives are absent, the appropriate result is **not evaluable**, rather than a post-hoc assignment of mechanism from a nearby proxy. This field-design problem motivates the formal question developed below: which direct channel measurements would convert a biologically rich but mechanism-ambiguous chain into partial or point identification?

A second problem appears when one stage is observed only through a proxy. Relative comparisons are commonly used to avoid unknown absolute calibration. If the proxy is `X_i=q_iF_i`, an unknown constant scale indeed cancels when `q_1=q_0`. But the scientifically relevant question is whether calibration transports across the regimes being compared.

We develop three linked quantitative results. First, net-only observations define an equivalence class rather than a unique mechanism decomposition. For a `k`-channel product this class has `k-1` free dimensions; each independent direct channel anchor removes one (Figure 2). Second, in the common two-channel proxy case, stable, bounded and unrestricted proxy transport form one calibration family that yields point identification, sharp partial identification and non-identification as limiting cases, together with a reference-invariant breakdown factor (Figure 3). Third, these boundaries generate operational rules: distinguish channel anchors from calibration anchors, match direct measurement effort to desired identification strength, and report calibration-induced uncertainty as a coupled joint set rather than independent marginal error bars.

The argument belongs to established traditions of structural identifiability, parametric identification, and partial identification (Bellman & Åström 1970; Rothenberg 1971; Manski 2003). We do not claim new identifiability algebra. The contribution is ecological and evidentiary: to add an explicit identification dimension to mechanistic evidence, make that distinction exact for a recurring ecological observation class, and carry the resulting information boundaries through sensitivity analysis to field-design and reporting consequences.

## 2. Observation models

### 2.1 Positive multiplicative chains

Let a declared ecological output be

```text
W(z) = prod_{j=1}^k F_j(z),    F_j(z)>0.
```

The factorisation must be biologically justified for the chosen output, domain and census interval. The theory does not assert that every ecological response is multiplicative. It asks what follows when investigators already use a multiplicative measurement architecture.

A net-only observation is any deterministic functional `O=Phi(W)`. This includes the full response curve, threshold-feasible sets, and any geometry or topology derived solely from them.

### 2.2 Two-channel proxy comparisons

For regimes `i in {0,1}`, let

```text
W_i = F_i E_i,
X_i = q_i F_i,
```

with positive channels and positive proxy conversion. Define

```text
rho_W=W_1/W_0,
rho_X=X_1/X_0,
rho_F=F_1/F_0,
rho_E=E_1/E_0,
kappa=q_1/q_0.
```

Then

```text
rho_X=kappa rho_F,
rho_W=rho_F rho_E,
rho_F=rho_X/kappa,
rho_E=(rho_W/rho_X)kappa.
```

Write `rho_E_hat=rho_W/rho_X` for the value obtained under stable calibration `kappa=1`.

## 3. Net-only observations define a quotient, not a mechanism

### Theorem N1 — two-channel net-only invariance

For any positive function `c(z)`, the transformation

```text
(F,E) -> (cF,E/c)
```

leaves `W=FE` unchanged. Every deterministic net-only observation `Phi(W)` is therefore invariant under that transformation. Complete performance curves, threshold-feasible sets and all geometry derived from them can describe the net ecological pattern arbitrarily well while containing no data-based information about how the product is allocated between latent channels.

The important point is not merely that products have many factorizations. It is that improving precision or dimensionality of an observation does not improve identification when the observation map remains invariant along the same mechanism-equivalence orbit.

### Theorem N1-k — a `k`-channel chain leaves `k-1` unresolved dimensions

For

```text
W = prod_{j=1}^k F_j,
```

let positive multipliers satisfy `prod_j c_j=1`. The transformation `F_j -> c_jF_j` leaves `W` unchanged. In log coordinates, product-preserving perturbations satisfy `sum_j d_j=0`, a `(k-1)`-dimensional subspace. Hence endpoint-only observation leaves a `(k-1)`-dimensional mechanism-equivalence class.

If `r` independent channel values—or in a before/after analysis, `r` independent channel ratios—are directly observed, each anchor fixes one independent coordinate. The residual unidentified dimension is

```text
k - 1 - r,    0 <= r <= k-1.
```

When `r=k-1`, the final channel is recovered from the product. Thus a four-stage chain observed only at its endpoint has three unresolved structural dimensions; one independent anchor leaves two, two leave one, and three point-identify the final stage.

**Channel-anchor rule.** For a declared positive `k`-stage product, `k-1` independent channel anchors are sufficient for point identification of all stages.

## 4. Calibration transport is one identification family

Let between-regime calibration satisfy the multiplicatively symmetric restriction

```text
1/Gamma <= kappa <= Gamma,    Gamma>=1.
```

Equivalently, `|log kappa|<=eta` with `eta=log Gamma`.

### Theorem T1 — calibration-transport family

Conditional on positive observed `rho_W` and `rho_X`, the sharp joint identified set is

```text
J_Gamma={(rho_X/kappa, rho_E_hat*kappa):
         1/Gamma <= kappa <= Gamma}.
```

Its marginal projections are

```text
rho_F in [rho_X/Gamma, rho_X*Gamma],
rho_E in [rho_E_hat/Gamma, rho_E_hat*Gamma].
```

Every admissible pair satisfies `rho_F rho_E=rho_W`. The set is sharp because every admissible `kappa` can be realised by choosing a positive baseline conversion, setting the second-regime conversion to `kappa` times that baseline, and reconstructing the latent channels exactly.

The familiar cases are one family:

```text
Gamma=1          -> point identification under stable calibration
1<Gamma<infinity -> sharp partial identification
Gamma->infinity  -> unrestricted transport and non-identification
```

## 5. Preserve the joint geometry

The same `kappa` generates both channel ratios. The identified object is one-dimensional, not the Cartesian product of the two marginal intervals. In log-ratio coordinates,

```text
log rho_F + log rho_E = log rho_W,
```

so `J_Gamma` is a line segment of slope `-1`.

**Design Rule 2 — Preserve the coupling.** Calibration-drift uncertainty for the two channels must not be reported as independently combinable intervals. The primary uncertainty object is the joint identified set. Marginal intervals are projections only. Sampling uncertainty is a separate layer that can be propagated around the structural set.

## 6. Breakdown factors expose assumption dependence

A finite `Gamma` is not identified from the same `W` and `X` observations whose identifying power is being assessed. Bounded-transport analysis therefore does not establish that a particular tolerance is true. It exposes exactly how the ecological conclusion depends on a declared transport assumption.

For a stable-calibration channel ratio `rho_hat`, the smallest symmetric multiplicative calibration distortion that reaches no change is

```text
Gamma*=max(rho_hat,1/rho_hat),
eta*=|log rho_hat|.
```

These measures are invariant to reversing the reference regime. For `rho_hat=1/1.34`, `Gamma*=1.34`. In the upward direction this corresponds to 34% calibration-ratio drift. The strict directional conclusion holds below the boundary, not at equality.

The breakdown factor reverses the burden of specification. Rather than asserting one uniquely correct `Gamma`, the analyst reports the smallest calibration distortion sufficient to overturn the conclusion and lets readers compare that threshold with calibration experiments, validation data, instrument knowledge or biological constraints.

## 7. Two anchor ladders answer different design questions

The word *anchor* refers to two distinct measurements and they should not be conflated.

**Channel anchors** directly observe latent stages in a `k`-stage product. `r` independent channel anchors leave `k-1-r` unresolved dimensions.

**Calibration anchors** measure proxy conversion within regimes. With zero direct calibration anchors, unrestricted transport gives non-identification. With one anchor, local conversion is known but cross-regime transport still requires an external finite `Gamma`. With two anchors, both `q_0` and `q_1` are observed, so `kappa=q_1/q_0` is measured and the transport sensitivity assumption is removed for that comparison.

**Design Rule 1 — Measure the missing identification information.** Use channel anchors to reduce unresolved mechanism dimensions and calibration anchors to replace transport assumptions with direct measurement.

## 8. Why the architecture is ecologically relevant

Seed dispersal effectiveness is explicitly decomposed as quantity times quality (Schupp et al. 2010). Pollination studies independently combine visitation frequency or rate with per-visit effectiveness (Rader et al. 2012; Reynolds & Fenster 2008; Ballantyne et al. 2017). These studies do not imply identical semantics across systems. They establish the narrower point needed here: rate-by-effectiveness and quantity-by-quality products are recurring ecological measurement architectures.

The pollinator-service example also distinguishes product and aggregation. The theorem applies directly to each contribution `V_mE_m`. If only the aggregate `sum_m V_mE_m` is observed, attribution among visitor types adds further ambiguity. Treating network degree or abundance as service can therefore collapse both within-type effectiveness and across-type allocation.

## 9. Relation to mechanistic ecology and identification theory

Ecology already contains multiple traditions of mechanistic explanation. Mechanistic models encode processes explicitly; molecular and genomic studies may measure components close to biological machinery; causal-mechanistic investigations assemble evidence about structures and processes linking causes to responses (Smith et al. 2020; Grace et al. 2025; Siegel & Dee 2025; Correia et al. 2025). Our distinction is complementary: **given a declared set of competing mechanisms, does the observation map distinguish them?**

This question cannot be answered from biological level alone. A genomic observation can be highly informative when alternatives predict different genomic states, but non-identifying when the same state is downstream of several alternatives (Ungerer et al. 2008; Rudman et al. 2018). A field observation can be weak when it records only an invariant endpoint, but strongly identifying when it anchors a missing channel.

Structural identifiability and parametric identification are classical problems of whether model structure or parameters are uniquely recoverable from observable behaviour (Bellman & Åström 1970; Rothenberg 1971), while partial identification explicitly treats cases in which the data and assumptions determine a set rather than a point (Manski 2003). The algebra used here is elementary relative to those traditions. The contribution has three quantitative parts: a net-only ecological observation class whose `k`-channel equivalence dimension is quantified; a calibration-transport family that supplies a sharp joint set and reference-invariant breakdown factor; and operational consequences connecting direct measurements to identification strength while preserving exact dependence when uncertainty is reported.

The results assume positive multiplicative stages where a product map is declared. Zeros require separate treatment. Sum-of-products architectures, additive interactions and other nonlinear maps can create additional equivalence structures and require their own observation maps. Transport bounds must be externally informed or explicitly treated as sensitivity parameters rather than chosen after seeing a desired conclusion.

## 10. Discussion

The main distinction is not between field data and molecular data. It is between **where an observation sits in a biological chain** and **what that observation identifies among competing mechanisms**. These properties can be related, but they are not the same dimension.

The product theorems make this point exact in one recurring ecological architecture. Endpoint-only observation of a positive `k`-stage product leaves `k-1` structural degrees of freedom, and measuring the endpoint more precisely does not change that dimension. Each independent direct channel measurement removes one. The investigator must change the observation map, impose scientifically defended restrictions, or report the remaining equivalence set.

Relative proxy comparisons add a different identification problem. They are protected not by taking ratios alone but by transport of the proxy-to-channel conversion. Once that hidden assumption is written as `kappa=q_1/q_0`, stable calibration, bounded uncertainty and unrestricted drift become one identification family.

The resulting workflow is: declare the competing mechanisms and observation map; ask which distinctions that map preserves; classify the current evidence by identification strength rather than measurement level alone; count unresolved dimensions or transport parameters; acquire channel or calibration anchors according to the inference required; and report the corresponding sharp set or point estimate while preserving the identified dependence structure.

## Figure captions

**Figure 1. Biological proximity and identification strength are distinct dimensions of mechanistic evidence.** Illustrative placements include a distal net pattern that is non-identifying, a field measurement that directly anchors a missing channel, a proximal molecular signature shared by several mechanisms, and a proximal intervention that separates alternatives. Positions are conditional on the candidate mechanism set and observation map.

**Figure 2. Direct channel measurements reduce the unresolved dimension of a positive multiplicative chain.** Endpoint-only observation leaves `k-1` dimensions; `r` independent channel anchors leave `k-1-r`; `k-1` anchors point-identify the final stage from the product.

**Figure 3. Calibration transport determines identification strength in the two-channel proxy case.** `Gamma=1` gives point identification; finite `Gamma` gives a sharp one-dimensional joint set; removing the finite bound recovers non-identification. In log-ratio coordinates the joint set has slope `-1`. The worked breakdown is `Gamma*=1.34`.

## References

- Ballantyne, G. et al. 2017. Pollinator importance networks illustrate the crucial value of bees in a highly speciose plant community. *Scientific Reports* 7:8383.
- Bellman, R. & Åström, K.J. 1970. On structural identifiability. *Mathematical Biosciences* 7:329–339.
- Correia, H.E., Dee, L.E. & Ferraro, P.J. 2025. Designing causal mediation analyses to quantify intermediary processes in ecology. *Biological Reviews* 100:1512–1533.
- Grace, J.B. et al. 2025. Causal effects versus causal mechanisms: two traditions with different requirements and contributions towards causal understanding. *Ecology Letters* 28:e70029.
- Manski, C.F. 2003. *Partial Identification of Probability Distributions*. Springer.
- Rader, R. et al. 2012. Spatial and temporal variation in pollinator effectiveness. *Journal of Applied Ecology*.
- Reynolds, R.J. & Fenster, C.B. 2008. Point and interval estimation of pollinator importance. *Oecologia* 156:325–332.
- Rothenberg, T.J. 1971. Identification in parametric models. *Econometrica* 39:577–591.
- Rudman, S.M. et al. 2018. What genomic data can reveal about eco-evolutionary dynamics. *Nature Ecology & Evolution* 2:9–15.
- Schupp, E.W., Jordano, P. & Gómez, J.M. 2010. Seed dispersal effectiveness revisited. *New Phytologist* 188:333–353.
- Siegel, K. & Dee, L.E. 2025. Foundations and future directions for causal inference in ecological research. *Ecology Letters* 28:e70053.
- Smith, J.A. et al. 2020. Zooming in on mechanistic predator–prey ecology. *Journal of Animal Ecology* 89:1997–2012.
- Ungerer, M.C., Johnson, L.C. & Herman, M.A. 2008. Ecological genomics. *Heredity* 100:178–183.
