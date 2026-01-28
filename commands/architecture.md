---
name: architecture
description: "Analyze architecture of ETL pipelines, data repos, or entire projects"
argument-hint: "[directory or repo to analyze]"
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
---

# Architecture Analysis

Analyze the architecture of data projects, ETL pipelines, or repositories.

## Process

1. **Explore** the project structure (files, directories, dependencies)
2. **Map** data flows and dependencies
3. **Identify** patterns, anti-patterns, and improvement opportunities
4. **Report** with diagrams and recommendations

## Analysis Scope

### Project Structure
- Directory organization
- Module dependencies
- Configuration management
- Test coverage

### Data Pipeline Architecture
- Source → Transform → Load flows
- Error handling and retry logic
- Logging and monitoring
- Scheduling and orchestration

### Data Modeling
- Schema design (star schema, snowflake, etc.)
- Normalization level
- Indexing strategy
- Partitioning

### Code Quality
- Invoke code-review for detailed code analysis
- Reusability and modularity
- Documentation completeness

## Output Format

```markdown
## Architecture Analysis: [project/scope]

### Overview
[High-level description]

### Structure Diagram
[ASCII or mermaid diagram]

### Data Flow
[Source → Transform → Target]

### Strengths
- [What's well designed]

### Issues
- [Architecture problems with impact]

### Recommendations
1. [Priority improvement with justification]
```

## Language

Respond in the same language as the user.
