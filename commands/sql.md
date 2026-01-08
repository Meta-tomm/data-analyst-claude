---
name: sql
description: Generate or optimize SQL queries from natural language
argument-hint: "\"natural language query\" [--dialect mysql|postgres|sqlite]"
allowed-tools:
  - Read
  - Write
---

# SQL Assistant Command

Transform natural language requests into SQL queries, optimize existing queries, or explain complex SQL.

## Capabilities

1. **Natural Language to SQL**: Convert requests like "find customers who ordered more than 3 times this month" into working SQL
2. **Query Optimization**: Analyze and improve query performance
3. **Query Explanation**: Break down complex queries into understandable parts

## Workflow

### For Natural Language Requests

1. **Parse Intent**
   - Identify tables/entities mentioned
   - Identify filters, aggregations, joins needed
   - Clarify ambiguities if needed

2. **Generate Query**
   - Use appropriate dialect (default: PostgreSQL)
   - Include comments explaining each section
   - Use CTEs for complex logic

3. **Explain the Query**
   - What each part does
   - Assumptions made
   - Performance considerations

### For Optimization Requests

1. **Analyze Current Query**
   - Identify performance bottlenecks
   - Check for anti-patterns

2. **Propose Optimizations**
   - Index suggestions
   - Query rewrites
   - Explain improvements

### For Explanation Requests

1. **Break Down Query**
   - Step-by-step explanation
   - Data flow visualization
   - Expected results description

## Output Format

```markdown
## Analysis
[Brief summary of what the query does]

## Code
```sql
-- Query description
-- Dialect: [PostgreSQL/MySQL/SQLite]

WITH monthly_orders AS (
    -- Get orders from current month
    SELECT
        customer_id,
        COUNT(*) as order_count
    FROM orders
    WHERE order_date >= DATE_TRUNC('month', CURRENT_DATE)
    GROUP BY customer_id
)
SELECT
    c.customer_id,
    c.name,
    c.email,
    mo.order_count
FROM customers c
INNER JOIN monthly_orders mo ON c.customer_id = mo.customer_id
WHERE mo.order_count > 3
ORDER BY mo.order_count DESC;
```

## Interpretation
[What this query returns and how it works]

## Next Steps
- Index recommendations
- Query variations
- Related queries to consider
```

## SQL Dialect Differences

### Date Functions
| Operation | PostgreSQL | MySQL | SQLite |
|-----------|------------|-------|--------|
| Current date | CURRENT_DATE | CURDATE() | DATE('now') |
| Month start | DATE_TRUNC('month', date) | DATE_FORMAT(date, '%Y-%m-01') | DATE(date, 'start of month') |
| Add days | date + INTERVAL '7 days' | DATE_ADD(date, INTERVAL 7 DAY) | DATE(date, '+7 days') |

### String Functions
| Operation | PostgreSQL | MySQL | SQLite |
|-----------|------------|-------|--------|
| Concat | col1 \|\| col2 | CONCAT(col1, col2) | col1 \|\| col2 |
| Substring | SUBSTRING(col, 1, 5) | SUBSTRING(col, 1, 5) | SUBSTR(col, 1, 5) |

### Pagination
| Dialect | Syntax |
|---------|--------|
| All | LIMIT n OFFSET m |
| MySQL also | LIMIT m, n |

## Common Patterns

### Running Total
```sql
SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING)
```

### Year-over-Year
```sql
LAG(value, 12) OVER (ORDER BY month)
```

### Deduplication
```sql
ROW_NUMBER() OVER (PARTITION BY key ORDER BY date DESC) = 1
```

### Conditional Aggregation
```sql
SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END)
```

## Language

Respond in the same language as the user.
