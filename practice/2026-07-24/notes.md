# Worked example — 2026-07-24

## Goal
<!-- What concept/skill is today's worked example targeting? -->
understanding bash history

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
configuring shell environment variables

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
in ~/.bashrc.d/history.bashrc

# Configuration for Bash history settings

# Keep a massive history in memory and on disk
HISTSIZE=100000
HISTFILESIZE=100000

# Ignore duplicate commands and commands starting with a space
HISTCONTROL=ignoreboth

# Append to history file instead of overwriting on shell exit
shopt -s histappend

# Save multi-line commands as a single history entry
shopt -s cmdhist

# Add timestamps to history entries (YYYY-MM-DD HH:MM:SS)
HISTTIMEFORMAT="%F %T "

## Reflection
<!-- What did you learn? What was hard? -->
this was a quick lesson on how bash history is kept in memory and on-disk.
larger history means data management considerations need to be prioritised, for example, using append-only - otherwise the whole file is recreated on exit
