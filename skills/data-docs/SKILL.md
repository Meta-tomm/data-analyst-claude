---
name: data-docs
description: "Use when creating, exporting, or importing data documentation. Covers data dictionaries, domain guides, glossary, offline cheatsheets, and external doc import."
---

# Data Documentation

Create, export, and import structured data documentation.

## Capabilities

1. **Catalog** - Data dictionaries, domain guides, glossary, contacts
2. **Export** - Offline cheatsheets and standalone references
3. **Import** - Integrate external docs (Confluence, Notion, wiki, Slack)

---

## 1. Documentation Catalog

**Output:** `docs/catalog/`

### Document Types

**Data Dictionary** (per table):
```markdown
# Table: [schema].[table_name]

## Overview
- **Purpose:** [what this table stores]
- **Source:** [where data comes from]
- **Update frequency:** [real-time/daily/weekly]
- **Row count:** [approximate]
- **Owner:** [team/person]

## Columns

| Column | Type | Nullable | Description | Example |
|--------|------|----------|-------------|---------|
| id | bigint | No | Primary key | 12345 |

## Relationships
- [column] -> [other_table].[column]

## Business Rules
- [Rule 1]

## Known Issues
- [Issue 1]
```

Save to: `docs/catalog/tables/[schema]-[table].md`

**Domain Guide** (per business domain):
```markdown
# Domain: [Sales/Marketing/Finance/etc]

## Overview
[What this domain covers]

## Key Tables
| Table | Purpose | Key Columns |
|-------|---------|-------------|

## Key Metrics
| Metric | Definition | Table/Column |
|--------|-----------|--------------|

## Common Queries
[Frequently used queries for this domain]
```

Save to: `docs/catalog/domains/[domain].md`

**Glossary:**

| Term | Definition | Context |
|------|-----------|---------|

Save to: `docs/catalog/glossary.md`

**Contact Directory:**

| Person | Role | Domain | Contact |
|--------|------|--------|---------|

Save to: `docs/catalog/contacts.md`

### Maintenance
- Update after each analysis session
- Weekly review for accuracy
- Flag stale documentation (>3 months without update)

---

## 2. Export (Offline References)

Generate standalone files usable without Claude.

**Output:** `exports/`

### Export Types

**SQL Cheatsheet** (dialect-specific): Date functions, string functions, window functions, common patterns. Save to `exports/sql-cheatsheet-[dialect].md`

**Domain Quick Reference:** Key tables, common queries, business rules, contacts. Save to `exports/[domain]-reference.md`

**DAX Reference:** Time intelligence, aggregations, rankings, common patterns. Save to `exports/dax-reference.md`

**Procedure Guide:** Prerequisites, steps with code, expected output, troubleshooting. Save to `exports/howto-[procedure].md`

---

## 3. Import (External Documentation)

Import and structure documentation from external sources.

### Supported Sources
- Confluence pages (paste content)
- Notion exports
- Wiki pages
- Slack threads (paste conversation)
- Email content
- Screenshots (describe structure)

### Import Process

1. **Receive content** (user pastes or provides file)
2. **Identify type** automatically (schema docs, business rules, process docs, data dictionary, meeting notes)
3. **Transform** into structured format matching catalog templates
4. **Check conflicts** with existing docs - if conflict: present both versions, let user choose
5. **Integrate** into `docs/catalog/` or appropriate location
6. **Track source** with frontmatter (source, import date, validation status)

### Conflict Resolution
When imported content contradicts existing docs:
- Show both versions side by side
- Highlight differences
- Ask user which is authoritative
- Update and note the change

---

## Language

Adapt to user's language (French or English).
