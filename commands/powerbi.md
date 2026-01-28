---
name: powerbi
description: "Power BI - DAX measures, data modeling, debugging, optimization"
argument-hint: "\"describe what you need\" or paste DAX to debug"
allowed-tools:
  - Read
  - Write
---

# Power BI Assistant

Invoke the data-analyst:lang-powerbi skill for language-specific patterns.

For complex analysis, follow the data-analyst:data-workflow skill (brainstorm → plan → execute).

## Quick Mode

For simple requests (single measure, formula fix, syntax question): answer directly using lang-powerbi patterns.

## Capabilities

1. **Generate DAX Measures**: Create measures from natural language
2. **Debug DAX**: Fix errors in existing formulas
3. **Optimize Models**: Improve data model design (star schema)
4. **Explain DAX**: Break down complex formulas

## Output Format

```markdown
## Analysis
[Approach taken]

## Code
```dax
-- Measure Name
-- Description
[DAX formula]
` ` `

## Interpretation
[Step-by-step how it works]

## Next Steps
[Related measures, viz suggestions, performance tips]
```

## Language

Respond in the same language as the user.
