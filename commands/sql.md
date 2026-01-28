---
name: sql
description: "SQL queries - generation, optimization, migration across dialects"
argument-hint: "\"natural language query\" [--dialect mysql|postgres|sqlite|tsql|snowflake]"
allowed-tools:
  - Read
  - Write
---

# SQL Assistant

Invoke the data-analyst:lang-sql skill for language-specific patterns.

For complex analysis, follow the data-analyst:data-workflow skill (brainstorm → plan → execute).

## Quick Mode

For simple requests (single query, syntax question, quick optimization): answer directly using lang-sql patterns.

## Capabilities

1. **Natural Language to SQL**: Convert requests into working queries
2. **Query Optimization**: Analyze and improve performance (EXPLAIN ANALYZE)
3. **Query Explanation**: Break down complex queries
4. **Migration**: Convert between dialects
5. **Schema Design**: Index strategy, partitioning, normalization

## Output Format

```markdown
## Analysis
[What the query does and approach]

## Code
```sql
-- Description
-- Dialect: [dialect]
[query]
` ` `

## Interpretation
[Expected results]

## Next Steps
[Index recommendations, variations]
```

## Language

Respond in the same language as the user.
