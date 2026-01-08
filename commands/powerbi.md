---
name: powerbi
description: Power BI assistance for DAX measures and data modeling
argument-hint: "\"describe what you need\" or paste DAX to debug"
allowed-tools:
  - Read
  - Write
---

# Power BI Assistant Command

Generate DAX measures, optimize data models, and debug formulas.

## Capabilities

1. **Generate DAX Measures**: Create measures from natural language
2. **Debug DAX**: Fix errors in existing formulas
3. **Optimize Models**: Improve data model design
4. **Explain DAX**: Break down complex formulas

## Workflow

### For DAX Generation

1. **Understand Requirement**
   - What metric is needed?
   - What context/filters apply?
   - What tables/columns involved?

2. **Generate Measure**
   - Write DAX with comments
   - Explain calculation logic
   - Include format string

3. **Provide Alternatives**
   - Simpler version if applicable
   - Performance considerations

### For Debugging

1. **Identify Error**
   - Parse error message
   - Locate problematic part

2. **Explain Issue**
   - Why it's failing
   - Common causes

3. **Provide Fix**
   - Corrected formula
   - Explanation of changes

## Output Format

```markdown
## Analysis
[What the measure does and approach taken]

## Code
```dax
-- Measure Name
-- Description: [what it calculates]
-- Usage: [how to use it]

Measure Name =
VAR CurrentValue = SUM(Sales[Amount])
VAR PreviousValue =
    CALCULATE(
        SUM(Sales[Amount]),
        SAMEPERIODLASTYEAR('Date'[Date])
    )
RETURN
    DIVIDE(
        CurrentValue - PreviousValue,
        PreviousValue,
        BLANK()
    )
```

## Interpretation
[How the measure works step by step]

## Next Steps
- Related measures to consider
- Visualization suggestions
- Performance tips
```

## Common DAX Patterns

### Time Intelligence

```dax
// Year-to-Date
YTD Sales =
TOTALYTD(SUM(Sales[Amount]), 'Date'[Date])

// Previous Year
PY Sales =
CALCULATE(
    SUM(Sales[Amount]),
    SAMEPERIODLASTYEAR('Date'[Date])
)

// Year-over-Year Growth %
YoY Growth % =
VAR CurrentYear = SUM(Sales[Amount])
VAR PreviousYear = [PY Sales]
RETURN
    DIVIDE(CurrentYear - PreviousYear, PreviousYear)

// Month-to-Date
MTD Sales =
TOTALMTD(SUM(Sales[Amount]), 'Date'[Date])

// Rolling 12 Months
Rolling 12M =
CALCULATE(
    SUM(Sales[Amount]),
    DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -12, MONTH)
)
```

### Running Totals

```dax
// Cumulative Total
Running Total =
CALCULATE(
    SUM(Sales[Amount]),
    FILTER(
        ALL('Date'),
        'Date'[Date] <= MAX('Date'[Date])
    )
)

// Running Total within Year
YTD Running =
CALCULATE(
    SUM(Sales[Amount]),
    FILTER(
        ALL('Date'),
        'Date'[Date] <= MAX('Date'[Date])
            && YEAR('Date'[Date]) = YEAR(MAX('Date'[Date]))
    )
)
```

### Averages

```dax
// Moving Average (30 days)
MA 30 Days =
AVERAGEX(
    DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -30, DAY),
    [Total Sales]
)

// Average per Category
Avg per Category =
AVERAGEX(
    VALUES(Products[Category]),
    [Total Sales]
)
```

### Rankings

```dax
// Rank by Sales
Sales Rank =
RANKX(
    ALL(Products[Product]),
    [Total Sales],
    ,
    DESC,
    Dense
)

// Top N Filter
Is Top 10 =
IF([Sales Rank] <= 10, 1, 0)
```

### Percentages

```dax
// % of Total
% of Total =
DIVIDE(
    SUM(Sales[Amount]),
    CALCULATE(SUM(Sales[Amount]), ALL(Sales))
)

// % of Parent
% of Parent =
DIVIDE(
    SUM(Sales[Amount]),
    CALCULATE(
        SUM(Sales[Amount]),
        ALLEXCEPT(Sales, Products[Category])
    )
)
```

### Conditional Measures

```dax
// Status with Multiple Conditions
Status =
SWITCH(
    TRUE(),
    [Growth %] > 0.1, "Strong Growth",
    [Growth %] > 0, "Growth",
    [Growth %] > -0.1, "Decline",
    "Strong Decline"
)
```

## Data Modeling Tips

### Star Schema Best Practices
- Fact tables: Numeric measures, foreign keys
- Dimension tables: Descriptive attributes
- Date table: Always create a dedicated date dimension
- Single direction relationships by default

### Performance Optimization
- Avoid bi-directional relationships when possible
- Use SUMMARIZE sparingly (prefer SUMMARIZECOLUMNS)
- Remove unused columns from import
- Use INT instead of DECIMAL when possible

## Common Errors and Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| Circular dependency | Measure references itself | Use VAR or restructure |
| A table of multiple values... | Filter returns multiple rows | Add aggregation or use SELECTEDVALUE |
| Column not found | Wrong table reference | Check table[column] syntax |
| BLANK handling | Division by zero or empty | Use DIVIDE() with 3rd param |

## Language

Respond in the same language as the user.
