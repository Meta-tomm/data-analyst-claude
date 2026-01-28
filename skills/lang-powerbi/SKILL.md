---
name: lang-powerbi
description: "Use when writing DAX, modeling Power BI data, or debugging Power BI formulas. Star schema, measures, optimization."
---

# Power BI & DAX

Best practices for DAX measures, data modeling, and Power BI optimization.

## Output Format

```markdown
## Analysis
[Approach taken]

## Code
```dax
-- Measure Name
-- Description
[DAX formula]
```

## Interpretation
[Step-by-step how it works]

## Next Steps
[Related measures, viz suggestions]
```

## Time Intelligence

```dax
// Year-to-Date
YTD Sales = TOTALYTD(SUM(Sales[Amount]), 'Date'[Date])

// Previous Year
PY Sales = CALCULATE(SUM(Sales[Amount]), SAMEPERIODLASTYEAR('Date'[Date]))

// YoY Growth %
YoY Growth % =
VAR Current = SUM(Sales[Amount])
VAR Previous = [PY Sales]
RETURN DIVIDE(Current - Previous, Previous)

// Month-to-Date
MTD Sales = TOTALMTD(SUM(Sales[Amount]), 'Date'[Date])

// Rolling 12 Months
Rolling 12M = CALCULATE(SUM(Sales[Amount]),
    DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -12, MONTH))

// Moving Average 30 Days
MA 30 = AVERAGEX(
    DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -30, DAY),
    [Total Sales])
```

## Running Totals

```dax
Running Total = CALCULATE(SUM(Sales[Amount]),
    FILTER(ALL('Date'), 'Date'[Date] <= MAX('Date'[Date])))
```

## Rankings

```dax
Sales Rank = RANKX(ALL(Products[Product]), [Total Sales], , DESC, Dense)
Is Top 10 = IF([Sales Rank] <= 10, 1, 0)
```

## Percentages

```dax
% of Total = DIVIDE(SUM(Sales[Amount]),
    CALCULATE(SUM(Sales[Amount]), ALL(Sales)))

% of Parent = DIVIDE(SUM(Sales[Amount]),
    CALCULATE(SUM(Sales[Amount]), ALLEXCEPT(Sales, Products[Category])))
```

## Conditional

```dax
Status = SWITCH(TRUE(),
    [Growth %] > 0.1, "Strong Growth",
    [Growth %] > 0, "Growth",
    [Growth %] > -0.1, "Decline",
    "Strong Decline")
```

## Data Modeling

### Star Schema
- Fact tables: numeric measures, foreign keys
- Dimension tables: descriptive attributes
- Date table: always create dedicated date dimension
- Single direction relationships by default

### Performance
- Avoid bi-directional relationships
- Use SUMMARIZECOLUMNS over SUMMARIZE
- Remove unused columns from import
- Use INT over DECIMAL when possible
- Prefer calculated columns over measures for static values

## Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| Circular dependency | Measure references itself | Use VAR or restructure |
| Multiple values | Filter returns multiple rows | SELECTEDVALUE or add aggregation |
| Column not found | Wrong table reference | Check table[column] syntax |
| BLANK issues | Division by zero | DIVIDE() with 3rd param |

## Language

Respond in the same language as the user.
