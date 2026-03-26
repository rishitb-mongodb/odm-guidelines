#!/usr/bin/env python3
"""
Update the ODM compliance triage counts in README.md.

For each ODM page in odms/, counts the number of guidelines with a non-Backlog
status (Done, In Progress, Won't Do) and updates the X/Y summary in README.md.
Y is derived from the number of .md files in guidelines/.

Run locally:   python scripts/update-compliance.py
Run in CI:     called by .github/workflows/update-compliance.yml
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
ODMS_DIR = REPO_ROOT / "odms"
GUIDELINES_DIR = REPO_ROOT / "guidelines"
README_PATH = REPO_ROOT / "README.md"

# Badge alt-text patterns that count as triaged
TRIAGED_STATUSES = {"Done", "In Progress", "Won't Do"}
BADGE_PATTERN = re.compile(r"!\[([^\]]+)\]\(https://img\.shields\.io/badge/")


def count_triaged(odm_file: Path) -> int:
    """Return the number of triaged (non-Backlog) guidelines in an ODM page."""
    content = odm_file.read_text(encoding="utf-8")
    statuses = BADGE_PATTERN.findall(content)
    return sum(1 for s in statuses if s in TRIAGED_STATUSES)


def main() -> int:
    if not ODMS_DIR.exists():
        print(f"ERROR: odms/ directory not found at {ODMS_DIR}", file=sys.stderr)
        return 1
    if not GUIDELINES_DIR.exists():
        print(f"ERROR: guidelines/ directory not found at {GUIDELINES_DIR}", file=sys.stderr)
        return 1
    if not README_PATH.exists():
        print(f"ERROR: README.md not found at {README_PATH}", file=sys.stderr)
        return 1

    total_guidelines = len(list(GUIDELINES_DIR.glob("*.md")))
    readme = README_PATH.read_text(encoding="utf-8")
    changed = False

    for odm_file in sorted(ODMS_DIR.glob("*.md")):
        stem = odm_file.stem
        triaged = count_triaged(odm_file)
        new_count = f"{triaged}/{total_guidelines}"

        # Match the ODM row in the README compliance table, e.g.:
        # | [Mongoose](odms/mongoose.md) | Node.js / JavaScript | 3/16 |
        pattern = re.compile(
            r"(\|\s*\[.*?\]\(odms/" + re.escape(stem) + r"\.md\)\s*\|[^|]*\|)\s*\d+/\d+\s*(\|)",
            re.MULTILINE,
        )
        updated, n = pattern.subn(rf"\g<1> {new_count} \2", readme)
        if n > 0 and updated != readme:
            readme = updated
            changed = True
            print(f"  {stem}: {new_count}")
        elif n == 0:
            print(f"  WARNING: no README row matched for '{stem}'", file=sys.stderr)

    if changed:
        README_PATH.write_text(readme, encoding="utf-8")
        print(f"\nREADME.md updated (total guidelines: {total_guidelines}).")
    else:
        print("README.md is already up to date.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
