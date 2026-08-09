# Feature Spec — <feature name>

> Produced by Loom (Mode 0/A). Every dimension below is **specified** or **cut with a stated reason** —
> a silent gap is a hole. ⚠ sections carry decisions the human must approve (Forge DNA §3.5).

| | |
|---|---|
| **Feature** | <one sentence — the one goal (F-001)> |
| **Problem it solves** | <the user's pain, in their words (F-003)> |
| **Success looks like** | <the observable outcome (F-004)> |
| **Out of scope** | <explicit exclusions (F-002)> |
| **Stack profile** | <flagship / web / mobile / backend / internal (F-005)> |
| **Date · budget** | <date> · <lean / standard / full> |

## Actors & permissions (F-010…F-015)

| Actor | Sees | Creates | Changes | Deletes | Denied-UX |
|-------|------|---------|---------|---------|-----------|
| <actor> | | | | | |

Role-change mid-feature: <answer or `Cut: <reason>`> · Ownership succession: <answer>

## User flows (F-020…F-028)

<text-diagram per `reference/flow-mapping.md` — entries, numbered spine, branches, ★ commit>

Abandonment per step: <table or inline> · Re-entry: <resume/restart/block>

## States (F-030…F-037)

| Screen | Empty | Loading | Error | Offline | Slow | Partial | Stale | External-wait |
|--------|-------|---------|-------|---------|------|---------|-------|---------------|
| <screen> | | | | | | | | |

## Data lifecycle (F-040…F-047)

Lifecycle lines:
```
<Object>: created → … → ends
```

⚠ Delete-story matrix:

| Object | Soft/hard | Cascades to | Others still see | Undo window |
|--------|-----------|-------------|------------------|-------------|
| | | | | |

Retention: <per object> · Audit: <what's trailed> · Export: <answer> · Old-shape policy: <default/backfill/version>

## Validation & limits (F-050…F-056)

| Field | Rules | On violation |
|-------|-------|--------------|
| | | |

Quotas: <caps> · Duplicates: <definition + handling> · Ceilings: <sizes> · Chaos inputs: <fields that matter>

## Concurrency & idempotency (F-060…F-065)

| Race | Winner | Loser sees | Guard |
|------|--------|-----------|-------|
| | | | |

Two devices: <policy> · Double-submit: <mechanism> · Retry-safety: <declaration>

## ⚠ Money path (F-070…F-076) — or `Cut: no money moves in this feature`

Money map: <hop-by-hop> · Currency/rounding: <rules> · Failure: <flow> · Refunds: <policy — human-approved> ·
Receipts: <what/where> · Disputes: <plan> · Commission: server-side, at <where>

## Notifications (F-080…F-085)

| Event | Who | Channel | Timing | Opt-out? |
|-------|-----|---------|--------|----------|
| | | | | |

Not notified: <the silent parties> · Delivery fallback: <answer>

## Abuse surface (F-090…F-094) — identified; severity → Bastion

- <malicious-twin move> → routed B-lane

## i18n, RTL & time (F-100…F-104)

Languages: <list or cut> · RTL screens: <list or cut> · **Timezones:** <per timestamp — stored/displayed/compared> ·
Formats: <locale rules or cut> · Expansion: <truncation rules or cut>

## Accessibility (F-110…F-113)

<floors committed, or cut with reason>

## Analytics (F-120…F-123)

Success metric: <the number> · Funnel events: <per spine step> · Failure metrics: <the burn signals> · PII: ids only

## Platform deltas (F-130…F-134)

<table or `Cut: single platform`>

## Rollout & existing data (F-140…F-144)

Old data: <default/backfill/exclude per object> · Discovery: <how users find it> · Mixed cohorts: <answer or cut> ·
Off-switch: <semantics> — mechanics → Relay

## System/API contract (F-150…F-158) — or `Cut: <profile reason>`

<contract, versioning, errors, idempotency, pagination, limits, webhooks, scopes, consumers>

## Acceptance criteria (`reference/acceptance-criteria.md`)

```
AC-1  Given <facts>
      When <one action/event>
      Then <observable outcome>            [F-###]
```
<⚠-mark money/auth/deletion criteria for human approval>

## Parked & Routed (F-161)

| Finding | Owner | Lane/ID | Status |
|---------|-------|---------|--------|
| <or "none parked"> | | | parked / dispatched → resolved / unresolved — needs human |

---

*Honesty line: This spec is the complete **definition** of the feature — every applied dimension
specified or cut with its reason. It is not a build (Cairn structures it), not proof it works (Anvil
tests it), and not a safety verdict (Bastion guards it). ⚠ decisions await human approval.*
