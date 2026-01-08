---
name: data-lineage
description: "Use when tracing data flows - understanding where data comes from, how it's transformed, and where it goes. Essential for debugging, impact analysis, and understanding complex data pipelines."
---

# Data Lineage

## Overview

Trace data flows from source to destination. Understand transformations, dependencies, and impact of changes.

**Announce at start:** "I'm using the data-lineage skill to trace this data flow."

**Output:** `docs/lineage/` folder with flow documentation

## When to Use

- "Where does this number come from?"
- "What happens if I change this table?"
- "Why is this metric different from that one?"
- "What feeds this dashboard?"
- Debugging data quality issues
- Planning migrations or changes

## The Process

### Step 1: Identify the Target

**Ask:**
1. What specific data point/metric/table are we tracing?
2. Upstream (where it comes from) or downstream (where it goes)?
3. How far do we need to trace?

### Step 2: Trace Upstream (Source → Target)

**For a metric/dashboard:**
```markdown
## Metric: [Name]

### Dashboard Location
- Tool: [Tableau/Power BI/etc.]
- Dashboard: [Name]
- Visual: [Chart/Card name]

### Immediate Source
- Query/Dataset: [Name]
- Table(s): [List]

### Query Logic
```sql
-- The actual query or calculation
SELECT ...
```

### Source Tables
For each table, trace further:
- Where does [table] come from?
- Is it a raw table or derived?
- What transforms it?
```

**For a table:**
```markdown
## Table: [schema.table_name]

### Classification
- [ ] Raw (direct from source system)
- [ ] Staging (cleaned/standardized)
- [ ] Intermediate (business logic applied)
- [ ] Mart (aggregated/ready for analysis)

### If Raw
- **Source System:** [Salesforce, App DB, etc.]
- **Ingestion:** [Fivetran, Airbyte, custom ETL]
- **Frequency:** [Real-time, hourly, daily]

### If Derived
- **Upstream Tables:**
  - [table1] → [columns used]
  - [table2] → [columns used]
- **Transformation:**
  - Tool: [dbt, Airflow, stored proc]
  - Location: [file/job name]
  - Logic: [brief description]
```

### Step 3: Trace Downstream (Target → Consumers)

```markdown
## Downstream of: [table_name]

### Direct Dependents

| Object | Type | Usage |
|--------|------|-------|
| daily_revenue | Table | Aggregates from this |
| sales_dashboard | Dashboard | Main revenue chart |
| weekly_report | Email | Pulls totals |

### Queries Using This Table
```sql
-- Found in: [location]
SELECT ... FROM [table]
```

### Impact Assessment
If this table changes:
- [X objects] would be affected
- [Critical: list critical downstream]
- [Notify: list owners to notify]
```

### Step 4: Document the Flow

**Visual format:**

```markdown
## Data Flow: [Name]

### Diagram

```
[Source System]
       ↓
   [Raw Table]
       ↓ (ETL: Fivetran)
  [Staging Table]
       ↓ (Transform: dbt)
   [Mart Table]
       ↓
[Dashboard] ← [Metric A]
            ← [Metric B]
```

### Flow Details

| Step | Object | Tool | Frequency | Owner |
|------|--------|------|-----------|-------|
| 1 | Salesforce.Opportunity | Source | - | Sales |
| 2 | raw.salesforce_opportunities | Fivetran | 15min | Data Eng |
| 3 | staging.opportunities | dbt | Hourly | Analytics |
| 4 | marts.sales_pipeline | dbt | Hourly | Analytics |
| 5 | Pipeline Dashboard | Tableau | Live | Sales Ops |
```

Save to: `docs/lineage/[flow-name].md`

## Common Patterns

### BI Tool → Source
```
Dashboard
    ↓ (data source)
Dataset/Extract
    ↓ (query)
Database Table(s)
    ↓ (trace further if derived)
...
```

### ETL Pipeline
```
Source System (OLTP)
    ↓ (extract)
Landing/Raw Layer
    ↓ (clean/standardize)
Staging Layer
    ↓ (business logic)
Integration/Intermediate
    ↓ (aggregate)
Marts/Reporting Layer
    ↓ (consume)
BI Tools / Exports
```

### dbt Project
```sql
-- Find model dependencies
-- In dbt: dbt docs generate → view DAG
-- Or check ref() calls in model files
```

## Investigation Queries

### Find table dependencies (PostgreSQL)
```sql
-- Views depending on a table
SELECT dependent_ns.nspname as dependent_schema,
       dependent_view.relname as dependent_view
FROM pg_depend
JOIN pg_rewrite ON pg_depend.objid = pg_rewrite.oid
JOIN pg_class as dependent_view ON pg_rewrite.ev_class = dependent_view.oid
JOIN pg_namespace dependent_ns ON dependent_view.relnamespace = dependent_ns.oid
WHERE pg_depend.refobjid = '[schema.table]'::regclass;
```

### Find column usage (search queries)
```sql
-- Check query logs if available
SELECT query_text
FROM query_history
WHERE query_text ILIKE '%table_name%'
  AND query_text ILIKE '%column_name%';
```

### dbt dependencies
```bash
# If using dbt
dbt ls --select +model_name  # upstream
dbt ls --select model_name+  # downstream
```

## Output Structure

```
docs/
  lineage/
    README.md                    # Index of documented flows
    [metric-name]-lineage.md     # Per-metric tracing
    [table-name]-lineage.md      # Per-table tracing
    [process-name]-flow.md       # End-to-end process flows
```

## Impact Analysis Template

```markdown
# Impact Analysis: [Proposed Change]

## Change Description
[What will change]

## Affected Objects

### Direct Impact
| Object | Type | Impact | Action Needed |
|--------|------|--------|---------------|
| [name] | Table | Schema change | Update queries |

### Indirect Impact
| Object | Type | Risk | Action Needed |
|--------|------|------|---------------|
| [dashboard] | Report | May break | Test after deploy |

## Stakeholders to Notify
- [ ] [Person/Team]: [Reason]

## Rollback Plan
[How to undo if needed]
```

## Remember

- Start from what you can see (dashboard, report)
- Trace one step at a time
- Document as you discover
- Check both code (transformations) and metadata (tools)
- Ask owners when stuck
- Some lineage may be undocumented (note this)

## Language

Adapt to user's language (French or English).
