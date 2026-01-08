---
name: data-brainstorming
description: "You MUST use this before any data analysis work - /analyze, /clean, /viz, /sql, /stats, /report, /transform, /powerbi. Explores user intent, data context, and analysis requirements before implementation."
---

# Brainstorming Data Analysis Into Designs

## Overview

Help turn data analysis ideas into fully formed designs through natural collaborative dialogue.

Start by understanding the current data context, then ask questions one at a time to refine the approach. Once you understand what's needed, present the design in small sections (200-300 words), checking after each section whether it looks right.

**Announce at start:** "I'm using the data-brainstorming skill to understand your analysis needs."

## The Process

**Understanding the need:**
- Check for existing project config (`.claude/data-analyst.local.md`)
- Ask questions one at a time to refine the idea
- Prefer multiple choice questions when possible
- Only one question per message
- Focus on: objective, deliverable type, constraints

**Key questions (one at a time):**
1. "What business question should this analysis answer?"
2. "What format do you need?" (Python script / DAX formulas / Excel formulas / SQL queries / Report)
3. "What data sources are involved?"
4. "Any specific constraints?" (performance, tools available, audience)

**Exploring approaches:**
- Propose 2-3 different approaches with trade-offs
- Lead with your recommendation and explain why
- Present options conversationally

**Presenting the design:**
- Once you understand what's needed, present the design
- Break it into sections of 200-300 words
- Ask after each section whether it looks right
- Cover: data flow, transformations, outputs, validation
- Be ready to go back and clarify

## Approach Templates by Output Type

**Python:**
```markdown
### Approaches

**A) Single script analysis** (Recommended)
- One executable .py file
- Outputs to ./outputs/
- Fast to implement

**B) Modular pipeline
- Separate functions/modules
- More reusable
- Takes longer

Which approach?
```

**Power BI / DAX:**
```markdown
### Approaches

**A) Individual measures** (Recommended)
- Each measure in .md file for copy-paste
- Easy to maintain
- Clear dependencies documented

**B) Calculated table + measures**
- Pre-compute in DAX table
- Better performance for large data
- More complex setup

Which approach?
```

**Excel:**
```markdown
### Approaches

**A) Cell formulas** (Recommended)
- SUMIFS, VLOOKUP, etc.
- No VBA needed
- Step-by-step instructions

**B) Pivot tables**
- More flexible
- Auto-refresh
- Setup guide provided

Which approach?
```

**SQL:**
```markdown
### Approaches

**A) Single query file** (Recommended)
- All queries in one .sql
- Well-commented sections
- Portable

**B) Multiple query files**
- Organized by purpose
- Better for large projects
- More files to manage

Which approach?
```

## After the Design

**Documentation:**
- Write the validated design to `docs/plans/YYYY-MM-DD-<topic>-design.md`
- Include: objective, data sources, approach, deliverable format

**Implementation:**
- Ask: "Ready to create the implementation plan?"
- **REQUIRED SUB-SKILL:** Use data-analyst:data-planning to create detailed plan

## Key Principles

- **One question at a time** - Don't overwhelm
- **Multiple choice preferred** - Easier to answer
- **YAGNI ruthlessly** - Only what's needed
- **Explore alternatives** - Always 2-3 approaches
- **Incremental validation** - Present in sections
- **Adapt to output type** - Different formats need different approaches

## Integration

**Called by:**
- `/data-analyst:brainstorm` command
- Any analysis command when context unclear

**Chains to:**
- **data-planning** - After design validated, create implementation plan
- **data-config** - If no project config exists, suggest setup

**Pairs with:**
- **data-describe** - If user needs to safely share data context

## Language

Adapt to user's language (French or English).
