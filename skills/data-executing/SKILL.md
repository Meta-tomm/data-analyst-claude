---
name: data-executing
description: "Use when you have an approved implementation plan to execute. Implements plan task-by-task with batch execution and review checkpoints. Generates appropriate outputs (Python .py, DAX/Excel .md, SQL .sql, Reports .md)."
---

# Executing Data Analysis Plans

## Overview

Load plan, review critically, execute tasks in batches, report for review between batches.

**Core principle:** Batch execution with checkpoints for user review.

**Announce at start:** "I'm using the data-executing skill to implement this plan."

## The Process

### Step 1: Load and Review Plan

1. Read plan file from `docs/plans/`
2. Review critically - identify any questions or concerns:
   - Missing data files?
   - Unclear transformations?
   - Ambiguous validation criteria?
3. If concerns: Raise them before starting
4. If no concerns: Create TodoWrite with all tasks and proceed

### Step 2: Execute Batch

**Default: First 3 tasks**

For each task:
1. Mark as `in_progress` in TodoWrite
2. Follow each step exactly (plan has bite-sized steps)
3. Run validations as specified
4. Show intermediate results
5. Mark as `completed`

**Execution by Output Type:**

**Python:**
- Execute code blocks
- Run validation commands
- Show outputs (shape, samples, etc.)
- Assemble into final script

**DAX/Excel (.md for copy-paste):**
- Write formulas to markdown file
- Include clear instructions for each
- Document dependencies and prerequisites
- Format for easy copy-paste

**SQL:**
- Write queries to .sql file
- Comment each section
- Adapt to specified dialect

**Reports:**
- Generate supporting analysis first
- Write sections with data
- Include visualizations if needed

### Step 3: Report

When batch complete:
```markdown
## Batch Complete

**Tasks completed:** 1-3

**Results:**
- Task 1: [Summary + validation passed]
- Task 2: [Summary + validation passed]
- Task 3: [Summary + validation passed]

**Intermediate outputs:**
- `outputs/partial-results.csv` created
- 1000 rows processed, 0 nulls remaining

Ready for feedback.
```

### Step 4: Continue

Based on feedback:
- Apply changes if needed
- Execute next batch
- Repeat until complete

### Step 5: Final Checkpoint

After all tasks complete:

```markdown
## Execution Complete

### Deliverables Generated

| File | Type | Status |
|------|------|--------|
| `scripts/analysis.py` | Python | Executable |
| `outputs/dax-formulas.md` | DAX | Ready to copy |
| `outputs/results.csv` | Data | Generated |

### Summary
[What was accomplished]

### How to Use
- **Python**: Run `python scripts/analysis.py`
- **DAX**: Open in Power BI, copy formulas from .md
- **Excel**: Open .md, copy formulas to cells as documented
- **SQL**: Execute in your database client

### Suggested Next Steps
- [Suggestion 1]
- [Suggestion 2]
```

## When to Stop and Ask for Help

**STOP executing immediately when:**
- Hit a blocker mid-batch (missing file, data error, unclear instruction)
- Plan has critical gaps preventing progress
- Validation fails and fix is unclear
- Output doesn't match expected

**Ask for clarification rather than guessing.**

Example:
```markdown
## Blocked at Task 3

**Problem:** The plan says to join on `customer_id` but the file only has `cust_id`.

**Options:**
1. Assume `cust_id` is the same column
2. Stop and clarify the mapping

Which should I do?
```

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**
- User updates the plan based on feedback
- Data structure differs from plan assumptions
- Fundamental approach needs rethinking

**Don't force through blockers** - stop and ask.

## Output Format Templates

### DAX Output (.md)

```markdown
# DAX Formulas - [Analysis Name]

Generated: YYYY-MM-DD

---

## Measure 1: Total Sales

### Formula
```dax
Total Sales = SUM(Sales[Amount])
```

### How to Create
1. Power BI Desktop > Modeling > New Measure
2. Paste formula above
3. Format: Currency, 2 decimals

### Where to Use
- Cards: Display total
- Charts: Y-axis values

---
```

### Excel Output (.md)

```markdown
# Excel Formulas - [Analysis Name]

Generated: YYYY-MM-DD

---

## Setup

### Expected Structure
- **Sheet "Data"**: Raw data
  - A: Date | B: Product | C: Revenue | D: Category
- **Sheet "Analysis"**: Results

---

## Formula 1: Sum by Category

### Formula
```excel
=SUMIFS(Data!$C:$C, Data!$D:$D, A2)
```

### Placement
- Sheet: Analysis
- Cell: B2
- Drag down for all categories

---
```

### SQL Output (.sql)

```sql
-- ================================================
-- [Analysis Name]
-- Generated: YYYY-MM-DD
-- Dialect: PostgreSQL
-- ================================================

-- Query 1: Monthly Revenue
-- Purpose: Aggregate revenue by month
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(amount) AS total_revenue
FROM orders
GROUP BY 1
ORDER BY 1;

-- ================================================
```

## Remember

- Review plan critically first
- Follow plan steps exactly
- Don't skip validations
- Between batches: just report and wait
- Stop when blocked, don't guess
- Adapt output format to deliverable type

## Integration

**Called by:**
- `/data-analyst:execute-plan` command
- **data-planning** - After plan saved and user confirms execution

**Pairs with:**
- **data-config** - Uses SQL dialect from config
- **data-export** - Can export cheatsheets after completion

## Language

Adapt to user's language (French or English).
