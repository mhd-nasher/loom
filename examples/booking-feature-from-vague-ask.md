# Example — «أبي ميزة حجز» → The Whole Fabric

> The flagship worked example: a real-world vague ask ("I want a booking feature") on the flagship
> stack (Flutter + Cloud Functions + Firestore + Stripe Connect marketplace), woven by Mode A into the
> details that would have burned in production. Abridged — a real spec fills
> `templates/feature-spec-template.md` completely; this shows **the catches**, each with its ID.

## The ask

> «أبي ميزة حجز — العميل يختار موعد عند مقدم الخدمة ويدفع.»
> *("I want a booking feature — the customer picks a slot with a provider and pays.")*

One sentence. Eleven words. Here is what it didn't say — and what shipping only those words costs.

## The feature card (F-001…F-005)

- **Goal:** a customer books one available slot with a provider and pays; both sides see it confirmed.
- **Problem:** booking happens over chat today; double-bookings and no-shows cost providers real money.
- **Success:** a paid, confirmed booking visible to both sides — `bookings_confirmed` counting it (F-120).
- **Out of scope (said aloud):** recurring bookings, group bookings, waiting lists — v2 candidates, parked.
- **Profile:** ⭐ flagship (Firebase/Flutter/Stripe Connect). Budget: standard.

## Ten catches the ask never mentioned

**1. The double-booking race — F-060/F-063 (P0).** Two customers, the last Friday slot, both at the pay
step. The commit must be a Firestore transaction that re-verifies the slot *inside* the write; the loser
gets the conflict state with alternatives (F-034), not a silent failure. Without this, the feature's
core promise — "the slot is yours" — is false under load.

**2. Double-tap = double-charge — F-062 (P0).** The pay button on a slow network gets tapped twice.
One idempotency key per booking attempt; the second tap returns the first result. The classic
burn: it demos perfectly, then the first real user on 3G pays twice.

**3. The provider cancels after payment — F-024/F-073 (P0 ⚠).** The ask specced the customer's path
only. The counterparty can cancel a paid booking: refund full (platform eats the Stripe fee? provider
does?), notify the customer with the reason, free the slot. **Refund policy proposed, human approves.**

**4. Payment failed ≠ flow over — F-072/F-022.** Declined card keeps the 5-minute slot hold (F-022's
hold-expiry answers what happens if they walk away), offers retry/change-card, and releases the hold on
expiry — otherwise declined cards become permanent slot locks.

**5. Whose 10:00? — F-102 (P0 for a booking feature).** Slots stored UTC, displayed in the **venue's**
timezone on both apps, with the zone shown when customer and venue differ. A UK provider, a traveling
customer, a "10:00" booking — without this line, someone stands outside a closed shop.

**6. Deleting a listed service with future bookings — F-041/F-042 (⚠).** Block deletion while paid
future bookings exist (offer: fulfil-then-hide, or cancel-with-refunds flow). Soft-delete hides from
search; past bookings keep the service snapshot (F-043 — the customer's receipt must still say what was
bought).

**7. The hold state nobody designed — F-030/F-037.** The slot picker needs: empty ("no availability" +
notify-me teach, F-031), loading (skeleton), **held-by-another** (live via snapshot — greyed with
countdown), payment-processing (external wait, honest about Stripe's seconds), and offline (F-033:
read-only calendar, booking blocked with message — chosen, not defaulted).

**8. The commission is server math — F-076 (routes to Bastion).** The 15% platform cut computed in the
Cloud Function from the server-side price — never from a client-supplied amount. Loom specs it;
whether the deployed rules actually enforce it is **Bastion**'s verdict (B-SEC client-trust lane) —
parked to the table below.

**9. Who is NOT notified — F-084/F-080.** Confirmed booking → customer (push+email receipt F-074),
provider (push). Admin: **not** per-booking (digest only — noise kills the channel, F-081). Slot freed
by cancellation → notify-me subscribers, once.

**10. Old chat-era bookings — F-140.** Providers already have hand-written bookings for next week.
Launch without a way to block those slots and the feature double-books its first weekend: a manual
"block slot" action ships **in** v1 (in-scope line added), migration of chat history stays out (F-002).

## Acceptance criteria (excerpt — the Anvil handshake)

```
AC-1  Given one remaining slot and two customers at the pay step
      When both confirm payment concurrently
      Then exactly one booking exists; the other sees the conflict state
       with alternatives, and is not charged                              [F-060, F-063, F-072]

AC-2  Given a customer on a slow connection
      When they tap Pay twice within the hold window
      Then exactly one charge and one booking exist                        [F-062]  ⚠ human-approve

AC-3  Given a paid future booking
      When the provider cancels it
      Then the customer is refunded per the approved policy, notified
       with the reason, and the slot returns to availability               [F-024, F-073]  ⚠
```

## Parked & Routed (F-161)

| Finding | Owner | Lane | Status |
|---------|-------|------|--------|
| Client-trust enforcement of commission math | Bastion | B-SEC | parked |
| Where hold/expiry logic lives (Function vs client) | Cairn | R | parked |
| Recurring bookings, waiting lists | Loom (future run) | F | parked |

---

*Honesty line: this spec fully defines the booking feature; it does not build, test, or secure it —
Cairn structures, Anvil proves (starting from the ACs above), Bastion guards. ⚠ items (refund policy,
deletion rule, charge criteria) await human approval.* **Weave closed.**
