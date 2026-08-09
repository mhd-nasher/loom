# The Handoff Protocol — Dispatch, Return Contract, Resume

> How Loom sends a discovered problem to the sibling that owns it **without losing the user or the
> weave**. This protocol exists for one reason: the moment a spec-in-progress detours into fixing a
> vulnerability or restructuring a module, the feature never finishes and the user is lost to the
> tangent. So the detour gets a *sealed envelope, a strict mission, and a hard return* — and the weave
> continues. The brief template lives at `templates/handoff-brief.md`; the routing rule is `F-160`.

## Decision rule: park or dispatch

For every non-feature finding (structure → **Cairn**, tests → **Anvil**, quality → **Lens**, security →
**Bastion**, deploy/rollout → **Relay**):

1. **Default: PARK.** Record it in the spec's **Parked & Routed** table (F-161) — finding, owner, sibling
   ID lane — and continue the weave. Most findings wait just fine.
2. **DISPATCH only when** (a) the finding **blocks the weave** — the spec cannot be completed truthfully
   without it resolved (e.g. Mode B can't reconstruct the implied spec because the code's auth model is
   undecipherable), or (b) the **user explicitly says fix it now**. Nothing else earns a dispatch.
3. **Never: fix it inline.** Loom adjudicating another lane is the boundary violation the suite is built
   to prevent (Forge DNA §4) — even when the fix looks like two lines.

## Dispatching

Fill `templates/handoff-brief.md` and send it as a **subagent** (in Claude Code: the Agent tool, general
subagent, with the brief as the entire prompt). Rules:

- **Context isolation.** The child sees ONLY the brief. Fold in everything it needs — file paths, code
  snippets, the stack profile, decisions already made. If the mission depends on something from the
  conversation, it goes *in the brief*, or the child doesn't know it.
- **One mission per brief.** One problem, named in the owner's ID lane (`R-`/`T-`/`Q-`/`B-`/`D-###`).
  Two problems = two dispatches (usually: two parks).
- **The sibling's skill governs the child.** The brief names which sibling skill the child must invoke
  and follow — the child works *as* Cairn/Anvil/Lens/Bastion/Relay, under that skill's own laws.
- **Iteration cap: 3.** If the mission isn't done after 3 rounds, the child returns with status
  `unresolved — needs human`, and Loom parks it with that status. No infinite detours.
- **Human-in-the-loop travels with the brief.** If the mission touches money, auth, access rules,
  deletion, or crypto, the brief says so — the child *proposes*; the human approves (Forge DNA §3.5).
  Dispatch does not launder the approval away.

## The return contract

Every brief ends with this block, verbatim:

> **Return contract:** You solve ONLY the mission named above — nothing else you notice along the way
> (park stray findings in one line each; their owner will get them). You have at most **3** iterations.
> When the mission's definition of done is met — or the cap is hit, in which case say so with status
> `unresolved — needs human` — end your **final message** with exactly this line and then stop
> completely: no follow-up questions, no suggestions, no "while I was there":
>
> **«خلاص تم حل المشكلة — ارجع للجلسة تبعك، أنا خلصت شغلي»**

That Arabic line is the contract's seal — it means *"done — the problem is solved; go back to your own
session, my work here is finished."* It is the child's last words in every dispatch, in any language the
rest of the work was done in.

## Resuming

The moment Loom sees the seal line (or the subagent's result arrives):

1. **Record the outcome** in the Parked & Routed table: `dispatched → resolved` (or `unresolved — needs
   human`), with the child's one-line evidence.
2. **Fold in only what the mission changed** — if Bastion's child rated the abuse finding, the spec's
   F-090 line gets the reference; the weave does not reopen other sections because the child existed.
3. **Continue from the exact point of interruption.** Re-show the gauge, name the current step, keep
   weaving. The detour is over; it does not get a retrospective.

## Fallback: no subagent tooling

If the environment has no Agent tool (a plain chat, another vendor's assistant), print the identical
brief in a fenced block and tell the user: *"Open a new session, paste this brief as the first message,
and come back when you see the seal line."* The brief is self-contained by design — the protocol is the
file, not the tool (the same portability rule the whole suite follows: no runtime coupling, Forge DNA
§7).

## The user-facing law behind all of this

The protocol is the One-Weave Law's enforcement arm: the user came for a complete feature. Every detour
is either parked in writing or sealed in an envelope with a return address — and when the weave is done,
Loom **stops** (F-162). The protocol never becomes a reason to do more work; it is the mechanism for
doing *less, in the right hands*.
