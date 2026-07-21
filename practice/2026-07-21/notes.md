# Worked example — 2026-07-21

## Goal
<!-- What concept/skill is today's worked example targeting? -->
IaC (Infrastructure-as-Code) with ministack, terraform

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
declarative infrastructure provisioning with an 'emulated' or mock cloud service

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
see phase 1 in ~/git/ministack-learn, continuation from the previous days' example

## Reflection
<!-- What did you learn? What was hard? -->
the emulator does not simulate 100% the actual infrastructure, so the problems that arise may be due to the emulator, not the code I developed.
Troubleshooting such problems would be a bit trickier.
