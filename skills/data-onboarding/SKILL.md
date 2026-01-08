---
name: data-onboarding
description: "Use when starting at a new company or project. Complete workflow for understanding data architecture, building knowledge base, and becoming productive. The main skill for taking your marks in a new environment."
---

# Data Onboarding

## Overview

Structured workflow for onboarding into a new data environment. Takes you from zero knowledge to productive contributor.

**Announce at start:** "I'm using the data-onboarding skill to help you get up to speed in this new environment."

**Duration:** Typically 2-4 weeks of progressive discovery

**Output:** Complete personal knowledge base in `docs/`

## The Onboarding Phases

### Phase 1: Orientation (Days 1-3)

**Goal:** Understand the landscape

**Questions to answer:**
1. What data systems exist? (databases, warehouses, BI tools)
2. Who are the key people to know?
3. What documentation already exists?
4. What are the most important business metrics?
5. What projects/dashboards are most used?

**Actions:**

```markdown
## Day 1-3 Checklist

### Access & Setup
- [ ] Get credentials for all data systems
- [ ] Set up local SQL client (DBeaver, DataGrip, etc.)
- [ ] Access BI tools (Tableau, Power BI, Looker)
- [ ] Join relevant Slack channels / Teams

### People
- [ ] Identify data team members and roles
- [ ] Schedule 1:1 with manager
- [ ] Identify go-to person for each domain

### Existing Resources
- [ ] Find existing documentation (wiki, Notion, Confluence)
- [ ] Get list of key dashboards/reports
- [ ] Understand current projects in flight

### First Impressions
- [ ] Note initial questions
- [ ] Identify priority areas to learn
```

**Create:** `docs/onboarding/phase1-orientation.md`

### Phase 2: Discovery (Days 4-10)

**Goal:** Map the data landscape

**Use:** `/discover` skill for systematic exploration

**Priority order:**
1. **Core business data** - customers, orders, revenue
2. **Most-used tables** - ask team what they query most
3. **Dashboard sources** - what powers key reports

**Actions:**

```markdown
## Discovery Checklist

### Per System
- [ ] List all schemas/databases
- [ ] Identify key tables (top 10-20)
- [ ] Understand refresh schedules
- [ ] Note data quality issues

### Cross-System
- [ ] How do systems connect?
- [ ] Where is the source of truth for each entity?
- [ ] What are the main data flows?

### Document
- [ ] Create schema maps
- [ ] Start data dictionary
- [ ] Note open questions
```

**Create:** `docs/discovery/` folder with findings

### Phase 3: Deep Dives (Days 11-20)

**Goal:** Understand priority domains in depth

**Pick 2-3 domains based on:**
- Your role's focus area
- Team's current priorities
- Most complex/critical data

**For each domain:**

```markdown
## Domain Deep Dive: [Name]

### Business Context
- What business process does this represent?
- Who are the stakeholders?
- What decisions does this data support?

### Data Flow
- Where does data originate?
- What transformations happen?
- Where does it end up?

### Key Tables (detailed)
- Column-level understanding
- Business rules encoded
- Known issues

### Metrics
- How are KPIs calculated?
- Where do dashboard numbers come from?
- What are the gotchas?

### Practice Queries
- Replicate a dashboard number
- Answer a business question
- Validate your understanding
```

**Create:** `docs/catalog/domains/[domain].md`

### Phase 4: Integration (Days 21+)

**Goal:** Become a contributor

**Actions:**

```markdown
## Integration Checklist

### First Contributions
- [ ] Fix a small data issue
- [ ] Answer a question from the team
- [ ] Improve existing documentation
- [ ] Create a useful query/view

### Validation
- [ ] Explain a metric to someone
- [ ] Walk through a data flow
- [ ] Identify an improvement opportunity

### Ongoing
- [ ] Continue documenting as you learn
- [ ] Update docs when things change
- [ ] Share knowledge with new joiners
```

## Weekly Check-In Template

```markdown
# Week [N] Onboarding Check-In

## What I Learned
- [Key insight 1]
- [Key insight 2]

## Systems Explored
- [System]: [What I understood]

## Open Questions
- [ ] [Question 1] - Ask [Person]
- [ ] [Question 2] - Need to investigate

## Next Week Focus
- [ ] [Priority 1]
- [ ] [Priority 2]

## Blockers
- [Any access issues, unclear areas]
```

Save to: `docs/onboarding/week-[n]-checkin.md`

## Onboarding Folder Structure

```
docs/
  onboarding/
    README.md                    # Onboarding overview
    phase1-orientation.md        # Initial setup
    phase2-discovery.md          # System mapping
    week-1-checkin.md
    week-2-checkin.md
    questions.md                 # Running list of questions
  discovery/
    00-inventory.md
    [system]-schema.md
  catalog/
    glossary.md
    contacts.md
    tables/
    domains/
```

## Tips for Success

### First Week
- Take lots of notes
- Don't try to understand everything
- Focus on access and people
- Ask "dumb" questions now

### First Month
- Document as you learn (not after)
- Validate understanding by explaining to others
- Start with breadth, then depth
- Build relationships with data owners

### Ongoing
- Keep documentation updated
- Share what you learn
- Become the expert in 1-2 areas
- Help onboard the next person

## Integration

**Called by:**
- `/data-analyst:onboard` command

**Uses (REQUIRED SUB-SKILLS):**
- **data-config** - First, set up environment config
- **data-discovery** - Phase 2: systematic data exploration
- **data-documentation** - Throughout: create documentation
- **data-lineage** - Phase 3: understand data flows

**Chains to:**
- **data-brainstorm** - Once onboarded, ready to do analysis work

**Pairs with:**
- **data-resume** - Continue onboarding between sessions
- **data-import** - Import existing company docs
- **data-export** - Export cheatsheets for offline reference

## Remember

- It's normal to feel lost at first
- Everyone was new once
- Documentation is your friend (create what you wish existed)
- Ask questions early and often

## Language

Adapt to user's language (French or English).
