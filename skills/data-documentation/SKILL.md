---
name: data-documentation
description: "Use when documenting data findings, creating data dictionaries, or building a personal knowledge base about a data environment. Essential for maintaining understanding over time."
---

# Data Documentation

## Overview

Create structured, maintainable documentation of data environment knowledge. Build a personal data catalog that grows with your understanding.

**Announce at start:** "I'm using the data-documentation skill to document these findings."

**Output:** `docs/catalog/` folder with structured documentation

## Documentation Types

### 1. Data Dictionary

**Per-table documentation:**

```markdown
# [Schema].[Table Name]

**Owner:** [Team/Person]
**Updated:** YYYY-MM-DD
**Source System:** [Where data originates]

## Purpose
[1-2 sentences: what this table represents in business terms]

## Refresh Frequency
- **Schedule:** Daily at 2am / Real-time / Manual
- **Latency:** ~4 hours behind source

## Columns

| Column | Type | Description | Example | Notes |
|--------|------|-------------|---------|-------|
| id | bigint | Primary key | 12345 | Auto-increment |
| user_id | bigint | FK to users.id | 67890 | Required |
| status | varchar(20) | Order state | 'completed' | Enum: pending, processing, completed, cancelled |
| total_amount | decimal(10,2) | Order total in EUR | 149.99 | Excludes tax |
| created_at | timestamp | Creation time | 2024-01-15 14:30:00 | UTC |

## Relationships

```
users.id ←── orders.user_id
orders.id ←── order_items.order_id
products.id ←── order_items.product_id
```

## Common Queries

### Get daily order totals
```sql
SELECT DATE(created_at) as day, SUM(total_amount) as revenue
FROM orders
WHERE status = 'completed'
GROUP BY 1;
```

## Known Issues
- [ ] `total_amount` sometimes null for legacy orders (pre-2022)
- [ ] Duplicate `user_id` entries exist (being investigated)

## Related Tables
- `order_items` - Line items for each order
- `users` - Customer information
- `products` - Product catalog
```

Save to: `docs/catalog/tables/[schema]-[table].md`

### 2. Domain Guide

**Per-business-domain documentation:**

```markdown
# [Domain Name] Data Guide

**Last Updated:** YYYY-MM-DD
**Domain Owner:** [Team/Person]

## Overview
[What this domain covers in business terms]

## Key Metrics

| Metric | Definition | Source Table | Calculation |
|--------|------------|--------------|-------------|
| Revenue | Total completed sales | orders | SUM(total_amount) WHERE status='completed' |
| Active Users | Users with activity in 30d | user_events | COUNT(DISTINCT user_id) WHERE date > NOW()-30 |

## Key Tables

| Table | Purpose | Update Frequency |
|-------|---------|------------------|
| orders | All customer orders | Real-time |
| order_items | Order line items | Real-time |
| daily_metrics | Pre-aggregated KPIs | Daily 3am |

## Important Business Rules
1. An order is "completed" only when payment confirmed AND shipped
2. Revenue excludes refunded orders (status = 'refunded')
3. Active user = at least 1 login OR 1 purchase in period

## Common Pitfalls
- Don't use `orders.amount` - deprecated, use `total_amount`
- Always filter `WHERE is_test = false` in production queries
- Time zones: all timestamps are UTC

## Useful Joins

### Orders with customer info
```sql
SELECT o.*, u.email, u.name
FROM orders o
JOIN users u ON o.user_id = u.id;
```

## Who to Ask
- Revenue questions: @finance-team
- User data: @data-platform
- Product catalog: @product-team
```

Save to: `docs/catalog/domains/[domain-name].md`

### 3. Glossary

**Business terms dictionary:**

```markdown
# Data Glossary

## A

### Active User
A user who has logged in or made a purchase within the last 30 days.
- **Source:** Calculated from `user_events` table
- **Related:** MAU, DAU, Churn

### ARR (Annual Recurring Revenue)
Total value of recurring subscriptions annualized.
- **Formula:** MRR × 12
- **Source:** `subscriptions` table

## C

### Churn
Percentage of users who cancel or don't renew.
- **Formula:** (Lost customers / Start customers) × 100
- **Period:** Usually monthly

### Cohort
Group of users who share a common characteristic (usually signup date).
- **Usage:** Cohort analysis tracks behavior over time
```

Save to: `docs/catalog/glossary.md`

### 4. Contact Directory

```markdown
# Data Contacts

## By Domain

### Sales/Revenue
| Person | Role | Slack | Knows About |
|--------|------|-------|-------------|
| Marie D. | Sales Analytics | @marie | Pipeline, forecasting |
| Jean P. | BI Lead | @jean | Dashboards, reporting |

### Product
| Person | Role | Slack | Knows About |
|--------|------|-------|-------------|
| Sophie L. | Product Analyst | @sophie | User behavior, funnels |

### Engineering/Data Platform
| Person | Role | Slack | Knows About |
|--------|------|-------|-------------|
| Thomas R. | Data Engineer | @thomas | ETL, pipelines, Airflow |
| Claire M. | DBA | @claire | PostgreSQL, performance |

## By System

| System | Primary Contact | Backup |
|--------|-----------------|--------|
| Snowflake | @thomas | @claire |
| Tableau | @jean | @marie |
| Salesforce | @sales-ops | - |
```

Save to: `docs/catalog/contacts.md`

## Folder Structure

```
docs/
  catalog/
    README.md              # Catalog overview and navigation
    glossary.md            # Business terms
    contacts.md            # Who to ask
    tables/
      public-users.md
      public-orders.md
      analytics-daily_metrics.md
    domains/
      sales.md
      product.md
      marketing.md
    systems/
      snowflake.md
      postgresql.md
```

## Maintenance

### Weekly Review
- Update tables you've used
- Add new terms learned
- Note new contacts

### After Each Analysis
- Document any new understanding
- Add useful queries
- Note pitfalls encountered

## Templates

**Quick table doc:**
```markdown
# [table_name]
**Purpose:** [one line]
**Key columns:** [list 3-5 most important]
**Gotchas:** [any surprises]
**Contact:** [who knows this table]
```

**Quick term:**
```markdown
### [Term]
[Definition in plain language]
- **Calculation:** [if applicable]
- **Source:** [table or system]
```

## Remember

- Document while learning (don't wait)
- Plain language over jargon
- Include examples
- Note what surprised you
- Update when things change

## Integration

**Called by:**
- `/data-analyst:document` command
- **data-onboarding** - Throughout all phases
- **data-discovery** - After exploring systems

**Pairs with:**
- **data-import** - Structure imported docs
- **data-export** - Export documentation for sharing
- **data-resume** - Documentation enables session continuity

## Language

Adapt to user's language (French or English).
