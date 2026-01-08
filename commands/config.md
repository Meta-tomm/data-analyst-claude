---
description: "Configure your data environment - SQL dialect, systems, contacts, jargon, plugin settings. Persists between sessions."
allowed-tools:
  - Read
  - Write
---

Invoke the data-analyst:data-config skill and follow it exactly.

# Additional Plugin Settings

## Quick Settings

| Setting | Current Value | Options |
|---------|---------------|---------|
| Default visualization library | Plotly | plotly, seaborn |
| Default cleaning strategy | conservative | conservative, aggressive |
| Default SQL dialect | PostgreSQL | mysql, postgres, sqlite, snowflake, bigquery |
| Default report audience | business | tech, business, executive |
| Auto-save scripts | false | true, false |
| Output directory | ./outputs/ | custom path |
| Scripts directory | ./scripts/ | custom path |
| Language | auto | auto, en, fr |

## Modify Settings

```bash
/config --viz-lib seaborn
/config --sql-dialect snowflake
/config --language fr
/config --reset
```

## Full Environment Config

For complete environment setup (systems, contacts, jargon), the skill creates `.claude/data-analyst.local.md` with:
- SQL dialect and systems
- Database connections
- Key contacts
- Internal jargon/glossary
- Business rules
- Naming conventions
