# Behavioural Change Diary

> **Date range:** 2026-07-01 → ~2026-07-21 (21 days)
> **Target behaviour:** 25-min coding sprint / worked example between 8–10am, measured by
> the first commit of the day.

## BI techniques used (track effectiveness)

| # | Technique (BCT) | Implementation | Status |
|---|---|---|---|
| 1 | Implementation intentions + habit stacking (1.4) | "After coffee at 08:00 → open editor → 25-min sprint → commit" | active (v1) |
| 2 | Self-monitoring (2.3) | `data/daily-log.csv` + `diary/log.md` + first-commit timestamp | active (v1) |

Cross-cutting lens: **EAST** (Easy pre-setup / Attractive worked examples / Social git history / Timely 8–10am window).

## How to log (daily)

1. Do the sprint → `git commit` (the practice) — *this is the measured behaviour*.
2. `python scripts/log_entry.py` — appends today's row to `data/daily-log.csv` and a
   section to `diary/log.md`, then commits the diary (second commit of the day).

## Schema legend (`data/daily-log.csv`)

| field | meaning |
|---|---|
| date | YYYY-MM-DD |
| day_number | 1 = 2026-07-01 |
| first_commit_time | HH:MM of first commit that day (objective measure) |
| sprint_completed | yes / no |
| in_window | yes if first commit 08:00–09:59 |
| worked_example | yes / no |
| bi_techniques_used | comma-sep list |
| trigger_cue | what started the session |
| barriers | comma-sep, free text |
| facilitators | comma-sep, free text |
| emotion | 1 (low) – 5 (high) |
| reflection | 1–2 sentences |
| plan_version | v1, v2, … (matches plan-changes.md) |

## Plan-version log

| version | effective from | change | rationale | see |
|---|---|---|---|---|
| v1 | Day 1 (2026-07-01) | baseline plan | initial design | `diary/plan-changes.md` |

(Add a row whenever the BI techniques change, after at least 5–7 days on the prior version.)
