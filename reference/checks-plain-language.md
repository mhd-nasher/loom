# Loom Checks — In Plain Language

> The same catalogue as `checks.md`, but every check is one plain sentence plus the question to ask
> yourself. No jargon required. Use this layer in Mode 0 (guided), and whenever the user isn't a
> specialist — translate, don't lecture. The stable IDs match `checks.md` exactly.

## Intent & scope — what are we actually building?

- **F-001** — One feature at a time. *"If I had to describe this in one sentence, is it one thing?"*
- **F-002** — Write down what it does NOT do. *"What will someone assume is included that isn't?"*
- **F-003** — Say the problem it solves, in the user's words. *"What annoys people today that this fixes?"*
- **F-004** — Decide what 'working' looks like before building. *"What will I see when this succeeds?"*
- **F-005** — Match the spec's depth to the project's size. *"Is this a weekend tool or a business?"*

## Actors — who touches this?

- **F-010** — List every kind of person (and robot) involved. *"Who did I forget — admin? support? a scheduled job?"*
- **F-011** — For each one: what can they see, add, change, delete? *"Can I draw this as a small table?"*
- **F-012** — Decide what signed-out visitors get. *"Browse first, or login wall? Where exactly?"*
- **F-013** — Design what 'you can't do that' looks like. *"Hidden button, grayed out, or an error — which, and why?"*
- **F-014** — Decide what happens when someone's role changes mid-use. *"Provider gets suspended — what happens to their open bookings?"*
- **F-015** — Every created thing has an owner. *"When the owner leaves, who inherits this?"*

## User flows — the paths people walk

- **F-020** — Draw the main path start to finish. *"Can I walk it screen by screen out loud?"*
- **F-021** — Every step needs a 'what if it fails' answer. *"What happens if this step says no?"*
- **F-022** — People quit halfway. Decide what survives. *"They close the app at step 3 — then what?"*
- **F-023** — People come back. Decide what they see. *"Resume, restart, or 'you already have one'?"*
- **F-024** — The other person acts too. *"What if the seller cancels after the buyer paid?"*
- **F-025** — The back button and refresh exist. *"What breaks if they press back right here?"*
- **F-026** — Phones interrupt. *"A call arrives during payment — what state do they return to?"*
- **F-027** — List every door into the flow. *"Push notification, link, home screen — do all of them land safely?"*
- **F-028** — Re-check the facts at the moment of commitment. *"Is the slot still free when they actually pay?"*

## States — what the screen shows

- **F-030** — Every screen needs its list of states. *"Empty, loading, error, offline — did I design each?"*
- **F-031** — The empty screen should teach. *"First-time user, zero data — what tells them what to do?"*
- **F-032** — Loading and slow are different things. *"At what point does 'loading' become 'try again'?"*
- **F-033** — Decide what offline does. *"Airplane mode — block, queue, or read-only?"*
- **F-034** — Every error names a way out. *"Does this error say what to DO, not just what broke?"*
- **F-035** — Half-success is real. *"3 of 5 photos uploaded — what does the user see?"*
- **F-036** — Old data on screen can lie. *"The price changed while they looked — which price wins?"*
- **F-037** — Waiting on outsiders needs its own screen. *"Payment processing takes a minute — what do they watch?"*

## Data lifecycle — from birth to deletion

- **F-040** — Draw each record's life: born, changed, ends. *"How does this thing die?"*
- **F-041** — Decide what delete means BEFORE building it. *"Trash-can-recoverable or gone forever — and who decides?"*
- **F-042** — Deleting a parent orphans its children. *"Listing deleted — what happens to its bookings and reviews?"*
- **F-043** — Others may still see traces after deletion. *"They delete their account — does the other side's receipt survive?"*
- **F-044** — Nothing should live forever by accident. *"How long do drafts, logs, and holds stick around?"*
- **F-045** — Some changes need a paper trail. *"In a dispute, can anyone see who changed what?"*
- **F-046** — People may want their data out. *"Can they export? What strands if they leave?"*
- **F-047** — Records outlive their shape. *"Next year we add a field — what do old records show?"*

## Validation & limits — what the feature refuses

- **F-050** — Every input field gets rules and an error message. *"What exactly is allowed here, and what do they see if not?"*
- **F-051** — The server re-checks everything the app checks. *"If someone bypasses the form, does the backend still refuse?"*
- **F-052** — Everything creatable gets a limit. *"How many can one person make before we say stop?"*
- **F-053** — Decide what counts as a duplicate. *"Two identical listings — block, merge, or allow?"*
- **F-054** — Uploads and text get ceilings. *"Biggest photo? Longest message? What happens at the cap?"*
- **F-055** — Real people type chaos. *"Emoji in the name field, a 40-character word — does the layout survive?"*
- **F-056** — Money fields get exact rules. *"Can they enter 0? Negative? 0.001?"*

## Concurrency — two things at once

- **F-060** — Name the collisions. *"Two customers, one slot — who wins and what does the loser see?"*
- **F-061** — One person, two devices. *"Editing on the laptop and phone at once — which save survives?"*
- **F-062** — People double-tap buttons. *"Two taps on Pay — one charge or two?"*
- **F-063** — Facts go stale between step 1 and the final step. *"Do we re-check at the moment that matters?"*
- **F-064** — Two editors, one record. *"Both admins hit save — does one lose silently?"*
- **F-065** — Retries must be harmless. *"If this runs twice by accident, is anything doubled?"*

## Money — every coin accounted for

- **F-070** — Draw where the money goes, every hop. *"Who pays, who holds, who receives, when?"*
- **F-071** — Fix currency and rounding rules. *"Is the number they saw exactly the number charged?"*
- **F-072** — Cards get declined constantly. *"Declined at the last step — what do they see, what gets released?"*
- **F-073** — Refund rules exist before the first sale. *"Who refunds, until when, who keeps the fee?"*
- **F-074** — Everyone gets proof. *"Where's the receipt, and how long does it live?"*
- **F-075** — Disputes happen at the bank, not in the app. *"Chargeback arrives — what freezes, who's told, what evidence exists?"*
- **F-076** — The platform's cut is computed on the server, once. *"Could a modified app pay less commission?"* (verdict → Bastion)

## Notifications — who hears about it

- **F-080** — Table every notification: event, receiver, channel. *"Who gets told, how, when this happens?"*
- **F-081** — Choose instant vs digest vs quiet hours. *"Ten events in a minute — ten pings?"*
- **F-082** — Let people opt out — except what they must hear. *"Which of these can they silence?"*
- **F-083** — Tapping it lands somewhere real. *"Notification about a deleted booking — where does the tap go?"*
- **F-084** — Decide who does NOT hear. *"Does the admin hear about every single booking?"*
- **F-085** — Messages fail to arrive. *"Email bounced — is there a backup way to know?"*

## Abuse — the malicious twin (name it, don't judge it — Bastion judges)

- **F-090** — Walk the feature as a bad actor. *"How would someone game this?"*
- **F-091** — Fake content will come. *"What stops fake listings and spam messages, and who removes them?"*
- **F-092** — Expensive operations get bounds. *"Could one user's loop drain the server bill?"*
- **F-093** — Features leak information sideways. *"What can someone LEARN through this that they shouldn't?"*
- **F-094** — Someone will misbehave at someone. *"Where's report, block, and appeal?"*

## Language, direction & time

- **F-100** — Declare the languages, or declare one. *"Which languages — and what shows when a string isn't translated?"*
- **F-101** — Arabic flips the layout, not just the words. *"Which screens must mirror for RTL?"*
- **F-102** — Every time needs a timezone. *"Booking at 10:00 — whose 10:00?"*
- **F-103** — Dates and numbers format per place. *"Is 03/04 March or April for this reader?"*
- **F-104** — Other languages are longer. *"Does the button survive the German translation?"*

## Accessibility

- **F-110** — Label what screen readers can't see. *"Does that icon-only button say its name?"*
- **F-111** — Meet the contrast and touch-size floor. *"Readable in sunlight? Tappable with a thumb?"*
- **F-112** — The whole flow works without a mouse. *"Can I Tab through checkout to the end?"*
- **F-113** — Respect reduce-motion and time limits. *"Does the countdown offer an extension?"*

## Measuring success

- **F-120** — Emit the number that proves it works. *"What one metric shows this feature succeeding?"*
- **F-121** — See where people give up. *"Which step bleeds users?"*
- **F-122** — Count the failures too. *"What number would show this feature silently burning?"*
- **F-123** — Analytics carry ids, not personal data. *"Is there a name or email inside any event?"* (verdict → Bastion)

## Platforms

- **F-130** — Table what differs per platform. *"Web vs iPhone vs Android vs API — what's different, what must match?"*
- **F-131** — Sequence the OS permission asks. *"Camera permission — asked when, and what if denied?"*
- **F-132** — Store rules constrain features. *"Does this violate an App Store payment or deletion rule?"*
- **F-133** — Each OS interrupts differently. *"Backgrounded mid-payment on iOS — then what?"*
- **F-134** — If one platform lags, say so in-product. *"What does the Android user see about the iOS-only part?"*

## Rollout — the feature meets the world

- **F-140** — Old data enters the new feature. *"What do last year's records look like inside this?"*
- **F-141** — Existing users must discover it. *"How does anyone find out this exists?"*
- **F-142** — During gradual rollout, cohorts mix. *"Flagged user's booking, unflagged provider — what does each see?"*
- **F-143** — Turning it off must mean something. *"Kill switch flipped — is the created data hidden, frozen, or gone?"*
- **F-144** — Replacing something old leaves leftovers. *"Old links, old notifications — where do they land now?"*

## APIs — when the consumer is a machine

- **F-150** — Write the contract before the code. *"Could someone build against this from the spec alone?"*
- **F-151** — Plan how breaking changes ship. *"When we rename a field, who breaks and how do they find out first?"*
- **F-152** — Errors are a vocabulary machines read. *"Can a consumer tell 'retry' from 'give up' from the response?"*
- **F-153** — Retries must return the original, not repeat the effect. *"Same request twice — two bookings or one?"*
- **F-154** — Lists paginate before they grow. *"What happens when this collection has 100k rows?"*
- **F-155** — Publish the rate limits. *"What does the consumer see at request 1001?"*
- **F-156** — Webhooks declare retry and ordering. *"Missed delivery — retried when? Delivered twice — deduped how?"*
- **F-157** — Name who may call each endpoint. *"Which tokens, which scopes, which audiences?"* (enforcement → Bastion)
- **F-158** — Know your consumers before removing a field. *"Who actually reads this field today?"*

## Weave discipline — staying on target

- **F-160** — Not-the-feature goes to its owner. *"Is this finding mine, or Cairn's/Anvil's/Lens's/Bastion's/Relay's?"*
- **F-161** — The parked list is part of the deliverable. *"Did every detour get written down with its owner?"*
- **F-162** — Done means stop. *"The weave is complete — am I about to offer more work? Don't."*
