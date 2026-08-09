# Contributing to Loom

Loom is open source (MIT) and authored by **Mohammed Nasher** ([@mhd-nasher](https://github.com/mhd-nasher)).
Contributions are welcome — Loom gets stronger the more real-world product surfaces it can spec well, the
sharper its sense of *which dimension to cut and why*, and the more failure modes its evals cover. It is part
of the [Forge](FORGE_DNA.md) suite: **Loom defines it**, Cairn designs it, Anvil proves it, Lens cleans it,
Bastion guards it, Relay ships it.

## Good contributions

- **New stack-feature profiles** in `reference/stack-feature-profiles.md` (APPLY/SUPPRESS/PARTIAL per
  dimension range for a stack Loom doesn't cover yet — a game, an embedded device, a data pipeline — with the
  reason stated for every suppression).
- **Sharper One-Weave guardrails** — the more precisely Loom distinguishes "this dimension must be specified"
  from "this dimension is a legitimate cut here," the more it's trusted. Tighten the Law and
  `reference/edge-case-hunting.md` so it never demands enterprise ceremony from a weekend tool — and never
  lets a money path ship with a silent gap.
- **More evals** in `evals/` — *especially* new `must_not` cases (things Loom must NOT do: invent requirements
  the product doesn't need, wander into a tangent mid-weave, keep talking after declaring done) **and** new
  `must_find` cases (a forgotten detail Loom must catch: a race, a delete cascade, an unhandled payment
  failure). Both directions keep it honest. A new `boundary` case (defers to Cairn/Anvil/Lens/Bastion/Relay)
  is just as valuable.
- **New checks** (next free ID in the relevant `F-###` range) — each with **Means / Why / Applies–Leave it
  alone when / Relates-to–Routes-to**, a **stack note saying when to SUPPRESS it**, and an eval. A dimension
  that can't say when it does *not* apply is dogma, not a check.
- **Worked examples** in `examples/` — vague ask → complete spec, or built feature → gap report, tagged with
  stable ids; showing the caught details, not just the format.
- **Plain-language / translation** improvements so more beginners can run the guided mode — Loom interviews
  in the user's own language, and its Arabic surface is a first-class citizen.

## How to contribute

1. Fork [github.com/mhd-nasher/loom](https://github.com/mhd-nasher/loom).
2. Make your change. Keep `SKILL.md` frontmatter minimal (`name`, `description`, `license` only).
3. Follow the skill-TDD loop in `evals/README.md`: add/adjust an eval, watch it **fail** without your change
   (RED), confirm it **passes** with it (GREEN), then tidy (REFACTOR). A check with no eval doesn't ship.
4. Open a pull request describing the change, the forgotten detail it catches (or the invented requirement it
   suppresses), and the eval that proves it.

## Ground rules

- **Stay stack-aware** — never add a dimension without saying *when to suppress it*. A rule that fires on a
  product it doesn't fit (i18n on a personal CLI, store-review constraints on a backend service) is noise,
  and noise is the thing the suite exists to kill.
- **Honor the One-Weave Law in the docs themselves** — every check, example, and workflow must respect one
  feature per run, explicit-cut-over-silent-gap, park-and-route for discoveries, and declare-done-then-stop.
  Don't add an example that wanders into a second feature or keeps selling work after the weave is complete.
  **Scope creep and invented requirements are bugs in Loom, not features.**
- **Be honest about scope** — Loom produces a complete *definition*, not a correctness or safety *guarantee*.
  Never add language that implies "fully specified = correct" or "audited by Loom = safe." A complete spec is
  what Anvil proves and Bastion guards; saying more is the false safety the suite is built to warn against.
- **Keep money/auth/deletion/crypto guidance human-in-the-loop.** Loom *proposes* what a payout, an access
  rule, or a delete cascade should do and explains why; the human approves. Don't add a check or example that
  silently decides sensitive behavior (Forge DNA §3.5).
- **Respect the boundary contract.** Loom owns the feature's definition only. Don't add a check that designs
  structure (Cairn), writes tests (Anvil), judges style (Lens), rates a vulnerability (Bastion), or plans a
  deploy (Relay) — route it to the owning sibling by name. **Every new `F-###` gets an eval.**

By contributing, you agree your contribution is licensed under the project's [MIT License](LICENSE).
