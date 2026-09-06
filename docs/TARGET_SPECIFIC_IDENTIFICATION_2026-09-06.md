# Target-specific identification over an observational equivalence class

`boundary` asks what the current observation map can identify in principle. The repository already separates unique mechanism identification from other valid estimands. This extension makes one useful consequence executable:

> Multiple mechanisms may remain observationally equivalent while a narrower target is already point-identified.

## 1. Compatible worlds first

Let the current observation map leave a non-empty compatible set

```text
E_y = {w_1,...,w_m}.
```

For a declared target map

```text
T: w -> target value,
```

define its image over the equivalence class

```text
T(E_y) = {T(w): w in E_y}.
```

Then

```text
|T(E_y)| = 1
-> target is point-identified under the current compatible set

|T(E_y)| > 1
-> target remains set-valued / unresolved.
```

This does **not** require `|E_y|=1`.

## 2. Structural identification is not downstream licensing

The implementation deliberately reports

```text
point_identified = True/False
```

rather than `licensed=True/False`.

That preserves repository ownership:

```text
boundary
-> structural compatible set and target image

CED / theouni / downstream reporting contract
-> whether an identified target is reportable or actionable.
```

So this module does not turn structural identification into a normative permission system.

## 3. Implementation

- `boundary_model/target_identification.py`
- `tests/test_target_identification.py`

The main API is

```python
result = identify_target(compatible_worlds, target)
```

with outputs

```text
compatible_world_count
target_values
point_identified
unresolved
identified_value  # only when singleton
```

## 4. Scientific use

This gives `boundary` a precise answer to a recurring ambiguity:

```text
mechanism not uniquely identified
!=
every target is unidentified.
```

For example, several mechanisms can disagree internally while all imply the same sign of a declared ecological contrast. The mechanism identity remains unresolved, but that sign is structurally point-identified relative to the declared compatible family.

Conversely, excellent model fit does not identify a target if compatible mechanisms map to different target values.

## 5. Tests

```bash
pytest -q tests/test_target_identification.py
```

The tests include the key witness in which three distinct mechanisms remain compatible but all map to the same target value.
