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

Perform comprehensive exploratory analysis on the provided dataset.

## Workflow

1. **Load Data**
   - If file path provided, read the file
   - If no file, ask user to paste data or provide path
   - Support CSV, Excel, JSON formats

2. **Generate Analysis Report**

   Structure the analysis as:

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

3. **Generate Python Script**

   Provide reproducible code that performs all analyses:

   ```python
   import pandas as pd
   import numpy as np

   # Load data
   df = pd.read_csv('file.csv')

   # Analysis code...
   ```

4. **Ask to Save**
   - Offer to save report to ./outputs/analysis_report.md
   - Offer to save script to ./scripts/eda_[filename].py

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
