---
name: data-workflow
description: "Use when starting any data analysis work. Enforces 3-phase workflow: brainstorm, plan, execute. Detects current phase and applies corresponding rules."
---

# Data Analysis Workflow

Enforced 3-phase workflow for all data analysis tasks. Detects the current phase and applies corresponding rules.

## Phase Detection

Check session state to determine current phase:
- No design doc exists → Phase 1: Brainstorm
- Design doc exists, no plan → Phase 2: Plan
- Plan exists and approved → Phase 3: Execute

## Workflow Enforcement

**MANDATORY for:** /python, /sql, /powerbi, /excel, /code-review, /architecture
**Exception:** Direct quick questions get immediate answers.

Red flags for skipping:
- "Just write the code" → Still brainstorm first
- "I know what I want" → Validate with 1-2 questions
- "Skip planning" → At minimum, outline steps

---

## Phase 1: Brainstorm

Help turn data analysis ideas into fully formed designs through collaborative dialogue.

**Announce:** "Using data-workflow (brainstorm phase) to understand your analysis needs."

### Process

1. **Understand the need:**
   - Check for existing project config (`.claude/data-analyst.local.md`)
   - Ask questions one at a time (multiple choice preferred)
   - Focus on: objective, deliverable type, constraints

2. **Key questions (one at a time):**
   - "What business question should this analysis answer?"
   - "What format do you need?" (Python script / DAX formulas / Excel formulas / SQL queries / Report)
   - "What data sources are involved?"
   - "Any specific constraints?" (performance, tools, audience)

3. **Explore approaches:**
   - Propose 2-3 approaches with trade-offs
   - Lead with recommendation and explain why
   - Present conversationally

4. **Present design:**
   - Break into 200-300 word sections
   - Ask after each section if it looks right
   - Cover: data flow, transformations, outputs, validation

### Approach Templates

**Python:**
- A) Single script analysis (Recommended) - One .py file, outputs to ./outputs/
- B) Modular pipeline - Separate functions/modules, more reusable

**Power BI / DAX:**
- A) Individual measures (Recommended) - Each in .md for copy-paste
- B) Calculated table + measures - Better perf for large data

**Excel:**
- A) Cell formulas (Recommended) - SUMIFS, VLOOKUP, no VBA
- B) Pivot tables - More flexible, auto-refresh

**SQL:**
- A) Single query file (Recommended) - All queries in one .sql
- B) Multiple query files - Organized by purpose

### After Design
- Save to `docs/plans/YYYY-MM-DD-<topic>-design.md`
- Ask: "Ready to create the implementation plan?"
- Transition to Phase 2

---

## Phase 2: Plan

Create detailed, bite-sized implementation plans. Each step = one action.

**Announce:** "Using data-workflow (planning phase) to create your implementation plan."

### Prerequisites
- Brainstorm phase completed (design doc exists)
- If no design: "No design found. Run brainstorm phase first."

### Plan Structure

Each task must include:
1. **Action**: What to do (one specific thing)
2. **Input**: What data/files needed
3. **Output**: What gets produced
4. **Validation**: How to verify it worked

### Task Templates by Output Type

**Python script:**
```
Task: [Description]
Action: Write Python function to [specific thing]
Input: [data file or previous output]
Output: [script file or data output]
Validation: Run script, check [specific metric/output]
```

**DAX formula:**
```
Task: [Description]
Action: Write DAX measure for [specific calculation]
Input: [table/column references]
Output: [measure name in .md file]
Validation: Expected result for test case: [value]
```

**Excel formula:**
```
Task: [Description]
Action: Create formula in [cell range]
Input: [source data range]
Output: [formula text + expected result]
Validation: Cross-check with [known value]
```

**SQL query:**
```
Task: [Description]
Action: Write query to [specific extraction/transformation]
Input: [tables involved]
Output: [.sql file with expected columns]
Validation: Run with LIMIT 10, verify columns and sample values
```

### Plan Output
- Save to `docs/plans/YYYY-MM-DD-<topic>-plan.md`
- Present plan summary for approval
- Ask: "Approve this plan to start execution?"
- On approval, transition to Phase 3

---

## Phase 3: Execute

Implement approved plan task by task with validation checkpoints.

**Announce:** "Using data-workflow (execution phase) to implement your plan."

### Prerequisites
- Plan exists and is approved
- If no plan: "No approved plan found. Run planning phase first."

### Execution Rules

1. **Batch execution:** Default 3 tasks per batch
2. **After each batch:** Show results, ask to continue
3. **Validation required:** Run validation for each task before marking done
4. **Stop conditions:**
   - Validation fails → report and ask
   - Unexpected data → report and ask
   - Ambiguity → ask before proceeding

### Output by Type

**Python:** Execute script, show output, save to ./scripts/ and ./outputs/
**DAX/Excel:** Write formulas in .md file for copy-paste
**SQL:** Write to .sql file, show sample results if possible
**Report:** Generate .md with analysis, code, interpretation, next steps

### Completion
- Summary of all outputs produced
- List of files created/modified
- Suggested follow-up analyses

---

## Key Principles

- **One question at a time** during brainstorm
- **YAGNI ruthlessly** - Only what is needed
- **Incremental validation** - Verify each step
- **Adapt to output type** - Different formats need different approaches
- **Language:** Respond in user language (French or English)

## Integration

**Commands that use this skill:**
- /brainstorm → Phase 1
- /write-plan → Phase 2
- /execute-plan → Phase 3
- /python, /sql, /powerbi, /excel → Full workflow if context unclear

**Pairs with:**
- **data-environment** - Config and context
- **lang-* skills** - Language-specific patterns
