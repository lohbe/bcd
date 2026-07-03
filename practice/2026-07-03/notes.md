# Worked example — 2026-07-03

## Goal
<!-- What concept/skill is today's worked example targeting? -->
Today's goal expands on the podman-based memgraph lab.
A cypherlang worked example was created by memgraph's MCP server and a linked LLM.

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
The worked example is tailored to the built in Wikipedia dataset.

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
The first example given was 

```cypher
MATCH (a:Article)-[:CONTAINS]->(t:Term)
RETURN a.name AS article_name, count(t) AS term_count
ORDER BY term_count DESC
LIMIT 5
```
with the results

#	article_name	term_count	
1	
Bob Dylan
4,275
2	
Ireland
3,665
3	
Manila
2,765
4	
Laurence Olivier
2,681
5	
Mortimer Wheeler
2,666

and to modify the query to:

1. Filter by a specific article: WHERE a.name = "Machine Learning"
2. Include the relationship count property: RETURN a.name, t.name, r.count
3. Find categories with the most articles: MATCH (c:Category)-[:PARENT_OF]->(a:Article) RETURN c.name, count(a) AS article_count ORDER BY article_count DESC LIMIT 5

Solution 1

```cypher
MATCH (a:Article)
WHERE a.name = "Ireland"
RETURN a
```

#	a	
1	
{

: Article
} ID 249


Solution 2

```cypher
MATCH (a:Article)-[r:CONTAINS]->(t:Term)
WHERE a.name = "Ireland"
RETURN a.name, t.name, r.count
```

#	a.name	t.name	r.count	
1	
Ireland
Ireland
271
2	
Ireland
/ˈaɪərlənd/
2
3	
Ireland
listen
2
4	
Ireland
Irish
156
5	
Ireland
Éire
3

(... many rows)

```cypher
MATCH (a:Article)-[r:CONTAINS]->(t:Term)
WHERE a.name = "Ireland"
RETURN COUNT(*);
```

3665 to be exact.

Solution 3 is given, so I just modify it to search which categories a particular article is linked to:

```cypher
MATCH (c:Category)-[:PARENT_OF]->(a:Article {name:"Ireland"})
RETURN c.name, count(a) AS article_count 
ORDER BY article_count DESC 
LIMIT 5;
```
#	c.name	article_count	
1	
Article Feedback Pilot
1
2	
Divided regions
1


## Reflection
<!-- What did you learn? What was hard? -->
The queries are deceptively difficult to write.
Mental models need to change from joining tables to following relations, and crafting a 'legal' query.

