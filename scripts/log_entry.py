#!/usr/bin/env python3
"""Append a structured daily-log entry, then commit the diary.

Prompts for barriers, facilitators, emotion, and a short reflection.
Reads the first-commit time for today from git log (the objective measure of the
target behaviour), appends a row to data/daily-log.csv and a section to diary/log.md,
then commits the diary (the second commit of the day).
"""
import csv
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "daily-log.csv"
LOG = ROOT / "diary" / "log.md"

FIELDS = [
    "date", "day_number", "first_commit_time", "sprint_completed",
    "in_window", "worked_example", "bi_techniques_used", "trigger_cue",
    "barriers", "facilitators", "emotion", "reflection", "plan_version",
]

START_DATE = date(2026, 7, 1)  # Day 1


def first_commit_today(today_iso: str) -> str:
    """Return HH:MM of the first commit made today (across the whole repo), or ''."""
    res = subprocess.run(
        ["git", "log", "--pretty=format:%aI"],
        cwd=ROOT, capture_output=True, text=True,
    )
    for line in res.stdout.splitlines():
        if "T" in line and line.startswith(today_iso):
            return line.split("T", 1)[1][:5]  # HH:MM
    return ""


def prompt(msg: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    val = input(f"{msg}{suffix}: ").strip()
    return val or default


def main() -> None:
    today = date.today()
    today_iso = today.isoformat()
    day_number = (today - START_DATE).days + 1

    fc = first_commit_today(today_iso)
    if fc:
        hh = int(fc.split(":")[0])
        in_window = "yes" if 8 <= hh < 10 else "no"
    else:
        in_window = ""

    print(f"Date: {today_iso} (Day {day_number})")
    print(f"First commit today: {fc or '(none yet — commit your practice first!)'}")

    sprint = prompt("Sprint completed? (yes/no)", "yes" if fc else "no")
    worked = prompt("Worked example done? (yes/no)", "yes" if fc else "no")
    bi = prompt("BI techniques used (comma-sep)",
                "implementation-intentions,self-monitoring")
    cue = prompt("Trigger/cue (what started the session?)", "morning coffee cue")
    barriers = prompt("Barriers (comma-sep, or blank)")
    facilitators = prompt("Facilitators (comma-sep, or blank)")
    emotion = prompt("Emotion 1-5 (1=low,5=high)", "3")
    reflection = input("Reflection (1-2 sentences): ").strip()
    plan_version = prompt("plan_version", "v1")

    row = {
        "date": today_iso,
        "day_number": day_number,
        "first_commit_time": fc,
        "sprint_completed": sprint,
        "in_window": in_window,
        "worked_example": worked,
        "bi_techniques_used": bi,
        "trigger_cue": cue,
        "barriers": barriers,
        "facilitators": facilitators,
        "emotion": emotion,
        "reflection": reflection,
        "plan_version": plan_version,
    }

    # append CSV
    exists = DATA.exists()
    with DATA.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if not exists:
            w.writeheader()
        w.writerow(row)

    # append log.md
    with LOG.open("a") as f:
        f.write(f"\n## {today_iso} — Day {day_number}\n\n")
        f.write(f"- **First commit:** {fc or '—'}  | in 8–10am window: **{in_window or '?'}**\n")
        f.write(f"- **Sprint completed:** {sprint} | **Worked example:** {worked}\n")
        f.write(f"- **BI techniques:** {bi}\n")
        f.write(f"- **Cue:** {cue}\n")
        f.write(f"- **Barriers:** {barriers or '—'}\n")
        f.write(f"- **Facilitators:** {facilitators or '—'}\n")
        f.write(f"- **Emotion (1-5):** {emotion}\n")
        f.write(f"- **Reflection:** {reflection or '—'}\n")

    print(f"Appended to {DATA} and {LOG}")
    print("Committing diary entry...")
    subprocess.run(["git", "add", str(DATA), str(LOG)], cwd=ROOT)
    subprocess.run(
        ["git", "commit", "-m", f"diary: day {day_number} ({today_iso})"],
        cwd=ROOT,
    )
    print("Done.")


if __name__ == "__main__":
    main()
