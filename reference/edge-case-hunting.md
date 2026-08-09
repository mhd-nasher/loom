# Edge-Case Hunting — The Interrogation Heuristics

> How Loom finds the details nobody wrote down. These are *questions to run against every feature*, not
> rules to enforce — each catch lands in its catalogue dimension. Balanced by the One-Weave Law: an edge
> case is specified when it's real for this product, and **cut aloud when it isn't** — hunting is not
> hoarding.

## The seven interrogations

Run each against the feature's spine. Each question that lands becomes a spec line with its `F-###`.

### 1. Zero, one, many, too-many
The list with 0 items (F-031), exactly 1 (does the UI say "1 items"?), a normal many, and 10,000
(F-054/F-154). The counter, the search, the export — each breaks at a different count.

### 2. First time, Nth time, last time
First-run teaches (F-031), the 50th run wants speed, and the *last* time — account closing, subscription
ending — is the path nobody walks (F-043/F-046). What does the feature look like on the way out?

### 3. Slow, offline, and halfway
Every network call: what if it's slow (F-032), fails (F-034), or dies *after the server succeeded but
before the client heard* — the halfway state that mints duplicates (F-062/F-065). The user's screen said
failed; the database said done. Which is true, and who reconciles?

### 4. Two at once
Two users, one resource (F-060). One user, two devices (F-061). One finger, two taps (F-062). The same
webhook, delivered twice (F-153/F-156). Anything that *can* arrive concurrently eventually will.

### 5. The halfway-abandoned
Every multi-step flow, killed at each step (F-022): what's held, what leaks, what expires? Holds without
expiry become permanent locks; drafts without retention become a junk drawer (F-044).

### 6. The other side moves
In any two-party feature: while the customer is at step 3, the provider cancels, edits the price,
deletes the listing, gets suspended (F-014/F-024). The counterparty is the edge-case generator that
never sleeps.

### 7. The malicious twin (F-090…F-094)
Walk the feature as someone who wants to game it: hoard slots with no intent to pay, scrape the
listings, spam the messages, review-bomb a rival. **Enumerate the moves; never rate them** — severity
and exploitability are **Bastion**'s verdicts (B-SEC/B-PEN). Loom's job is that the surface is *named*
in the spec, so Bastion has a map.

## The chaos-input drawer (F-055)

Real users will type: emoji in the name field · a 200-character single word · RTL text in an LTR form ·
leading/trailing spaces · `+tag` emails · zero-width characters · paste-from-Word artifacts. The spec
picks the fields where this matters (names, titles, anything displayed to others) and states the rule.

## When to stop hunting

The hunt is bounded by the stack profile and the complexity budget (F-005): a weekend tool answers
interrogations 1, 3, and 5 and cuts the rest aloud; a marketplace answers all seven. An edge case you
can't name a real occurrence path for is a false alarm — park the paranoia, keep the weave
(`../FORGE_DNA.md` §3, No-False-Alarm). When the applied dimensions are swept, **stop** — the
interrogations generate spec lines, not new scope (F-162).
