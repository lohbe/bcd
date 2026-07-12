# Worked example — 2026-07-12

## Goal
<!-- What concept/skill is today's worked example targeting? -->
graph querying with cypher

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
aggregation, grouping
advanced pattern matching
real-world complex query

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
Level 1: The Basics (MATCH & RETURN)
Goal: Retrieve all teams in a specific league.

MATCH (t:Team)-[:PLAYS_IN]->(l:League {name: "Premier League"})
RETURN t.name
📖 Learning Points:

MATCH defines the pattern you want to find.
(t:Team) matches a node with label Team and aliases it as t.
{name: "Premier League"} filters the League node by property.
RETURN specifies what to output.

Level 2: Filtering & Sorting (WHERE, ORDER BY, LIMIT)
Goal: Find the top 5 most expensive transfers (ignoring free transfers).

MATCH (p:Player)-[:TRANSFERRED_IN]->(tr:Transfer)
WHERE tr.fee IS NOT NULL
RETURN p.name, tr.fee
ORDER BY tr.fee DESC
LIMIT 5
📖 Learning Points:

WHERE filters results. IS NOT NULL is crucial here because only ~31% of transfers have a recorded fee.
ORDER BY tr.fee DESC sorts highest to lowest.
LIMIT 5 restricts output to the top 5 rows.

Level 3: Traversing Relationships
Goal: Find all players who moved from Team A to Team B.

MATCH (src:Team {name: "Chelsea"})-[:TRANSFERRED_FROM]->(tr:Transfer)-[:TRANSFERRED_TO]->(dst:Team {name: "Arsenal"})
<-[:TRANSFERRED_IN]-(p:Player)
RETURN p.name, tr.year, tr.fee
📖 Learning Points:

Cypher reads like a diagram. Arrows -> and <- show relationship direction.
You can chain patterns: (src)-[:REL]->(mid)<-[:REL]-(dst)
This query reconstructs the full transfer path: Source Team → Transfer → Destination Team ← Player.


Level 4: Aggregation & Grouping (COUNT, SUM, AVG)
Goal: Calculate the average transfer fee per season.

MATCH (tr:Transfer)-[:HAPPENED_IN]->(s:Season)
WHERE tr.fee IS NOT NULL
RETURN s.name, 
       count(tr) AS total_transfers, 
       avg(tr.fee) AS average_fee
ORDER BY average_fee DESC

📖 Learning Points:

Aggregation functions (count, avg, sum, min, max) automatically group by non-aggregated columns in the RETURN clause.
AS aliases make column names readable.

Level 5: Advanced Pattern Matching & Path Variables
Goal: Find players who transferred multiple times in the same season.

MATCH (p:Player)-[:TRANSFERRED_IN]->(tr:Transfer)-[:HAPPENED_IN]->(s:Season)
WITH p, s, count(tr) AS transfer_count
WHERE transfer_count > 1
RETURN p.name, s.name, transfer_count
ORDER BY transfer_count DESC

📖 Learning Points:

WITH acts like a pipeline. It passes intermediate results to the next clause, allowing you to filter on aggregated values (WHERE transfer_count > 1).
This is essential for multi-step logic in Cypher.

Level 6: Real-World Complex Query
Goal: Find the most valuable transfer destination team per league.

MATCH (t:Team)-[:PLAYS_IN]->(l:League)<-[:TRANSFERRED_TO]-(tr:Transfer)
WHERE tr.fee IS NOT NULL
WITH l.name AS league, t.name AS team, sum(tr.fee) AS total_spent
ORDER BY league, total_spent DESC
WITH league, collect({team: team, spent: total_spent}) AS teams
RETURN league, teams[0].team AS top_spenders, teams[0].spent AS highest_spending

📖 Learning Points:

collect() aggregates rows into a list of maps.
teams[0] grabs the first item (highest spender due to ORDER BY).
Demonstrates how to solve "top-N per group" problems in graph databases.

NOTE: the above is wrong. corrected query

MATCH (tr:Transfer)-[:TRANSFERRED_TO]->(t:Team)-[:PLAYS_IN]->(l:League)
WHERE tr.fee IS NOT NULL
WITH l.name AS league, t.name AS team, sum(tr.fee) AS total_spent
ORDER BY league, total_spent DESC
WITH league, collect({team: team, spent: total_spent}) AS teams
RETURN league, teams[0].team AS top_spenders, teams[0].spent AS highest_spending;

## Reflection
<!-- What did you learn? What was hard? -->
Today's tips provided by Qwen was very useful. I liked the 'levels' of competence and will prompt accordingly in future.
The last query (level 6) is wrong and corrected.

