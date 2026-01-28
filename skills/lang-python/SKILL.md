---
name: lang-python
description: "Use when writing Python for data analysis. Covers pandas, numpy, scipy, matplotlib, seaborn, polars. Patterns, anti-patterns, best practices."
---

# Python Data Analysis

Best practices and patterns for Python data analysis.

## Output Format

```markdown
## Analysis
[2-3 sentence summary]

## Code
[Complete Python script with imports]

## Interpretation
[What results mean in plain language]

## Next Steps
[Suggested follow-up]
```

## Code Standards

1. **Imports first** with standard ordering (stdlib, third-party, local)
2. **Reproducibility:** `random_state=42` or `np.random.seed(42)`
3. **Vectorized operations** over loops (pandas/numpy)
4. **Type hints** for function signatures
5. **Comments:** explain "why", not "what"

### Script Convention
- Display code first
- Ask: "Save to ./scripts/[name].py?"
- Outputs (CSVs, images) go to ./outputs/

## Pandas Patterns

### Loading Data
```python
import pandas as pd

df = pd.read_csv('file.csv',
    encoding='utf-8',
    parse_dates=['date_col'],
    na_values=['NA', 'N/A', '', 'null']
)
df = pd.read_excel('file.xlsx', sheet_name='Sheet1')
```

### Exploration
```python
df.shape; df.dtypes; df.info()
df.describe(include='all')
df.isnull().sum()
df.isnull().sum() / len(df) * 100
df.nunique()
df['col'].value_counts()
```

### Transformations
```python
# Filter
df[df['col'] > value]
df.query('col > @value')

# Group and aggregate
df.groupby('cat_col').agg({
    'num_col': ['mean', 'sum', 'count'],
    'other_col': 'first'
}).reset_index()

# Pivot / Unpivot
df.pivot_table(values='val', index='row', columns='col', aggfunc='sum', fill_value=0)
df.melt(id_vars=['id'], value_vars=['col1', 'col2'])

# Merge
pd.merge(df1, df2, on='key', how='left')

# Window functions
df['rolling_mean'] = df.groupby('cat')['val'].transform(lambda x: x.rolling(7).mean())
df['rank'] = df.groupby('cat')['val'].rank(method='dense', ascending=False)
df['cumsum'] = df.groupby('cat')['val'].cumsum()
df['pct_change'] = df.groupby('cat')['val'].pct_change()
```

### Date Operations
```python
df['date'] = pd.to_datetime(df['date_str'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['weekday'] = df['date'].dt.day_name()
df['quarter'] = df['date'].dt.quarter

# Resample time series
df.set_index('date').resample('M')['value'].sum()
df.set_index('date').resample('W')['value'].mean()
```

### String Operations
```python
df['col'].str.lower()
df['col'].str.contains('pattern', case=False, na=False)
df['col'].str.extract(r'(\d+)')
df['col'].str.split('-', expand=True)
df['col'].str.replace(r'\s+', ' ', regex=True)
```

## Data Cleaning Patterns

```python
# Missing values
df['num'].fillna(df['num'].median(), inplace=True)
df['cat'].fillna('Unknown', inplace=True)
df.dropna(subset=['critical_col'])

# Duplicates
df.drop_duplicates(subset=['key1', 'key2'], keep='first')

# Outliers (IQR)
Q1, Q3 = df['col'].quantile([0.25, 0.75])
IQR = Q3 - Q1
mask = (df['col'] >= Q1 - 1.5*IQR) & (df['col'] <= Q3 + 1.5*IQR)
df_clean = df[mask]

# Type conversion
df['col'] = pd.to_numeric(df['col'], errors='coerce')
df['col'] = df['col'].astype('category')
```

## Statistical Tests

| Test | When | Code |
|------|------|------|
| t-test (independent) | Compare 2 group means | `scipy.stats.ttest_ind(a, b)` |
| t-test (paired) | Same group before/after | `scipy.stats.ttest_rel(before, after)` |
| ANOVA | Compare 3+ group means | `scipy.stats.f_oneway(g1, g2, g3)` |
| Chi-square | Categorical association | `scipy.stats.chi2_contingency(table)` |
| Pearson | Linear correlation | `scipy.stats.pearsonr(x, y)` |
| Spearman | Monotonic correlation | `scipy.stats.spearmanr(x, y)` |
| Mann-Whitney | Non-parametric 2 groups | `scipy.stats.mannwhitneyu(a, b)` |
| Shapiro-Wilk | Normality (n<5000) | `scipy.stats.shapiro(data)` |

**P-value:** <0.05 = significant. Always report effect size.

## Visualization

### Chart Selection
| Data Type | Goal | Chart |
|-----------|------|-------|
| Categorical | Distribution | Bar chart |
| Numeric | Distribution | Histogram, Box plot |
| Time series | Trend | Line chart |
| Two numeric | Relationship | Scatter plot |
| Correlation matrix | Relationships | Heatmap |

### Plotly (default)
```python
import plotly.express as px

fig = px.line(df, x='date', y='value', color='category', title='Trend')
fig.update_layout(template='plotly_white')
fig.write_html('outputs/chart.html')
```

### Seaborn
```python
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=df, x='cat', y='val', ax=ax)
plt.tight_layout()
plt.savefig('outputs/chart.png', dpi=150)
```

### Colorblind-safe palettes
```python
sns.color_palette("colorblind")  # Categorical
sns.color_palette("viridis")     # Sequential
sns.color_palette("RdBu")        # Diverging
```

## Polars (Alternative for Large Data)

```python
import polars as pl

df = pl.read_csv('large_file.csv')
result = (
    df.lazy()
    .filter(pl.col('status') == 'active')
    .group_by('category')
    .agg(pl.col('amount').sum().alias('total'))
    .sort('total', descending=True)
    .collect()
)
```

Use polars when: >1M rows, performance critical, or memory constrained.

## Anti-Patterns

| Bad | Good |
|-----|------|
| `for i, row in df.iterrows()` | Vectorized ops or `.apply()` |
| `df['col'].apply(lambda x: ...)` for simple ops | `df['col'] * 2` |
| `pd.concat` in loop | Collect list, concat once |
| `import *` | Explicit imports |
| No `random_state` | Always set seed |
| `.inplace=True` everywhere | Assign to variable |

## Language

Respond in the same language as the user.
