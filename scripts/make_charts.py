#!/usr/bin/env python3
"""Generate charts from the daily log + git first-commit times into charts/.

Outputs (PNG):
  - first_commit_times.png  first-commit time per day with 8-10am target band
  - weekly_adherence.png    weekly adherence %
  - barriers.png            barrier frequency
  - facilitators.png        facilitator frequency

Usage: python scripts/make_charts.py
"""
import csv
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "daily-log.csv"
CHARTS = ROOT / "charts"
CHARTS.mkdir(exist_ok=True)

_NIL = {"", "-", "—", "none", "n/a", "na"}


def _split(field: str) -> list:
    return [x.strip() for x in field.split(",") if x.strip().lower() not in _NIL]


def first_commits() -> dict:
    res = subprocess.run(
        ["git", "log", "--reverse", "--pretty=format:%aI"],
        cwd=ROOT, capture_output=True, text=True,
    )
    out = {}
    for line in res.stdout.splitlines():
        if "T" not in line:
            continue
        day, t = line.split("T", 1)
        if day not in out:
            hh, mm = t[:2], t[3:5]
            out[day] = int(hh) + (int(mm) / 60 if mm.isdigit() else 0)
    return out


def main() -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fc = first_commits()
    if fc:
        days = list(fc)
        times = [fc[d] for d in days]
        fig, ax = plt.subplots(figsize=(10, 5))
        colors = ["green" if 8 <= t < 10 else "red" for t in times]
        ax.scatter(range(len(days)), times, c=colors, zorder=3)
        ax.axhspan(8, 10, color="green", alpha=0.1, label="Target 8–10am")
        ax.set_xticks(range(len(days)))
        ax.set_xticklabels([d[5:] for d in days], rotation=45, ha="right", fontsize=8)
        ax.set_ylabel("First commit time (hour)")
        ax.set_title("First commit time per day")
        ax.legend()
        fig.tight_layout()
        fig.savefig(CHARTS / "first_commit_times.png", dpi=120)
        plt.close(fig)
        print(f"saved charts/first_commit_times.png ({len(days)} days)")

    if not DATA.exists():
        print("No daily-log.csv yet; skipping diary-based charts.")
        return
    rows = list(csv.DictReader(DATA.open()))
    if not rows:
        return

    # weekly adherence
    weeks: dict = {}
    for r in rows:
        try:
            dnum = int(r["day_number"])
        except (ValueError, KeyError):
            continue
        wk = (dnum - 1) // 7 + 1
        weeks.setdefault(wk, []).append(r["sprint_completed"].strip().lower() == "yes")
    if weeks:
        fig, ax = plt.subplots(figsize=(6, 4))
        labels = [f"Week {k}" for k in weeks]
        vals = [100 * sum(v) / len(v) for v in weeks.values()]
        ax.bar(labels, vals, color="steelblue")
        ax.set_ylabel("Adherence %")
        ax.set_ylim(0, 100)
        ax.set_title("Weekly adherence")
        fig.tight_layout()
        fig.savefig(CHARTS / "weekly_adherence.png", dpi=120)
        plt.close(fig)
        print("saved charts/weekly_adherence.png")

    # barriers
    barriers = Counter()
    for r in rows:
        barriers.update(_split(r["barriers"]))
    if barriers:
        fig, ax = plt.subplots(figsize=(7, 4))
        items = list(barriers.most_common())[::-1]
        ax.barh([k for k, _ in items], [v for _, v in items], color="indianred")
        ax.set_xlabel("Frequency")
        ax.set_title("Barriers")
        fig.tight_layout()
        fig.savefig(CHARTS / "barriers.png", dpi=120)
        plt.close(fig)
        print("saved charts/barriers.png")

    # facilitators
    facilitators = Counter()
    for r in rows:
        facilitators.update(_split(r["facilitators"]))
    if facilitators:
        fig, ax = plt.subplots(figsize=(7, 4))
        items = list(facilitators.most_common())[::-1]
        ax.barh([k for k, _ in items], [v for _, v in items], color="seagreen")
        ax.set_xlabel("Frequency")
        ax.set_title("Facilitators")
        fig.tight_layout()
        fig.savefig(CHARTS / "facilitators.png", dpi=120)
        plt.close(fig)
        print("saved charts/facilitators.png")

    print(f"\nAll charts in {CHARTS}")


if __name__ == "__main__":
    main()
