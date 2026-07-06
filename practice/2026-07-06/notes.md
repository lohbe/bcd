# Worked example — 2026-07-06

## Goal
<!-- What concept/skill is today's worked example targeting? -->
Graph databases, cypher language

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
Step-by-step examples for queries, filtering, traversal, aggregation, etc

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
1. Find all articles (return 10)

MATCH (a:Article)
RETURN a.name
LIMIT 10

2. Find all terms (return 10)

MATCH (t:Term)
RETURN t.name
LIMIT 10

3. Find all categories (return 10)

MATCH (c:Category)
RETURN c.name
LIMIT 10;

4. Find articles with specific names

MATCH (a:Article)
WHERE a.name CONTAINS 'Maeda'
RETURN a.name;

5. Terms with high frequency


MATCH (a:Article)-[r:CONTAINS]->(t:Term)
WHERE r.count > 100
RETURN t.name, r.count
ORDER BY r.count DESC
LIMIT 10

6. Find all terms contained in an article

MATCH (a:Article {name: 'Mitsuyo Maeda'})-[:CONTAINS]->(t:Term)
RETURN t.name
LIMIT 20

7. Fnd  category of article

MATCH (c:Category)-[:PARENT_OF]->(a:Article {name: 'Mitsuyo Maeda'})
RETURN c.name;

8. Count terms per article

MATCH (a:Article)-[:CONTAINS]->(t:Term)
RETURN a.name, count(t) AS term_count
ORDER BY term_count DESC
LIMIT 10;

9. Find articles connected through shared terms

MATCH (a1:Article)-[:CONTAINS]->(t:Term)<-[:CONTAINS]-(a2:Article)
WHERE a1.name <> a2.name
RETURN a1.name, a2.name, t.name
LIMIT 10;

10. Find category -> article -> term paths

MATCH (c:Category)-[:PARENT_OF]->(a:Article)-[:CONTAINS]->(t:Term)
WHERE c.name = 'Japanese judoka'
RETURN c.name, a.name, t.name
LIMIT 10;

11. articles with terms appearing more than 50 times

MATCH (a:Article)-[r:CONTAINS]->(t:Term)
WHERE r.count > 50
RETURN a.name, t.name, r.count
ORDER BY r.count DESC
LIMIT 10;

12. Categories with most articles

MATCH (c:Category)-[:PARENT_OF]->(a:Article)
RETURN c.name, count(a) AS article_count
ORDER BY article_count DESC
LIMIT 10;

13. Find most connected terms (i.e. appearing in many articles)

MATCH (t:Term)<-[:CONTAINS]-(a:Article)
RETURN t.name, count(a) AS article_count
ORDER BY article_count DESC
LIMIT 10;

14. Articles that share most terms

MATCH (a1:Article)-[:CONTAINS]->(t:Term)<-[:CONTAINS]-(a2:Article)
WHERE a1.name < a2.name
WITH a1, a2, collect(t.name) AS shared_terms
RETURN a1.name, a2.name, size(shared_terms) AS shared_term_count, shared_terms
ORDER BY shared_term_count DESC
LIMIT 5;

## Reflection
<!-- What did you learn? What was hard? -->
Today's exercises were comprehensive and varied, spanning a number of functions. It started easy, but gradually became more advanced, and time was quickly used up.
