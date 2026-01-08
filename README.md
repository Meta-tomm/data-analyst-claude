# Data Analyst Plugin

Expert Data Analyst assistant for Python, SQL, and Power BI workflows.

## Features

- **Exploratory Analysis** (`/analyze`) - Complete dataset exploration with statistics and correlations
- **Data Cleaning** (`/clean`) - Smart data cleaning with Python scripts
- **SQL Assistant** (`/sql`) - Natural language to SQL, optimization, explanations
- **Visualization** (`/viz`) - Charts with Plotly/Seaborn, accessible palettes
- **Report Generation** (`/report`) - Professional reports for any audience
- **ETL Pipelines** (`/transform`) - Build pandas transformation pipelines
- **Statistical Tests** (`/stats`) - Hypothesis testing with clear interpretations
- **Power BI Helper** (`/powerbi`) - DAX measures and model optimization
- **Quick Reference** (`/quick`) - Fast answers for pandas/numpy syntax

## Installation

Copy to your Claude plugins directory or use with `--plugin-dir`:

```bash
claude --plugin-dir ./data-analyst
```

## Usage

All commands support bilingual output (French/English) - Claude adapts to your language.

### Quick Examples

```
/analyze sales.csv
/clean data.csv --strategy conservative
/sql "find customers with more than 3 orders this month"
/viz revenue.csv --type line
/report --audience executive
/stats --test correlation
/powerbi "create YoY growth measure"
/quick "how to pivot a dataframe"
```

## Output Format

All commands follow a consistent structure:

```
## Analysis
[2-3 sentence summary]

## Code
[Commented Python/SQL script]

## Interpretation
[What results mean concretely]

## Next Steps
[Suggested actions]
```

## Configuration

Scripts are displayed first, then you're asked if you want to save them to `./scripts/`.
Outputs go to `./outputs/` when generated.

## Supported Stack

- **Python**: pandas, numpy, scipy, matplotlib, seaborn, plotly
- **SQL**: MySQL, PostgreSQL, SQLite
- **Power BI**: DAX measures, data modeling
