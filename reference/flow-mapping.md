# Flow Mapping — The Happy Spine and Every Exit

> How Loom draws a user flow so nothing hides. Used by every mode; Mode C
> (`workflows/map-user-flows.md`) is this file applied alone. The catalogue behind it: `F-020…F-028`.

## The method

1. **Name the entry points first (F-027).** Every door in: home screen, deep link, push tap, email link,
   direct URL, another feature's button. Each entry states what context it arrives with — and what happens
   when that context is missing (deep link into step 3 with no step-1 state).
2. **Draw the happy spine (F-020).** The single main path from entry to the success definition (F-004),
   one line per step, numbered. A step is one user-visible action or one system commitment — not a screen
   redesign, not a code function.
3. **Branch every decision.** At each step ask: can the user choose differently? can the system say no?
   can the other side act (F-024)? Each "yes" is a branch with its own landing.
4. **Give every step an unhappy exit (F-021).** Failure, rejection, timeout, "no slots", declined card —
   each lands on a designed state (F-034), never on nothing.
5. **Walk the abandonments (F-022).** Close the app at each step: what persists, what expires, what
   greets the return (F-023)?
6. **Mark the commitment point (F-028, F-063).** The step where the world changes — booked, paid,
   published. Facts are re-verified *here*, and this step gets the double-submit guard (F-062).
7. **Walk it backwards (F-025/F-026).** Back-button and refresh at each step on web; interruption and
   process death at each step on mobile.

## The text-diagram convention

Flows are written as indented text — reviewable in a diff, readable by anyone:

```
ENTRY: listing page → [Book] button        (also: deep link /book/{id} — requires listing loaded)
1. Pick a slot            → no slots?        → EMPTY-STATE: "no availability" + notify-me   [F-031]
2. Confirm details        → back?            → return to 1, slot held 5 min                 [F-025]
                          → abandon?         → hold expires, no record                      [F-022]
3. Pay                    → declined?        → ERROR-STATE: retry/change card, hold kept    [F-072]
                          → double-tap?      → one charge (idempotency key)                 [F-062]
   ★ COMMIT: re-verify slot free inside the transaction                                    [F-063]
                          → slot taken?      → CONFLICT-STATE: "just missed it" + alternatives [F-060]
4. Confirmation           → both sides notified                                             [F-080]
EXIT: booking exists, receipt sent, success metric emitted                                  [F-004, F-120]
```

Conventions: numbered spine · `→ condition?` branches with their landing · `★ COMMIT` marks the
commitment point (exactly one per flow, usually) · every branch cites its `F-###` · `ENTRY`/`EXIT` are
explicit.

## Completeness test for a flow map

A flow map is done when: every entry point listed · every step has ≥1 unhappy exit · abandonment
answered at every step · the commit point marked and guarded · the counterparty's moves drawn (F-024) ·
every landing is a named state, not a shrug. `scripts/spec_lint.py` flags spine steps with no branches —
a lead, not a verdict: some steps genuinely can't fail, and saying so aloud is the fix.
