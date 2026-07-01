#!/usr/bin/env python3
"""Print the first-commit time per day from git log.

The first commit of each day is the OBJECTIVE measure of the target behaviour
(a daily 25-min coding sprint between 8-10am). Usage: python scripts/first_commits.py
"""
import subprocess
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def first_commits() -> "OrderedDict[str, str]":
    res = subprocess.run(
        ["git", "log", "--reverse", "--pretty=format:%aI"],
        cwd=ROOT, capture_output=True, text=True,
    )
    out: "OrderedDict[str, str]" = OrderedDict()
    for line in res.stdout.splitlines():
        if "T" not in line:
            continue
        day, time = line.split("T", 1)
        if day not in out:
            out[day] = time[:5]  # HH:MM
    return out


def main() -> None:
    data = first_commits()
    print("date,first_commit_time,in_window_8_to_10")
    for day, t in data.items():
        hh = int(t.split(":")[0])
        in_window = "yes" if 8 <= hh < 10 else "no"
        print(f"{day},{t},{in_window}")


if __name__ == "__main__":
    main()
