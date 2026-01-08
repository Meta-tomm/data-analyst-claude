---
name: using-data-analyst
description: This skill should be used at the start of any data analysis conversation to establish the structured workflow. It defines how to use brainstorming, planning, and executing skills for all data analysis tasks.
---

# Using Data Analyst Plugin

This plugin enforces a structured workflow for all data analysis tasks.

## The Rule

**Invoke relevant skills BEFORE any response or action.** Even a 1% chance a skill might apply means invoke it first.

```
User request received
        ↓
Is this a data analysis task?
        ↓ yes
Invoke data-brainstorming FIRST
        ↓
Then data-planning
        ↓
Then data-executing
```

## Workflow Overview

### Phase 1: Brainstorming (REQUIRED)

Before ANY analysis work:
1. Understand what the user really needs
2. Explore the data context
3. Clarify assumptions
4. Propose approaches

**Trigger:** Any analysis request (`/analyze`, `/clean`, `/viz`, `/sql`, `/stats`, `/report`, `/transform`, `/powerbi`)

### Phase 2: Planning (REQUIRED)

After brainstorming is complete:
1. Document the analysis plan
2. List specific steps
3. Identify outputs expected
4. Get user approval

### Phase 3: Executing (REQUIRED)

After plan is approved:
1. Execute step by step
2. Show intermediate results
3. Validate each step
4. Deliver final output

## Red Flags

These thoughts mean STOP - you're skipping the workflow:

| Thought | Reality |
|---------|---------|
| "This is a simple analysis" | Simple analyses still benefit from clarity |
| "I know what they want" | Assumptions cause wasted work |
| "Let me just run this quick" | Quick work without planning = rework |
| "The data is straightforward" | Data always has surprises |

## Skill Priority

1. **data-brainstorming** - Always first for any task
2. **data-planning** - After brainstorming complete
3. **data-executing** - After plan approved

## Integration with Commands

When a user invokes a command like `/analyze`:
1. DO NOT execute immediately
2. First invoke `data-brainstorming`
3. Then invoke `data-planning`
4. Then invoke `data-executing`

## Quick Mode Exception

For `/quick` command only: Skip workflow, provide immediate answer.
This is the only exception - all other commands require the full workflow.
