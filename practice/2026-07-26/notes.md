# Worked example — 2026-07-26

## Goal
<!-- What concept/skill is today's worked example targeting? -->
opentofu/terraform libvirt provisioning

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
declarative infrastructure management

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
see ~/git/terraform-learn

## Reflection
<!-- What did you learn? What was hard? -->
destruction of environments with tofu destroy. destruction completeness depends on how the resources were built. not difficult, but one is required to understand the underlying resources and how they interact (architecture). so a good design would necessarily require understanding.
