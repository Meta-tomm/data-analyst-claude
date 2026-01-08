---
name: analyze
description: Perform exploratory data analysis on a dataset
argument-hint: "[file.csv] or paste data"
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
---

# Exploratory Data Analysis Command

## REQUIRED WORKFLOW

**Before executing this command, follow the structured workflow:**

1. **FIRST**: Use `data-analyst:data-brainstorming` skill
   - Understand the analysis goals
   - Explore data context
   - Confirm approach with user

2. **THEN**: Use `data-analyst:data-planning` skill
   - Create detailed analysis plan
   - Define tasks and validation criteria
   - Get user approval

3. **FINALLY**: Use `data-analyst:data-executing` skill
   - Execute plan task by task
   - Validate each step
   - Deliver results

**DO NOT skip directly to analysis code.**

---

## Analysis Scope

Once workflow is complete, the analysis should cover:

### Dataset Overview
- Shape (rows x columns)
- Column names and data types
- Memory usage

### Missing Values
- Count and percentage per column
- Pattern analysis (random vs systematic)

### Descriptive Statistics
- Numeric: mean, median, std, min, max, quartiles
- Categorical: unique values, mode, frequency distribution

### Distribution Analysis
- Identify skewness in numeric columns
- Detect potential outliers (IQR method)

### Correlation Analysis
- Compute correlation matrix for numeric columns
- Highlight strong correlations (|r| > 0.7)

### Key Findings
- 3-5 bullet points summarizing notable patterns
- Potential data quality issues
- Suggested next steps

## Output Format

```markdown
## Analysis
[2-3 sentence summary of dataset characteristics]

## Dataset Overview
[Table with shape, types, memory]

## Missing Values
[Table or summary]

## Descriptive Statistics
[Statistics tables]

## Correlations
[Key correlations found]

## Key Findings
- Finding 1
- Finding 2
- Finding 3

## Code
[Complete Python script]

## Next Steps
- Suggested cleaning steps
- Recommended visualizations
- Further analysis ideas
```

## Language

Respond in the same language as the user (French or English).
