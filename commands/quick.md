---
name: quick
description: Quick answers for pandas, numpy, SQL, and DAX syntax
argument-hint: "\"your question\""
allowed-tools:
  - Read
---

# Quick Reference Command

Fast, concise answers for common data analysis syntax questions.

## Response Style

- **Direct**: Answer first, explanation second
- **Concise**: One-liners when possible
- **Practical**: Working code snippets
- **Copy-ready**: Easy to paste and use

## Output Format

```markdown
## Code
```python
# [One-liner solution]
df.pivot_table(values='val', index='row', columns='col', aggfunc='sum')
```

## Explanation
[Brief explanation if needed]

## Alternatives
[Other approaches if relevant]
```

## Quick Reference Categories

### Pandas One-Liners

```python
# Pivot table
df.pivot_table(values='val', index='row', columns='col', aggfunc='sum')

# Unpivot (melt)
df.melt(id_vars=['id'], value_vars=['col1', 'col2'])

# Group and aggregate multiple
df.groupby('cat').agg({'col1': 'sum', 'col2': 'mean'})

# Conditional column
df['new'] = df['col'].apply(lambda x: 'A' if x > 0 else 'B')
# or faster:
df['new'] = np.where(df['col'] > 0, 'A', 'B')

# Filter multiple conditions
df[(df['col1'] > 10) & (df['col2'] == 'A')]
# or:
df.query('col1 > 10 and col2 == "A"')

# Drop duplicates keeping first
df.drop_duplicates(subset=['col1', 'col2'], keep='first')

# Rank within groups
df['rank'] = df.groupby('cat')['val'].rank(ascending=False)

# Rolling average
df['ma_7'] = df['val'].rolling(7).mean()

# Cumulative sum
df['cumsum'] = df.groupby('cat')['val'].cumsum()

# Percentage of total
df['pct'] = df['val'] / df['val'].sum()

# Forward fill nulls
df['col'].fillna(method='ffill')

# String to datetime
pd.to_datetime(df['date'], format='%Y-%m-%d')

# Extract year/month from date
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# Merge/Join
pd.merge(df1, df2, on='key', how='left')

# Concat vertically
pd.concat([df1, df2], ignore_index=True)

# Sample n rows
df.sample(n=100, random_state=42)

# Value counts with percentage
df['col'].value_counts(normalize=True)

# Cross-tabulation
pd.crosstab(df['col1'], df['col2'])

# Bin numeric to categories
pd.cut(df['val'], bins=5, labels=['A','B','C','D','E'])

# Replace values
df['col'].replace({'old': 'new', 'old2': 'new2'})

# Rename columns
df.rename(columns={'old_name': 'new_name'})

# Reorder columns
df = df[['col3', 'col1', 'col2']]

# Memory usage
df.memory_usage(deep=True).sum() / 1024**2  # MB
```

### NumPy Quick Ref

```python
# Create array
np.array([1, 2, 3])
np.zeros((3, 4))
np.ones((3, 4))
np.arange(0, 10, 2)
np.linspace(0, 1, 5)

# Random
np.random.seed(42)
np.random.rand(3, 4)      # Uniform [0,1)
np.random.randn(3, 4)     # Standard normal
np.random.randint(0, 10, size=(3, 4))

# Statistics
np.mean(arr, axis=0)
np.std(arr)
np.percentile(arr, [25, 50, 75])

# Reshape
arr.reshape(3, 4)
arr.flatten()
arr.T  # Transpose

# Boolean indexing
arr[arr > 0]
np.where(arr > 0, arr, 0)
```

### SQL Quick Ref

```sql
-- Window function rank
ROW_NUMBER() OVER (PARTITION BY cat ORDER BY val DESC)

-- Running total
SUM(val) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING)

-- Lag/Lead
LAG(val, 1) OVER (ORDER BY date)

-- Case when
CASE WHEN cond1 THEN 'A' WHEN cond2 THEN 'B' ELSE 'C' END

-- Coalesce (first non-null)
COALESCE(col1, col2, 'default')

-- String concat
CONCAT(col1, ' ', col2)  -- MySQL
col1 || ' ' || col2      -- PostgreSQL/SQLite

-- Date truncate
DATE_TRUNC('month', date_col)  -- PostgreSQL
DATE_FORMAT(date_col, '%Y-%m-01')  -- MySQL

-- Extract
EXTRACT(YEAR FROM date_col)

-- Current date
CURRENT_DATE  -- PostgreSQL
CURDATE()     -- MySQL
DATE('now')   -- SQLite
```

### DAX Quick Ref

```dax
// Sum with filter
CALCULATE(SUM(Table[Col]), Table[Category] = "A")

// Year-to-date
TOTALYTD(SUM(Sales[Amount]), 'Date'[Date])

// Previous year
SAMEPERIODLASTYEAR('Date'[Date])

// Divide safely (no error on zero)
DIVIDE(numerator, denominator, 0)

// Distinct count
DISTINCTCOUNT(Table[Col])

// Rank
RANKX(ALL(Table), [Measure], , DESC)

// If blank
IF(ISBLANK([Measure]), 0, [Measure])

// Selected value (single selection)
SELECTEDVALUE(Table[Col], "Default")

// All except (keep filter on specific columns)
ALLEXCEPT(Table, Table[Col1])
```

## Language

Respond in the same language as the user.
