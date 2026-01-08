# Visualization Templates

## Plotly Templates

### Line Chart (Time Series)

```python
import plotly.express as px
import plotly.graph_objects as go

fig = px.line(
    df,
    x='date',
    y='value',
    color='category',
    title='Trend Over Time',
    labels={'value': 'Sales ($)', 'date': 'Date'}
)
fig.update_layout(
    template='plotly_white',
    hovermode='x unified',
    legend=dict(orientation='h', yanchor='bottom', y=1.02)
)
fig.show()
```

### Bar Chart

```python
fig = px.bar(
    df,
    x='category',
    y='value',
    color='group',
    barmode='group',
    title='Comparison by Category',
    text_auto='.2s'
)
fig.update_layout(
    template='plotly_white',
    xaxis_tickangle=-45
)
fig.show()
```

### Scatter Plot with Regression

```python
fig = px.scatter(
    df,
    x='x_col',
    y='y_col',
    color='category',
    size='size_col',
    trendline='ols',
    title='Relationship Analysis',
    hover_data=['extra_col']
)
fig.update_layout(template='plotly_white')
fig.show()
```

### Heatmap (Correlation Matrix)

```python
import numpy as np

corr = df.select_dtypes(include=[np.number]).corr()

fig = px.imshow(
    corr,
    text_auto='.2f',
    aspect='auto',
    color_continuous_scale='RdBu_r',
    title='Correlation Matrix'
)
fig.update_layout(template='plotly_white')
fig.show()
```

### Box Plot

```python
fig = px.box(
    df,
    x='category',
    y='value',
    color='group',
    title='Distribution by Category',
    points='outliers'
)
fig.update_layout(template='plotly_white')
fig.show()
```

### Histogram

```python
fig = px.histogram(
    df,
    x='value',
    nbins=30,
    color='category',
    marginal='box',
    title='Value Distribution'
)
fig.update_layout(template='plotly_white', bargap=0.1)
fig.show()
```

### Pie/Donut Chart

```python
fig = px.pie(
    df,
    values='value',
    names='category',
    hole=0.4,  # 0 for pie, >0 for donut
    title='Composition'
)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.show()
```

## Seaborn Templates

### Distribution Plot

```python
import seaborn as sns
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(data=df, x='value', hue='category', kde=True, ax=ax)
ax.set_title('Value Distribution')
plt.tight_layout()
plt.show()
```

### Box Plot with Swarm

```python
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='category', y='value', ax=ax)
sns.swarmplot(data=df, x='category', y='value', color='black', alpha=0.5, ax=ax)
ax.set_title('Distribution with Individual Points')
plt.tight_layout()
plt.show()
```

### Pair Plot

```python
g = sns.pairplot(
    df,
    hue='category',
    diag_kind='kde',
    corner=True,
    palette='colorblind'
)
g.fig.suptitle('Pairwise Relationships', y=1.02)
plt.show()
```

### Heatmap with Annotations

```python
fig, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(
    df.corr(),
    annot=True,
    fmt='.2f',
    cmap='RdBu_r',
    center=0,
    vmin=-1,
    vmax=1,
    ax=ax
)
ax.set_title('Correlation Matrix')
plt.tight_layout()
plt.show()
```

### Faceted Plot

```python
g = sns.FacetGrid(df, col='category', col_wrap=3, height=4)
g.map_dataframe(sns.histplot, x='value')
g.set_titles(col_template='{col_name}')
g.fig.suptitle('Distribution by Category', y=1.02)
plt.show()
```

## Export Templates

### Save to File

```python
# Plotly - Interactive HTML
fig.write_html('outputs/chart.html')

# Plotly - Static image (requires kaleido)
fig.write_image('outputs/chart.png', scale=2)

# Matplotlib/Seaborn
plt.savefig('outputs/chart.png', dpi=300, bbox_inches='tight')
plt.savefig('outputs/chart.pdf', bbox_inches='tight')
```

### Dashboard Layout (Plotly)

```python
from plotly.subplots import make_subplots

fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=('Chart 1', 'Chart 2', 'Chart 3', 'Chart 4'),
    specs=[[{'type': 'xy'}, {'type': 'xy'}],
           [{'type': 'xy'}, {'type': 'domain'}]]
)

# Add traces to each subplot
fig.add_trace(go.Bar(x=df['cat'], y=df['val']), row=1, col=1)
fig.add_trace(go.Scatter(x=df['date'], y=df['val']), row=1, col=2)
fig.add_trace(go.Box(y=df['val']), row=2, col=1)
fig.add_trace(go.Pie(values=df['val'], labels=df['cat']), row=2, col=2)

fig.update_layout(height=800, title_text='Dashboard')
fig.show()
```

## Color Palettes

### Colorblind-Safe Options

```python
# Plotly
color_discrete_sequence=px.colors.qualitative.Safe

# Seaborn
palette='colorblind'
palette='viridis'
palette='cividis'

# Custom accessible palette
ACCESSIBLE_COLORS = [
    '#0072B2',  # Blue
    '#E69F00',  # Orange
    '#009E73',  # Green
    '#CC79A7',  # Pink
    '#F0E442',  # Yellow
    '#56B4E9',  # Light blue
    '#D55E00',  # Red-orange
]
```

## Styling Best Practices

```python
# Remove chart junk
fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font_family='Arial',
    title_font_size=16,
    showlegend=True,
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    )
)

# Clean axes
fig.update_xaxes(
    showgrid=True,
    gridwidth=1,
    gridcolor='lightgray',
    showline=True,
    linewidth=1,
    linecolor='gray'
)
```
