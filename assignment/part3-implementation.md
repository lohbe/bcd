# Part 3 — Implementing Your Nudging Plan & Creating Your Behavioural Diary

> Target length: **~300 words + diary in appendix.**

## How the BI techniques were combined into a self-nudging plan

The two techniques form a closed loop: **implementation intentions + habit stacking**
*initiate* the behaviour at a fixed cue, and **self-monitoring** *closes the feedback loop*
so the plan can be revised. The combination is designed through the **EAST** lens
(Behavioural Insights Team, 2014):

- **Easy** — the repository is pre-set-up; `python scripts/new_day.py` scaffolds the day's
  folder, so the first action is opening a file, not deciding what to do.
- **Attractive** — worked examples (not "study") are intrinsically rewarding and produce a
  tangible artefact (a commit).
- **Social** — a public git history is a visible commitment device to self.
- **Timely** — the 8–10am window and the coffee cue make the nudge time-locked.

**The if–then plan:** *"After I pour my coffee at 08:00, I will open the editor and start a
25-minute sprint, then commit."* **The monitoring plan:** log the entry via
`scripts/log_entry.py` immediately after.

## Implementation over 3 weeks (and plan changes)

<!-- ~150 words. Update this section as the 3 weeks unfold. Cross-reference diary/plan-changes.md. -->

- **Week 1 (Days 1–7):** baseline plan as above. Ran `new_day.py` → sprint → commit →
  `log_entry.py` daily.
- **Week 2 (Days 8–14):** <!-- note any adjustments if barriers recur >5–7 days -->
- **Week 3 (Days 15–21):** <!-- consolidation / tapering of reminders -->

> Per the brief, I committed to the original plan for at least 5–7 days before adjusting.
> Any changes to the BI techniques are documented in `diary/plan-changes.md` with rationale
> and the day number, and summarised here.

## Data collected & observations

<!-- What you tracked and what you saw. Reference charts/ PNGs. -->

- **Objective:** first-commit time per day (`scripts/first_commits.py` →
  `charts/first_commit_times.png`).
- **Structured:** `data/daily-log.csv` (sprint completed, in-window, cue, barriers,
  facilitators, emotion 1–5, reflection).
- **Reflective:** `diary/log.md` (daily) and `diary/weekly-reflections.md` (weekly).
- **Visuals:** `charts/weekly_adherence.png`, `charts/barriers.png` (see Part 4).

## Appendix — Behavioural Change Diary

The full diary is in:
- `diary/log.md` — daily logs
- `diary/weekly-reflections.md` — weekly reflections
- `diary/plan-changes.md` — documented BI changes + rationale
- `data/daily-log.csv` — structured quantitative data
- `data/plan-changes.csv` — change log
- `charts/` — generated visuals
