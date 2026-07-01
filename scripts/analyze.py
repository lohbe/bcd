#!/usr/bin/env python3
"""Summarise the daily log: adherence %, streaks, barrier/facilitator/emotion frequencies.

Usage: python scripts/analyze.py
"""
import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "daily-log.csv"

_NIL = {"", "-", "—", "none", "n/a", "na"}


def _split(field: str) -> list:
    return [x.strip() for x in field.split(",") if x.strip().lower() not in _NIL]


def main() -> None:
    if not DATA.exists():
        print("No data yet. Run log_entry.py after your first sprint.")
        return
    rows = list(csv.DictReader(DATA.open()))
    n = len(rows)
    if n == 0:
        print("daily-log.csv is empty.")
        return
    completed = sum(1 for r in rows if r["sprint_completed"].strip().lower() == "yes")
    in_window = sum(1 for r in rows if r["in_window"].strip().lower() == "yes")
    print(f"Total logged days : {n}")
    print(f"Sprint completed  : {completed}/{n} ({100*completed/n:.0f}%)")
    print(f"In 8-10am window  : {in_window}/{n} ({100*in_window/n:.0f}%)")

    streak = best = 0
    for r in rows:
        if r["sprint_completed"].strip().lower() == "yes":
            streak += 1
            best = max(best, streak)
        else:
            streak = 0
    print(f"Best streak       : {best}")

    barriers = Counter()
    for r in rows:
        barriers.update(_split(r["barriers"]))
    if barriers:
        print("\nBarriers:")
        for b, c in barriers.most_common():
            print(f"  {b}: {c}")

    facilitators = Counter()
    for r in rows:
        facilitators.update(_split(r["facilitators"]))
    if facilitators:
        print("\nFacilitators:")
        for f, c in facilitators.most_common():
            print(f"  {f}: {c}")

    emo = [int(r["emotion"]) for r in rows if r["emotion"].strip().isdigit()]
    if emo:
        print(f"\nMean emotion (1-5): {sum(emo)/len(emo):.2f}")


if __name__ == "__main__":
    main()
