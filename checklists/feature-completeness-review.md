# Feature-Completeness Review — The Deep Checklist

> The dimension-by-dimension review of a spec (Mode A output) or a built feature (Mode B). Work through
> the ranges the stack profile APPLIES; for each suppressed range, confirm the cut is written with its
> reason. Every item cites its catalogue ID — details in `../reference/checks.md`.

## Intent & scope
- [ ] One feature, one named goal; out-of-scope written (F-001, F-002)
- [ ] The user's problem and the success definition stated (F-003, F-004)
- [ ] Spec depth matches the complexity budget (F-005)

## Actors & permissions
- [ ] Every actor enumerated — including admin, support, guests, system jobs (F-010)
- [ ] Capability matrix per actor: see/create/change/delete (F-011)
- [ ] Guest story and the sign-in wall placed (F-012)
- [ ] Permission-denied UX designed per actor (F-013)
- [ ] Role-change mid-feature and ownership succession answered (F-014, F-015)

## User flows
- [ ] Every entry point listed with its required context (F-027)
- [ ] Happy spine drawn end-to-end (F-020)
- [ ] Every step has an unhappy exit landing on a designed state (F-021, F-034)
- [ ] Abandonment and re-entry answered per step (F-022, F-023)
- [ ] Counterparty moves drawn for two-sided flows (F-024)
- [ ] Back/refresh (web) or interruption/process-death (mobile) walked (F-025, F-026, F-133)
- [ ] ★ Commit point marked; facts re-verified there (F-028, F-063)

## States
- [ ] State × screen table complete — all eight states specified or cut (F-030…F-036)
- [ ] External-wait operations have visible, honest states (F-037)

## Data lifecycle
- [ ] Lifecycle line drawn per created object (F-040)
- [ ] Delete-story matrix filled: soft/hard, cascades, others-still-see, undo (F-041…F-043) ⚠
- [ ] Retention, audit, export answered (F-044…F-046)
- [ ] Old-shape records defined for future fields (F-047)

## Validation & limits
- [ ] Every input has rules + violation message (F-050)
- [ ] Server-side re-validation stated as the contract (F-051)
- [ ] Quotas, duplicates, size ceilings, chaos inputs, money-input rules (F-052…F-056)

## Concurrency & idempotency
- [ ] The feature's races named, each with winner + loser experience (F-060)
- [ ] Two-devices, double-submit, stale-commit, concurrent-edit, retry-safety (F-061…F-065)

## Money path ⚠
- [ ] Money flow drawn hop by hop (F-070)
- [ ] Currency/rounding fixed; displayed = charged (F-071)
- [ ] Payment failure, refunds, receipts, disputes specified (F-072…F-075)
- [ ] Platform cut computed server-side, once (F-076)

## Notifications
- [ ] Event → receiver → channel table (F-080); timing/batching chosen (F-081)
- [ ] Opt-out boundaries, landing targets, silent parties, delivery fallback (F-082…F-085)

## Abuse surface (identify; severity → Bastion)
- [ ] Malicious-twin walk recorded (F-090); fake content, drain, exposure, recourse (F-091…F-094)

## i18n, RTL & time
- [ ] Languages declared or single-language cut aloud (F-100)
- [ ] RTL mirroring, timezone per timestamp, locale formats, text expansion (F-101…F-104)

## Accessibility
- [ ] Labels, contrast/touch floors, keyboard completeness, motion/timers (F-110…F-113)

## Analytics
- [ ] Success metric, funnel events, failure metrics, PII-free events (F-120…F-123)

## Platform deltas
- [ ] Per-platform table; permissions sequenced; store rules checked; parity debt explicit (F-130…F-134)

## Rollout & existing data
- [ ] Old data's meaning in the new feature chosen (F-140)
- [ ] Discovery, mixed-cohort surfaces, off-switch semantics, sunset (F-141…F-144)

## System/API contract (when the profile applies it)
- [ ] Contract written before the handler (F-150)
- [ ] Versioning, error vocabulary, idempotency, pagination, rate limits (F-151…F-155)
- [ ] Webhook delivery semantics, auth scopes, consumer inventory (F-156…F-158)

## Weave discipline
- [ ] Non-feature findings routed by name, never adjudicated (F-160)
- [ ] Parked & Routed table present — even if "none parked" (F-161)
- [ ] The output declares done and stops (F-162)

---

**⚠ rows** touch money or deletion — their decisions are proposed to the human, never silently made
(Forge DNA §3.5). A review that ends with unexplained unchecked boxes isn't failed — it's unfinished:
every box is checked, or its dimension is cut aloud.
