---
name: data-planning
description: "Use when you have completed brainstorming and have a validated design for data analysis. Creates detailed, bite-sized implementation plans adapted to target output (Python, DAX, Excel, SQL, Reports)."
---

# Writing Data Analysis Plans

## Overview

Write comprehensive analysis plans assuming the implementer has zero context. Document everything: which files to touch, exact transformations, validation criteria, how to test. Give the whole plan as bite-sized tasks.

Assume they are skilled but know nothing about the specific data or business domain.

**Announce at start:** "I'm using the data-planning skill to create the implementation plan."

**Context:** Should follow a completed brainstorming session with validated design.

**Save plans to:** `docs/plans/YYYY-MM-DD-<analysis-name>.md`

## Bite-Sized Task Granularity

**Each step is one action (2-5 minutes):**
- "Load the CSV file" - step
- "Check the shape and types" - step
- "Handle nulls in revenue column" - step
- "Validate: no nulls remain" - step
- "Create the aggregation" - step

**Never combine multiple actions into one step.**

## Plan Document Header

**Every plan MUST start with this header:**

```markdown
# [Analysis Name] Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use data-analyst:data-executing to implement this plan task-by-task.

**Goal:** [One sentence describing what this analysis produces]

**Target Output:** [Python script (.py) | DAX formulas (.md) | Excel formulas (.md) | SQL queries (.sql) | Report (.md)]

**Data Sources:** [List input files/tables]

---
```

## Task Structure by Output Type

### Python Script Tasks

```markdown
### Task N: [Component Name]

**Files:**
- Input: `data/sales.csv`
- Output: `outputs/analysis.csv`
- Script: `scripts/analysis.py`

**Step 1: Load data**

```python
df = pd.read_csv('data/sales.csv', parse_dates=['date'])
```

**Step 2: Validate load**

Run: `print(df.shape, df.dtypes)`
Expected: `(1000, 5)`, date as datetime64

**Step 3: Handle nulls**

```python
df['revenue'] = df['revenue'].fillna(df['revenue'].median())
```

**Step 4: Validate nulls**

Run: `print(df['revenue'].isna().sum())`
Expected: `0`
```

### DAX Formula Tasks

```markdown
### Task N: [Measure Name]

**Output:** `outputs/dax-formulas.md`

**Step 1: Write base measure**

```dax
Total Sales = SUM(Sales[Amount])
```

**Step 2: Document usage**

Write in output file:
- Where to create: Modeling > New Measure
- Format: Currency, 2 decimals
- Use in: Cards, Charts Y-axis

**Step 3: Write dependent measure (if any)**

```dax
YoY Growth =
VAR CurrentYear = [Total Sales]
VAR PreviousYear = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
RETURN DIVIDE(CurrentYear - PreviousYear, PreviousYear)
```

**Step 4: Document dependencies**

Prerequisite: Total Sales measure must exist first
```

### Excel Formula Tasks

```markdown
### Task N: [Formula Name]

**Output:** `outputs/excel-formulas.md`

**Step 1: Document structure**

Write expected sheet structure:
- Sheet "Data": A=Date, B=Product, C=Revenue
- Sheet "Analysis": Results go here

**Step 2: Write formula**

```excel
=SUMIFS(Data!$C:$C, Data!$D:$D, A2)
```

**Step 3: Document placement**

- Sheet: Analysis
- Cell: B2
- Action: Drag down for all categories
```

### SQL Query Tasks

```markdown
### Task N: [Query Name]

**Output:** `scripts/queries.sql`
**Dialect:** PostgreSQL

**Step 1: Write query**

```sql
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(amount) AS total_revenue
FROM orders
GROUP BY 1
ORDER BY 1;
```

**Step 2: Document expected output**

Columns: month (date), total_revenue (numeric)
Rows: One per month in data range
```

### Report Tasks

```markdown
### Task N: [Section Name]

**Output:** `outputs/report.md`

**Step 1: Write section header**

```markdown
## Key Findings
```

**Step 2: Generate supporting data**

Run analysis to get numbers for this section.

**Step 3: Write content**

3-5 bullet points, each with:
- Finding
- Supporting number
- Business implication
```

## Validation Criteria

Every task MUST have:
1. **Expected output** - What should exist after
2. **Validation command** - How to verify
3. **Expected result** - What success looks like

## Remember

- Exact file paths always
- Complete code in plan (not "add validation")
- One action per step
- Dependencies explicit between tasks
- Adapt format to target output type

## Execution Handoff

After saving the plan, offer execution:

**"Plan complete and saved to `docs/plans/<filename>.md`. Ready to execute?**

**If yes:**
- **REQUIRED SUB-SKILL:** Use data-analyst:data-executing
- Follow that skill exactly to implement task-by-task

## Integration

**Called by:**
- `/data-analyst:write-plan` command
- **data-brainstorming** - After design validated

**Chains to:**
- **data-executing** - After plan saved, execute task-by-task

**Pairs with:**
- **data-config** - Uses SQL dialect and naming conventions from config
- **data-describe** - If data context needed for planning

## Language

Adapt to user's language (French or English).
