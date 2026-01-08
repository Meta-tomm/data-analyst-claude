---
name: data-config
description: "Use to create or update project configuration. Stores environment info (SQL dialect, systems, contacts, jargon) that persists between sessions. Auto-loaded at session start."
---

# Data Configuration

## Overview

Create and maintain a project configuration file that stores your environment context. This file is read at the start of each session so Claude understands your setup without re-explaining.

**Announce at start:** "I'm using the data-config skill to configure your data environment."

**Config file:** `.claude/data-analyst.local.md`

## Configuration File Structure

```markdown
---
# Data Analyst Configuration
# This file is auto-loaded at session start

environment:
  name: "[Company/Project Name]"
  sql_dialect: "postgresql"  # postgresql, snowflake, sqlserver, mysql, bigquery
  timezone: "Europe/Paris"

systems:
  primary_warehouse: "Snowflake"
  bi_tool: "Power BI"
  etl_tool: "dbt"
  orchestrator: "Airflow"

databases:
  - name: "prod_warehouse"
    type: "snowflake"
    schemas: ["raw", "staging", "marts"]
    description: "Main data warehouse"
  - name: "app_db"
    type: "postgresql"
    schemas: ["public"]
    description: "Application database (read replica)"

naming_conventions:
  tables: "snake_case"
  columns: "snake_case"
  prefix_raw: "raw_"
  prefix_staging: "stg_"
  prefix_mart: "dim_, fact_, rpt_"
---

# Environment Context

## Company Overview
[Brief description of the company and data team]

## Key Contacts

| Person | Role | Domain | Contact |
|--------|------|--------|---------|
| [Name] | Data Engineer | ETL, Pipelines | @slack |
| [Name] | Analytics Lead | BI, Reporting | @slack |
| [Name] | DBA | Database perf | @slack |

## Internal Jargon

| Term | Meaning |
|------|---------|
| [Internal term] | [What it actually means] |
| ARR | Annual Recurring Revenue |
| MQL | Marketing Qualified Lead |

## Important Business Rules

1. [Rule 1: e.g., "Revenue = completed orders only, excludes refunds"]
2. [Rule 2: e.g., "Active user = login in last 30 days"]
3. [Rule 3]

## Data Quality Notes

- [Known issue 1]
- [Known issue 2]

## Current Projects

- [ ] [Project 1]: [Brief description]
- [ ] [Project 2]: [Brief description]
```

## Setup Process

### First Time Setup

**Questions to ask (one at a time):**

1. "What's the name of your company/project?"
2. "What SQL dialect do you primarily use?" (PostgreSQL, Snowflake, SQL Server, MySQL, BigQuery)
3. "What BI tool does your team use?" (Power BI, Tableau, Looker, Metabase, other)
4. "What are the main databases/warehouses you'll work with?"
5. "Any specific naming conventions for tables/columns?"

**After gathering info:**
1. Create `.claude/data-analyst.local.md`
2. Fill in the YAML frontmatter
3. Add placeholders for contacts, jargon, rules
4. Explain how to update it over time

### Updating Config

**Add contact:**
```markdown
| Marie D. | Sales Analytics | Revenue, Pipeline | @marie |
```

**Add jargon:**
```markdown
| Churn | Customer cancellation rate, monthly basis |
```

**Add business rule:**
```markdown
3. Active subscription = status='active' AND end_date > NOW()
```

## Auto-Load Behavior

When a session starts in a project with `.claude/data-analyst.local.md`:

1. Read the config file
2. Apply SQL dialect for query generation
3. Use naming conventions
4. Reference contacts when suggesting "ask [person]"
5. Use correct jargon in responses

## Quick Config Templates

### Startup / Small Team
```yaml
environment:
  name: "Startup Analytics"
  sql_dialect: "postgresql"
systems:
  primary_warehouse: "PostgreSQL"
  bi_tool: "Metabase"
databases:
  - name: "production"
    type: "postgresql"
    schemas: ["public"]
```

### Enterprise / Data Team
```yaml
environment:
  name: "Enterprise Corp"
  sql_dialect: "snowflake"
systems:
  primary_warehouse: "Snowflake"
  bi_tool: "Tableau"
  etl_tool: "dbt"
  orchestrator: "Airflow"
databases:
  - name: "analytics"
    type: "snowflake"
    schemas: ["raw", "staging", "intermediate", "marts"]
  - name: "app_replica"
    type: "postgresql"
    schemas: ["public"]
```

### Power BI Focus
```yaml
environment:
  name: "BI Team"
  sql_dialect: "sqlserver"
systems:
  primary_warehouse: "Azure Synapse"
  bi_tool: "Power BI"
databases:
  - name: "dwh"
    type: "sqlserver"
    schemas: ["dbo", "reporting"]
```

## Commands

**View current config:**
```
/data-analyst:config show
```

**Update specific section:**
```
/data-analyst:config add contact "Marie D." "Sales Analytics" "@marie"
/data-analyst:config add jargon "MQL" "Marketing Qualified Lead"
/data-analyst:config set dialect snowflake
```

## Remember

- Update config as you learn
- Add jargon when you encounter new terms
- Add contacts when you meet people
- Note business rules when you discover them
- This is YOUR knowledge base

## Integration

**Called by:**
- `/data-analyst:config` command
- **data-onboarding** - First step: setup environment

**Used by (all skills read config):**
- **data-planning** - SQL dialect, naming conventions
- **data-executing** - SQL dialect for queries
- **data-discovery** - Dialect-specific exploration queries
- **data-export** - Dialect for cheatsheets

**Pairs with:**
- **data-resume** - Config enables session continuity

## Language

Adapt to user's language (French or English).
