# Worked example — 2026-07-23

## Goal
<!-- What concept/skill is today's worked example targeting? -->
terraform/opentofu libvirt provider

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
declarative infrastructure provisioning, hcl syntax

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
see ~/git/terraform-learn

issues encountered:
1. libvirt provider detecting downloaded content differently from what we set.
2. libvirt provider thinks os.type is optional, but libvirt requires it.
3. permissions issue in qemu, so changed pool from images -> vm.

## Reflection
<!-- What did you learn? What was hard? -->
similarly from yesterday, a lot of time was spent troubleshooting instead of coding.
but this is probably necessary, given the complexity of the task.
