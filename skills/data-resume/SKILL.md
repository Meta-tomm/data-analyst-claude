---
name: data-resume
description: "Use at the start of a session to restore context from previous work. Loads config, recent progress, open questions, and current focus areas. Enables continuity across sessions."
---

# Data Resume

## Overview

Restore context from previous sessions. Load your environment config, recent discoveries, and ongoing work to continue where you left off.

**Announce at start:** "I'm using the data-resume skill to restore your session context."

## What Gets Loaded

1. **Environment Config** (`.claude/data-analyst.local.md`)
   - SQL dialect, systems, contacts
   - Business jargon and rules

2. **Onboarding Progress** (`docs/onboarding/`)
   - Current phase
   - Completed checklists
   - Latest weekly check-in

3. **Recent Discoveries** (`docs/discovery/`)
   - Schema maps
   - Data profiles
   - Quick wins identified

4. **Open Questions** (`docs/onboarding/questions.md`)
   - Pending questions
   - Who to ask

5. **Session Log** (`.claude/session-log.md`)
   - What was done last session
   - Current focus area

## Session Log Format

**File:** `.claude/session-log.md`

```markdown
# Session Log

## Last Session: YYYY-MM-DD HH:MM

### Focus
[What you were working on]

### Accomplished
- [x] [Task 1]
- [x] [Task 2]
- [ ] [Task 3 - incomplete]

### Discoveries
- [New thing learned]
- [Question answered]

### Blockers
- [Issue encountered]

### Next Session
- [ ] [Continue with...]
- [ ] [Start on...]

---

## Previous Sessions

### YYYY-MM-DD
[Summary]
```

## Resume Workflow

### At Session Start

**Say:** "/data-analyst:resume"

**Claude will:**
1. Read environment config
2. Check session log for last activity
3. Summarize current state
4. Ask what you want to focus on

**Output:**

```markdown
## Session Restored

**Environment:** [Company Name]
**SQL Dialect:** [dialect]
**Last Session:** [date] - [what you did]

### Current State
- **Onboarding Phase:** [phase]
- **Focus Area:** [domain/system]
- **Open Questions:** [count]

### Incomplete from Last Session
- [ ] [Task]
- [ ] [Task]

### Ready to continue. What would you like to focus on?
1. Continue where you left off
2. Start something new
3. Review open questions
4. Update documentation
```

### At Session End

**Say:** "/data-analyst:save" (or Claude prompts automatically)

**Claude will:**
1. Summarize what was done
2. Note any new discoveries
3. List incomplete tasks
4. Suggest next session focus
5. Update session log

## Quick Resume Commands

```markdown
/data-analyst:resume              # Full context restore
/data-analyst:resume brief        # Just environment + last session
/data-analyst:resume questions    # Focus on open questions
/data-analyst:resume [domain]     # Resume work on specific domain
```

## Session Continuity Tips

### Before Ending a Session
- Note what you were doing
- List open questions
- Mark incomplete tasks
- Claude will prompt to save

### Starting a New Session
- Always `/resume` first
- Review context before diving in
- Update if things changed

### Long Gaps Between Sessions
- Review discoveries made
- Check if questions were answered
- Things may have changed - validate

## Context Files Summary

| File | Purpose | Updated |
|------|---------|---------|
| `.claude/data-analyst.local.md` | Environment config | Manually, as you learn |
| `.claude/session-log.md` | Session history | Each session |
| `docs/onboarding/questions.md` | Open questions | As questions arise/resolve |
| `docs/onboarding/week-N-checkin.md` | Weekly progress | Weekly |
| `docs/discovery/*` | Schema maps, profiles | During discovery |

## Handling Context Loss

**If Claude doesn't remember:**
1. `/data-analyst:resume` loads saved context
2. Point to specific files if needed
3. Worst case: brief re-explanation + update docs

**Prevention:**
- Keep session log updated
- Document discoveries immediately
- Save questions when they arise

## Remember

- Resume at session start
- Save at session end (or when switching tasks)
- Documentation IS your memory
- Small updates > big catch-ups

## Language

Adapt to user's language (French or English).
