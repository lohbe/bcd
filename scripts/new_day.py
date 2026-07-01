#!/usr/bin/env python3
"""Scaffold a new practice folder for today.

Creates practice/YYYY-MM-DD/ with a notes.md prompt.
Does NOT commit — the practice commit is your measured behaviour (run after your sprint).
"""
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRACTICE = ROOT / "practice"


def main() -> None:
    today = date.today().isoformat()
    day_dir = PRACTICE / today
    if day_dir.exists():
        print(f"Today's folder already exists: {day_dir}")
    else:
        day_dir.mkdir(parents=True)
        print(f"Created: {day_dir}")

    notes = day_dir / "notes.md"
    if not notes.exists():
        notes.write_text(
            f"# Worked example — {today}\n\n"
            "## Goal\n<!-- What concept/skill is today's worked example targeting? -->\n\n"
            "## Approach\n<!-- e.g. graph thinking, functional approach, recursion, data structure -->\n\n"
            "## Worked example\n<!-- The worked example / code goes here or in a sibling file -->\n\n"
            "## Reflection\n<!-- What did you learn? What was hard? -->\n"
        )
        print(f"Created: {notes}")
    else:
        print(f"Notes already exist: {notes}")

    print("\nNext steps:")
    print(f"  1. Add your worked-example file(s) in {day_dir}")
    print("  2. Do the 25-minute sprint")
    print("  3. git add practice/ && git commit   <- this timestamp IS the measured behaviour")
    print("  4. python scripts/log_entry.py        <- record the diary entry")


if __name__ == "__main__":
    main()
