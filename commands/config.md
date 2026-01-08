---
name: config
description: Configure plugin preferences
allowed-tools:
  - Read
  - Write
---

# Configuration Command

Display and modify plugin configuration options.

## Current Configuration

Display current settings:

```markdown
## Data Analyst Configuration

| Setting | Current Value | Options |
|---------|---------------|---------|
| Default visualization library | Plotly | plotly, seaborn |
| Default cleaning strategy | conservative | conservative, aggressive |
| Default SQL dialect | PostgreSQL | mysql, postgres, sqlite |
| Default report audience | business | tech, business, executive |
| Auto-save scripts | false | true, false |
| Output directory | ./outputs/ | custom path |
| Scripts directory | ./scripts/ | custom path |
| Language | auto | auto, en, fr |
```

## Modify Settings

To change a setting, specify:

```bash
/config --viz-lib seaborn
/config --clean-strategy aggressive
/config --sql-dialect mysql
/config --auto-save true
/config --output-dir ./results/
/config --language fr
```

## Configuration File

Settings are stored in `.claude/data-analyst.local.md`:

```yaml
---
viz_library: plotly
clean_strategy: conservative
sql_dialect: postgres
report_audience: business
auto_save: false
output_dir: ./outputs/
scripts_dir: ./scripts/
language: auto
---
```

## Setting Descriptions

### viz_library
- `plotly`: Interactive charts, HTML export, modern look
- `seaborn`: Static charts, publication-quality, matplotlib-based

### clean_strategy
- `conservative`: Preserve data, impute missing, flag outliers
- `aggressive`: Remove missing rows, remove outliers, normalize

### sql_dialect
- `postgres`: PostgreSQL syntax (DATE_TRUNC, ||, etc.)
- `mysql`: MySQL syntax (DATE_FORMAT, CONCAT, etc.)
- `sqlite`: SQLite syntax (strftime, ||, etc.)

### report_audience
- `tech`: Full methodology, code, statistical details
- `business`: Actionable insights, visualizations, recommendations
- `executive`: Executive summary, key metrics, strategic points

### auto_save
- `true`: Automatically save scripts to scripts_dir
- `false`: Display code, ask before saving

### language
- `auto`: Detect from user message
- `en`: Always respond in English
- `fr`: Always respond in French

## Reset to Defaults

```bash
/config --reset
```

## Response

When user runs `/config`:

1. If no arguments: Display current configuration
2. If `--setting value`: Update the setting
3. If `--reset`: Reset all to defaults

Respond in the user's language.
