# Mode B — Audit a Built Feature

> The "وش غلطت؟" mode — *what did I miss?* For a feature that already exists in code: reconstruct what
> it *actually* handles, diff that against what the catalogue says a complete version handles, and
> deliver the gaps as a prioritized, confidence-labeled report. This is the mode born from shipping the
> feature's essence and getting burned by its details.

## Steps

### 1. Step 0 discovery

Identify the feature under audit (one feature — F-001 applies to audits too), detect the stack, load
the profile. Locate the feature's code surface: screens/widgets, handlers/functions, rules, schema
touchpoints. **Read before judging** — the audit's credibility is that every claim points at code.

```
[███░░░░░░░░░░░░░░░░░] 15% — Step 1/5: Feature scoped, code located
```

### 2. Reconstruct the implied spec

From the code, write what the feature *actually* does today: the flows it implements, the states it
renders, the lifecycle it handles, the validations it enforces, the money hops it makes. This is the
**implied spec** — the fabric as actually woven, holes and all. No judgment yet; reconstruction only.

```
[███████░░░░░░░░░░░░░] 35% — Step 2/5: Implied spec reconstructed from code
```

### 3. Diff against the catalogue

Walk every dimension range the profile APPLIES and compare: what does a complete weave specify that the
implied spec lacks? Each miss becomes a **gap** with:

- its **F-###**,
- a **priority** — P0 (loses money/data: unguarded commit race, undefined delete cascade, unhandled
  payment failure) → P3 (polish),
- a **confidence label** — **CONFIRMED** (the code shows the hole: `file:line`), **LIKELY** (implied by
  what's absent), **HYPOTHESIS** (can't tell from code — a question for the user),
- the **evidence** — the file/line or the absence that proves it. No evidence, no gap (Forge DNA §3.3).

Suppressed dimensions are listed with their reason — an audit that dings a CLI for missing i18n is the
false alarm the Law bans.

```
[████████████░░░░░░░░] 60% — Step 3/5: Gaps identified with evidence
```

### 4. Route what isn't completeness

A gap that's really a vulnerability (the hole is *exploitable*, not just unspecced) → enumerate under
F-090s and route to **Bastion** for severity — never rate it here. A structural cause → **Cairn**. A
missing test for existing correct behavior → **Anvil**. Style noise noticed on the way → **Lens**, or
silence. Everything routed lands in the Parked & Routed table (F-161); blocking items may dispatch per
`reference/handoff-protocol.md`.

```
[████████████████░░░░] 80% — Step 4/5: Findings routed to their owners
```

### 5. Deliver the gap report, stop

Fill `templates/gap-report.md`: implied-spec summary → gap table (sorted P0 first) → HYPOTHESIS
questions for the user → Parked & Routed → the honesty line:

> *This report lists completeness gaps with evidence. CONFIRMED gaps are visible in the code cited;
> HYPOTHESIS items need your answer. It is not a security verdict (Bastion), a test plan (Anvil), or a
> refactor plan (Cairn/Lens). Fixing is a separate decision — yours.*

Declare the audit done. **Stop** (F-162) — the report does not volunteer to fix the gaps, spec the
missing pieces, or audit a second feature. Each of those is a new run the user may choose.

```
[████████████████████] 100% — Step 5/5: Gap report delivered — audit closed
```
