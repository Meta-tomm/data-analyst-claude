---
name: lang-sql
description: "Use when writing SQL queries. Covers PostgreSQL, MySQL, SQLite, T-SQL, Snowflake, BigQuery. Window functions, CTEs, optimization, indexing."
---

# SQL Reference

Best practices and patterns for SQL across dialects.

## Output Format

```markdown
## Analysis
[What the query does and approach]

## Code
```sql
-- Description
-- Dialect: [PostgreSQL/MySQL/SQLite/T-SQL/Snowflake]
[query]
```

## Interpretation
[Expected results]

## Next Steps
[Index recommendations, variations]
```

## Dialect Differences

### Date Functions
| Operation | PostgreSQL | MySQL | SQLite | T-SQL | Snowflake |
|-----------|------------|-------|--------|-------|-----------|
| Current date | CURRENT_DATE | CURDATE() | DATE('now') | GETDATE() | CURRENT_DATE |
| Month start | DATE_TRUNC('month', d) | DATE_FORMAT(d, '%Y-%m-01') | DATE(d, 'start of month') | DATEFROMPARTS(YEAR(d),MONTH(d),1) | DATE_TRUNC('month', d) |
| Add days | d + INTERVAL '7 days' | DATE_ADD(d, INTERVAL 7 DAY) | DATE(d, '+7 days') | DATEADD(day, 7, d) | DATEADD(day, 7, d) |
| Diff days | d1 - d2 | DATEDIFF(d1, d2) | JULIANDAY(d1)-JULIANDAY(d2) | DATEDIFF(day, d2, d1) | DATEDIFF(day, d2, d1) |

### String Functions
| Operation | PostgreSQL | MySQL | SQLite | T-SQL |
|-----------|------------|-------|--------|-------|
| Concat | col1 \|\| col2 | CONCAT(col1, col2) | col1 \|\| col2 | col1 + col2 |
| Substring | SUBSTRING(s,1,5) | SUBSTRING(s,1,5) | SUBSTR(s,1,5) | SUBSTRING(s,1,5) |

### Pagination
- Standard: LIMIT n OFFSET m
- T-SQL: OFFSET m ROWS FETCH NEXT n ROWS ONLY

## Common Patterns

### CTEs
```sql
WITH filtered AS (
    SELECT * FROM orders WHERE status = 'completed'
),
aggregated AS (
    SELECT customer_id, SUM(amount) as total
    FROM filtered GROUP BY customer_id
)
SELECT c.name, a.total
FROM aggregated a
JOIN customers c ON c.id = a.customer_id;
```

### Window Functions
```sql
-- Running total
SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING)

-- Rank
ROW_NUMBER() OVER (PARTITION BY category ORDER BY amount DESC)
RANK() OVER (PARTITION BY category ORDER BY amount DESC)
DENSE_RANK() OVER (PARTITION BY category ORDER BY amount DESC)

-- Lag/Lead
LAG(value, 1) OVER (ORDER BY date)
LEAD(value, 1) OVER (ORDER BY date)

-- Moving average
AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW)

-- Percent of total
amount * 100.0 / SUM(amount) OVER ()

-- Year-over-Year
LAG(value, 12) OVER (ORDER BY month)
```

### Deduplication
```sql
WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY key ORDER BY date DESC) as rn
    FROM table_name
)
SELECT * FROM ranked WHERE rn = 1;
```

### Conditional Aggregation
```sql
SELECT
    SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed,
    SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) as pending,
    COUNT(*) as total
FROM orders;
```

### Gap Analysis
```sql
WITH dates AS (
    SELECT DISTINCT DATE(created_at) as dt FROM events
),
all_dates AS (
    SELECT generate_series(MIN(dt), MAX(dt), '1 day')::date as dt FROM dates
)
SELECT a.dt as missing_date
FROM all_dates a
LEFT JOIN dates d ON a.dt = d.dt
WHERE d.dt IS NULL;
```

### Pivot (Generic CASE)
```sql
SELECT category,
    SUM(CASE WHEN month = 1 THEN total END) as jan,
    SUM(CASE WHEN month = 2 THEN total END) as feb,
    SUM(CASE WHEN month = 3 THEN total END) as mar
FROM monthly_sales GROUP BY category;
```

## Optimization

### Index Strategy
- Index columns in WHERE, JOIN, ORDER BY
- Composite index: match query column order
- Covering index: include SELECT columns
- Partial index (PostgreSQL): WHERE condition

### Query Optimization Checklist
1. EXPLAIN ANALYZE to check execution plan
2. Avoid SELECT * (select needed columns only)
3. Avoid functions on indexed columns in WHERE
4. EXISTS instead of IN for subqueries
5. UNION ALL instead of UNION when possible
6. Limit JOIN complexity
7. Partition large tables by date/range

### Anti-Patterns
| Bad | Good |
|-----|------|
| SELECT * | SELECT specific columns |
| WHERE YEAR(date) = 2024 | WHERE date >= '2024-01-01' AND date < '2025-01-01' |
| NOT IN (with NULLs) | NOT EXISTS |
| Correlated subquery in SELECT | JOIN or window function |
| UNION when UNION ALL works | UNION ALL |
| ORDER BY without LIMIT | Add LIMIT or remove ORDER BY |

## Language

Respond in the same language as the user.
