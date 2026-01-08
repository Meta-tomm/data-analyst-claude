# SQL Optimization Techniques

## Index Usage

### When to Create Indexes

- Columns in WHERE clauses
- Columns in JOIN conditions
- Columns in ORDER BY
- Columns with high selectivity (many unique values)

### Index Types

```sql
-- B-tree (default, most common)
CREATE INDEX idx_name ON table(column);

-- Composite index (order matters)
CREATE INDEX idx_multi ON table(col1, col2);

-- Partial index (PostgreSQL)
CREATE INDEX idx_active ON users(email) WHERE active = true;

-- Covering index (all needed columns)
CREATE INDEX idx_cover ON orders(customer_id) INCLUDE (order_date, total);
```

## Query Optimization Patterns

### Avoid SELECT *

```sql
-- Bad
SELECT * FROM orders WHERE customer_id = 1;

-- Good
SELECT order_id, order_date, total FROM orders WHERE customer_id = 1;
```

### Use EXISTS Instead of IN for Subqueries

```sql
-- Less efficient
SELECT * FROM customers
WHERE id IN (SELECT customer_id FROM orders WHERE total > 1000);

-- More efficient
SELECT * FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o
    WHERE o.customer_id = c.id AND o.total > 1000
);
```

### Avoid Functions on Indexed Columns

```sql
-- Bad (can't use index on created_at)
SELECT * FROM orders WHERE YEAR(created_at) = 2024;

-- Good (can use index)
SELECT * FROM orders
WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01';
```

### Use UNION ALL Instead of UNION

```sql
-- UNION removes duplicates (slower)
SELECT id FROM table1 UNION SELECT id FROM table2;

-- UNION ALL keeps all rows (faster)
SELECT id FROM table1 UNION ALL SELECT id FROM table2;
```

## Join Optimization

### Join Order

Put smaller tables or more restrictive conditions first:

```sql
SELECT o.*, c.name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id
WHERE o.order_date > '2024-01-01'  -- Filters first
```

### Avoid Cartesian Products

```sql
-- Dangerous (no join condition)
SELECT * FROM table1, table2;

-- Explicit join required
SELECT * FROM table1 CROSS JOIN table2;  -- Only if intentional
```

## Aggregation Patterns

### Pre-filter Before Aggregating

```sql
-- Filter first, then aggregate
SELECT customer_id, SUM(total)
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY customer_id;

-- Not: aggregate everything then filter with HAVING
```

### Use HAVING Only for Aggregate Conditions

```sql
-- Good: filter rows with WHERE, aggregates with HAVING
SELECT customer_id, COUNT(*) as order_count
FROM orders
WHERE status = 'completed'
GROUP BY customer_id
HAVING COUNT(*) > 5;
```

## Common Table Expressions (CTEs)

### Readable Complex Queries

```sql
WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', order_date) as month,
        SUM(total) as revenue
    FROM orders
    GROUP BY 1
),
growth AS (
    SELECT
        month,
        revenue,
        LAG(revenue) OVER (ORDER BY month) as prev_revenue
    FROM monthly_sales
)
SELECT
    month,
    revenue,
    (revenue - prev_revenue) / prev_revenue * 100 as growth_pct
FROM growth;
```

## Window Functions

### Avoid Self-Joins with Window Functions

```sql
-- Instead of self-join for running total
SELECT
    order_date,
    total,
    SUM(total) OVER (ORDER BY order_date) as running_total
FROM orders;

-- Rank within groups
SELECT
    category,
    product_name,
    sales,
    RANK() OVER (PARTITION BY category ORDER BY sales DESC) as rank
FROM products;
```

## EXPLAIN Analysis

### Reading EXPLAIN Output

```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 1;
```

Key metrics to watch:
- **Seq Scan**: Full table scan (bad for large tables)
- **Index Scan**: Using index (good)
- **Nested Loop**: OK for small result sets
- **Hash Join**: Good for larger joins
- **Sort**: Memory usage for ORDER BY
- **Rows**: Estimated vs actual row counts

## Pagination

### Efficient Pagination

```sql
-- Offset pagination (slow for large offsets)
SELECT * FROM orders ORDER BY id LIMIT 20 OFFSET 10000;

-- Keyset pagination (faster)
SELECT * FROM orders
WHERE id > 10000
ORDER BY id
LIMIT 20;
```

## Batch Operations

### Batch Inserts

```sql
-- Single insert (slow)
INSERT INTO table VALUES (1, 'a');
INSERT INTO table VALUES (2, 'b');

-- Batch insert (faster)
INSERT INTO table VALUES
    (1, 'a'),
    (2, 'b'),
    (3, 'c');
```

### Batch Updates

```sql
-- Use CASE for multiple conditions
UPDATE products
SET price = CASE
    WHEN category = 'A' THEN price * 1.1
    WHEN category = 'B' THEN price * 1.05
    ELSE price
END
WHERE category IN ('A', 'B');
```
