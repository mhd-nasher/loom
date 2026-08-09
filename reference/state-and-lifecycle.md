# States & Lifecycle — What Users Meet, and How Data Lives and Dies

> The deep-dive behind `F-030…F-037` (states) and `F-040…F-047` (lifecycle). Flows describe movement;
> states describe what the user is looking at *right now*; lifecycle describes what the data does when
> nobody is looking.

## The eight UI states (F-030)

Every screen or section a feature adds is specified against all eight — applied or cut aloud:

| # | State | The question | Check |
|---|-------|--------------|-------|
| 1 | **Empty** | Zero data, first visit — what teaches the next step? | F-031 |
| 2 | **Loading** | What holds the space — skeleton, spinner, stale copy? | F-032 |
| 3 | **Populated** | The designed case — the only one everyone specs. | F-030 |
| 4 | **Error** | What went wrong, in user words, with a way out? | F-034 |
| 5 | **Offline** | Block, queue, or degrade read-only — chosen, not defaulted. | F-033 |
| 6 | **Slow** | At what threshold does loading become "try again"? | F-032 |
| 7 | **Partial** | Half the operation succeeded — show the truth. | F-035 |
| 8 | **Stale** | The data on screen aged — when does it refresh, who wins? | F-036 |

Plus the external-wait state (F-037) wherever a third party is involved: payment processing,
verification pending, webhook awaited — visible, honest about duration, never a spinner pretending.

**The state × screen table.** In a spec, states are recorded as a table — screens down, states across,
each cell either a one-line description or `cut: <reason>`. `spec_lint.py` flags screens whose row is
empty.

## The lifecycle line (F-040)

Every object the feature creates gets one line showing its whole arc:

```
Booking: created(pending) → confirmed → completed → archived(90d) → deleted(hard)
         └→ cancelled(by either side) → refunded? → archived(90d)
Draft:   created → edited(n) → submitted | expired(48h, auto-delete)
```

Each arrow is a transition with an owner (who/what causes it) — the diagram makes missing transitions
visible: if nothing points to "deleted", retention (F-044) is unspecced; if "cancelled" has no
refund branch, the money path (F-073) has a hole.

## The delete-story matrix (F-041…F-043)

For every deletable object, four columns, answered:

| Object | Soft or hard? | Cascades to | Others still see | Undo window |
|--------|---------------|-------------|------------------|-------------|
| Listing | soft (hidden) | bookings: kept, frozen · reviews: kept | past customers: receipt survives | 30 days, owner-only |
| Account | soft 30d → hard | listings: soft-deleted · messages: anonymized | counterparties: "deleted user" placeholder | 30 days |

Rules of the matrix: **soft-vs-hard is a business decision** (recovery, disputes, legal) surfaced to the
human — never an ORM default. **Cascade choices are per-relationship**, not global. **"Others still
see" is the column everyone forgets** — the counterparty's receipts, reviews, and messages have their own
claim on the data (F-043), and legal retention duties are the human's call; Loom forces the question,
never answers it alone (Forge DNA §3.5).

## Retention (F-044) and audit (F-045)

Every generated object declares a lifespan — and "forever" is a declaration too, with a stated reason.
Drafts, holds, logs, and notifications are the usual immortals-by-accident. Audit needs are decided by
stakes: money movements and admin actions get who-did-what-when; low-stakes personal data can decline
the trail aloud.

## Old data meets new shape (F-047, F-140)

When the feature adds a field or changes meaning, three options per object — default, backfill, or
version — chosen in the spec, because the v1 record renders inside the v2 feature on day one. The
*mechanics* of running the migration belong to **Relay** (F-140 routes there); the *definition* of what
old data must mean is Loom's, and it's decided before the handler is written.
