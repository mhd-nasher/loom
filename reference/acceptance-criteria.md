# Acceptance Criteria — Where the Weave Ends and Anvil Begins

> The spec's last section and its most consequential: Given/When/Then criteria are the feature's
> definition of done for *behavior* — and the handshake with **Anvil**, who turns each criterion into a
> test at the right level (T-002 reads Loom's flow map as the list of valuable paths). Loom writes
> criteria; **Loom never writes a test.**

## The format

```
AC-1  Given a listed slot with no booking
      When two customers confirm payment for it concurrently
      Then exactly one booking exists, one customer sees confirmation,
       and the other sees the conflict state with alternatives          [F-060, F-063]
```

Rules — each criterion:

1. **One behavior per criterion.** If the Then contains "and also…" about a *different* behavior, split
   it. (Multiple observable facts of the *same* behavior — one booking AND the loser's state — belong
   together: they're one outcome.)
2. **Given states facts, not history.** The starting world, not the clicks that built it.
3. **When is one action or one event** — a user act, a webhook, a timeout firing.
4. **Then is observable.** A record exists, a state shows, a message sends — never "the code should",
   never internals Anvil can't observe from outside.
5. **Cites its dimensions.** Every criterion carries the `F-###` it proves — that's what makes the spec
   traceable end-to-end.
6. **Unhappy criteria outnumber happy ones.** The happy spine yields a handful; the exits, races, and
   lifecycle turns yield the rest. A criteria list that's mostly Given-good/When-good/Then-good specced
   only the easy 20% (F-021's echo).

## Coverage rule

Minimum criteria set for a complete weave: the spine's success (F-004) · every unhappy exit that changes
data or money · the commit-point race (F-060/F-063) · the double-submit guard (F-062) · each delete-story
row (F-041/F-042) · each money outcome — paid, failed, refunded (F-070s). UI-polish states (skeleton
styles) usually don't need criteria — they're design review, not behavior; say so rather than padding
the list.

## The Anvil handshake

What Anvil needs from each criterion, and gets from this format: the **behavior named** (its test name),
the **level implied** (pure rule → unit; seam crossing — Firestore, Stripe — → integration/emulator;
full journey → E2E, sparingly), and the **evidence defined** (the Then is the assertion). Money, auth,
access, and deletion criteria carry one more line — `⚠ human-approve` — because a test that enshrines
wrong sensitive behavior is worse than no test (Forge DNA §3.5): the human confirms the criterion before
Anvil locks it in.

Handing off: deliver the criteria block + the flow map. Do not suggest which test framework, which
doubles, or how many tests — that is Anvil re-decided, and F-160 forbids it.
