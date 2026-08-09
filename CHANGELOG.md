# Changelog

All notable changes to Loom are documented here.

## [1.0.0] — 2026-08-09

### Loom is born — where one ask becomes the whole fabric

First release of Loom as an independent, self-contained feature-completeness engine, created and authored by
**Mohammed Nasher** ([@mhd-nasher](https://github.com/mhd-nasher)). Released open source under MIT. Part of the
[Forge](FORGE_DNA.md) suite — **Loom defines it**, Cairn designs it, Anvil proves it, Lens cleans it, Bastion
guards it, Relay ships it (the suite's security member is [Bastion](https://github.com/mhd-nasher/bastion)).

- **Four modes:** Mode 0 — Guided Spec (beginner, plain-language interview in the user's own language, with
  progress gauges); Mode A — Spec a New Feature (vague ask → complete, buildable spec); Mode B — Audit a Built
  Feature (existing code → reconstructed implied spec → gap report with confidence labels); Mode C — Map User
  Flows (the flow map alone: happy spine + every exit).
- **Mandatory Step 0 discovery** — detect the stack and product surface, read Cairn's structure and complexity
  budget if present, scope the ONE feature and its real goal, and gauge the user's level before weaving.
- **Stack-aware feature profiles** (`reference/stack-feature-profiles.md`) — per-stack APPLY/SUPPRESS/PARTIAL
  for every dimension range: **Firebase/Flutter/Next/Stripe** as the flagship, plus web app, mobile app,
  backend/API/system service (where the consumer is the user and flows are call sequences), and internal
  tool/CLI. Dimensions that don't fit are suppressed with a stated reason — a weekend tool is never asked for
  enterprise ceremony.
- **The F-### catalogue** (`reference/checks.md`) — every completeness dimension with a stable ID across 17
  themes: intent & scope (`F-001…005`), actors & permissions (`F-010…015`), user flows (`F-020…028`), states
  (`F-030…037`), data lifecycle (`F-040…047`), validation & limits (`F-050…056`), concurrency & idempotency
  (`F-060…065`), money path (`F-070…076`), notifications (`F-080…085`), abuse surface (`F-090…094`), i18n/RTL
  & time (`F-100…104`), accessibility (`F-110…113`), analytics (`F-120…123`), platform deltas (`F-130…134`),
  rollout & existing data (`F-140…144`), system/API contract (`F-150…158`), and weave discipline
  (`F-160…162`). Each carries Means / Why / Applies–Leave it alone when / Relates-to–Routes-to, with a
  plain-language mirror (`reference/checks-plain-language.md`).
- **The One-Weave Law** — Loom's anti-distraction core: weave one feature at a time, weave it whole, and cut
  it loose when it is done. Every applied dimension is specified or explicitly cut with a stated reason — a
  silent gap is a hole users fall through. Discoveries outside the feature's goal are parked and routed, never
  explored inline; when the weave completes, Loom declares done and stops. Mirrors Cairn's
  Anti-Over-Engineering Law and the suite's No-False-Alarm Law.
- **The subagent handoff protocol** (`reference/handoff-protocol.md` + `templates/handoff-brief.md`) — when a
  routed finding blocks the weave, Loom dispatches a subagent carrying the owning sibling's skill and a
  self-contained brief (context-isolated, 3-iteration cap) whose final message must end with the strict return
  line — «خلاص تم حل المشكلة — ارجع للجلسة تبعك، أنا خلصت شغلي» — and then stop. Loom resumes the weave the
  moment it sees that line. Non-blocking findings are parked in the spec's Parked & Routed table instead.
- **Flow, state, and edge craft** (`reference/flow-mapping.md`, `reference/state-and-lifecycle.md`,
  `reference/edge-case-hunting.md`) — the happy spine + every exit convention, the eight UI states, the
  delete-story matrix, and the interrogation heuristics (zero/one/many, first/Nth time, slow/offline,
  two-at-once, halfway-abandoned, the malicious twin).
- **Acceptance criteria as the Anvil handshake** (`reference/acceptance-criteria.md`) — the weave ends at
  Given/When/Then; Anvil begins there (T-002 reads Loom's flow map as the list of valuable paths). Loom never
  writes a test.
- **Checklists** — `feature-completeness-review.md` (the deep, dimension-by-dimension review) and
  `pre-build-gate.md` (the short `F-GATE-###` gate a feature passes before code is written).
- **Templates** — `feature-spec-template.md` (the fabric: every dimension pre-marked Applies/Cut, acceptance
  criteria, Parked & Routed table, honesty line), `gap-report.md`, `handoff-brief.md`.
- **Worked examples** — a vague «أبي ميزة حجز» ask woven into a complete booking spec with the forgotten
  details ID-tagged; a built payout screen audited into a gap report; a partner-webhook API feature proving
  the systems half of the lane (UI dimensions suppressed aloud, `F-150…158` swept).
- **`scripts/spec_lint.py`** — the one self-tested script: flags silent gaps (dimensions neither specified nor
  cut), happy-only flows, TBD/placeholder debt, malformed Given/When/Then, and a missing Parked list. Leads,
  not verdicts.
- **Evals** (`evals/`) — trigger evals (bilingual English/Arabic queries, sibling-boundary negatives) and
  behavior evals across `must_find` / `must_not` / `boundary` types, with the skill-TDD loop documented in
  `evals/README.md`.
