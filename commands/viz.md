---
name: viz
description: Create data visualizations with appropriate chart types
argument-hint: "[file.csv] [--type auto|bar|line|scatter|heatmap|box|hist]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
---

# Visualization Command

Create effective, accessible visualizations using Plotly (default) or Seaborn.

## Workflow

1. **Understand Data**
   - Load and inspect dataset
   - Identify column types (numeric, categorical, datetime)
   - Understand relationships to visualize

2. **Select Chart Type**
   - If `--type auto`: Recommend based on data and context
   - Otherwise use specified type

3. **Generate Visualization Code**
   - Use Plotly by default (interactive)
   - Include accessible color palette
   - Add proper labels, title, legend

4. **Offer Export Options**
   - Interactive HTML
   - Static PNG (high resolution)
   - Save to ./outputs/

## Chart Selection Guide

| Data | Goal | Chart Type |
|------|------|------------|
| 1 categorical | Distribution | Bar chart |
| 1 numeric | Distribution | Histogram |
| 1 numeric by category | Comparison | Box plot, Violin |
| 2 numeric | Relationship | Scatter plot |
| Time + numeric | Trend | Line chart |
| Many numerics | Correlations | Heatmap |
| Parts of whole | Composition | Pie (if <6), Stacked bar |
| Category + numeric | Ranking | Horizontal bar |

## Output Format

```markdown
## Analysis
[Why this chart type is appropriate for this data]

## Code
```python
import plotly.express as px
import pandas as pd

# Load data
df = pd.read_csv('data.csv')

# Create visualization
fig = px.bar(
    df,
    x='category',
    y='value',
    color='group',
    title='Chart Title',
    labels={'value': 'Value ($)', 'category': 'Category'},
    color_discrete_sequence=px.colors.qualitative.Safe  # Colorblind-safe
)

# Style
fig.update_layout(
    template='plotly_white',
    font_family='Arial',
    title_font_size=16
)

# Show
fig.show()

# Export
fig.write_html('outputs/chart.html')
fig.write_image('outputs/chart.png', scale=2)
```

## Interpretation
[What the visualization reveals about the data]

## Next Steps
- Alternative visualizations to consider
- Follow-up analyses
```

## Plotly Chart Templates

### Line (Time Series)
```python
fig = px.line(df, x='date', y='value', color='category',
              title='Trend Over Time')
fig.update_layout(hovermode='x unified')
```

### Bar
```python
fig = px.bar(df, x='cat', y='val', color='group',
             barmode='group', text_auto='.2s')
```

### Scatter
```python
fig = px.scatter(df, x='x', y='y', color='cat',
                 size='size_col', trendline='ols')
```

### Heatmap
```python
fig = px.imshow(df.corr(), text_auto='.2f',
                color_continuous_scale='RdBu_r')
```

### Box
```python
fig = px.box(df, x='category', y='value',
             color='group', points='outliers')
```

### Histogram
```python
fig = px.histogram(df, x='value', nbins=30,
                   color='cat', marginal='box')
```

## Accessibility

Always use colorblind-safe palettes:
- `px.colors.qualitative.Safe`
- `px.colors.sequential.Viridis`
- `px.colors.diverging.RdBu`

Add text labels when possible for clarity.

## Language

Respond in the same language as the user.
