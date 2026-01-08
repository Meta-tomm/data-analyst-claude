---
name: Data Analyst Core
description: This skill should be used when the user asks to "analyze data", "clean a dataset", "write SQL queries", "create visualizations", "generate reports", "transform data", "run statistical tests", "create DAX measures", or any data analysis task involving Python, pandas, SQL, or Power BI.
version: 1.0.0
---

# Data Analyst Core Knowledge

Specialized knowledge base for data analysis workflows with Python, SQL, and Power BI.

## Output Format Standard

All data analysis responses follow this structure:

```markdown
## Analysis
[2-3 sentence summary of findings or approach]

## Code
[Commented Python/SQL script with imports and seed if applicable]

## Interpretation
[What results mean in plain language]

## Next Steps
[Suggested actions or follow-up analyses]
```

## Language Detection

Detect user language from their message. Respond in the same language (French or English). Default to English if unclear.

## Code Standards

### Python Best Practices

1. **Imports first**: Always include necessary imports at script start
2. **Reproducibility**: Set `random_state=42` or `np.random.seed(42)` when randomness involved
3. **Vectorized operations**: Prefer pandas/numpy vectorized ops over loops
4. **Type hints**: Include type hints for function signatures
5. **Comments**: Explain the "why", not the "what"

### Script Saving Convention

When generating scripts:
1. Display the complete code first
2. Ask: "Save this script to ./scripts/[descriptive-name].py?"
3. If confirmed, save with appropriate name
4. Outputs (CSVs, images) go to ./outputs/

## Core Pandas Patterns

### Loading Data

```python
import pandas as pd

# CSV with common issues handled
df = pd.read_csv('file.csv',
    encoding='utf-8',  # or 'latin-1' for Windows files
    parse_dates=['date_col'],
    na_values=['NA', 'N/A', '', 'null']
)

# Excel
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')

# From clipboard (interactive)
df = pd.read_clipboard()
```

### Quick Exploration

```python
# Shape and types
df.shape
df.dtypes
df.info()

# Statistics
df.describe(include='all')

# Missing values
df.isnull().sum()
df.isnull().sum() / len(df) * 100  # Percentage

# Unique values
df.nunique()
df['col'].value_counts()
```

### Common Transformations

```python
# Filter
df[df['col'] > value]
df.query('col > @value')

# Group and aggregate
df.groupby('cat_col').agg({
    'num_col': ['mean', 'sum', 'count'],
    'other_col': 'first'
}).reset_index()

# Pivot
df.pivot_table(
    values='value_col',
    index='row_col',
    columns='col_col',
    aggfunc='sum',
    fill_value=0
)

# Melt (unpivot)
df.melt(id_vars=['id'], value_vars=['col1', 'col2'])
```

## SQL Dialect Reference

### MySQL Specifics

```sql
-- Date formatting
DATE_FORMAT(date_col, '%Y-%m-%d')
-- String concat
CONCAT(col1, ' ', col2)
-- Limit with offset
LIMIT 10 OFFSET 20
-- Auto increment
AUTO_INCREMENT
```

### PostgreSQL Specifics

```sql
-- Date formatting
TO_CHAR(date_col, 'YYYY-MM-DD')
-- String concat
col1 || ' ' || col2
-- Limit with offset
LIMIT 10 OFFSET 20
-- Serial
SERIAL or GENERATED ALWAYS AS IDENTITY
-- Arrays
ARRAY_AGG(col), ANY(array)
-- JSON
data->>'key', jsonb_agg()
```

### SQLite Specifics

```sql
-- Date formatting
strftime('%Y-%m-%d', date_col)
-- String concat
col1 || ' ' || col2
-- Limit with offset
LIMIT 10 OFFSET 20
-- No native date type - use TEXT
```

## Statistical Tests Quick Reference

| Test | When to Use | Python |
|------|-------------|--------|
| t-test (independent) | Compare 2 group means | `scipy.stats.ttest_ind(a, b)` |
| t-test (paired) | Compare same group before/after | `scipy.stats.ttest_rel(before, after)` |
| ANOVA | Compare 3+ group means | `scipy.stats.f_oneway(g1, g2, g3)` |
| Chi-square | Categorical association | `scipy.stats.chi2_contingency(table)` |
| Pearson correlation | Linear relationship | `scipy.stats.pearsonr(x, y)` |
| Spearman correlation | Monotonic relationship | `scipy.stats.spearmanr(x, y)` |
| Shapiro-Wilk | Normality test (n<5000) | `scipy.stats.shapiro(data)` |
| Kolmogorov-Smirnov | Normality test (large n) | `scipy.stats.kstest(data, 'norm')` |

### Interpreting P-values

- p < 0.05: Statistically significant (reject null hypothesis)
- p >= 0.05: Not statistically significant (fail to reject null)
- Always report effect size alongside p-value

## Visualization Guidelines

### Chart Selection

| Data Type | Goal | Chart |
|-----------|------|-------|
| Categorical | Distribution | Bar chart |
| Numeric | Distribution | Histogram, Box plot |
| Time series | Trend | Line chart |
| Two numeric | Relationship | Scatter plot |
| Categories x Numeric | Comparison | Grouped bar, Box plot |
| Correlation matrix | Relationships | Heatmap |
| Parts of whole | Composition | Pie (if <6 cats), Stacked bar |

### Accessible Color Palettes

```python
# Colorblind-safe palettes
import seaborn as sns

# Categorical (up to 10 colors)
sns.color_palette("colorblind")

# Sequential
sns.color_palette("viridis")
sns.color_palette("cividis")  # Also colorblind-safe

# Diverging
sns.color_palette("RdBu")
```

## DAX Patterns

### Common Measures

```dax
// Year-over-Year Growth
YoY Growth =
VAR CurrentYear = [Total Sales]
VAR PreviousYear = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
RETURN DIVIDE(CurrentYear - PreviousYear, PreviousYear)

// Running Total
Running Total =
CALCULATE(
    [Total Sales],
    FILTER(
        ALL('Date'),
        'Date'[Date] <= MAX('Date'[Date])
    )
)

// Moving Average (30 days)
MA 30 Days =
AVERAGEX(
    DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -30, DAY),
    [Total Sales]
)
```

## Additional Resources

### Reference Files

For detailed patterns and advanced techniques, consult:
- **`references/pandas-patterns.md`** - Advanced pandas transformations
- **`references/sql-optimization.md`** - Query optimization techniques
- **`references/visualization-templates.md`** - Ready-to-use chart templates
