# Example — Auditing a Built Payout Screen (Mode B)

> The "وش غلطت؟" example: a provider-payout screen that already ships (Flutter + Cloud Functions +
> Stripe Connect), audited by `workflows/audit-built-feature.md`. The feature's *essence* works — money
> reaches providers — and the details around it are where the gaps live. Names and lines are
> illustrative of the pattern.

## The implied spec (reconstructed from code, before judging)

`payout_screen.dart` renders a balance and a "Withdraw" button → calls `requestPayout` (callable
Function) → creates a `payouts/{id}` doc and a Stripe transfer → screen shows a green snackbar. The
code handles: authenticated provider, positive balance check (server-side ✓), transfer creation, one
success state. That is the whole implied fabric — the happy spine, alone.

## Gaps

| # | F-ID | Gap | Priority | Confidence | Evidence |
|---|------|-----|----------|------------|----------|
| 1 | F-062/F-065 | `requestPayout` has no idempotency key; a double-tap or a Functions retry creates **two transfers** | **P0** | **CONFIRMED** | `functions/payouts.ts:31` — `stripe.transfers.create` called with no idempotency key; button not disabled during flight (`payout_screen.dart:88`) |
| 2 | F-037/F-030 | No in-progress state: transfer takes seconds→days, screen shows success instantly — Stripe failure after the snackbar is invisible to the provider | **P0** | **CONFIRMED** | `payout_screen.dart:92` — snackbar on Function return, no `payouts.status` listener; no `failed` branch renders |
| 3 | F-072/F-085 | Transfer-failure webhook unhandled: `payouts/{id}` stays `pending` forever; no notification, no in-app record of failure | **P0** | **CONFIRMED** | `functions/webhooks.ts` — no `transfer.*` failure event handler registered |
| 4 | F-060 | Balance check and transfer are not atomic — two concurrent requests can both pass the check (two devices, F-061) | P1 | **LIKELY** | `payouts.ts:24-31` — read then write, no transaction around balance debit |
| 5 | F-034 | The one error path shows raw exception text to the provider | P1 | **CONFIRMED** | `payout_screen.dart:97` — `catch (e) => snackbar(e.toString())` |
| 6 | F-074/F-044 | No payout receipt/record view; history exists in Firestore but no UI, no retention decision | P2 | **CONFIRMED** | no route reads `payouts` collection in `lib/` |
| 7 | F-045 | No audit trail on payout mutations — a dispute can't show who triggered what, when | P2 | **LIKELY** | `payouts.ts` — doc has `amount, status`, no actor/timestamp fields beyond `createdAt` |
| 8 | F-011 | Admin payout powers undefined: can support pause/retry a stuck payout? Nothing in code says | P2 | **HYPOTHESIS** | absence — no admin surface touches `payouts` |

## Questions for you (HYPOTHESIS)

1. Should support/admin be able to retry or cancel a stuck payout — and does that need an audit entry
   (F-045) when they do?
2. Minimum-payout threshold and payout schedule: is instant-on-demand the intended policy, or a batch?

## Suppressed dimensions (not gaps on this stack/feature)

- F-100/F-101 i18n·RTL — app currently single-locale by product decision; **F-102 stays applied** (payout
  timestamps display in provider's zone — currently raw UTC string at `payout_screen.dart:61`, folded
  into gap 6's fix).
- F-150…F-158 — `requestPayout` is an `onCall` consumed only by this app in lockstep (profile's stated
  exception).

## Parked & Routed (F-161)

| Finding | Owner | Lane | Status |
|---------|-------|------|--------|
| Can a modified client trigger payouts beyond balance (gap 4's exploit twin)? | Bastion | B-SEC | parked — severity is Bastion's |
| Regression tests for gaps 1–4 once fixed | Anvil | T | parked |
| `payouts.ts` mixes validation/transfer/write in one 90-line handler | Cairn | R | parked |

---

*Honesty line: completeness gaps with evidence — CONFIRMED items are at the citations; two HYPOTHESIS
items need your answers. Not a security verdict (Bastion holds gap 4's twin), not a test plan (Anvil),
not a refactor plan (Cairn). Fixing is your decision.* **Audit closed.**
