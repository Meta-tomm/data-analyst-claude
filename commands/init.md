---
name: init
description: Initialize a data analysis project - import data, setup workspace, configure environment
argument-hint: "[folder path]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
---

# Initialize Data Analysis Project

Collaborative setup of a data analysis workspace with the user.

## Purpose

Before any analysis, establish:
- Working directory
- Data sources
- Project context
- Output preferences

## Workflow

### Step 1: Workspace Setup

Ask the user:

```markdown
## Project Initialization

Let's set up your analysis workspace.

**1. Working Directory**
Where should we work?
- Current directory: `[current path]`
- Or specify another path

**2. Project Name**
What's a short name for this analysis? (e.g., "sales-q4-2024", "customer-churn")
```

Create structure:
```
project-name/
├── data/           # Raw data files
├── outputs/        # Analysis results
├── scripts/        # Generated Python/SQL scripts
└── docs/           # Plans, reports, notes
```

### Step 2: Data Import

```markdown
**3. Data Sources**

Where is your data?
- [ ] Local file(s) - provide path(s)
- [ ] Database - provide connection info
- [ ] Clipboard - paste data
- [ ] URL - provide link
- [ ] Already in ./data/ folder

**4. Data Format**
- [ ] CSV
- [ ] Excel (.xlsx)
- [ ] JSON
- [ ] SQL export
- [ ] Other: ___
```

Actions:
- Copy files to `./data/` if needed
- Verify files are readable
- Quick preview (first 5 rows, shape)

### Step 3: Context Gathering

```markdown
**5. Analysis Context**

What's the goal of this analysis?
- [ ] Exploratory (understand the data)
- [ ] Reporting (create dashboards/reports)
- [ ] Statistical (test hypotheses)
- [ ] Predictive (build models)
- [ ] Cleaning (prepare data for other tools)

**6. Target Output**

Where will results be used?
- [ ] Python/Jupyter - generate .py scripts
- [ ] Power BI - generate DAX formulas (.md to copy)
- [ ] Excel - generate formulas (.md to copy)
- [ ] SQL database - generate queries
- [ ] Report/Presentation - generate insights
- [ ] Multiple targets

**7. Audience**
- [ ] Technical (show code, stats)
- [ ] Business (show insights, recommendations)
- [ ] Executive (show key metrics only)
```

### Step 4: Environment Check

Verify tools available:

```python
# Check Python environment
import sys
print(f"Python: {sys.version}")

# Check key libraries
libraries = ['pandas', 'numpy', 'matplotlib', 'seaborn', 'plotly', 'scipy']
for lib in libraries:
    try:
        __import__(lib)
        print(f"✓ {lib}")
    except ImportError:
        print(f"✗ {lib} - not installed")
```

### Step 5: Save Configuration

Create `./docs/project-config.md`:

```markdown
# Project Configuration

**Name**: [project-name]
**Created**: YYYY-MM-DD
**Goal**: [analysis goal]

## Data Sources
- [file1.csv] - [description]
- [file2.xlsx] - [description]

## Target Outputs
- Primary: [Power BI / Python / Excel / etc.]
- Format: [.py / .md with formulas / .sql]

## Audience
- [Technical / Business / Executive]

## Notes
[Any special considerations]
```

### Step 6: Ready Confirmation

```markdown
## Project Initialized

**Workspace**: `[path]`
**Data files**:
- [file1] (X rows, Y columns)
- [file2] (X rows, Y columns)

**Configuration saved**: `./docs/project-config.md`

Ready to start analysis. Suggested next command:
- `/analyze` for exploratory analysis
- `/clean` to prepare data
- `/viz` for quick visualizations

What would you like to do first?
```

## Output Handling by Target

Based on "Target Output" selection:

### For Python
- Generate `.py` scripts in `./scripts/`
- Full executable code

### For Power BI
- Generate `.md` files with DAX formulas
- Format for easy copy-paste:
```markdown
## Measure: YoY Growth

```dax
YoY Growth =
VAR CurrentYear = SUM(Sales[Amount])
VAR PreviousYear = CALCULATE(SUM(Sales[Amount]), SAMEPERIODLASTYEAR('Date'[Date]))
RETURN DIVIDE(CurrentYear - PreviousYear, PreviousYear)
```

**Copy this formula to Power BI Desktop → Modeling → New Measure**
```

### For Excel
- Generate `.md` files with Excel formulas
- Include cell references guidance:
```markdown
## Formula: Running Total

```excel
=SUM($B$2:B2)
```

**Paste in column C, starting at C2. Assumes data in column B.**
```

### For SQL
- Generate `.sql` files
- Include database-specific syntax notes

## Language

Conduct initialization in the user's language (French or English).
