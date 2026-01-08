---
name: data-describe
description: "Use to describe data without exposing sensitive values. Creates anonymized schema descriptions, statistical summaries, and sample structures that can be safely shared with Claude."
---

# Data Describe

## Overview

Describe your data without exposing sensitive information. Generate schema descriptions, statistical profiles, and sample structures that are safe to share.

**Announce at start:** "I'm using the data-describe skill to create a safe description of your data."

**Output:** Anonymized descriptions you can paste to Claude

## Why This Matters

**You should NOT paste:**
- Real customer names, emails, addresses
- Financial account numbers
- Personal identifiers (SSN, passport, etc.)
- Internal credentials or tokens
- Proprietary business data

**You CAN safely share:**
- Column names and types
- Row counts and statistics
- Anonymized sample structures
- Data quality metrics

## Description Templates

### 1. Schema Description

**Generate this query, run it, share results:**

```sql
-- PostgreSQL / Snowflake
SELECT
    column_name,
    data_type,
    is_nullable,
    character_maximum_length
FROM information_schema.columns
WHERE table_name = '[your_table]'
ORDER BY ordinal_position;
```

**Safe to share format:**

```markdown
## Table: [table_name]

| Column | Type | Nullable | Notes |
|--------|------|----------|-------|
| id | bigint | No | PK |
| user_id | bigint | No | FK |
| amount | decimal(10,2) | No | Currency |
| status | varchar(20) | No | Enum |
| created_at | timestamp | No | UTC |

Row count: ~1.5M
Date range: 2022-01 to present
```

### 2. Statistical Profile (No Real Values)

**Generate these queries:**

```sql
-- Numeric column stats
SELECT
    'amount' as column_name,
    COUNT(*) as total_rows,
    COUNT(amount) as non_null,
    ROUND(AVG(amount), 2) as mean,
    ROUND(STDDEV(amount), 2) as std_dev,
    MIN(amount) as min_val,
    MAX(amount) as max_val,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount) as median
FROM orders;

-- Categorical distribution (counts only, not values if sensitive)
SELECT
    status,
    COUNT(*) as count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) as percentage
FROM orders
GROUP BY status;

-- Date range
SELECT MIN(created_at), MAX(created_at) FROM orders;

-- Null analysis
SELECT
    column_name,
    COUNT(*) - COUNT(column_value) as null_count,
    ROUND(100.0 * (COUNT(*) - COUNT(column_value)) / COUNT(*), 2) as null_pct
FROM (
    SELECT 'amount' as column_name, amount as column_value FROM orders
    UNION ALL
    SELECT 'status', status FROM orders
) t
GROUP BY column_name;
```

**Safe to share format:**

```markdown
## Table: orders - Statistical Profile

### Numeric Columns

| Column | Non-Null | Mean | Std Dev | Min | Max | Median |
|--------|----------|------|---------|-----|-----|--------|
| amount | 1.5M | 89.50 | 45.20 | 0.01 | 9999.99 | 65.00 |

### Categorical Columns

| Column | Distinct Values | Top Value (%) | Null % |
|--------|-----------------|---------------|--------|
| status | 5 | completed (65%) | 0% |
| category | 12 | electronics (25%) | 2% |

### Date Coverage
- Earliest: 2022-01-01
- Latest: 2024-01-15
- Density: Daily, no gaps

### Data Quality
- Null in amount: 0%
- Null in status: 0%
- Null in category: 2%
```

### 3. Anonymized Sample Structure

**Instead of real data, describe the pattern:**

```markdown
## Sample Structure: users table

**DO NOT share real values. Describe patterns:**

| Column | Pattern | Example Format |
|--------|---------|----------------|
| id | Sequential integer | 12345 |
| email | firstname.lastname@domain.com | [REDACTED] |
| name | "First Last" format | [REDACTED] |
| created_at | ISO timestamp | 2024-01-15T14:30:00Z |
| plan_type | Enum: free/pro/enterprise | "pro" |
| company_id | Foreign key, nullable | 789 or NULL |

**Relationships:**
- users.company_id → companies.id (nullable, ~60% have company)
- orders.user_id → users.id
```

### 4. Problem Description (No Data)

**Template for asking Claude about issues:**

```markdown
## Data Issue Description

**Table:** orders
**Row count:** ~1.5M
**Problem:** Duplicate detection

**Schema relevant columns:**
- order_id (bigint, PK)
- user_id (bigint, FK)
- created_at (timestamp)
- amount (decimal)

**Issue observed:**
- Same user_id + created_at within 1 second = potential duplicate
- Found ~500 cases (0.03% of data)

**Question:** Best approach to identify and handle these?
```

## Quick Describe Workflow

1. **Identify what you need help with**
2. **Run the appropriate query locally**
3. **Format results using templates above**
4. **Remove/redact any sensitive values**
5. **Share with Claude**

## Sensitive Data Checklist

Before sharing, verify NO:
- [ ] Real names (use "User A", "Customer 123")
- [ ] Email addresses
- [ ] Phone numbers
- [ ] Physical addresses
- [ ] Financial account numbers
- [ ] Social security / national IDs
- [ ] Passwords, tokens, API keys
- [ ] Internal URLs or IPs
- [ ] Proprietary business data (if confidential)

## Safe Substitutions

| Instead of | Share |
|------------|-------|
| "john.doe@company.com" | "[email]" or pattern "name@domain" |
| "123-45-6789" | "[SSN]" or "9-digit ID" |
| Real revenue numbers | Relative (indexed to 100) or ranges |
| Customer names | "Customer A", "User 123" |
| Internal URLs | "[internal_url]" or "https://[redacted]" |

## Output Location

Save descriptions to: `docs/data-descriptions/[table-name].md`

Reuse when asking Claude questions about that table.

## Remember

- When in doubt, redact
- Stats and structure are usually safe
- Actual values often are not
- Your company may have specific policies - follow them
- Claude can help effectively with structure alone

## Language

Adapt to user's language (French or English).
