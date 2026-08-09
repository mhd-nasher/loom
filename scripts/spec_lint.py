#!/usr/bin/env python3
"""
spec_lint.py — Loom's silent-gap finder for feature specs.

Reads a feature spec (a markdown file shaped like `templates/feature-spec-template.md`, or any spec that
uses Loom's conventions) and flags **silent gaps** — the places where a dimension was neither specified
nor explicitly cut with a reason. It exists because the One-Weave Law's whole point is "specified or cut
aloud, never skipped silently" — and a human eye slides right past an empty section at review time.

What it checks:
    1. empty-section        A dimension heading exists but its body is blank or placeholder-only.
    2. silent-gap           A known dimension section is missing entirely AND no `Cut:` line covers it.
    3. happy-only-flow      The flow section has spine steps but no unhappy tokens (error/cancel/abandon/
                            declined/timeout/conflict/…) — the easy-20% smell (F-021).
    4. placeholder-debt     TBD / TODO / `<fill>` / `???` / template angle-bracket stubs left in the body.
    5. malformed-criteria   An acceptance-criteria block whose entries lack Given+When+Then.
    6. missing-parked       No "Parked & Routed" section and no "none parked" declaration (F-161).

IMPORTANT — what this is and isn't:
    A flag is a **lead, not a verdict** (the suite's No-False-Alarm Law). An empty money section on a
    feature where no money moves is CORRECT — *if* the spec says `Cut: no money moves`. The tool cannot
    judge whether a cut's reason is good, whether a criterion is meaningful, or whether the spec matches
    the product. A human (or Loom in session) judges every lead; the tool only guarantees nothing was
    skipped *silently*.

Usage:
    python3 spec_lint.py <spec.md> [--json] [--quiet]
    python3 spec_lint.py --self-test          # run built-in correctness tests and exit

Exit codes:
    0  no leads — every dimension specified or cut aloud
    1  at least one lead found (review them; a justified cut clears it by being written down)
    2  usage / IO error
    3  --self-test failed

The pre-build gate runs this as F-GATE-007 (`checklists/pre-build-gate.md`); Relay may wire it into a
pipeline's spec stage — Loom owns the check, Relay owns the pipeline (Forge DNA §4).
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional

# --------------------------------------------------------------------------------------
# The dimension sections a Loom-shaped spec declares, with the F-ranges they carry.
# A section is satisfied by EITHER a real body OR an explicit `Cut: <reason>` mention.
# --------------------------------------------------------------------------------------

DIMENSION_SECTIONS = [
    ("Actors",        r"actors?\s*(&|and)?\s*permissions?",           "F-010…F-015"),
    ("User flows",    r"user\s+flows?|flows?\s*\(f-02",               "F-020…F-028"),
    ("States",        r"^states?\b",                                   "F-030…F-037"),
    ("Data lifecycle", r"data\s+lifecycle|lifecycle\s*\(f-04",         "F-040…F-047"),
    ("Validation",    r"validation\s*(&|and)?\s*limits?",              "F-050…F-056"),
    ("Concurrency",   r"concurrency|races?\s*(&|and)|idempotency",     "F-060…F-065"),
    ("Money path",    r"money\s+path|money\s*\(f-07",                  "F-070…F-076"),
    ("Notifications", r"notifications?",                               "F-080…F-085"),
    ("Abuse surface", r"abuse|misuse",                                 "F-090…F-094"),
    ("Acceptance criteria", r"acceptance\s+criteria",                  "AC coverage"),
]

PLACEHOLDER_RE = re.compile(
    r"(?i)\bTBD\b|\bTODO\b|\?\?\?|<fill[^>]*>|<answer[^>]*>|<one sentence[^>]*>|<[a-z][a-z /+·—-]{0,60}>"
)
CUT_RE = re.compile(r"(?i)\bcut\s*:\s*\S|\bsuppress(ed)?\b.{0,40}\breason|—\s*cut\b")
UNHAPPY_TOKENS_RE = re.compile(
    r"(?i)error|fail|declin|cancel|abandon|timeout|offline|expire|conflict|reject|retry|no\s+slots?|unhappy"
)
SPINE_STEP_RE = re.compile(r"^\s*\d+\.\s+\S", re.MULTILINE)
PARKED_RE = re.compile(r"(?i)parked\s*(&|and)?\s*routed|none\s+parked")
GWT_G_RE = re.compile(r"(?i)\bgiven\b")
GWT_W_RE = re.compile(r"(?i)\bwhen\b")
GWT_T_RE = re.compile(r"(?i)\bthen\b")


@dataclass
class Lead:
    rule: str          # one of the six check names
    section: str       # the dimension/section concerned
    detail: str        # one line: what was seen / not seen
    ids: str           # the F-range it concerns

    def line(self) -> str:
        return f"  LEAD  {self.rule:<18} {self.section:<22} {self.detail}  [{self.ids}]"


def split_sections(text: str) -> List[tuple]:
    """Return (heading, body) pairs for every markdown heading of level 1-3."""
    parts = re.split(r"(?m)^(#{1,3}\s+.*)$", text)
    out = []
    # parts: [pre, h1, body1, h2, body2, ...]
    for i in range(1, len(parts) - 1, 2):
        heading = re.sub(r"^#{1,3}\s+", "", parts[i]).strip()
        out.append((heading, parts[i + 1]))
    if len(parts) % 2 == 0 and len(parts) >= 2:  # trailing heading with no body
        heading = re.sub(r"^#{1,3}\s+", "", parts[-1]).strip()
        out.append((heading, ""))
    return out


def body_is_empty(body: str) -> bool:
    """A body is empty if, after stripping table scaffolding and placeholders, nothing remains.

    Table *scaffolding* (a header row + its |---| separator) is not content — only data rows and
    prose are. A section holding just an unfilled table skeleton is exactly the silent gap this
    linter exists to catch.
    """
    stripped = PLACEHOLDER_RE.sub("", body)
    stripped = re.sub(r"(?m)^\s*\|.*\|\s*\n\s*\|[\s|:\-]+\|?\s*$", "", stripped)  # header+separator pairs
    stripped = re.sub(r"(?m)^\s*\|[\s|:\-]*\|?\s*$", "", stripped)                # stray separator rows
    stripped = re.sub(r"(?m)^\s*\|.*\|\s*$",
                      lambda m: "" if not re.search(r"[A-Za-z؀-ۿ]{3}",
                                                    re.sub(r"[|\s\-:*]", "", m.group(0)))
                      else m.group(0),
                      stripped)                                                   # empty-celled data rows
    stripped = re.sub(r"(?m)^\s*```.*$", "", stripped)                            # fence markers
    return not re.search(r"[A-Za-z؀-ۿ]{3}", stripped)


def scan_spec(text: str) -> List[Lead]:
    leads: List[Lead] = []
    sections = split_sections(text)
    lowered = [(h.lower(), h, b) for h, b in sections]

    # 1 & 2 — per-dimension: present-but-empty, or absent-with-no-cut
    for name, pattern, ids in DIMENSION_SECTIONS:
        matches = [(h, b) for hl, h, b in lowered if re.search(pattern, hl)]
        if matches:
            heading, body = matches[0]
            has_cut = CUT_RE.search(heading) or CUT_RE.search(body)
            if body_is_empty(body) and not has_cut:
                leads.append(Lead("empty-section", name,
                                  "heading exists, body is blank/placeholder and not cut aloud", ids))
        else:
            if not CUT_RE.search(text) or name.lower() not in text.lower():
                leads.append(Lead("silent-gap", name,
                                  "no section and no `Cut:` line mentions it", ids))

    # 3 — happy-only flow
    flow_bodies = [b for hl, h, b in lowered if re.search(r"user\s+flows?|flows?\s*\(f-02", hl)]
    for body in flow_bodies:
        if SPINE_STEP_RE.search(body) and not UNHAPPY_TOKENS_RE.search(body):
            leads.append(Lead("happy-only-flow", "User flows",
                              "spine steps present but no unhappy exit token anywhere", "F-021"))

    # 4 — placeholder debt (whole document)
    debt = PLACEHOLDER_RE.findall(text)
    if debt:
        leads.append(Lead("placeholder-debt", "whole spec",
                          f"{len(debt)} placeholder(s) left (TBD/TODO/<stub>)", "—"))

    # 5 — malformed criteria: AC entries missing any of G/W/T
    ac_bodies = [b for hl, h, b in lowered if re.search(r"acceptance\s+criteria", hl)]
    for body in ac_bodies:
        entries = re.split(r"(?m)^\s*AC-\d+\s*", body)[1:]
        for i, entry in enumerate(entries, 1):
            if not (GWT_G_RE.search(entry) and GWT_W_RE.search(entry) and GWT_T_RE.search(entry)):
                leads.append(Lead("malformed-criteria", f"AC entry {i}",
                                  "missing one of Given/When/Then", "acceptance-criteria.md"))

    # 6 — parked list presence
    if not PARKED_RE.search(text):
        leads.append(Lead("missing-parked", "Parked & Routed",
                          "no Parked & Routed section and no 'none parked' declaration", "F-161"))

    return leads


def report(leads: List[Lead], path: str, as_json: bool, quiet: bool) -> str:
    if as_json:
        return json.dumps({"spec": path, "leads": [asdict(l) for l in leads],
                           "count": len(leads)}, indent=2, ensure_ascii=False)
    lines = []
    if not quiet:
        lines.append(f"spec_lint — {path}")
        for l in leads:
            lines.append(l.line())
    lines.append(f"Summary: {len(leads)} lead(s). A lead is not a verdict — a written `Cut: <reason>` "
                 f"clears a dimension legitimately; review each before treating it as a gap.")
    return "\n".join(lines)


# --------------------------------------------------------------------------------------
# Self-test: proves the linter catches each gap type and stays quiet on a clean spec.
# --------------------------------------------------------------------------------------

CLEAN_SPEC = """# Feature Spec — Demo
## Actors & permissions
| Actor | Sees | Creates |
|---|---|---|
| Customer | own bookings | booking |
## User flows
1. Pick a slot -> no slots? -> empty state
2. Pay -> declined? -> error state, retry offered
## States
Empty teaches next step; loading skeleton; error names the way out.
## Data lifecycle
Booking: created -> confirmed -> archived(90d). Delete: soft, cascades frozen.
## Validation & limits
| Field | Rules | On violation |
|---|---|---|
| amount | 1..500 GBP, 2dp | inline message |
## Concurrency & idempotency
Double-tap: one charge via idempotency key. Commit re-verifies slot.
## Money path
Customer pays 50, platform keeps 15%, provider transfer 42.50. Refund window 24h.
## Notifications
| Event | Who | Channel |
|---|---|---|
| confirmed | both sides | push |
## Abuse surface
Slot hoarding without payment -> routed to Bastion.
## Acceptance criteria
AC-1  Given one slot and two buyers
      When both pay concurrently
      Then exactly one booking exists
## Parked & Routed
| Finding | Owner |
|---|---|
| hold logic placement | Cairn |
"""

SILENT_GAP_SPEC = CLEAN_SPEC.replace("## Money path\nCustomer pays 50, platform keeps 15%, provider transfer 42.50. Refund window 24h.\n", "")
EMPTY_SECTION_SPEC = CLEAN_SPEC.replace(
    "## States\nEmpty teaches next step; loading skeleton; error names the way out.",
    "## States\n| Screen | Empty |\n|---|---|\n")
HAPPY_ONLY_SPEC = CLEAN_SPEC.replace(
    "1. Pick a slot -> no slots? -> empty state\n2. Pay -> declined? -> error state, retry offered",
    "1. Pick a slot\n2. Pay\n3. Confirmation shown")
DEBT_SPEC = CLEAN_SPEC.replace("Refund window 24h.", "Refund window TBD.")
BAD_AC_SPEC = CLEAN_SPEC.replace(
    "AC-1  Given one slot and two buyers\n      When both pay concurrently\n      Then exactly one booking exists",
    "AC-1  Two buyers pay at once and it should work correctly")
NO_PARKED_SPEC = CLEAN_SPEC.replace("## Parked & Routed\n| Finding | Owner |\n|---|---|\n| hold logic placement | Cairn |\n", "")
CUT_SPEC = SILENT_GAP_SPEC.replace("## Abuse surface",
                                   "Money path — Cut: no money moves in this feature.\n## Abuse surface")


def self_test() -> int:
    cases = [
        ("clean spec -> 0 leads",              CLEAN_SPEC,        None),
        ("removed money section -> silent-gap", SILENT_GAP_SPEC,  "silent-gap"),
        ("blank states body -> empty-section",  EMPTY_SECTION_SPEC, "empty-section"),
        ("no unhappy tokens -> happy-only",     HAPPY_ONLY_SPEC,  "happy-only-flow"),
        ("TBD left -> placeholder-debt",        DEBT_SPEC,        "placeholder-debt"),
        ("AC without G/W/T -> malformed",       BAD_AC_SPEC,      "malformed-criteria"),
        ("no parked table -> missing-parked",   NO_PARKED_SPEC,   "missing-parked"),
        ("cut aloud clears the gap",            CUT_SPEC,         None),
    ]
    failures = 0
    for desc, text, expected_rule in cases:
        leads = scan_spec(text)
        rules = {l.rule for l in leads}
        if expected_rule is None:
            ok = not leads
            got = f"leads={sorted(rules)}" if leads else "clean"
        else:
            ok = expected_rule in rules
            got = f"leads={sorted(rules)}"
        print(f"  {'PASS' if ok else 'FAIL'}  {desc} ({got})")
        if not ok:
            failures += 1
    print(f"\nSelf-test: {'ALL PASSED' if failures == 0 else f'{failures} FAILED'}")
    return 0 if failures == 0 else 3


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Loom's silent-gap finder — leads, not verdicts.",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("spec", nargs="?", help="Path to a feature spec markdown file.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of the text report.")
    parser.add_argument("--quiet", action="store_true", help="Only print the summary line.")
    parser.add_argument("--self-test", action="store_true",
                        help="Run built-in correctness tests and exit.")
    args = parser.parse_args()

    if args.self_test:
        return self_test()
    if not args.spec:
        parser.print_usage(sys.stderr)
        print("error: provide a spec file or --self-test", file=sys.stderr)
        return 2
    path = Path(args.spec)
    if not path.is_file():
        print(f"error: no such file: {path}", file=sys.stderr)
        return 2
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        print(f"error: cannot read {path}: {e}", file=sys.stderr)
        return 2

    leads = scan_spec(text)
    print(report(leads, str(path), args.json, args.quiet))
    return 1 if leads else 0


if __name__ == "__main__":
    sys.exit(main())
