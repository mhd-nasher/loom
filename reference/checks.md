# Loom Checks — The Feature-Completeness Catalogue

> This is the enforceable layer of Loom. Every check has a **stable ID** (`F-###`), what it means, why it
> matters, **when it applies** and **when cutting it is right** (the anti-ceremony judgment), and how it
> **relates to / routes to** the sibling skills in the Forge suite (`../FORGE_DNA.md`). These IDs are cited
> by Loom's workflows, checklists, templates, examples, and evals.
>
> Loom owns *the feature's complete definition*: actors, flows, states, edge cases, data lifecycle,
> acceptance criteria. It does **not** design structure (**Cairn**), write tests (**Anvil**), judge style
> (**Lens**), rate vulnerabilities (**Bastion**), or plan deploys (**Relay**). When the weave surfaces one
> of those, Loom **routes it to the owner** — it never adjudicates another lane. A complete spec is not a
> correct or safe build — see the Honesty Contract in `SKILL.md`.

## ID map

| Range | Theme |
|-------|-------|
| `F-001…F-005` | Intent & scope — the one feature and its real goal |
| `F-010…F-015` | Actors, roles & permissions — who exists and what each may do |
| `F-020…F-028` | User flows — the happy spine and every exit |
| `F-030…F-037` | States — what the user sees in every condition |
| `F-040…F-047` | Data lifecycle — create to delete, and what remains |
| `F-050…F-056` | Validation & limits — what the feature refuses |
| `F-060…F-065` | Concurrency, races & idempotency — two things at once |
| `F-070…F-076` | Money path — every coin accounted for |
| `F-080…F-085` | Notifications & comms — who hears, when, and who doesn't |
| `F-090…F-094` | Abuse & misuse surface — the malicious twin (identify only) |
| `F-100…F-104` | i18n, RTL & time — language, direction, timezone |
| `F-110…F-113` | Accessibility — everyone can use it |
| `F-120…F-123` | Analytics & success metrics — how you'll know it works |
| `F-130…F-134` | Platform deltas — web vs iOS vs Android vs API consumers |
| `F-140…F-144` | Rollout & existing data — the feature meets the world |
| `F-150…F-158` | System/API contract — when the consumer is a machine |
| `F-160…F-162` | Weave discipline — routing, parking, stopping |

Each entry: **Means** · **Why** · **Applies / Cut it when** · **Relates to / Routes to**.

---

## Intent & scope

### F-001 — One feature, one real goal
**Means:** The spec names exactly one feature and the user-visible outcome it exists to produce ("a customer
books a slot and both sides know it's confirmed"), not a grab-bag. **Why:** A feature without a named goal
can't be judged complete — and two features in one ask is how both ship half-done. **Applies:** always — this
is where every weave starts. **Relates to:** the One-Weave Law (`SKILL.md`), F-162.

### F-002 — The out-of-scope list is written
**Means:** What this feature deliberately does NOT do, written down ("no recurring bookings in v1, because
X"). **Why:** Unstated non-scope becomes assumed scope; the argument happens in production instead of in the
spec. **Applies:** always. **Cut it when:** never — even "nothing is out of scope" must be said aloud.

### F-003 — The user's actual problem is stated
**Means:** One sentence on the pain this feature removes, from the user's view — not the implementation.
**Why:** A feature specced from the solution backward misses the details only the problem reveals.
**Applies:** always. **Relates to:** F-120 (the success metric measures this sentence).

### F-004 — Success is defined before build
**Means:** What observable outcome makes this feature "working" — a completed booking, a delivered webhook,
a paid payout. **Why:** Without it, "done" means "code merged," which is how burned features ship.
**Applies:** always. **Relates to:** F-120…F-123; **Anvil** turns this into the highest-value test (T-002).

### F-005 — The feature fits the complexity budget
**Means:** The spec's depth matches the shared budget (Forge DNA §5): a solo MVP gets a lean fabric, a
regulated platform gets the full sweep. **Why:** A spec heavier than the product is ceremony; lighter than
the product is a hole. **Applies:** always — set in Step 0. **Routes to:** **Cairn** originates the budget;
Loom honors it.

---

## Actors, roles & permissions

### F-010 — Every actor is enumerated
**Means:** List everyone who touches the feature: the customer, the provider, the admin, support staff,
anonymous visitors, scheduled jobs, webhooks, other services. **Why:** The forgotten actor (usually admin or
the system itself) is where features break — nobody specced what support sees when a booking disputes.
**Applies:** always. **Cut it when:** a single-actor personal tool — say so.

### F-011 — Each actor's capabilities are defined
**Means:** Per actor: what they can see, create, change, and delete in this feature — a small matrix beats a
paragraph. **Why:** "Users can edit listings" hides the real questions: which users, whose listings, which
fields, when? **Applies:** always. **Relates to:** F-041 (delete rights), F-090 (capability abuse).

### F-012 — The guest/anonymous story is told
**Means:** What a signed-out user sees and where the sign-in wall sits — browse-then-login, or login-first?
**Why:** The guest path is the most-traveled and least-specced; a wrong wall kills conversion or leaks data.
**Applies:** any feature reachable before auth. **Cut it when:** the surface is entirely behind auth — state
it.

### F-013 — Permission denied is a designed experience
**Means:** What each actor sees when they *can't* do the thing: hidden button, disabled with reason, or
explicit error? **Why:** "403" is a spec decision, not an implementation detail — a hidden feature reads as
broken, a leaky error reads as an invitation. **Applies:** any feature with roles. **Routes to:** whether
the *enforcement* holds is **Bastion** (B-SEC auth checks); Loom specs the experience.

### F-014 — Role changes mid-feature are handled
**Means:** What happens to in-flight state when a role changes — the provider is suspended with open
bookings, the admin demotes a user mid-session? **Why:** Role transitions are the edge nobody specs and
support inherits. **Applies:** features with long-lived state + roles. **Cut it when:** roles can't change
or there's no in-flight state — say which.

### F-015 — Ownership is explicit
**Means:** Every object the feature creates has a named owner and a rule for what "owner" grants — and what
happens when the owner leaves (F-046). **Why:** Orphaned objects and "who can touch this?" disputes are
lifecycle holes. **Applies:** any feature creating shared/visible objects.

---

## User flows

### F-020 — The happy spine is drawn end-to-end
**Means:** The main path from entry to the success definition (F-004), step by step, screen by screen or
call by call — see `reference/flow-mapping.md`. **Why:** The spine is the skeleton every other branch hangs
off; unwritten, every developer imagines a different one. **Applies:** always.

### F-021 — Every flow has an unhappy exit
**Means:** For each step of the spine: what happens on failure, rejection, timeout, or "no"? Every step has
at least one exit that isn't forward. **Why:** The happy path is the easy 20% — production is made of the
exits. **Applies:** always. **Relates to:** F-030…F-037 (each exit lands on a state).

### F-022 — Abandonment mid-flow is specified
**Means:** The user closes the app at step 3 of 5 — what persists, what expires, what do they see on
return? Draft saved, hold released, payment voided? **Why:** Users abandon constantly; unspecced
abandonment leaks holds, drafts, and half-created records. **Applies:** any multi-step flow. **Cut it
when:** the flow is a single atomic action.

### F-023 — Re-entry and resume are defined
**Means:** Entering the flow again after abandoning, after success, after failure — resume, restart, or
block with "you already have one"? **Why:** Re-entry is where duplicate records are born. **Applies:** any
multi-step or once-per-user flow. **Relates to:** F-062 (duplicate submission).

### F-024 — The other side's moves are specced
**Means:** In any two-party flow: what happens when the *counterparty* acts — provider declines, seller
cancels after payment, admin removes the listing mid-checkout? **Why:** Marketplace disasters live here —
one side's cancel is the other side's undefined state. **Applies:** any multi-actor flow. **Cut it when:**
single-actor feature — say so.

### F-025 — Back, refresh, and the browser are respected
**Means:** Back-button at each step, refresh mid-form, opening the flow in two tabs — what survives?
**Why:** The browser's buttons are the most-used feature of every web app and the least-specced.
**Applies:** web flows. **Cut it when:** native-only — but then F-026 applies.

### F-026 — Interruptions are survivable
**Means:** On mobile: the call that interrupts checkout, the app killed at payment, airplane mode at step
4 — what state greets the user back? **Why:** Mobile flows are interrupted constantly; "restart from zero"
is a spec decision, usually the wrong one. **Applies:** mobile flows. **Cut it when:** web-only.

### F-027 — Every entry point is listed
**Means:** All the ways into the flow: home screen, deep link, push notification, email link, QR, direct
URL, another feature. Each lands where, with what context? **Why:** A deep link into step 3 without the
state from steps 1–2 crashes or corrupts; unlisted entries are untested entries. **Applies:** always.
**Relates to:** F-130 (per-platform entry differences).

### F-028 — Flow permissions are checked per step, not per door
**Means:** The spec says at which steps eligibility is *re*-checked — the slot still free at payment, the
listing still live at confirm? **Why:** Checking only at entry means acting on stale truth at commit.
**Applies:** flows over shared mutable state. **Relates to:** F-063 (stale reads); enforcement is
**Bastion**'s lane.

---

## States

### F-030 — Every screen has its state set specified
**Means:** For each screen/section the feature adds: empty, loading, populated, error — written before
pixels. The eight states live in `reference/state-and-lifecycle.md`. **Why:** The unspecced state ships as
a blank div or an infinite spinner; users meet states, not flows. **Applies:** any feature with UI.
**Cut it when:** headless/API feature (then F-150 owns the equivalent).

### F-031 — The empty state teaches
**Means:** First-run and zero-data: what does the user see and what does it tell them to do next?
**Why:** Every user meets the empty state first; a dead-end empty screen kills the feature at hello.
**Applies:** any list/collection UI. **Cut it when:** the feature can't be empty (pre-seeded) — say why.

### F-032 — Loading and slow are designed
**Means:** What shows during fetch — skeleton, spinner, stale-while-revalidate? And at what threshold does
"slow" get its own treatment (timeout message, retry offer)? **Why:** "It's loading" and "it's broken" look
identical to users unless the spec separates them. **Applies:** any async UI.

### F-033 — Offline and flaky-network behavior is chosen
**Means:** Airplane mode, dead spots, request-fails-midway: block with a message, queue and sync, or
degrade read-only? A deliberate choice, per feature. **Why:** Mobile users are offline daily; the default
(silent failure) is the worst of the options. **Applies:** mobile always; web where it matters. **Cut it
when:** internal desktop tool on a LAN — say so.

### F-034 — Error states name the way out
**Means:** Every error state carries what happened (in user words) and what to do next — retry, contact,
go back. Distinguish user-fixable from system errors. **Why:** A dead-end error is abandonment; "something
went wrong" with no exit is a hole. **Applies:** always. **Relates to:** F-021 (each unhappy exit lands
here).

### F-035 — Partial success is represented
**Means:** When an operation half-succeeds (3 of 5 photos uploaded, booking created but email failed) —
does the user see all-or-nothing or the true partial state? **Why:** Pretending partial is success corrupts
trust; pretending it's failure discards work. **Applies:** batch/multi-part operations. **Cut it when:**
the operation is atomic.

### F-036 — Stale data has a policy
**Means:** How old may displayed data be, and what invalidates it — the listing price changed while the
user stared at it: honor what they saw or force refresh? **Why:** Staleness is invisible until it costs
money (F-028, F-063). **Applies:** shared mutable data with real-time stakes. **Cut it when:**
single-user data.

### F-037 — In-progress external operations are visible
**Means:** States driven by outside systems — payment processing, verification pending, webhook awaited —
have their own visible state, not a spinner pretending it's quick. **Why:** External operations take
seconds to days; hiding that reads as broken. **Applies:** any feature awaiting third parties.

---

## Data lifecycle

### F-040 — Every object's lifecycle is drawn
**Means:** For each record the feature creates: born how, changed by whom, ends how — a lifecycle line per
object (`reference/state-and-lifecycle.md`). **Why:** Features are specced at creation and burned at
deletion; the lifecycle line forces the whole arc. **Applies:** any feature that writes data.

### F-041 — The delete story is defined
**Means:** Soft or hard? Who may delete, what does "deleted" hide, can it be undone, and for how long?
**Why:** Delete is the most consequential verb in the feature and the least specced — the NasGo class of
disaster. **Applies:** any deletable object. **Cut it when:** append-only by design — state it. **Routes
to:** destructive-action *approval* stays human (Forge DNA §3.5).

### F-042 — Cascades and orphans are resolved
**Means:** Deleting a parent (listing, account, provider) — what happens to its children (bookings,
reviews, messages)? Delete, orphan-with-placeholder, or block the delete? **Why:** Orphans crash renders
and leak "deleted" content; cascade choices are business decisions, not ORM defaults. **Applies:** any
related data. **Relates to:** F-024 (the other side sees the cascade).

### F-043 — What others still see after deletion
**Means:** After a user deletes their account/content: what remains visible to counterparties — past
bookings, reviews they left, messages they sent? **Why:** "Delete my account" meets "the other side's
records" — an unspecced collision with legal weight. **Applies:** multi-actor data. **Routes to:** legal
retention duties are the human's call; Loom forces the question.

### F-044 — Retention and expiry are chosen
**Means:** How long does each object live — drafts, logs, holds, completed bookings? What expires
automatically and what does expiry do? **Why:** Data without an end date accumulates cost and liability
silently. **Applies:** always for generated data. **Cut it when:** trivial volume, no sensitivity — say so.

### F-045 — Edit history and audit needs are stated
**Means:** Does anyone need to see who changed what — disputes, support, compliance? Full audit trail,
last-edited-by, or nothing (and why nothing is fine)? **Why:** Retrofitting an audit trail after the
dispute is too late. **Applies:** money, disputes, admin actions. **Cut it when:** low-stakes personal
data.

### F-046 — Export and portability are answered
**Means:** Can the user take their data out — and does the account-holder's departure (F-015) strand
anything? **Why:** GDPR-class duties and "the provider left, the customer's receipts must survive" both
live here. **Applies:** user-generated data in real products. **Cut it when:** ephemeral/internal data.

### F-047 — Migration of the object's shape is anticipated
**Means:** The spec notes which fields are likely to evolve and what old records do when the shape changes
(default, backfill, or version). **Why:** The v2 field that's null on every v1 record is a slow-motion
crash. **Applies:** long-lived objects. **Routes to:** migration *mechanics* → **Relay** (F-140).

---

## Validation & limits

### F-050 — Every input names its rules
**Means:** Per field: type, format, length, range, required/optional, and the error message when violated.
**Why:** "Validate the input" is not a spec; the rule-less field accepts the thing that breaks page two.
**Applies:** always. **Relates to:** F-034 (violations land on designed errors).

### F-051 — Server-side re-validation is the contract
**Means:** The spec states that every client rule is re-enforced server-side — the client validates for
UX, the server for truth. **Why:** The client is a suggestion; the API accepts what the form refuses.
**Applies:** always. **Routes to:** *whether* enforcement holds → **Bastion** (client-trust findings).

### F-052 — Quotas and rate limits are set
**Means:** How many may a user create — listings, bookings, requests per hour? What happens at the cap?
**Why:** The unlimited feature is the abusable feature (F-090) and the surprise-cost feature. **Applies:**
any user-creatable object. **Cut it when:** trusted-internal tools — say so.

### F-053 — Duplicates are defined and handled
**Means:** What makes two things "the same" (same slot? same title? same email?) and what happens on
duplicate — block, merge, or allow with warning? **Why:** Nobody defines duplicate until the list is full
of them. **Applies:** user-created collections. **Relates to:** F-062 (double-submit races).

### F-054 — Size and content ceilings exist
**Means:** Max photo size/count, max message length, max attachments — with the at-limit UX. **Why:**
The ceiling-less upload is a cost hole and an abuse hole. **Applies:** any user content. **Relates to:**
F-090.

### F-055 — Format edge inputs are enumerated
**Means:** Emoji in names, RTL text in LTR fields, zero-width chars, leading/trailing spaces, `+` in
emails, very long words that break layout. **Why:** Real users type real chaos; each unhandled edge is a
support ticket. **Applies:** free-text inputs. **Cut it when:** enum-only inputs.

### F-056 — Money and quantity inputs have exact rules
**Means:** Decimal places, min/max amounts, zero allowed?, negative blocked?, currency fixed or chosen?
**Why:** A price field that accepts 0.001 or -5 is a money bug born in the spec. **Applies:** any numeric
money/quantity input. **Relates to:** F-070…F-076.

---

## Concurrency, races & idempotency

### F-060 — The feature's races are named
**Means:** List where two actions can collide: two customers, one slot; edit while delete; pay while
cancel. Each named race gets a winner and a loser experience. **Why:** Races don't appear in demos — they
appear at scale, as double-bookings and lost money. **Applies:** shared mutable state. **Cut it when:**
single-user local data — say so.

### F-061 — Two devices, one account
**Means:** The same user acts from phone and laptop simultaneously — last-write-wins, lock, or merge? What
does the losing device see? **Why:** Every real user is two devices; unspecced multi-device is silent data
loss. **Applies:** account-based features with mutable state.

### F-062 — Double-submit is disarmed
**Means:** Double-tap the pay button, retry on timeout, resubmit the form — the spec says: one effect, and
how (disable, dedupe key, idempotent endpoint). **Why:** The double-charge is the classic spec-hole; users
double-tap *because* the first tap looked slow. **Applies:** any create/pay/send action. **Relates to:**
F-153 (idempotency keys), F-032 (slow looks broken).

### F-063 — Acting on stale truth is prevented at commit
**Means:** The step that commits (book, pay, publish) re-verifies the facts it depends on — the slot still
free, the price unchanged, the listing still live. **Why:** Validation at step 1 is decoration if commit is
at step 5. **Applies:** multi-step flows over shared state. **Relates to:** F-028, F-036.

### F-064 — Concurrent edits have a policy
**Means:** Two admins edit the same record: lock, last-write-wins with warning, or field-level merge — and
does the loser lose silently? **Why:** "We'll never edit at the same time" is false the day the team is
two. **Applies:** shared editable records. **Cut it when:** single-writer by design.

### F-065 — Retries are safe by specification
**Means:** Every automatic retry (client or server) is declared safe — the operation is idempotent, or
deduped, or the retry is forbidden. **Why:** A retry on a non-idempotent operation is a duplicate side
effect: two emails, two charges, two bookings. **Applies:** anything with retries or flaky networks.
**Relates to:** F-153; **Anvil** proves it (T-00x); mechanics of pipelines → **Relay**.

---

## Money path

### F-070 — The money flow is drawn end-to-end
**Means:** Who pays whom, when, through what — hold, capture, transfer, commission, payout — as a diagram
or table with every hop. **Why:** Money specced as "user pays" hides the six hops where it goes wrong.
**Applies:** any paid feature. **Cut it when:** no money moves — and F-071…F-076 fall with it, said aloud.

### F-071 — Currency, rounding, and display are fixed
**Means:** Which currency, stored in what unit (pence/halalas, never floats), rounded how, displayed how —
and is the displayed total *exactly* the charged total? **Why:** A penny of drift across commission math is
a reconciliation nightmare and a trust breaker. **Applies:** any money display or math. **Relates to:**
F-056.

### F-072 — Payment failure is a first-class flow
**Means:** Card declined, 3DS abandoned, wallet timeout — each lands on a designed state with a way out;
what was reserved is released. **Why:** Payment failure is common; unspecced failure strands holds and
inventory. **Applies:** any charge. **Relates to:** F-022 (abandonment), F-037 (external ops).

### F-073 — Refunds have rules before the first sale
**Means:** Who can refund, until when, full or partial, fees kept or returned, commission reversed? — and
who clicks the button. **Why:** The first refund request arrives before the policy unless the spec beat it.
**Applies:** any charge. **Routes to:** refund *execution* stays human-approved (Forge DNA §3.5).

### F-074 — Receipts and records are specified
**Means:** What written proof each party gets — receipt email, in-app record, invoice — with what fields,
kept how long (F-044). **Why:** "Where's my receipt?" is the first support ticket of every paid feature.
**Applies:** any charge.

### F-075 — Disputes and chargebacks are anticipated
**Means:** When the customer disputes at the processor: what freezes, who's notified, what evidence exists
(F-045)? **Why:** Chargebacks arrive with deadlines; the unspecced dispute costs the merchandise *and* the
fee. **Applies:** card-payment features. **Cut it when:** no card rails.

### F-076 — The platform's cut is computed server-side, once
**Means:** Commission/fees are defined in one server-side place; the spec forbids client-supplied amounts
from being trusted. **Why:** The client-computed total is the oldest marketplace exploit. **Applies:**
marketplace/commission features. **Routes to:** exploitability verdict → **Bastion** (client-trust class).

---

## Notifications & comms

### F-080 — Every notification is listed with its trigger
**Means:** A table: event → who's notified → channel (push/email/in-app/SMS) → content summary. **Why:**
Notifications specced ad-hoc arrive duplicated, missing, or to the wrong side. **Applies:** any
multi-actor or async feature. **Cut it when:** truly silent feature — say so.

### F-081 — Timing and batching are chosen
**Means:** Instant, digest, or quiet-hours-aware? Ten events in a minute = ten pings or one summary?
**Why:** Notification fatigue is feature abandonment; the spec decides cadence, not the queue. **Applies:**
any recurring notification.

### F-082 — Opt-out and preferences exist
**Means:** What can the user silence, per channel — and what is non-silenceable (security, legal, money)?
**Why:** No opt-out is a spam report; all-opt-out kills the transactional messages that must arrive.
**Applies:** any notification feature.

### F-083 — The notification lands somewhere real
**Means:** Tapping the push/email deep-links into the right screen with the right state (F-027) — including
when the object is gone (F-042). **Why:** A notification into a 404 is worse than none. **Applies:** any
actionable notification.

### F-084 — Who is NOT notified is decided
**Means:** The silent parties are named: does the admin hear about every booking? Does the other customer
know the slot filled? **Why:** Over-notification leaks activity (F-090-adjacent) and under-notification
strands actors. **Applies:** multi-actor features.

### F-085 — Delivery failure has a fallback
**Means:** Push token dead, email bounced — is there a fallback channel or at least an in-app record of
what they missed? **Why:** Delivery is not guaranteed; a money-critical message with no fallback is a
silent hole. **Applies:** notifications that carry obligations (bookings, payments). **Cut it when:**
purely-informational pings.

---

## Abuse & misuse surface

*Loom **identifies** the surface. Severity, exploitability, and the verdict are **Bastion**'s
(`B-SEC/B-PEN` lanes) — Loom never rates them.*

### F-090 — The malicious twin walks the feature
**Means:** For each capability, ask what the malicious twin does with it: fake bookings, review bombing,
scraping listings, hoarding slots. Enumerate, don't judge. **Why:** Every feature is used twice — as
designed, and as gamed; the second use arrives unspecced. **Applies:** any public-facing feature. **Cut it
when:** trusted-internal only — say so. **Routes to:** **Bastion** for severity.

### F-091 — Fake and spam content is anticipated
**Means:** What stops (or later removes) fake listings, spam messages, bot signups — and who wields it
(F-010's admin)? **Why:** The marketplace with no spam story becomes spam. **Applies:** user-generated
content. **Routes to:** **Bastion** rates the vectors.

### F-092 — Resource-drain misuse is bounded
**Means:** The expensive operations (image processing, exports, searches) have per-user bounds (F-052) so
one actor can't drain the budget. **Why:** On serverless, someone else's loop is your bill. **Applies:**
metered-cost operations. **Routes to:** cost-attack verdict → **Bastion** (B-PERF/B-SEC).

### F-093 — Data exposure through the feature is walked
**Means:** What can be *learned* through the feature — user enumeration via search, presence via "last
seen", income via public booking counts? **Why:** Features leak by composition; each new surface reveals
old data in new ways. **Applies:** any feature exposing user data. **Routes to:** **Bastion** owns the
leak verdict.

### F-094 — Moderation and recourse exist
**Means:** Report button, block, admin takedown, appeal — the minimum recourse loop for the feature's
content and conduct. **Why:** The first harassment case shouldn't invent the policy. **Applies:**
user-to-user features. **Cut it when:** no user-to-user surface.

---

## i18n, RTL & time

### F-100 — Languages and locales are declared
**Means:** Which languages ship, which is the fallback, and what happens to untranslated strings.
**Why:** "We'll translate later" hardcodes English into a thousand strings. **Applies:** multi-language
products. **Cut it when:** single-language product — say so, it's a legitimate cut.

### F-101 — RTL is a layout requirement, not a translation
**Means:** Arabic/Hebrew flip layout, icons, progress direction, and text alignment — the spec says which
screens must mirror. **Why:** RTL as an afterthought is a broken UI for every Arabic user — the NasGo
market. **Applies:** products with RTL locales. **Cut it when:** LTR-only market, stated.

### F-102 — Timezones are assigned to every timestamp
**Means:** Every time in the feature declares its zone: stored (UTC), displayed (whose local — the
customer's, the provider's, the venue's?), and compared. **Why:** A booking at "10:00" without a zone is a
missed appointment across any two zones. **Applies:** any timestamped feature — bookings above all.

### F-103 — Locale formats are applied
**Means:** Dates (order, calendar), numbers (separators), currency position, week start — per locale.
**Why:** 03/04 is March or April depending on the reader; ambiguity in a booking is a no-show.
**Applies:** i18n products. **Cut it when:** F-100 cut single-language/locale.

### F-104 — Text expansion and long content survive
**Means:** The layout holds when German doubles the label or Arabic triples the line height — truncation
rules are chosen (ellipsis where, tooltip when). **Why:** The button that fits in English overflows in
production. **Applies:** translated UIs.

---

## Accessibility

### F-110 — Screen-reader labels are part of the spec
**Means:** Interactive elements name their accessible labels — especially icon-only buttons and images
that carry meaning. **Why:** An unlabeled icon is an invisible feature to a screen-reader user.
**Applies:** UI features in real products. **Cut it when:** internal tooling with a known audience — say
so, and know what you're accepting.

### F-111 — Contrast and touch targets meet floor values
**Means:** Text contrast ≥ 4.5:1 (large text 3:1), touch targets ≥ 44pt — the spec names the floor it
commits to. **Why:** Below-floor UI excludes users and fails store review (F-132). **Applies:** UI
features.

### F-112 — Keyboard and switch navigation complete the flow
**Means:** The whole flow is completable without a pointer — focus order, visible focus, no
keyboard traps. **Why:** Pointer-only flows lock out keyboard and assistive-tech users entirely.
**Applies:** web UI. **Cut it when:** native-mobile-only (then platform a11y in F-110/F-111 covers it).

### F-113 — Motion and time limits have alternatives
**Means:** Animations respect reduce-motion; timed steps (checkout countdowns, session expiry) offer
extension or a non-timed path. **Why:** Motion sickness and slow input are real; a hard timer is a hard
wall. **Applies:** animated or timed features. **Cut it when:** neither exists in the feature.

---

## Analytics & success metrics

### F-120 — The success metric is instrumented
**Means:** The one number that proves F-004 — bookings completed, webhooks delivered — is emitted by the
feature from day one. **Why:** A feature that can't report its success can't be judged, improved, or
killed. **Applies:** real products. **Cut it when:** personal/throwaway tools — a legitimate cut, stated.

### F-121 — The funnel's drop points are observable
**Means:** Each step of the spine (F-020) emits an event, so where users abandon is visible. **Why:**
"Nobody uses it" and "everybody abandons at step 3" need different fixes; without the funnel you guess.
**Applies:** multi-step flows in real products.

### F-122 — Failure is measured, not just success
**Means:** Error rates, payment-failure rates, notification bounce rates — the feature's *failure* signals
are named and counted. **Why:** The metric that would reveal the feature is burning is the one nobody
added. **Applies:** real products. **Routes to:** alerting on these signals → **Relay** (D-030s).

### F-123 — Analytics respect privacy boundaries
**Means:** Events carry ids, not raw PII; what's collected is listed and defensible. **Why:** The
analytics pipeline is the leak nobody audits (F-093). **Applies:** any instrumented feature. **Routes
to:** **Bastion** for exposure verdicts.

---

## Platform deltas

### F-130 — Per-platform behavior differences are tabled
**Means:** One table: this feature on web / iOS / Android / API — what differs (payments, deep links,
permissions, capabilities) and what must stay identical. **Why:** "Same feature everywhere" is never
literally true; undocumented deltas become bug reports. **Applies:** multi-platform products. **Cut it
when:** single-platform, stated.

### F-131 — OS permission prompts are sequenced
**Means:** Which OS permissions the feature needs (camera, location, notifications), when each is
requested (in context, not at launch), and the denied-permission experience. **Why:** A denied permission
with no fallback is a dead feature; a launch-time wall of prompts is a delete. **Applies:** mobile
features using device capabilities.

### F-132 — Store review constraints are respected
**Means:** The feature's compliance with store rules is checked at spec time — IAP vs external payment
rules, account deletion requirements, content policies. **Why:** The feature that violates review
guidelines ships six weeks late, redesigned. **Applies:** app-store-distributed features. **Cut it when:**
web/API only.

### F-133 — Platform-specific interruptions are covered
**Means:** iOS/Android lifecycle (backgrounding mid-payment, low memory kills) map onto F-026's
interruption spec per platform. **Why:** Each OS interrupts differently; one generic answer misses both.
**Applies:** mobile flows with state.

### F-134 — Feature parity debt is explicit
**Means:** If a platform ships later or lesser, the gap is written (F-002) and the cross-platform user's
experience of the gap is designed ("available on web" states). **Why:** Silent parity gaps read as bugs
and split support load. **Applies:** staggered multi-platform releases.

---

## Rollout & existing data

*Loom defines **what** the rollout must handle. Pipeline, flags, and deploy mechanics are **Relay**'s
(`D-###`).*

### F-140 — Existing data meets the new feature
**Means:** What do pre-feature records look like inside the new feature — old bookings without the new
field, old users without the new consent? Default, backfill, or exclude: chosen per object. **Why:** The
feature that works for new data and crashes on old data fails on launch day, for everyone. **Applies:**
any feature touching existing objects. **Cut it when:** greenfield product — say so.

### F-141 — First-sight of the feature is designed
**Means:** How existing users discover it — announcement, badge, empty-state teach (F-031), or silent?
**Why:** Undiscovered features measure as failures (F-120) even when they work. **Applies:** user-facing
features in live products.

### F-142 — Partial-rollout experience is specified
**Means:** If flagged/staged (Relay's mechanics): what does a user *without* the feature see, and what
happens on shared surfaces between have/have-not users (the flagged user's booking seen by an unflagged
provider)? **Why:** Mixed-cohort surfaces are the rollout edge nobody specs. **Applies:** staged rollouts
on shared-data features. **Cut it when:** all-at-once release.

### F-143 — The off-switch semantics are defined
**Means:** If the feature is disabled after launch, what happens to data it created — hidden, read-only,
or gone? **Why:** "Just turn it off" is impossible when off is undefined and bookings exist. **Applies:**
features behind kill-switches. **Routes to:** switch mechanics → **Relay**.

### F-144 — Sunset of the replaced thing is planned
**Means:** If this feature replaces an old one: overlap period, data carry-over, and the old links'
destinations (F-083). **Why:** The replaced feature's leftovers — bookmarks, notifications, muscle
memory — outlive it. **Applies:** replacement features. **Cut it when:** net-new capability.

---

## System/API contract

*When the consumer is a machine, the contract **is** the UX. On API/backend features these replace the UI
dimensions — suppression stated per `reference/stack-feature-profiles.md`.*

### F-150 — The contract is written before the handler
**Means:** Method, path, request/response shapes, and semantics — written as the spec, not recovered from
the code. **Why:** An API whose contract lives in its implementation changes contract on every refactor.
**Applies:** any API/webhook/exported-function feature.

### F-151 — Versioning and deprecation are policies, not events
**Means:** How breaking changes ship (URL version, header, additive-only) and how consumers learn a field
is dying (deprecation window, sunset header). **Why:** The unversioned API can never change again — or
breaks someone every time it does. **Applies:** externally-consumed APIs. **Cut it when:** single
first-party consumer deployed in lockstep — say so.

### F-152 — Error responses are a designed vocabulary
**Means:** The error shape (code, message, details), the distinction between validation/auth/not-found/
conflict/server, and retryability signaled per error. **Why:** Machines can't read "something went wrong";
consumers implement *your* error vocabulary. **Applies:** any API feature. **Relates to:** F-034's twin
for machines.

### F-153 — Idempotency is contractual
**Means:** Which operations accept idempotency keys, how long keys are honored, and what a replay returns
(the original result, not a duplicate effect). **Why:** Every network consumer retries; without contractual
idempotency, retries are duplicates (F-062/F-065 for machines). **Applies:** mutating endpoints —
payment-adjacent above all.

### F-154 — Pagination, filtering, and limits are specified
**Means:** Page scheme (cursor/offset), max page size, default sort, and the over-limit response. **Why:**
The unpaginated list endpoint works until the table grows — then it takes the service down. **Applies:**
collection endpoints.

### F-155 — Rate limits and quotas are part of the contract
**Means:** Limits per consumer, the 429 shape, retry-after signaling, and burst behavior. **Why:**
Unpublished limits are outages consumers can't code against (F-052 for machines). **Applies:** external
APIs. **Cut it when:** internal trusted single consumer, stated.

### F-156 — Webhooks specify delivery, retry, and ordering
**Means:** At-least-once vs at-most-once, retry schedule, timeout, ordering guarantees (or the explicit
lack), and the consumer's ack contract. **Why:** A webhook without retry semantics silently drops the
booking-confirmed event; one without dedupe delivers it twice (F-153). **Applies:** webhook-emitting
features. **Relates to:** signature verification is **Bastion**'s lane (B-SEC webhook checks).

### F-157 — Auth scopes and audiences are named
**Means:** Which token types/scopes may call each operation, and which callers each endpoint serves
(user, admin, service). **Why:** The endpoint specced without an audience is the one that ships open
(F-013 for machines). **Applies:** any authenticated API. **Routes to:** enforcement verdict → **Bastion**.

### F-158 — Backward compatibility of payloads is tested against real consumers
**Means:** The spec lists known consumers and what each depends on; removing/renaming a field checks that
list first. **Why:** "Nobody uses that field" is discovered false in production. **Applies:**
multi-consumer APIs. **Relates to:** consumer contract tests → **Anvil**.

---

## Weave discipline

### F-160 — Route non-feature findings to the owner
**Means:** If the weave uncovers a structural question → **Cairn**; a test need → **Anvil**; a quality
smell → **Lens**; a vulnerability → **Bastion**; a deploy concern → **Relay**. Name the owner and the ID
lane; don't adjudicate it in the feature lane. Blocking findings may be dispatched under
`reference/handoff-protocol.md`; the rest are parked. **Why:** This is the boundary contract that keeps
the suite from colliding (Forge DNA §4). **Applies:** always — Loom raises *completeness* findings only.

### F-161 — The Parked & Routed table is mandatory
**Means:** Every spec and gap report ends with the table of discoveries that were parked or routed —
finding, owner, ID — even when empty ("none parked"). **Why:** Parking without a ledger is forgetting with
extra steps; the table is what makes the One-Weave Law honest. **Applies:** every Loom output.

### F-162 — Declare done, then stop
**Means:** When every applied dimension is specified or cut and the criteria are written, Loom states the
weave is complete, delivers the honesty line, and stops — no "want me to also…", no new threads.
**Why:** The tool that keeps selling work trains the user to distrust "done" — and distraction from the
real goal is the failure Loom exists to prevent. **Applies:** every run, without exception.

---

## The catalogue at a glance

| Theme | IDs | Count |
|-------|-----|-------|
| Intent & scope | F-001…F-005 | 5 |
| Actors, roles & permissions | F-010…F-015 | 6 |
| User flows | F-020…F-028 | 9 |
| States | F-030…F-037 | 8 |
| Data lifecycle | F-040…F-047 | 8 |
| Validation & limits | F-050…F-056 | 7 |
| Concurrency, races & idempotency | F-060…F-065 | 6 |
| Money path | F-070…F-076 | 7 |
| Notifications & comms | F-080…F-085 | 6 |
| Abuse & misuse surface | F-090…F-094 | 5 |
| i18n, RTL & time | F-100…F-104 | 5 |
| Accessibility | F-110…F-113 | 4 |
| Analytics & success metrics | F-120…F-123 | 4 |
| Platform deltas | F-130…F-134 | 5 |
| Rollout & existing data | F-140…F-144 | 5 |
| System/API contract | F-150…F-158 | 9 |
| Weave discipline | F-160…F-162 | 3 |
| **Total** | | **102** |

**Adding a check:** take the next free ID in its range, give it **Means / Why / Applies–Cut it when /
Relates-to–Routes-to**, a stack note saying when to SUPPRESS it, and an eval. A check without an eval does
not belong in this catalogue (see `CONTRIBUTING.md`).
