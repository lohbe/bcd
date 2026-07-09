# Worked example — 2026-07-09

## Goal
<!-- What concept/skill is today's worked example targeting? -->
Node filtering, relationship traversal and aggregation

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
Using a cities dataset in Memgraph

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
1. top 5 cities by population

MATCH (c:City)
WHERE c.population IS NOT NULL
RETURN c.name, c.country_name, c.population
ORDER BY c.population DESC
LIMIT 5;

2. List cities and it's border cities in France

MATCH (c:City {country_name: "France"})-[:BORDERS_WITH]->(c2:City)
RETURN c.name,c2.name;

3. List the 12 CONNECTS_WITH relations and find what it means

MATCH ()-[r:CONNECTS_WITH]->()
RETURN count(*);

MATCH (c1:City)-[:CONNECTS_WITH]->(c2:City)
RETURN c1.name AS City1, c1.country_name AS Country1, 
       c2.name AS City2, c2.country_name AS Country2
       ;

It seems like a relationship between cities in a country. Are they bordering cities?

MATCH (c1:City)-[:CONNECTS_WITH]->(c2:City)
OPTIONAL MATCH (c1)-[b:BORDERS_WITH]->(c2)
RETURN c1.name AS City1, 
       c1.country_name AS Country1, 
       c2.name AS City2, 
       c2.country_name AS Country2,
       b IS NOT NULL AS AlsoBorders
       ;

4. Countries with most cities in the dataset

MATCH (c:City)
RETURN c.country_name AS country, count(c) as count
ORDER BY count DESC
LIMIT 5;

## Reflection
<!-- What did you learn? What was hard? -->
My first aggregation query was a simple one. There were some basic queries I thought through and had some follow up, so I investigated those.
As usual, putting that curiousity requires me to think about the question clearly, then structuring it to fit the language.
I had to do it iteratively, to make it easier to reason about.
