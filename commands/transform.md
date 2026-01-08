---
name: transform
description: Build data transformation pipelines
argument-hint: "\"describe transformations in natural language\""
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
---

# Data Transformation Pipeline Command

Build reproducible ETL pipelines and pandas transformation chains from natural language descriptions.

## Workflow

1. **Parse Transformation Request**
   - Identify source data
   - List transformations in order
   - Identify output format

2. **Design Pipeline**
   - Plan transformation steps
   - Identify dependencies between steps
   - Optimize order for performance

3. **Generate Pipeline Code**
   - Method chaining for readability
   - Clear documentation
   - Validation checks

4. **Test and Validate**
   - Show sample output
   - Verify row/column counts
   - Check for data loss

## Output Format

```markdown
## Analysis
[Summary of transformations to apply]

## Pipeline Steps
1. [Step 1 description]
2. [Step 2 description]
3. [Step 3 description]

## Code
```python
import pandas as pd
import numpy as np

def transform_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Data transformation pipeline.

    Steps:
    1. [Step 1]
    2. [Step 2]
    3. [Step 3]

    Args:
        df: Input DataFrame

    Returns:
        Transformed DataFrame
    """
    return (
        df
        # Step 1: Filter
        .query('condition')
        # Step 2: Transform
        .assign(new_col=lambda x: x['col'] * 2)
        # Step 3: Aggregate
        .groupby('category')
        .agg({'value': 'sum'})
        .reset_index()
    )

if __name__ == '__main__':
    df = pd.read_csv('input.csv')
    result = transform_pipeline(df)
    result.to_csv('output.csv', index=False)
    print(f"Transformed: {len(df)} -> {len(result)} rows")
```

## Validation
| Check | Result |
|-------|--------|
| Input rows | 1000 |
| Output rows | 250 |
| Columns | 5 -> 3 |
| Null values | 0 |

## Interpretation
[What the pipeline does and why]

## Next Steps
- Additional transformations
- Scheduling suggestions
- Data quality checks
```

## Common Transformation Patterns

### Aggregation
```python
(df
 .groupby(['cat1', 'cat2'])
 .agg(
     total=('value', 'sum'),
     count=('id', 'count'),
     avg=('value', 'mean')
 )
 .reset_index())
```

### Pivot
```python
(df
 .pivot_table(
     values='value',
     index='date',
     columns='category',
     aggfunc='sum',
     fill_value=0
 ))
```

### Unpivot (Melt)
```python
(df
 .melt(
     id_vars=['id', 'date'],
     value_vars=['col1', 'col2', 'col3'],
     var_name='metric',
     value_name='value'
 ))
```

### Window Functions
```python
(df
 .assign(
     running_total=lambda x: x.groupby('category')['value'].cumsum(),
     pct_of_total=lambda x: x['value'] / x.groupby('category')['value'].transform('sum'),
     rank=lambda x: x.groupby('category')['value'].rank(ascending=False)
 ))
```

### Date Aggregation
```python
(df
 .assign(month=lambda x: x['date'].dt.to_period('M'))
 .groupby('month')
 .agg({'value': 'sum'})
 .reset_index())
```

### Join Multiple Sources
```python
(df1
 .merge(df2, on='key', how='left')
 .merge(df3, on='key', how='left'))
```

## Pipeline Best Practices

1. **Method Chaining**: Use `.pipe()` for custom functions
2. **Immutability**: Always return new DataFrames
3. **Documentation**: Document each step
4. **Validation**: Add assertions for data quality
5. **Logging**: Track row counts at each step

```python
def log_shape(df, step_name):
    print(f"{step_name}: {df.shape}")
    return df

(df
 .pipe(log_shape, "Input")
 .query('value > 0')
 .pipe(log_shape, "After filter")
 .groupby('cat').sum()
 .pipe(log_shape, "After aggregation"))
```

## Language

Respond in the same language as the user.
