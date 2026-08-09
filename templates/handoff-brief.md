# LOOM → <SIBLING> HANDOFF — <feature name>

> Loom's dispatch envelope (`reference/handoff-protocol.md`). Sent as a subagent's **entire prompt** —
> the child sees ONLY this document. One mission per brief. The return contract at the bottom is
> mandatory and verbatim.

## What happened

<2–3 sentences: what Loom found, where, and why it blocks the weave (or that the user said "fix it
now").>

## Context you need (you see ONLY this)

- **Project & stack:** <path, stack profile, the feature being woven>
- **Files:** <absolute paths the mission touches>
- **Snippets:** <the relevant code/rules/config, inline — do not assume repo access beyond these paths>
- **Cairn budget/structure (if present):** <the constraints you must honor>

## Decisions already made (do not reopen)

1. <decision> — reasoning: <why>

## Assumptions to fact-check

- <assumption the child should verify before acting>

## Your mission

Invoke and follow the **<sibling>** skill. Solve ONLY this, in its lane:

> <ONE problem, named with the owner's ID lane — e.g. "Rate the severity and exploitability of the
> unauthenticated admin action at functions/admin.ts:42 (B-SEC lane) and propose the fix" / "Design
> where the booking-hold logic should live (R-lane)">

⚠ If this mission touches money, auth, access rules, deletion, or crypto: **propose, never apply** —
the human approves (Forge DNA §3.5).

## Definition of done

<the observable evidence that ends the mission — a rated finding with reasoning, a named structure with
file paths, a written fix proposal>

## Return contract

You solve ONLY the mission named above — nothing else you notice along the way (park stray findings in
one line each; their owner will get them). You have at most **3** iterations. When the definition of
done is met — or the cap is hit, in which case say so with status `unresolved — needs human` — end your
**final message** with exactly this line and then stop completely: no follow-up questions, no
suggestions, no "while I was there":

**«خلاص تم حل المشكلة — ارجع للجلسة تبعك، أنا خلصت شغلي»**
