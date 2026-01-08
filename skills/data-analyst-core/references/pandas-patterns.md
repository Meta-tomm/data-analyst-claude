# Advanced Pandas Patterns

## Data Cleaning Patterns

### Handling Missing Values

```python
# Strategy 1: Drop rows with any null
df.dropna()

# Strategy 2: Drop rows where specific columns are null
df.dropna(subset=['important_col'])

# Strategy 3: Impute with statistics
df['num_col'].fillna(df['num_col'].median(), inplace=True)
df['cat_col'].fillna(df['cat_col'].mode()[0], inplace=True)

# Strategy 4: Forward/backward fill (time series)
df['value'].fillna(method='ffill', inplace=True)

# Strategy 5: Interpolation
df['value'].interpolate(method='linear', inplace=True)
```

### Outlier Detection

```python
# IQR method
Q1 = df['col'].quantile(0.25)
Q3 = df['col'].quantile(0.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
outliers = df[(df['col'] < lower) | (df['col'] > upper)]

# Z-score method
from scipy import stats
z_scores = stats.zscore(df['col'])
outliers = df[abs(z_scores) > 3]
```

### Data Type Conversions

```python
# String to datetime
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

# String to numeric (handling errors)
df['num'] = pd.to_numeric(df['num'], errors='coerce')

# Category for memory efficiency
df['cat_col'] = df['cat_col'].astype('category')

# Boolean from string
df['bool'] = df['bool_str'].map({'yes': True, 'no': False})
```

## String Operations

```python
# Clean whitespace
df['col'] = df['col'].str.strip()

# Case conversion
df['col'] = df['col'].str.lower()

# Extract with regex
df['code'] = df['text'].str.extract(r'(\d{3}-\d{4})')

# Split into multiple columns
df[['first', 'last']] = df['name'].str.split(' ', n=1, expand=True)

# Replace patterns
df['col'] = df['col'].str.replace(r'\s+', ' ', regex=True)
```

## Date Operations

```python
# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.day_name()
df['quarter'] = df['date'].dt.quarter

# Date arithmetic
df['days_since'] = (pd.Timestamp.now() - df['date']).dt.days

# Resample time series
df.set_index('date').resample('M').agg({
    'sales': 'sum',
    'customers': 'nunique'
})

# Rolling calculations
df['ma_7'] = df['value'].rolling(window=7).mean()
df['cumsum'] = df['value'].cumsum()
```

## Merge Patterns

```python
# Inner join
pd.merge(df1, df2, on='key', how='inner')

# Left join with suffixes
pd.merge(df1, df2, on='key', how='left', suffixes=('_left', '_right'))

# Multiple keys
pd.merge(df1, df2, on=['key1', 'key2'])

# Different column names
pd.merge(df1, df2, left_on='id1', right_on='id2')

# Concat vertically
pd.concat([df1, df2], ignore_index=True)

# Concat horizontally
pd.concat([df1, df2], axis=1)
```

## Window Functions

```python
# Rank within groups
df['rank'] = df.groupby('category')['value'].rank(method='dense', ascending=False)

# Lag/Lead
df['prev_value'] = df.groupby('id')['value'].shift(1)
df['next_value'] = df.groupby('id')['value'].shift(-1)

# Percent change
df['pct_change'] = df.groupby('id')['value'].pct_change()

# Cumulative sum per group
df['cum_sum'] = df.groupby('id')['value'].cumsum()
```

## Performance Tips

```python
# Use query() for filtering (faster for large DataFrames)
df.query('col > 100 and category == "A"')

# Use eval() for column operations
df.eval('new_col = col1 + col2')

# Iterate efficiently with itertuples (not iterrows)
for row in df.itertuples():
    process(row.col1, row.col2)

# Vectorized string operations
df['col'].str.contains('pattern')  # vs apply with regex

# Categorical for repeated strings
df['category'] = df['category'].astype('category')
```

## Memory Optimization

```python
# Downcast numeric types
df['int_col'] = pd.to_numeric(df['int_col'], downcast='integer')
df['float_col'] = pd.to_numeric(df['float_col'], downcast='float')

# Check memory usage
df.memory_usage(deep=True)

# Read in chunks for large files
chunks = pd.read_csv('large.csv', chunksize=10000)
for chunk in chunks:
    process(chunk)
```
