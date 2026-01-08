---
name: data-discovery
description: "Use when exploring a new data environment. Maps data sources, explores schemas, identifies key tables and relationships. Essential for onboarding in a new company or project."
---

# Data Discovery

## Overview

Systematically explore and map an unknown data environment. Build understanding of what data exists, where it lives, and how it's structured.

**Announce at start:** "I'm using the data-discovery skill to explore this data environment."

**Output:** `docs/discovery/` folder with mapping files

## The Process

### Step 1: Environment Inventory

**Ask one question at a time:**

1. "What data systems do you have access to?" (databases, data warehouses, BI tools, files)
2. "Do you have connection strings/credentials ready?"
3. "Is there existing documentation I should know about?"

**Create initial inventory:**

```markdown
# Data Environment Inventory

Created: YYYY-MM-DD
Status: In Progress

## Systems Identified

| System | Type | Access Status | Priority |
|--------|------|---------------|----------|
| [Name] | PostgreSQL/Snowflake/etc | Connected/Pending | High/Medium/Low |

## Contacts

| Person | Role | Knows About |
|--------|------|-------------|
| [Name] | [Role] | [Systems/domains] |
```

Save to: `docs/discovery/00-inventory.md`

### Step 2: Schema Exploration

**For each database/warehouse:**

```sql
-- List all schemas
SELECT schema_name FROM information_schema.schemata;

-- List tables per schema
SELECT table_schema, table_name, table_type
FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema', 'pg_catalog')
ORDER BY table_schema, table_name;

-- Row counts (approximate for large tables)
SELECT schemaname, relname, n_live_tup as row_count
FROM pg_stat_user_tables
ORDER BY n_live_tup DESC
LIMIT 50;
```

**Adapt for specific dialects:**
- Snowflake: `SHOW SCHEMAS; SHOW TABLES;`
- SQL Server: `sys.schemas`, `sys.tables`
- BigQuery: `INFORMATION_SCHEMA.TABLES`

**Document findings:**

```markdown
# [Database Name] Schema Map

Explored: YYYY-MM-DD

## Overview

- **Total schemas:** X
- **Total tables:** Y
- **Largest tables:** [list]

## Schema: [schema_name]

### Purpose
[What this schema seems to contain]

### Key Tables

| Table | Rows (approx) | Description | Key Columns |
|-------|---------------|-------------|-------------|
| users | 1.2M | Customer accounts | id, email, created_at |
| orders | 5.4M | All orders | id, user_id, total, status |

### Relationships Identified
- orders.user_id → users.id
- [other FKs]
```

Save to: `docs/discovery/[database-name]-schema.md`

### Step 3: Data Profiling

**For key tables, run profiling queries:**

```sql
-- Column analysis
SELECT
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_name = '[table]';

-- Value distribution (categorical)
SELECT [column], COUNT(*) as cnt
FROM [table]
GROUP BY [column]
ORDER BY cnt DESC
LIMIT 20;

-- Numeric stats
SELECT
    MIN([column]) as min_val,
    MAX([column]) as max_val,
    AVG([column]) as avg_val,
    COUNT(DISTINCT [column]) as distinct_count,
    COUNT(*) - COUNT([column]) as null_count
FROM [table];

-- Date range
SELECT
    MIN([date_column]) as earliest,
    MAX([date_column]) as latest
FROM [table];
```

**Document in table profile:**

```markdown
## Table: [table_name]

### Columns

| Column | Type | Nullable | Distinct Values | Sample Values |
|--------|------|----------|-----------------|---------------|
| status | varchar | No | 5 | pending, active, cancelled... |

### Data Quality Notes
- [Column X] has 15% nulls
- [Column Y] has outliers beyond expected range
- Date coverage: 2020-01-01 to present

### Business Context
[What you learned about what this data represents]
```

### Step 4: Quick Wins Identification

**Identify immediately useful data:**

```markdown
# Quick Wins

## Ready-to-Use Tables
Tables that are clean and immediately useful:
- [table1]: [why useful]
- [table2]: [why useful]

## Needs Attention
Tables that need cleaning or understanding:
- [table3]: [issue]
- [table4]: [issue]

## Questions for Team
- What is the difference between [table_a] and [table_b]?
- Where does [metric] come from?
- Who owns the [domain] data?
```

Save to: `docs/discovery/quick-wins.md`

## Output Structure

```
docs/
  discovery/
    00-inventory.md         # Master inventory
    [db-name]-schema.md     # Per-database schema maps
    [domain]-profile.md     # Detailed profiling
    quick-wins.md           # Actionable findings
    questions.md            # Open questions for team
```

## Dialect-Specific Queries

### PostgreSQL
```sql
-- Table sizes
SELECT relname, pg_size_pretty(pg_total_relation_size(relid))
FROM pg_catalog.pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;
```

### Snowflake
```sql
-- Table metadata
SELECT table_schema, table_name, row_count, bytes
FROM information_schema.tables
ORDER BY bytes DESC;
```

### SQL Server
```sql
-- Table info
SELECT s.name as schema_name, t.name as table_name,
       SUM(p.rows) as row_count
FROM sys.tables t
JOIN sys.schemas s ON t.schema_id = s.schema_id
JOIN sys.partitions p ON t.object_id = p.object_id
WHERE p.index_id IN (0, 1)
GROUP BY s.name, t.name;
```

## Remember

- One system at a time
- Document as you go
- Note questions immediately
- Identify contacts for each domain
- Don't try to understand everything at once
- Focus on high-priority/frequently-used tables first

## Next Steps

After discovery, use:
- `/document` to formalize findings
- `/lineage` to trace data flows
- `/onboard` for full onboarding workflow

## Integration

**Called by:**
- `/data-analyst:discover` command
- **data-onboarding** - Phase 2: Discovery

**Chains to:**
- **data-documentation** - Document findings after discovery
- **data-lineage** - Trace flows for complex tables

**Pairs with:**
- **data-config** - Uses SQL dialect from config
- **data-describe** - Safe data sharing during discovery

## Language

Adapt to user's language (French or English).
