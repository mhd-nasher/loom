# Glossary — Plain-Language Terms

> Every term Loom uses, in one or two sentences each. Beginner-first: jargon is introduced *after* the
> idea, in parentheses, per the guided mode's rules.

- **Feature** — one user-visible capability with one goal ("book a slot", "export my data"). Loom weaves
  one per run (F-001).
- **Spec (specification)** — the written, complete definition of a feature: who, what flows, what
  states, what data, what proves it done. The output of Modes 0/A; the measuring stick of Mode B.
- **The weave** — Loom's name for a run: sweeping every applied dimension until the fabric is whole.
- **Dimension** — one theme of completeness (states, money, races…). The catalogue (`checks.md`) holds
  17.
- **Applied / Cut** — each dimension's verdict for this feature: swept and specified, or excluded with a
  stated reason. A cut is a decision; a silent gap is a hole (the One-Weave Law).
- **Silent gap** — a dimension nobody specified and nobody cut — the thing that burns in production.
  Loom's reason to exist.
- **Happy spine** — the main success path of a flow, drawn step by step (F-020). Everything else hangs
  off it.
- **Unhappy exit** — where a step goes when it fails, is refused, or is abandoned (F-021). Every step
  has at least one.
- **Commit point** — the step where the world changes (booked, paid, published) — marked `★`, guarded
  against staleness (F-063) and double-submit (F-062).
- **State** — what a screen shows in one condition: empty, loading, error, offline… (the eight,
  `state-and-lifecycle.md`).
- **Lifecycle** — a record's whole arc, born → changed → ended (F-040). The delete story (F-041) is its
  hardest chapter.
- **Soft delete / hard delete** — hidden-but-recoverable vs gone-forever. A business decision surfaced
  to the human, never a default.
- **Cascade / orphan** — what happens to child records when the parent dies: removed with it, or left
  parentless (F-042).
- **Race** — two actions colliding on one resource (two customers, one slot — F-060). Races are specced,
  not patched.
- **Idempotent** — safe to run twice with one effect. What retries and double-taps require (F-062,
  F-065, F-153).
- **Stale** — data on screen (or in hand) that the world has since changed (F-036, F-063).
- **Actor** — anyone and anything that touches the feature: user, guest, admin, support, scheduled job,
  webhook (F-010).
- **Counterparty** — the other side of a two-party feature; its moves are the edge cases nobody specs
  (F-024).
- **Acceptance criterion (Given/When/Then)** — one testable statement of behavior: starting facts, one
  action, observable outcome (`acceptance-criteria.md`). The handshake with Anvil.
- **Gap report** — Mode B's output: what the built feature is missing, each gap with an F-ID, a
  priority, and a confidence label (`templates/gap-report.md`).
- **Confidence labels** — **CONFIRMED** (seen in the code) / **LIKELY** (implied) / **HYPOTHESIS**
  (needs the user's answer) — the suite's shared vocabulary (Forge DNA §6).
- **P0…P3** — priority from impact: P0 loses money/data or blocks launch; P3 is backlog polish.
- **Parked & Routed table** — the spec's ledger of discoveries that belong to a sibling: finding, owner,
  ID lane (F-161). Parking is remembering, not ignoring.
- **Dispatch** — sending a blocking finding to its owning sibling as a sealed subagent mission
  (`handoff-protocol.md`).
- **The seal line** — the dispatch's mandatory last words:
  «خلاص تم حل المشكلة — ارجع للجلسة تبعك، أنا خلصت شغلي» —
  "done; back to your session; my work is finished."
- **Stack profile** — the per-surface APPLY/SUPPRESS map (`stack-feature-profiles.md`), loaded in Step 0.
- **Complexity budget** — how much structure/ceremony the project warrants (solo MVP vs regulated
  platform). Cairn originates it; Loom sizes the fabric to it (F-005).
- **The honesty line** — the closing statement of every significant output: what's verified, what's
  proposed, what still needs a human or a sibling (Forge DNA §6).
- **The One-Weave Law** — Loom's core law: one feature, whole fabric, explicit cuts, park the strays,
  declare done, stop (`SKILL.md`).
