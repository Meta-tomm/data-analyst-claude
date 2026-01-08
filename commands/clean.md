---
name: clean
description: Clean and preprocess a dataset
argument-hint: "[file.csv] [--strategy conservative|aggressive]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
---

# Data Cleaning Command

Propose and apply data cleaning transformations with reproducible Python scripts.

## Strategies

### Conservative (Default)
- Preserve data when possible
- Impute missing values (median for numeric, mode for categorical)
- Flag outliers without removing
- Document all transformations

### Aggressive
- Remove rows with missing values in key columns
- Remove outliers using IQR method (1.5x)
- Standardize numeric columns
- One-hot encode categoricals

## Workflow

1. **Load and Assess**
   - Read the dataset
   - Identify data quality issues:
     - Missing values (count, percentage, pattern)
     - Duplicates
     - Outliers
     - Inconsistent formats
     - Invalid values

2. **Propose Transformations**
   - List each issue found
   - Propose specific fix for each
   - Explain rationale

3. **Generate Cleaning Script**

   ```python
   import pandas as pd
   import numpy as np

   def clean_data(df: pd.DataFrame) -> pd.DataFrame:
       """
       Clean dataset with [strategy] strategy.

       Transformations applied:
       1. [transformation 1]
       2. [transformation 2]
       ...
       """
       df = df.copy()

       # Step 1: Handle missing values
       # ...

       # Step 2: Handle duplicates
       # ...

       # Step 3: Handle outliers
       # ...

       return df

   if __name__ == '__main__':
       df = pd.read_csv('input.csv')
       df_clean = clean_data(df)
       df_clean.to_csv('output_clean.csv', index=False)
       print(f"Cleaned: {len(df)} -> {len(df_clean)} rows")
   ```

4. **Show Before/After Summary**
   - Row count change
   - Column changes
   - Data quality metrics improvement

5. **Ask to Save**
   - Save script to ./scripts/clean_[filename].py
   - Save cleaned data to ./outputs/[filename]_clean.csv

## Output Format

```markdown
## Analysis
[Summary of data quality issues found]

## Issues Detected
| Issue | Column | Count | Proposed Fix |
|-------|--------|-------|--------------|
| Missing | col1 | 15% | Impute median |
| Outliers | col2 | 23 | Flag in new column |

## Code
[Complete cleaning script]

## Before/After
| Metric | Before | After |
|--------|--------|-------|
| Rows | 1000 | 985 |
| Missing % | 12% | 0% |

## Interpretation
[What was done and why]

## Next Steps
- Validation suggestions
- Further cleaning if needed
```

## Cleaning Techniques Reference

### Missing Values
- **Drop**: If <5% and random
- **Impute numeric**: median (robust to outliers) or mean
- **Impute categorical**: mode or "Unknown"
- **Forward fill**: Time series data
- **Interpolate**: Continuous time series

### Outliers
- **IQR method**: Values outside Q1-1.5*IQR to Q3+1.5*IQR
- **Z-score**: Values with |z| > 3
- **Domain knowledge**: Business rules

### Encoding
- **Label encoding**: Ordinal categories
- **One-hot**: Nominal categories (<10 unique)
- **Target encoding**: High cardinality

### Normalization
- **StandardScaler**: Mean=0, Std=1 (when distribution ~normal)
- **MinMaxScaler**: Range [0,1] (when bounds matter)
- **RobustScaler**: Using median/IQR (when outliers present)

## Language

Respond in the same language as the user.
