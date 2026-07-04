# Worked example — 2026-07-04

## Goal
<!-- What concept/skill is today's worked example targeting? -->
graph content analysis, knowledge extraction and semantic search

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
Find the most frequently used technical terms across all articles in a specific category ("Mathematics")
With the wikipedia dataset.

## Worked example
<!-- The worked example / code goes here or in a sibling file -->

1. Find articles in a category
2. Extract terms from those articles
3. aggregate and rank terms across the category
4. Visualize top terms and articles

0. get schema of current graph
Nodes: Article, Term, Category
Relationships:
Category → PARENT_OF → Article
Article → CONTAINS → Term (with a count property)

this structure is good for graph databases excel at hierarchical traversal, content extraction, and aggregation across connections.

1. 

```cypher
MATCH (c:Category {name: 'Japanese judoka'})-[:PARENT_OF]->(a:Article)
RETURN a.name
LIMIT 5;
```

Mitsuyo Maeda

only 1 article - this is key, because the subsequent queries give the same results

2.

'single highest article'

```cypher
MATCH (c:Category {name: 'Japanese judoka'})-[:PARENT_OF]->(a:Article)-[r:CONTAINS]->(t:Term)
RETURN t.name, r.count AS termcount
ORDER BY termcount DESC
LIMIT 10;
```

modified the given example to show the top 10 highest frequency terms:
"What are the highest instances of a term appearing in a single article?"

3.
By including SUM(), you are grouping the data by the term's name. It asks: "What is the total combined count of this term across all articles in this category?"

'global aggregate'

```cypher
MATCH (c:Category {name: 'Japanese judoka'})-[:PARENT_OF]->(a:Article)-[r:CONTAINS]->(t:Term)
WITH t.name AS term, SUM(r.count) AS total_frequency
ORDER BY total_frequency DESC
LIMIT 10
RETURN term, total_frequency
```

4.

```cypher
MATCH (c:Category {name: 'Japanese judoka'})-[:PARENT_OF]->(a:Article)-[r:CONTAINS]->(t:Term)
WITH t, SUM(r.count) AS total_frequency
ORDER BY total_frequency DESC
LIMIT 5
MATCH (t)<-[r2:CONTAINS]-(a2:Article)
RETURN t.name AS term, total_frequency, collect(DISTINCT a2.name) AS related_articles
```

this query uses the top 5 terms, then traverse backwards <-:CONTAINS to find matching articles
collect(DISTINCT ...) gathers into a list.
showcases bidirectional traversal and how graphs naturally model many-to-many relationships

one of the related articles for the term 'judo' was 'Perry the Platypus' - which is interesting.
because the cartoon character is actually associate with judo.
"That was your last highly-improbable judo maneuver Perry the Platypus. I will now evaporate-inate you into non existence!"

## Reflection
<!-- What did you learn? What was hard? -->
i learnt about bidirectional traversal for many-to-many relationships in knowledge graphs. the 2 main difficulties are - thinking of a question, and then encoding the question into a query.

