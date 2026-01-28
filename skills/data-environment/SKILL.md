---
name: data-environment
description: "Use when exploring, configuring, or resuming a data environment. Covers onboarding, discovery, lineage, config, session resume, and data description."
---

# Data Environment

Comprehensive skill for understanding, configuring, and navigating data environments.

## Capabilities

1. **Config** - Create/maintain project configuration
2. **Discovery** - Explore and map data sources
3. **Onboarding** - Structured workflow for new environments
4. **Lineage** - Trace data flows
5. **Resume** - Restore session context
6. **Describe** - Anonymize data for safe sharing

---

## 1. Configuration

**Config file:** `.claude/data-analyst.local.md`

### Structure

```yaml
environment:
  name: "[Company/Project]"
  sql_dialect: "postgresql"  # postgresql, snowflake, sqlserver, mysql, bigquery
  timezone: "Europe/Paris"

systems:
  primary_warehouse: "Snowflake"
  bi_tool: "Power BI"
  etl_tool: "dbt"

databases:
  - name: "prod_warehouse"
    type: "snowflake"
    schemas: ["raw", "staging", "marts"]

naming_conventions:
  tables: "snake_case"
  prefix_raw: "raw_"
  prefix_staging: "stg_"
  prefix_mart: "dim_, fact_, rpt_"
```

Plus markdown sections for: Company Overview, Key Contacts, Internal Jargon, Business Rules, Data Quality Notes, Current Projects.

### Setup Questions (one at a time)
1. Company/project name?
2. SQL dialect?
3. BI tool?
4. Main databases?
5. Naming conventions?

### Quick Templates

**Startup:** PostgreSQL, Metabase, single DB
**Enterprise:** Snowflake, Tableau, dbt, multi-schema
**Power BI:** SQL Server/Azure Synapse, Power BI

---

## 2. Discovery

Systematically explore and map unknown data environments.

**Output:** `docs/discovery/`

### Process

**Step 1: Environment Inventory**
- List systems, access status, priority
- Identify contacts
- Save to `docs/discovery/00-inventory.md`

**Step 2: Schema Exploration**

Adapt for: Snowflake, SQL Server, BigQuery.

Save to `docs/discovery/[db]-schema.md`

**Step 3: Data Profiling** (for key tables)
- Column types, nullability
- Value distributions
- Numeric stats (min/max/avg)
- Date ranges

**Step 4: Quick Wins**
- Identify most-used tables
- Find obvious relationships (FK patterns)
- Note data quality issues

---

## 3. Onboarding

Structured 4-phase workflow for new data environments.

**Phase 1 - Orientation (Days 1-3):**
- Get access to systems
- Identify key contacts
- Run data-config setup

**Phase 2 - Discovery (Days 4-10):**
- Map data landscape (use Discovery process)
- Document schemas and key tables
- Identify relationships

**Phase 3 - Deep Dives (Days 11-20):**
- Priority domain analysis
- Document business rules
- Build lineage for critical flows

**Phase 4 - Integration (Days 21+):**
- Become contributor
- Create reusable queries/scripts
- Complete documentation

Weekly check-in template:
```markdown
## Week [N] Check-in
- Explored: [systems/schemas]
- Documented: [tables/domains]
- Open questions: [list]
- Next week focus: [priorities]
```

---

## 4. Lineage

Trace data flows from source to destination.

**Output:** `docs/lineage/`

### Investigation Types

**Upstream:** Where does this data come from?
**Downstream:** Where does this data go?
**Impact:** What breaks if this changes?

### Investigation Queries

See SQL examples in discovery section. Key technique: query pg_depend to find view dependencies on tables.

### Documentation Format
```markdown
## Lineage: [entity/table]

### Flow Diagram
Source -> Transform1 -> Transform2 -> Target

### Detailed Steps
| Step | Source | Transform | Target | Owner |
|------|--------|-----------|--------|-------|
| 1 | raw.events | dbt model | staging.events | Data Eng |
```

---

## 5. Session Resume

Restore context from previous sessions.

### Session Start
1. Read `.claude/data-analyst.local.md` (config)
2. Read `.claude/session-log.md` (progress)
3. Check `docs/` for recent discoveries
4. Present restore summary:

```markdown
## Session Restored
- Environment: [name]
- Last session: [date]
- Incomplete tasks: [list]
- Focus options: [suggestions]
```

### Session End
1. Save progress to `.claude/session-log.md`
2. Note new discoveries
3. List incomplete tasks
4. Suggest next session focus

---

## 6. Data Description (Safe Sharing)

Describe data without exposing sensitive information.

**Output:** `docs/data-descriptions/`

### Safe to share: column names/types, row counts, statistics, patterns
### Never share: real names, contact info, financial data, credentials

### Templates

**Schema description:**
```markdown
| Column | Type | Nullable | Notes |
|--------|------|----------|-------|
| id | bigint | No | PK |
| amount | decimal(10,2) | No | Currency |
```

**Statistical profile:** counts, means, distributions (no real PII values)
**Anonymized samples:** patterns, not real values

### Sensitive Data Checklist
Before sharing, verify NO: real names, contact details, phone numbers, addresses, account numbers, IDs, secrets, internal URLs.

---

## Language

Adapt to the language used by the user (French or English).
