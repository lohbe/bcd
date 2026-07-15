# Worked example — 2026-07-15

## Goal
<!-- What concept/skill is today's worked example targeting? -->
visualising graphs and using GDS python client

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
using bokeh the visualisation library to showcase some graphs, networkx and neo4j GDS driver

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
The base worked example is here: https://neo4j.com/blog/developer/get-started-with-neo4j-gds-python-client/

modified from ipython -> marimo and seaborn to bokeh

see ~/git/gds-bokeh

i spotted isolated graphs immediately in neo4j desktop 2. For bokeh, i needed to use spectral layout. But bokeh does offer different types of viz through networkx.

## Reflection
<!-- What did you learn? What was hard? -->
Today I was late, having watched the FIFA WC2026 late into wee hours of the morning.
The combination of neo4j, networkx, bokeh and gds make it quite involved to get a graph viz running.
I compared it with neo4j desktop 2, which has fewer options for visualisations, and it still appears more aesthetic and useable than bokeh.
