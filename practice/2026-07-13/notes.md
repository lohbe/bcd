# Worked example — 2026-07-13

## Goal
<!-- What concept/skill is today's worked example targeting? -->
graph analysis

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
graph thinking, in stages, with levels 1-4. 4 being similar to real-world complex queries.

## Worked example
<!-- The worked example / code goes here or in a sibling file -->

Level 1: Basic Queries
Simple property retrieval and filtering

Example 1.1: Find a country by name
MATCH (c:Country {name: 'Germany'})
RETURN c.name, c.iso3, c.total_export_amount, c.total_import_amount

Example 1.2: List top 10 countries by export volume
MATCH (c:Country)
RETURN c.name, c.total_export_amount
ORDER BY c.total_export_amount DESC
LIMIT 10

Example 1.3: Find countries with positive trade balance
MATCH (c:Country)
WHERE c.balance > 0
RETURN c.name, c.balance
ORDER BY c.balance DESC
LIMIT 5

Level 2: Intermediate Queries
Aggregations, relationships, and basic graph traversals

Example 2.1: Find all countries Germany exports to
MATCH (germany:Country {name: 'Germany'})-[:EXPORTS]->(partner:Country)
RETURN partner.name, partner.iso3
ORDER BY partner.name

Example 2.2: Calculate total exports from a country
MATCH (c:Country {name: 'Japan'})-[:EXPORTS]->(partner)
RETURN c.name, 
       count(partner) AS export_partners,
       sum(1) AS relationship_count

Example 2.3: Find trade partners with export amounts
MATCH (c:Country {name: 'United States'})-[:EXPORTS {amount: amount}]->(partner)
RETURN partner.name, amount
ORDER BY amount DESC
LIMIT 10

Level 3: Advanced Queries
Complex aggregations, pattern matching, and graph algorithms

Example 3.1: Find countries with highest total trade volume (imports + exports)
MATCH (c:Country)
RETURN c.name, 
       c.total_export_amount + c.total_import_amount AS total_trade_volume,
       c.balance
ORDER BY total_trade_volume DESC
LIMIT 10

Example 3.2: Find mutual trade relationships (countries that both import and export to each other)
MATCH (a:Country)-[:EXPORTS]->(b:Country),
      (b)-[:EXPORTS]->(a)
WHERE id(a) < id(b)
RETURN a.name AS country_a, b.name AS country_b
ORDER BY a.name
LIMIT 10

Example 3.3: Find the most connected trade hubs using PageRank
// Run PageRank algorithm to find most influential trade nodes
CALL algo.pageRank.stream() YIELD node, rank
RETURN node.name, rank
ORDER BY rank DESC
LIMIT 10

This is wrong. Use:

CALL pagerank.get() YIELD node, rank
RETURN node.name, rank
ORDER BY rank DESC
LIMIT 10



Level 4: Real-World Complex Query
Business intelligence scenario: Trade dependency analysis

Scenario:
Identify countries that are heavily dependent on imports from a single source, while also being major exporters themselves. This helps identify potential supply chain vulnerabilities.

// Step 1: Find countries with high import concentration
MATCH (importer:Country)<-[:IMPORTS {amount: import_amount}]-(supplier:Country)
WITH importer, supplier, import_amount,
     importer.total_import_amount AS total_imports
WHERE total_imports > 0
WITH importer, 
     collect({supplier: supplier.name, amount: import_amount}) AS import_sources,
     total_imports,
     importer.total_export_amount AS total_exports,
     importer.name AS importer_name
WITH importer_name, total_imports, total_exports, import_sources,
     max(import_sources.amount) AS max_import_from_single_source,
     size(import_sources) AS num_suppliers
// Step 2: Filter for high dependency (>30% from single source) AND significant exporter
WHERE (max_import_from_single_source / total_imports) > 0.3
  AND total_exports > 1000000000  // Over 1 billion in exports
// Step 3: Calculate dependency ratio and rank
RETURN importer_name AS country,
       total_exports AS export_volume,
       total_imports AS import_volume,
       max_import_from_single_source AS largest_import_source_amount,
       round((max_import_from_single_source / total_imports) * 100, 2) AS dependency_percentage,
       num_suppliers AS total_suppliers,
       round(total_exports / total_imports, 2) AS export_import_ratio
ORDER BY dependency_percentage DESC, export_volume DESC
LIMIT 15
What this query does:
Aggregates import data per country to find the largest single import source
Calculates dependency ratio (largest source / total imports)
Filters for countries with >30% dependency on one supplier AND >$1B in exports
Returns a risk profile showing export/import ratios and supplier concentration
Orders by highest dependency first, then by export volume
This type of query is useful for:

Supply chain risk assessment
Trade policy analysis
Identifying countries vulnerable to trade disruptions
Economic resilience planning

The above is wrong too, only Qwen3.7-max could solve it:

// Step 1: Find countries with high import concentration
MATCH (importer:Country)<-[r:IMPORTS]-(supplier:Country)
WITH importer, supplier, r.amount AS import_amount, importer.total_import_amount AS total_imports
WHERE total_imports > 0
WITH importer,
     collect({supplier: supplier.name, amount: import_amount}) AS import_sources,
     total_imports,
     importer.total_export_amount AS total_exports,
     importer.name AS importer_name,
     max(import_amount) AS max_import_from_single_source,
     count(supplier) AS num_suppliers
// Step 2: Filter for high dependency (>30% from single source) AND significant exporter
WHERE (max_import_from_single_source / total_imports) > 0.3
  AND total_exports > 100000
// Step 3: Calculate dependency ratio and rank
RETURN importer_name AS country,
       total_exports AS export_volume,
       total_imports AS import_volume,
       max_import_from_single_source AS largest_import_source_amount,
       round((max_import_from_single_source / total_imports) * 10000) / 100.0 AS dependency_percentage,
       num_suppliers AS total_suppliers,
       round(total_exports / total_imports * 100) / 100.0 AS export_import_ratio
ORDER BY dependency_percentage DESC, export_volume DESC
LIMIT 15

## Reflection
<!-- What did you learn? What was hard? -->
Even with a simple schema, one can derive quite a lot of information from it. More practice required to think about how to 1. find questions, 2. frame questions.
