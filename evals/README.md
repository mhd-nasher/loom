# Loom Evals — Skill-TDD (RED · GREEN · REFACTOR)

Loom's promise is double-edged, so its evals guard both edges. **The miss** — the forgotten detail that
burns in production (an unguarded commit race, an undefined delete cascade, an unhandled payment
failure) — is why the skill exists; if Loom stops catching those, it is decoration. **The invented
requirement and the tangent** — demanding i18n from a weekend script, refactoring code mid-spec,
selling more work after declaring done — are how completeness tools become noise machines users turn
off; the One-Weave Law is only real if evals can fail it. A Loom that catches everything but never cuts,
or cuts everything but never catches, is broken in a way only both eval directions reveal.

## Files

- **`trigger-eval.json`** — 28 queries (19 should-trigger, 9 should-not). The should-nots include
  sibling-boundary asks — "review my architecture" (Cairn), "write tests" (Anvil), "find
  vulnerabilities" (Bastion), "set up CI/CD" (Relay), "clean this function" (Lens) — because
  over-triggering into a sibling's lane is a boundary bug, not a reach. Arabic queries are first-class:
  Loom's users ask «وش نسيت في الميزة؟» as often as "what am I forgetting".
- **`evals.json`** — 10 behavior cases: 5 `must_find` (the catch classes: races, lifecycle, contract,
  notifications, concurrency), 2 `must_not` (the ceremony refusal and the tangent refusal), 3
  `boundary` (structure → Cairn, severity → Bastion, tests → Anvil — including the sealed-brief return
  contract).
- **`README.md`** — this file.

## The loop

1. **RED** — Run the eval prompt against a session *without* the guidance you're about to add. Record
   the exact failure: which detail it missed, which ceremony it invented, which lane it wandered into,
   or where it kept talking after done.
2. **GREEN** — Add the *specific* guidance (a check's Means/Cut-it-when, a profile verdict, a Law
   clause, a workflow step) that turns that exact failure into a pass. Not a vague exhortation — the
   sentence that would have stopped the failure.
3. **REFACTOR** — Re-read the addition hunting for the new rationalization it accidentally licenses
   ("cut aloud" must not become "cut everything"; "park the tangent" must not become "ignore the P0").
   Tighten until the eval passes for the right reason.

## How to run

Validate the files parse:

```bash
python3 -c "import json; json.load(open('trigger-eval.json')); json.load(open('evals.json')); print('evals OK')"
```

Trigger evals: paste each query into a fresh session with Loom installed; check activation matches
`should_trigger`. Behavior evals: run each `prompt` (with its `code` where present) and grade against
`expectations` / `forbidden` / `route_to`.

## Grading rubric (per behavior case)

| Outcome | `must_find` | `must_not` / `boundary` |
|---------|-------------|--------------------------|
| **Pass** | Expectations met; expected ids (or same-range neighbors) cited; ends with declare-done + stop | No forbidden behavior; routing named with the owner's lane; seal-line contract intact where dispatch occurs |
| **Partial** | Catches the details but without ids, or suppresses correctly without stating the reason | Routes correctly but adjudicates "just a little" (a severity adjective, a refactor hint), or stops without the parked table |
| **Fail** | Misses a P0-class detail, or delivers without criteria/parked/honesty line | Produces the sibling's deliverable, invents ceremony the profile suppresses, or invites more work after done |

## When to re-run

After **any** change to `SKILL.md`, `reference/checks.md`, the stack profiles, the handoff protocol, or
a workflow — the catalogue and the Law are load-bearing, and a wording change that looks cosmetic can
license a new rationalization. Re-run the two `must_not` cases most often; they are the ones that decay.
