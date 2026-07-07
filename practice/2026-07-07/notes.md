# Worked example — 2026-07-07

## Goal
<!-- What concept/skill is today's worked example targeting? -->
Cypher graph query language, with some nesting/chaining

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
graph thinking, with a bit of statistics

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
1. Find categories with the highest number of articles

MATCH (c:Category)-[p:PARENT_OF]->(a:Article)
RETURN c.name, count(a) as article_count
ORDER BY article_count DESC
LIMIT 10


2. Find top 10 frequent terms in the category with highest article count

// 1. Find the Category with the most articles
MATCH (c:Category)-[p:PARENT_OF]->(a:Article)
WITH c, count(a) as article_count
ORDER BY article_count DESC
LIMIT 1

// 2. Pipe that specific Category 'c' forward to find its top 10 terms
MATCH (c)-[:PARENT_OF]->(a:Article)-[rel:CONTAINS]->(t:Term)
RETURN c.name, article_count, t.name, sum(rel.count) AS freq
ORDER BY freq DESC
LIMIT 10;

or, using subqueries (CALL)

## Reflection
<!-- What did you learn? What was hard? -->
Learnt how to do a chained query. It was difficult to form the query in my head, but breaking it down step by step while working backwards helped. In this case, it was 1. highest article count first, then 2. frequent terms in (1).
