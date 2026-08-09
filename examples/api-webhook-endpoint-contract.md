# Example — A Partner Webhook Endpoint (System/API Feature)

> The systems example: "give partners a webhook when a booking is confirmed" — no UI anywhere. Proves
> the Backend/API profile: **UI dimensions suppressed aloud, the contract range (F-150…F-158) swept in
> full.** The consumer is a machine; the contract is the UX. Abridged to the catches.

## The ask

> "Partners want to be notified when a booking confirms — add a webhook."

## The feature card

- **Goal:** a partner registers an HTTPS endpoint and receives a `booking.confirmed` event within 60s
  of confirmation. **Success:** partner-acknowledged deliveries counted (F-120 as service metric).
- **Out of scope:** partner dashboard UI (separate feature), event replay portal (v2 — parked).
- **Profile: Backend/API/system.** Suppressed aloud per profile: F-030…F-037 UI states, F-110s a11y,
  F-100s i18n except **F-102 — every payload timestamp is ISO-8601 UTC, stated in the contract**;
  F-080s human channels (the machine twin F-156 replaces them).

## The contract sweep (F-150…F-158)

**F-150 — written before the handler.** `POST <partner_url>` with body
`{ id, type: "booking.confirmed", created (ISO-8601 UTC), data: { booking_id, provider_id, slot, amount } }` —
the envelope is the spec; fields partners may rely on are listed, everything else is explicitly
non-contractual.

**F-151 — versioning is a policy.** Envelope carries `version: "2026-08-09"`; changes are additive-only
within a version; breaking changes ship as a new version with a 90-day dual-delivery window and a
deprecation notice event. Without this line, the first field rename breaks every partner at once.

**F-152 — errors are a vocabulary** (for the registration API): `400 invalid_url`, `409
already_registered`, `422 unreachable_endpoint` — each with `retryable: true/false`. Machines can't
read "something went wrong".

**F-153 — replays return, not repeat.** Every event has a stable `id`; partners are contractually told
deliveries are **at-least-once** and must dedupe by `id`. The docs say it because the schedule below
guarantees duplicates will happen.

**F-156 — delivery semantics are the feature.** Timeout 10s; non-2xx → retry at 1m, 5m, 30m, 2h, 12h
(jittered); after final failure the endpoint is marked `failing`, a partner-visible status (the
F-037 twin: long-running truth exposed, machine-readably at `GET /webhook/status`). Ordering: **not
guaranteed**, stated — partners order by `created`, not arrival. Silence here is how partners silently
lose bookings.

**F-155 — limits published.** One endpoint per partner (v1), max 10 events/s burst with overflow
queued, status endpoint rate-limited 60/min with `429 + Retry-After`.

**F-157 — audiences named.** Registration API: partner-scoped API keys only. Deliveries signed
(HMAC header) so partners can verify origin — **signature scheme's strength and secret handling:
Bastion's lane, parked.**

**F-158 — consumer inventory.** v1 consumers: the two launch partners, listed with what each reads;
removing any `data.*` field checks that list first.

**F-142 (rollout, applied):** launch partners onboard behind an allowlist; mixed cohort = partners
without webhooks keep polling the existing API — both paths stay truthful during rollout.

## The races (F-060s — concurrency is the normal case here)

Confirmation and cancellation 2s apart → two events, order not guaranteed (partners told: state wins by
`created`, F-156). Delivery worker crash mid-send → retry fires → duplicate delivery → partner's `id`
dedupe absorbs it (F-153/F-065: the same decision, spelled once, cited twice).

## Acceptance criteria (excerpt)

```
AC-1  Given a registered, reachable partner endpoint
      When a booking is confirmed
      Then exactly one booking.confirmed event with a stable id is
       delivered within 60s, and acknowledged deliveries increment        [F-150, F-156, F-120]

AC-2  Given a delivery attempt that returned 500
      When the retry schedule runs
      Then the SAME event id is redelivered per schedule, and a partner
       deduping by id records exactly one booking                          [F-153, F-156, F-065]
```

## Parked & Routed (F-161)

| Finding | Owner | Lane | Status |
|---------|-------|------|--------|
| HMAC scheme, secret storage & rotation | Bastion | B-SEC | parked |
| Delivery worker queue placement (Function vs Task Queue) | Cairn | R | parked |
| Contract tests against the two launch partners' consumers | Anvil | T | parked |
| Alerting on `failing` endpoints & delivery-lag metric | Relay | D | parked |

---

*Honesty line: complete definition of the webhook feature — the suppressed UI dimensions are stated with
the profile's reason, the contract range swept in full. Signature security (Bastion), queue structure
(Cairn), contract tests (Anvil), and alerting (Relay) are parked to their owners.* **Weave closed.**
