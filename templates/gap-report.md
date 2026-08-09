# Gap Report — <feature name>

> Produced by Loom Mode B (`workflows/audit-built-feature.md`). Every gap carries evidence — a
> `file:line` or a demonstrable absence. No evidence, no gap (Forge DNA §3.3).

| | |
|---|---|
| **Feature audited** | <name — one feature (F-001)> |
| **Stack profile** | <profile> |
| **Code surface read** | <files/dirs walked> |
| **Date** | <date> |

## The implied spec (what the code actually handles today)

<5–15 lines: the flows it implements, states it renders, lifecycle it handles, validations it enforces,
money hops it makes — reconstruction, not judgment>

## Gaps

| # | F-ID | Gap | Priority | Confidence | Evidence |
|---|------|-----|----------|------------|----------|
| 1 | F-0## | <what's missing, one line> | P0–P3 | CONFIRMED / LIKELY / HYPOTHESIS | `file:line` or <the absence> |

Sort P0 first. **P0** = loses money/data or strands users (unguarded commit race, undefined delete
cascade, unhandled payment failure). **CONFIRMED** = the cited code shows it. **LIKELY** = implied by
what's absent. **HYPOTHESIS** = can't tell from code — answer below.

## Questions for you (the HYPOTHESIS items)

1. <question — what the code can't reveal>

## Suppressed dimensions (not gaps on this stack)

- <range> — <profile's stated reason>

## Parked & Routed (F-161)

| Finding | Owner | Lane | Status |
|---------|-------|------|--------|
| <e.g. exploitable admin action> | Bastion | B-SEC | parked / dispatched → resolved |

---

*Honesty line: This report lists **completeness gaps with evidence**. CONFIRMED gaps are visible at the
citations; HYPOTHESIS items need your answers. It is not a security verdict (Bastion), a test plan
(Anvil), or a refactor plan (Cairn/Lens). Fixing is a separate decision — yours.*
