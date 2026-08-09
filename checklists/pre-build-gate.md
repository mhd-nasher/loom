# Pre-Build Gate — The Short Gate Before Code

> Seven items a feature passes **before code is written**. Relay may run this gate as a pipeline's
> spec-stage; Loom owns the items (Forge DNA §4 — the owner defines, the neighbor fulfills). Format:
> every item has a runnable check and its catalogue IDs. **A single failed ⚠ item blocks the build —
> don't negotiate it down.** Non-⚠ failures are P1 debts: build may start, the debt is written.

- [ ] **F-GATE-001** — The feature is ONE feature with a named goal and a written out-of-scope list.
  *Check:* the spec's feature card states one goal sentence and ≥1 explicit exclusion (or "nothing
  excluded — stated").
  *ID:* F-001, F-002

- [ ] **F-GATE-002** — Every actor is enumerated with capabilities.
  *Check:* the actor matrix exists; admin/support/guest each appear as a row or as an explicit cut.
  *ID:* F-010, F-011

- [ ] **F-GATE-003** — Every flow step has an unhappy exit, and the commit point is guarded.
  *Check:* the flow map shows ≥1 non-forward exit per spine step; exactly one ★ commit with staleness
  re-check + double-submit guard noted.
  *ID:* F-021, F-028, F-062, F-063

- [ ] **F-GATE-004** — The state × screen table is complete.
  *Check:* every screen row has all eight states specified or cut with reason; no empty cells.
  *ID:* F-030…F-036

- [ ] **F-GATE-005** [⚠] — The delete story is defined before the first record exists.
  *Check:* the delete matrix answers soft/hard, cascades, others-still-see, undo — and carries the
  human's approval mark.
  *ID:* F-041, F-042, F-043

- [ ] **F-GATE-006** [⚠] — If money moves, the money path is fully specified.
  *Check:* the money map shows every hop; failure/refund/receipt rows filled; commission server-side;
  human approval on refund policy. (No money → this gate is "cut: no money moves", stated.)
  *ID:* F-070…F-076

- [ ] **F-GATE-007** — The spec is lint-clean and the parked list exists.
  *Check:* `python3 scripts/spec_lint.py <spec>.md` exits 0 (or each lead is justified in writing);
  the Parked & Routed table is present; acceptance criteria cover the minimum set.
  *ID:* F-161, F-162, plus `../reference/acceptance-criteria.md` coverage rule

---

**Passing this gate means the definition is complete — nothing more.** Correctness is Anvil's evidence,
safety is Bastion's verdict, structure is Cairn's design; the gate keeps the promise honest (Forge DNA
§3.4).
