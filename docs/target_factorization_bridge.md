# Target factorization: the Boundary -> MROD identification/design contract

Status: internal cross-paper theory and executable contract. The active Boundary
Perspective and MROD manuscript, public objectives and frozen results are unchanged.
This is an application of standard factorization and information identities, not
an invention of identifiability, the Doob-Dynkin lemma or goal-oriented design.

## 1. Domain, question and observation must be declared separately

Let D be a nonempty declared feasible-world domain, O:D->Y the current exact
observation map, and T:D->V the target asked about. For a question-relative
mechanism target, T=tau(S); a general ecological target may also depend on other
world coordinates. Fix T before inspecting candidate outcomes, and use the same
T across candidates. Candidate rationale metadata does not define T.

For an attainable y, let C_y={w in D:O(w)=y}. Local target identification means
|T(C_y)|=1. It neither requires C_y to contain one world nor implies identification
at other observation values. A finite enumerated domain is not automatically an
exhaustive description of a biological system.

## 2. Factorization theorem (global, exact, set-theoretic)

The following are equivalent:

1. For every y in O(D), |T(C_y)|=1.
2. For every w,w' in D, O(w)=O(w') implies T(w)=T(w').
3. There exists g:O(D)->V such that T=g composed with O on D.

Proof: (1) and (2) say the same thing within each fibre. Under (2), define g(y)
as the unique target value of any world in C_y; constancy makes this well-defined.
Then g(O(w))=T(w). Conversely a factorization gives equal targets at equal O.
The reconstruction map is unique on O(D); no claim is made off that image.

Local identification at the actually observed y only defines g at that y.
It must not be promoted to a global factorization. This elementary finite/set
statement is distinct from measurable or almost-sure factorization results,
which require their own hypotheses [1].

The internal `boundary_model/target_factorization.py` reuses `identify_target`
to return each fibre's target image. When factorization fails, it retains two
world indices with the same O but different T. When it holds, it constructs g.
It refuses empty domains, missing labels and non-finite numeric labels rather
than treating them as evidence of identification.

## 3. Exactly what an added observation must separate

For a deterministic candidate Q, replace O by (O,Q). The target is identified
throughout the refined observation image if and only if

```text
O(w)=O(w') and T(w)!=T(w')  =>  Q(w)!=Q(w')
```

for every pair of feasible worlds. Apply the same statement on C_y for the
current-data problem. This is a complete-repair criterion, not a criterion for
any positive information gain. Separating only some disagreeing pairs may help
without identifying the target after every possible result.

A new observation can split worlds that already share T. That adds full-world
information without resolving the question contrast. Conversely a target can
already be identified while substantial within-target mechanism detail remains.

## 4. Entropy bridge: the full-support qualifier is essential

For a finite D and a distribution mu with mu(w)>0 for every w in D, discrete
Shannon entropy gives

```text
T factors through O on D  <=>  H_mu(T|O)=0.
```

Proof: H_mu(T|O) is a nonnegative weighted sum of entropies on fibres. Every
attainable fibre and every declared world has positive mass. The sum is zero
exactly when each fibre's target distribution has singleton support.

Without full support, zero entropy implies only an almost-sure statement on the
weighted support. Example: two compatible worlds have O=0 and T=0,1, but weights
1,0. The weighted entropy is zero while the structural target image is {0,1}.
Omitting the second world from a simulation pool creates the same false upgrade.
Low probability, numerical rounding and finite-pool absence are not structural
exclusion. These identities use discrete entropy, not differential entropy.

On a current finite C_y with strictly positive weights and a verified candidate
partition, MROD's existing target layer satisfies

```text
I_mu(T;Q|C_y) = H_mu(T|C_y) - E_q[H_mu(T|C_y,Q=q)].
```

Consequently complete repair of all current-data branches is equivalent to
I_mu(T;Q|C_y)=H_mu(T|C_y), not merely I_mu(T;Q|C_y)>0. If H_mu(T|C_y)=0,
every candidate has zero additional target information, although some can still
inform S. The converse using only registered candidate values is false: all
registered candidates may miss an unresolved target distinction.

## 5. Current-data processing versus new measurement

If a reported statistic is h(O), its fibre contains the original O-fibre.
Postprocessing cannot distinguish a pair already identical under retained O.
Keeping the full record or recovering previously discarded raw variables is a
change of the retained observation map, not a magical property of a new estimator.
A new independent noisy replicate is not in general a deterministic h(O).

For noisy statistical models, the structural observation map may instead be
w -> P_w(Y), the observable sampling law. Equality of one realised data vector
is not equality of sampling laws. Do not use this finite deterministic audit to
claim that repeated sampling never helps. Likewise a tolerance-thickened accepted
region is not an exact O-fibre; resolving its finite sample is conditional on the
specified approximation and support.

## 6. One shared executable contract, separate implementations

Both repositories retain the byte-identical fixture
`tests/fixtures/target_factorization_v1.json`, contract
`boundary-mrod-target-factorization-v1`, with SHA-256:

```text
d12478f3354170130a8ed11e0c019a0099f5dc942d4365195770619ae3f14841
```

Boundary tests construct g or a conflicting pair. MROD tests use its existing
`target_observation_information_value` and actual outcome filtering, then compare
zero residual entropy with an independent pair-separation oracle. Neither repo
imports the other or requires network access during tests. The fixture is a
controlled mathematical witness, not empirical ecological data.

Cases include an already resolved question with two remaining mechanism bits;
a target-irrelevant deep assay; local but not global identification; the zero-mass
counterexample; and a three-target case where partial measurement gains
0.918295834 bits but leaves 2/3 bit unresolved. Boundary additionally enumerates
all 4,096 triples of binary O,T,Q maps on four labelled worlds.

The MROD adapter is documented in
https://github.com/zuizui0223/mrod/blob/main/docs/target_factorization_bridge.md .

## 7. Reporting and ownership

Report the declared target, compatible target image, scope of identification,
remaining conflicting worlds, candidate predictive coverage, expected target
information, and unresolved post-observation branches. Never replace these by a
single claim that the entire mechanism has been established.

Boundary owns the structural certificate. MROD owns conditional candidate values
and next-observation comparison. Incomplete candidate predictions remain
prediction-limited; positive singleton information does not establish a globally
optimal sequence; zero singleton information does not rule out joint synergy.
The existing stopping-depth contract still applies.

Identifying a process contrast does not automatically establish historical
adaptation, a fitness effect, a molecular pathway or an intervention effect.
Those can be separate targets requiring additional assumptions and evidence.
No normative permission to publish or act follows merely from factorization.

## 8. Prior art and claim ceiling

[1] Taraldsen, G. (2018). *Optimal Learning from the Doob-Dynkin lemma*.
https://arxiv.org/abs/1801.00974 . This provides measurable-factorization context;
the elementary proof above is stated separately to avoid importing unstated
measurability or almost-sure assumptions.

[2] Attia, A., Alexanderian, A. & Saibaba, A.K. (2018). *Goal-Oriented Optimal
Design of Experiments for Large-Scale Bayesian Linear Inverse Problems*.
https://arxiv.org/abs/1802.06517 . Targeted experimental design is prior art.

[3] Chakraborty, A., Huan, X. & Catanach, T. (2024). *A Likelihood-Free Approach
to Goal-Oriented Bayesian Optimal Experimental Design*.
https://arxiv.org/abs/2408.09582 . Likelihood-free goal-oriented information design
using ABC also predates this audit. Neither targeting T nor using a simulation
pool is claimed as a new method here.

The repository contribution is the explicit, tested identification-to-design
interface, including support and scope guards, not a new general theorem or
optimization algorithm.
