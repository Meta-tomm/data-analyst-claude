---
name: data-import
description: "Use to import external documentation into your knowledge base. Process content from Confluence, Notion, wikis, or any text - Claude structures and integrates it into your docs."
---

# Data Import

## Overview

Import existing documentation into your structured knowledge base. Paste content from wikis, Confluence, Notion, or any source - Claude processes and integrates it.

**Announce at start:** "I'm using the data-import skill to process this documentation."

**Output:** Structured files in `docs/` folder

## Import Process

### Step 1: Receive Content

**User pastes or describes:**
- Confluence page content
- Notion export
- Wiki text
- Slack messages with context
- Email with explanations
- Screenshots (describe what you see)

### Step 2: Identify Type

**Claude determines:**
- Is this about a table/schema? → `docs/catalog/tables/`
- Is this about a domain/process? → `docs/catalog/domains/`
- Is this a glossary/terms? → Add to `docs/catalog/glossary.md`
- Is this about contacts/people? → Add to `docs/catalog/contacts.md`
- Is this a procedure? → `docs/procedures/`
- Is this general context? → `docs/notes/`

### Step 3: Structure Content

**Transform raw content into structured format:**

**Before (raw paste):**
```
hey so the orders table is in the analytics schema, it has order_id which is the pk, user_id refs users,
amount is the total in euros, status can be pending/processing/shipped/completed/cancelled,
oh and created_at is when it was made. we refresh it every hour from the prod db.
talk to thomas if you have questions about the etl
```

**After (structured):**
```markdown
# analytics.orders

**Owner:** Thomas (ETL questions)
**Refresh:** Hourly from production DB

## Purpose
Order transactions with status tracking.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| order_id | PK | Order identifier |
| user_id | FK → users | Customer reference |
| amount | decimal | Total in EUR |
| status | enum | pending/processing/shipped/completed/cancelled |
| created_at | timestamp | Order creation time |

## Notes
- Hourly refresh from production database
- Contact Thomas for ETL questions
```

### Step 4: Integrate

**Add to existing docs or create new:**
- Merge with existing table doc if exists
- Add new terms to glossary
- Update contacts list
- Cross-reference with related docs

## Import Templates by Source

### From Confluence/Wiki

```markdown
/data-analyst:import

[Paste confluence content]

---
Source: Confluence - Data Team Space
Page: Orders Table Documentation
Last Updated: 2024-01-10
```

### From Slack Conversation

```markdown
/data-analyst:import

Context: Slack thread with Thomas about the orders table

Thomas: "the orders table gets refreshed every hour, it pulls from prod via fivetran"
Thomas: "status field is an enum: pending, processing, shipped, completed, cancelled"
Me: "what about refunds?"
Thomas: "refunds are separate table, orders_refunds, linked by order_id"

---
Extract: Table refresh info, status values, refunds relationship
```

### From Email

```markdown
/data-analyst:import

From: marie@company.com
Subject: RE: Revenue calculation

The revenue metric on the dashboard is:
- Sum of amount from orders where status = 'completed'
- Excludes orders with is_test = true
- Currency is always EUR
- Refunds are subtracted (negative amounts in orders_refunds)

---
Extract: Revenue calculation business rule
```

### From Screenshot Description

```markdown
/data-analyst:import

Describing screenshot of ERD diagram:

Tables shown:
- users (id, email, name, created_at)
- orders (id, user_id FK→users, amount, status, created_at)
- order_items (id, order_id FK→orders, product_id FK→products, quantity, price)
- products (id, name, category, price)

Relationships:
- users 1:N orders
- orders 1:N order_items
- products 1:N order_items

---
Extract: Schema relationships
```

## Quick Import Commands

```markdown
/data-analyst:import                     # Interactive mode
/data-analyst:import table               # Expecting table info
/data-analyst:import glossary            # Expecting terms
/data-analyst:import procedure           # Expecting how-to
/data-analyst:import context             # General knowledge
```

## Integration Checklist

After import, Claude should:
- [ ] Save to appropriate location
- [ ] Update related docs (cross-references)
- [ ] Add new terms to glossary
- [ ] Add new contacts to contacts.md
- [ ] Note source and date
- [ ] Flag anything unclear for follow-up

## Handling Conflicts

**If imported info conflicts with existing:**

```markdown
## Conflict Detected

**Existing:** Revenue excludes refunds
**Imported:** Revenue includes refunds as negative values

**Options:**
1. Keep existing (import source may be outdated)
2. Update to imported (more recent info)
3. Flag for clarification with [person]

Which should I do?
```

## Source Tracking

Every imported doc includes:

```markdown
---
Imported: YYYY-MM-DD
Source: [Confluence/Slack/Email/etc.]
Original: [Page name/Thread/Subject]
Validated: [Yes/No/Pending with person]
---
```

## Remember

- Always note the source
- Flag uncertain info for validation
- Merge don't duplicate
- Update timestamps
- Cross-reference related docs

## Language

Adapt to user's language (French or English).
