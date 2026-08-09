# Stack Feature Profiles — Apply/Suppress per Product Surface

> **Load this in Step 0 of every workflow.** Loom is stack-aware: a dimension applies only where the
> product surface makes it pay. The rule of thumb: dimensions about *intent, actors, flows, lifecycle,
> and races* apply almost everywhere — they are what a feature *is*. Dimensions tied to a surface you
> don't have (UI states on a headless API, store-review rules on a web app, i18n on a personal script)
> are **suppressed with a stated reason** until you confirm that surface exists. A suppression spoken
> aloud is a spec decision; a suppression assumed silently is a hole (the No-False-Alarm Law,
> `../FORGE_DNA.md` §3).

## How to read a profile

- **APPLY** — sweep this range fully; gaps here are findings.
- **APPLY (flagship)** — this range is where this stack's features actually burn; sweep it first and deepest.
- **PARTIAL** — apply the named subset; the rest is cut with the profile's reason.
- **SUPPRESS** — do not raise these as gaps on this stack; state the profile's reason in the spec's Cut column.
- **Weave defaults** — the priorities and assumptions Loom starts from on this stack.
- **Sweep order** — the order that finds the expensive holes soonest.

---

## ⭐ Flagship Profile: Firebase / Serverless + Flutter + Next.js + Stripe

*Detect:* `firebase.json`, `functions/`, `firestore.rules`, `pubspec.yaml`, `next.config.*`, Stripe keys
in env/config, `onCall`/`onRequest` handlers. This is the NasGo-class stack: a Flutter/web client + Cloud
Functions + Firestore + Stripe (often Connect). Its defining trait for features: **the client is
untrusted, the database is reachable from the client through Rules, money moves through webhooks, and
every actor sees real-time data** — so races, lifecycle, and money dimensions dominate.

| Range | Verdict | Reason |
|-------|---------|--------|
| F-001…F-005 Intent & scope | **APPLY** | Always — the weave starts here on every stack. |
| F-010…F-015 Actors & permissions | **APPLY (flagship)** | Rules-readable data means every actor definition becomes a Security Rule; the forgotten actor becomes an open document. |
| F-020…F-028 User flows | **APPLY (flagship)** | Real-time multi-actor flows (customer + provider + admin) are this stack's product shape. F-024 (counterparty moves) is where marketplaces burn. |
| F-030…F-037 States | **APPLY** | Flutter/Next UIs with streams: loading/offline/stale states are met daily. F-036/F-037 elevated — snapshots go stale mid-checkout, Stripe operations are external waits. |
| F-040…F-047 Data lifecycle | **APPLY (flagship)** | Firestore has no cascading deletes — F-042 orphans are the default outcome unless specced. Soft-delete vs hard-delete is a Rules decision too. |
| F-050…F-056 Validation & limits | **APPLY (flagship)** | The client validates for UX only; F-051 server re-validation (Functions + Rules) is the contract. F-052 quotas guard the serverless bill. |
| F-060…F-065 Concurrency & idempotency | **APPLY (flagship)** | Double-booking the same slot is THE class bug: F-060/F-063 demand a transaction at commit. F-062/F-065: Functions retry — every handler's effect must be dedupe-safe. |
| F-070…F-076 Money path | **APPLY (flagship)** | Stripe Connect: holds, transfers, commission (F-076 server-side, once), webhooks confirming payment (F-037), refunds reversing transfers (F-073). Sweep this range completely on any paid feature. |
| F-080…F-085 Notifications | **APPLY** | FCM push + email; F-085 matters — FCM tokens die silently, money messages need an in-app record. |
| F-090…F-094 Abuse surface | **APPLY** | Public marketplace surface. Identify; severity → Bastion (B-SEC/B-PEN). |
| F-100…F-104 i18n, RTL & time | **APPLY** | Arabic/English products make F-101 RTL and F-102 timezones first-class. Single-language products: PARTIAL — keep F-102 (bookings always have timezones), cut the rest with reason. |
| F-110…F-113 Accessibility | **APPLY** | Store review (F-132) and real users both demand the floor values. |
| F-120…F-123 Analytics | **APPLY** | Firebase Analytics is one import away; F-122 failure metrics feed Relay's alerts (D-030s). |
| F-130…F-134 Platform deltas | **APPLY** | Flutter iOS/Android + Next web = three surfaces; F-131 permission prompts and F-132 store rules are mobile-real. |
| F-140…F-144 Rollout & existing data | **APPLY** | Live products with existing Firestore data; F-140 backfill decisions are per-collection. Mechanics → Relay. |
| F-150…F-158 API contract | **PARTIAL** | Apply to `onRequest` HTTP endpoints, exported webhooks, and any partner-facing surface. Cut for `onCall`-only internal functions consumed by your own clients in lockstep (F-151's own exception) — state it. |
| F-160…F-162 Weave discipline | **APPLY** | Always, every stack. |

**Weave defaults:** money and races before pixels; every commit step is a transaction question; every
delete is a Rules + orphans question; timezones explicit on anything bookable.
**Sweep order:** F-070 money → F-060 races → F-040 lifecycle → F-010 actors → F-020 flows → the rest.

---

## Profile: Web App (Next.js / React SPA, no mobile)

*Detect:* `next.config.*` / `vite.config.*` without `pubspec.yaml`; no app-store artifacts.

| Range | Verdict | Reason |
|-------|---------|--------|
| F-001…F-065, F-080…F-094, F-120…F-123, F-140…F-144 | **APPLY** | Feature fundamentals — stack-independent. |
| F-025 Back/refresh/tabs | **APPLY (flagship)** | The browser's buttons are this surface's interruption model. |
| F-026 / F-133 Mobile interruptions | **SUPPRESS** | No native lifecycle; the browser tab model (F-025) covers it. |
| F-030…F-037 States | **APPLY** | Full set; F-033 offline usually PARTIAL (block-with-message is a legitimate web answer — state it). |
| F-070…F-076 Money | **APPLY** | If money moves; otherwise cut the range with "no money moves in this feature". |
| F-100…F-104 i18n | **APPLY / PARTIAL** | Per product market; single-locale products cut F-100/F-101/F-103/F-104 aloud, keep F-102 if anything is scheduled. |
| F-110…F-113 Accessibility | **APPLY (flagship)** | Keyboard nav (F-112) is fully in scope on web — and legally real in many markets. |
| F-130…F-134 Platform deltas | **SUPPRESS (mostly)** | Single platform. Keep F-130 only if an API/mobile consumer exists; F-131/F-132/F-133 suppressed — no OS prompts, no store review. |
| F-150…F-158 API contract | **PARTIAL** | Apply to public/partner API routes; cut for purely internal BFF routes consumed only by this same app, deployed together. |

**Weave defaults:** browser-first interruptions; keyboard completeness; SEO/deep-link entries in F-027.
**Sweep order:** F-020 flows → F-030 states → F-050 validation → F-060 races → the rest.

---

## Profile: Mobile App (Flutter / native, app-store distributed)

*Detect:* `pubspec.yaml` / Xcode + Gradle projects; store metadata.

| Range | Verdict | Reason |
|-------|---------|--------|
| F-001…F-065, F-080…F-094, F-120…F-123, F-140…F-144 | **APPLY** | Feature fundamentals. |
| F-026 Interruptions / F-133 OS lifecycle | **APPLY (flagship)** | Calls, backgrounding, process death mid-flow: this surface's daily reality. |
| F-033 Offline | **APPLY (flagship)** | Mobile users are offline every day; a deliberate offline choice is mandatory per feature. |
| F-025 Browser behavior | **SUPPRESS** | No browser chrome; deep links (F-027) and OS back handling live in F-130/F-133. |
| F-080…F-085 Notifications | **APPLY (flagship)** | Push is the surface's channel; F-083 deep-link landing and F-085 dead-token fallback are mobile-real. |
| F-110…F-113 Accessibility | **APPLY** | Platform a11y (TalkBack/VoiceOver) via F-110/F-111/F-113; F-112 keyboard PARTIAL (hardware-keyboard/switch users exist — note it). |
| F-130…F-134 Platform deltas | **APPLY (flagship)** | Two OSes, two permission models, two review boards. F-132 store rules can kill a specced feature — check at spec time, not submit time. |
| F-150…F-158 API contract | **SUPPRESS** | The app consumes APIs; it doesn't publish them. If this feature ships a backend endpoint too, spec that as its own weave under the Backend profile. |

**Weave defaults:** interruption-survivable flows; offline decided per feature; permission prompts in
context; review rules read before spec sign-off.
**Sweep order:** F-020 flows (with F-026 at every step) → F-033 offline → F-130 deltas → F-080
notifications → the rest.

---

## Profile: Backend / API / System Service (no UI)

*Detect:* API routes/handlers without a client app in-repo; service/daemon code; exported webhooks;
message consumers. **The consumer is the user — flows are call sequences, states are response shapes,
and the contract is the UX.**

| Range | Verdict | Reason |
|-------|---------|--------|
| F-001…F-005 Intent & scope | **APPLY** | Always. |
| F-010…F-015 Actors | **APPLY** | Actors are callers: services, jobs, partners, admins. F-013 becomes F-157 (denied = auth error shape). |
| F-020…F-028 Flows | **APPLY (as call sequences)** | The "flow" is the call choreography: request → validation → effect → response/webhook. F-022 abandonment = client disconnects mid-operation; F-024 = the upstream/downstream system's moves. |
| F-030…F-037 UI States | **SUPPRESS** | No screens. The machine twin is F-152 (error vocabulary) + F-037's equivalent: long-running operations expose status endpoints. State the suppression. |
| F-040…F-047 Data lifecycle | **APPLY** | Fully — services own the data of record. |
| F-050…F-056 Validation | **APPLY** | F-051 is the whole game here — there is no client to half-trust. |
| F-060…F-065 Concurrency | **APPLY (flagship)** | Concurrent consumers are the normal case, not the edge. F-065 retry-safety and F-153 idempotency are the same spec decision. |
| F-070…F-076 Money | **APPLY** | If money moves through the service. |
| F-080…F-085 Notifications | **PARTIAL** | Human channels usually out of scope; the machine twin (webhooks/events emitted) is F-156. Keep F-085's spirit: delivery failure handling. |
| F-090…F-094 Abuse | **APPLY** | Public endpoints are the abuse surface. Severity → Bastion. |
| F-100…F-104 i18n | **SUPPRESS (mostly)** | No UI strings. Keep F-102 — timestamps in payloads declare their zone (ISO-8601 UTC is a spec decision, write it). |
| F-110…F-113 Accessibility | **SUPPRESS** | No human interface. State it. |
| F-120…F-123 Analytics | **PARTIAL** | F-120/F-122 as service metrics (success and failure rates); alerting mechanics → Relay. |
| F-130…F-134 Platform deltas | **PARTIAL** | F-130 as consumer-parity (v1 vs v2 clients); F-131/F-132/F-133 suppressed — no OS, no store. |
| F-140…F-144 Rollout | **APPLY** | F-140 existing-data migration and F-142 mixed-consumer cohorts are service-real. |
| F-150…F-158 API contract | **APPLY (flagship)** | This range IS the feature on this stack. Sweep all nine, always. |
| F-160…F-162 Weave discipline | **APPLY** | Always. |

**Weave defaults:** the contract written before the handler; idempotency contractual on every mutation;
every error retryable-or-not by design; timestamps zone-explicit.
**Sweep order:** F-150 contract → F-060 concurrency → F-040 lifecycle → F-090 abuse → the rest.

---

## Profile: Internal Tool / CLI / Personal Script

*Detect:* CLI entry points, small audience, no store/marketing surface, often single-user; the user says
"weekend tool", "internal", "just for me/us".

| Range | Verdict | Reason |
|-------|---------|--------|
| F-001…F-005 Intent & scope | **APPLY** | Always — small tools drift scope fastest. |
| F-010…F-015 Actors | **PARTIAL** | Often one actor; say so (F-010's own cut) and the range collapses honestly. |
| F-020…F-028 Flows | **APPLY (lean)** | Happy spine + failure exits (F-020/F-021); ceremony branches (F-023 re-entry, F-027 multi-entry) only if they exist. |
| F-030…F-037 States | **PARTIAL** | Error and empty output for a CLI (F-031/F-034 as stdout/stderr design); suppress the rest with reason. |
| F-040…F-047 Lifecycle | **PARTIAL** | Keep F-041 (what does delete/overwrite do — even a script can destroy data) and F-044 if it accumulates output; cut the rest aloud. |
| F-050…F-056 Validation | **APPLY (lean)** | F-050 input rules and F-055 chaotic input still bite scripts; quotas (F-052) usually cut. |
| F-060…F-065 Concurrency | **PARTIAL** | Keep F-065 if it retries or runs on a schedule (double-run safety); two-device/two-user races usually cut. |
| F-070…F-076 Money | **APPLY if money** | A billing script gets the full range; otherwise cut in one line. |
| F-080…F-094, F-100…F-104, F-110…F-113, F-120…F-123 | **SUPPRESS** | No audience that needs them — *and this is the profile's core point:* demanding i18n, a11y floors, analytics funnels, or abuse moderation from a personal tool is invented ceremony, the exact false alarm the One-Weave Law bans. State the cut once, move on. |
| F-130…F-134 Platform deltas | **SUPPRESS** | One machine, one platform. |
| F-140…F-144 Rollout | **SUPPRESS (mostly)** | Keep F-140 only if it processes pre-existing data files. |
| F-150…F-158 API contract | **APPLY if it serves others** | A CLI with a `--json` output consumed by scripts has a contract (F-152's shape stability); a human-only tool cuts the range. |
| F-160…F-162 Weave discipline | **APPLY** | Always — small tools deserve done-and-stop too. |

**Weave defaults:** lean fabric; loud cuts; the spec fits on one page and says so proudly.
**Sweep order:** F-001 scope → F-021 failure exits → F-041 destructive actions → F-050 input → done.

---

## When no profile matches

Name the nearest profile, say what differs, and adjust aloud — Loom degrades gracefully to the universal
ranges (intent, actors, flows, lifecycle, races, weave discipline) and says so, exactly as the suite's
honesty law requires (`../FORGE_DNA.md` §2). Never pretend expertise on a surface this file doesn't cover;
never skip the universal ranges because the surface is unusual.
