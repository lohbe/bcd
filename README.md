# Behaviour Change Diary (BCD)

A self-nudging project to establish a habitual daily coding practice, scaffolded as a git
repository so that **the first commit of each day is the objective measure of the target
behaviour**.

## Target behaviour

> Initiate a 25-minute coding sprint or worked example between 8–10am daily,
> measured by the timestamp of the first commit of the day.

- **Day 1**: 2026-07-01
- **Window**: 21 days (through ~2026-07-21)
- **SMART**: Specific (sprint/worked example), Measurable (first-commit time),
  Achievable (25 min), Relevant (computational/graph/functional thinking), Time-bound (21 days).

## Why a git repo?

This single repository holds **both** the diary **and** the actual daily practice. So
`git log` of one repo cleanly yields the first-commit-of-day timestamp — no aggregation
across repos, no manual recording, no self-report bias on the timing measure.

## Daily workflow

1. **Scaffold the day** (optional, creates a folder + prompt):
   ```
   python scripts/new_day.py
   ```
2. **Do the 25-minute sprint / worked example** inside `practice/YYYY-MM-DD/`.
3. **Commit the practice** — this timestamp IS the measured behaviour:
   ```
   git add practice/ && git commit -m "practice: day N - <topic>"
   ```
4. **Log the diary entry** (prompts for barriers/mood/reflection, appends CSV + log.md,
   and commits the diary as a *second* commit):
   ```
   python scripts/log_entry.py
   ```

So: **first commit of day = the behaviour**, **second commit = the self-monitoring record**.
Clean separation.

## Review & visualise

- `python scripts/first_commits.py` — prints first-commit time per day (the objective data).
- `python scripts/analyze.py` — adherence %, streaks, barrier/facilitator/emotion frequencies.
- `python scripts/make_charts.py` — writes PNGs into `charts/` for the Parts 3–4 write-ups.

## Structure

```
assignment/   the 4-part write-up + references
practice/     daily worked examples / sprints (committing this = the measured behaviour)
diary/        append-only daily log, plan changes, weekly reflections
data/         structured CSV tracking
scripts/      automation
charts/       generated visuals (evidence for Parts 3–4)
evidence/     screenshots of GenAI prompts/outputs for the AI-usage statement
```

## BI techniques (self-nudging plan)

1. **Implementation intentions + habit stacking** (BCT 1.4, Action planning)
2. **Self-monitoring** (BCT 2.3) — the diary + the commit timestamp

EAST is used as a cross-cutting *design lens* (Easy / Attractive / Social / Timely) in Part 3,
not as a third technique.

## Setup

```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
