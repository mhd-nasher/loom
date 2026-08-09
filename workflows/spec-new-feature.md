# Mode A — Spec a New Feature

> For a user who knows their product and wants the vague ask turned into a complete, buildable spec —
> fast, expert-paced, no interview theater. The discipline is identical to Mode 0; only the translation
> layer is dropped.

## Steps

### 1. Step 0 discovery (mandatory)

Detect the stack, load `reference/stack-feature-profiles.md`, read Cairn's structure/budget if present
(Forge DNA §5), and write the feature card: one goal (F-001), the problem (F-003), success definition
(F-004), out-of-scope list (F-002). If the ask holds two features, split now — weave one, park the
other, say so. Confirm the card in one exchange **only if** the ask was genuinely ambiguous; otherwise
state your reading and proceed (an expert corrects a wrong card faster than they answer a
questionnaire).

```
[████░░░░░░░░░░░░░░░░] 20% — Step 1/5: Feature card + profile loaded
```

### 2. Map the flows

Entry points, happy spine, every branch, every unhappy exit, abandonment per step, the ★ commit point
guarded (F-020…F-028; convention in `reference/flow-mapping.md`). Counterparty moves (F-024) drawn for
any two-sided feature.

```
[████████░░░░░░░░░░░░] 40% — Step 2/5: Flows mapped, exits landed
```

### 3. Sweep the dimensions

Walk every range the profile APPLIES, in the profile's sweep order (money → races → lifecycle first on
the flagship stack). For each: specify, or **cut with the stated reason** in the spec's Cut column.
Silent gaps are the failure mode; loud cuts are craft. States table (F-030s), lifecycle lines + delete
matrix (F-040s), validation rules (F-050s), races + idempotency (F-060s), money map (F-070s ⚠),
notifications table (F-080s), abuse surface enumerated (F-090s → Bastion for severity), i18n/timezones
(F-100s), a11y floors (F-110s), metrics (F-120s), platform deltas (F-130s), rollout definitions
(F-140s → Relay for mechanics), API contract if the profile applies it (F-150s).

Non-feature discoveries: park in the Parked & Routed table (F-161) or dispatch per
`reference/handoff-protocol.md` if blocking.

```
[████████████░░░░░░░░] 60% — Step 3/5: Dimensions swept — specified or cut aloud
```

### 4. Write the acceptance criteria

Given/When/Then per `reference/acceptance-criteria.md`: the spine's success, every data/money-changing
exit, the commit race, double-submit, the delete rows, the money outcomes. ⚠-mark the money/auth/
deletion criteria for human approval. Assemble everything into `templates/feature-spec-template.md`.

```
[████████████████░░░░] 80% — Step 4/5: Criteria written, spec assembled
```

### 5. Lint, deliver, stop

Run `scripts/spec_lint.py` against the spec (or apply its checks by hand in chat-only contexts) — clear
the leads or justify them. Deliver the spec with the Parked & Routed table and the honesty line:

> *Complete definition: every applied dimension specified or cut with reason. Not a build, test, or
> security verdict — that's Cairn/Anvil/Bastion. ⚠ items await your approval.*

Declare the weave done. **Stop** (F-162).

```
[████████████████████] 100% — Step 5/5: Fabric delivered — weave closed
```
