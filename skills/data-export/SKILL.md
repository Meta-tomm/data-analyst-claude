---
name: data-export
description: "Use to generate offline cheatsheets and exportable documentation. Creates standalone MD/SQL files usable without Claude - query templates, quick references, procedure guides."
---

# Data Export

## Overview

Generate standalone documentation and cheatsheets that work offline. Export your knowledge into files you can use without Claude, share with colleagues, or print.

**Announce at start:** "I'm using the data-export skill to create exportable documentation."

**Output:** `exports/` folder with standalone files

## Export Types

### 1. SQL Cheatsheet

**Command:** `/data-analyst:export sql`

**Generates:** `exports/sql-cheatsheet-[dialect].md`

```markdown
# SQL Cheatsheet - [Dialect]

Generated: YYYY-MM-DD
Environment: [Company Name]

---

## Quick Reference

### Date Functions
```sql
-- Current date/time
SELECT CURRENT_DATE, CURRENT_TIMESTAMP;

-- Date truncation
SELECT DATE_TRUNC('month', order_date) as month;

-- Date arithmetic
SELECT order_date + INTERVAL '7 days';

-- Extract parts
SELECT EXTRACT(YEAR FROM order_date);
```

### Aggregations
```sql
-- Basic
SELECT
    category,
    COUNT(*) as count,
    SUM(amount) as total,
    AVG(amount) as average,
    MIN(amount) as min_val,
    MAX(amount) as max_val
FROM orders
GROUP BY category;

-- With filtering
SELECT category, SUM(amount)
FROM orders
GROUP BY category
HAVING SUM(amount) > 1000;
```

### Window Functions
```sql
-- Running total
SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING)

-- Rank
RANK() OVER (PARTITION BY category ORDER BY amount DESC)

-- Lag/Lead
LAG(amount, 1) OVER (ORDER BY date)
```

### CTEs
```sql
WITH monthly_sales AS (
    SELECT
        DATE_TRUNC('month', order_date) as month,
        SUM(amount) as revenue
    FROM orders
    GROUP BY 1
)
SELECT * FROM monthly_sales;
```

---

## Environment-Specific Queries

### [Database 1]
```sql
-- [Common query 1]
-- [Common query 2]
```

---

## Useful Patterns

### Null Handling
```sql
COALESCE(column, 'default')
NULLIF(column, '')
```

### String Operations
```sql
CONCAT(first_name, ' ', last_name)
UPPER(name), LOWER(name)
TRIM(column)
```
```

### 2. Domain Quick Reference

**Command:** `/data-analyst:export domain [name]`

**Generates:** `exports/domain-[name]-reference.md`

```markdown
# [Domain] Quick Reference

Generated: YYYY-MM-DD

---

## Key Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| orders | All orders | id, user_id, total, status |
| users | Customers | id, email, created_at |

## Key Metrics

| Metric | Formula | Query |
|--------|---------|-------|
| Revenue | Sum of completed orders | `SUM(total) WHERE status='completed'` |
| AOV | Revenue / Order count | `AVG(total) WHERE status='completed'` |

## Common Queries

### Daily Revenue
```sql
SELECT DATE(created_at), SUM(total)
FROM orders
WHERE status = 'completed'
GROUP BY 1;
```

### Top Customers
```sql
SELECT user_id, SUM(total) as lifetime_value
FROM orders
GROUP BY user_id
ORDER BY 2 DESC
LIMIT 10;
```

## Business Rules
1. [Rule 1]
2. [Rule 2]

## Contacts
- [Person]: [Domain expertise]
```

### 3. Procedure Guide

**Command:** `/data-analyst:export procedure [name]`

**Generates:** `exports/procedure-[name].md`

```markdown
# Procedure: [Name]

Generated: YYYY-MM-DD

---

## Purpose
[What this procedure accomplishes]

## Prerequisites
- [ ] Access to [system]
- [ ] [Other requirement]

## Steps

### Step 1: [Action]
[Detailed instructions]

```sql
-- Query to run
```

**Expected result:** [What you should see]

### Step 2: [Action]
[Detailed instructions]

### Step 3: [Action]
[Detailed instructions]

## Troubleshooting

| Problem | Solution |
|---------|----------|
| [Issue 1] | [Fix] |
| [Issue 2] | [Fix] |

## Contacts
If stuck, contact: [Person]
```

### 4. DAX Reference

**Command:** `/data-analyst:export dax`

**Generates:** `exports/dax-reference.md`

```markdown
# DAX Quick Reference

Generated: YYYY-MM-DD

---

## Aggregations
```dax
Total Sales = SUM(Sales[Amount])
Order Count = COUNTROWS(Orders)
Distinct Customers = DISTINCTCOUNT(Orders[CustomerID])
Average Order = AVERAGE(Orders[Total])
```

## Time Intelligence
```dax
-- Year to Date
YTD Sales = TOTALYTD([Total Sales], 'Date'[Date])

-- Previous Year
PY Sales = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))

-- Year over Year
YoY Growth = DIVIDE([Total Sales] - [PY Sales], [PY Sales])

-- Month to Date
MTD Sales = TOTALMTD([Total Sales], 'Date'[Date])
```

## Filters
```dax
-- With filter
Completed Sales = CALCULATE([Total Sales], Orders[Status] = "Completed")

-- Remove filter
All Sales = CALCULATE([Total Sales], ALL(Orders[Category]))

-- Keep filter
Filtered Sales = CALCULATE([Total Sales], KEEPFILTERS(Orders[Region]))
```

## Iterators
```dax
-- Row by row calculation
Weighted Avg = SUMX(Products, Products[Price] * Products[Weight]) / SUM(Products[Weight])
```

## Environment Measures
[Pre-built measures for your environment]
```

### 5. Full Knowledge Export

**Command:** `/data-analyst:export all`

**Generates:** `exports/knowledge-base-YYYY-MM-DD/`

```
exports/
  knowledge-base-2024-01-15/
    README.md                 # Index
    sql-cheatsheet.md
    domain-sales.md
    domain-marketing.md
    glossary.md
    contacts.md
    procedures/
      monthly-report.md
      data-refresh.md
```

## Export Options

```markdown
/data-analyst:export sql                    # SQL cheatsheet
/data-analyst:export sql snowflake          # Specific dialect
/data-analyst:export domain sales           # Domain reference
/data-analyst:export procedure "monthly"    # Procedure guide
/data-analyst:export dax                    # DAX reference
/data-analyst:export glossary               # Terms only
/data-analyst:export contacts               # Contacts only
/data-analyst:export all                    # Everything
```

## Sharing Exports

**With team:**
- Copy to shared drive
- Add to Confluence/Notion
- Commit to team repo

**Personal use:**
- Print for desk reference
- Save to phone/tablet
- Quick lookup without Claude

## Remember

- Exports are snapshots - regenerate when things change
- Include date in filename
- Adapt to what YOU need most
- Share useful exports with team

## Integration

**Called by:**
- `/data-analyst:export` command

**Uses:**
- **data-config** - SQL dialect, environment name
- **data-documentation** - Domain and table knowledge

**Pairs with:**
- **data-onboarding** - Export cheatsheets during onboarding
- **data-executing** - Export after completing analysis

## Language

Adapt to user's language (French or English).
