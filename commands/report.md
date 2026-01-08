---
name: report
description: Generate professional analysis reports
argument-hint: "[--audience tech|business|executive] [--format md|html]"
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
---

# Report Generation Command

Create structured, professional data analysis reports adapted to the target audience.

## Audience Styles

### Technical (tech)
- Include methodology details
- Show statistical tests and p-values
- Full code snippets
- Technical terminology OK
- Detailed assumptions and limitations

### Business (business)
- Focus on actionable insights
- Visualizations over tables
- Plain language explanations
- ROI/business impact emphasis
- Recommendations with priorities

### Executive (executive)
- Executive summary first (1 paragraph)
- Key metrics and KPIs
- High-level findings (3-5 bullets)
- Strategic recommendations
- One page if possible

## Report Structure

### Technical Audience
```markdown
# Analysis Report: [Title]

## Executive Summary
[2-3 sentences]

## Methodology
### Data Sources
### Analysis Approach
### Statistical Methods Used

## Data Overview
[Dataset description, quality notes]

## Analysis Results
### Finding 1
[Detailed analysis with code]
### Finding 2
...

## Statistical Tests
[Test results, p-values, confidence intervals]

## Limitations
[Assumptions, data quality issues, caveats]

## Conclusions

## Appendix
[Full code, additional tables]
```

### Business Audience
```markdown
# [Title]: Key Insights and Recommendations

## Summary
[3-4 sentence overview]

## Key Findings
1. **[Finding 1]**: [Impact] - [Recommendation]
2. **[Finding 2]**: [Impact] - [Recommendation]
3. **[Finding 3]**: [Impact] - [Recommendation]

## Detailed Analysis
### [Topic 1]
[Visual + interpretation + business impact]

### [Topic 2]
[Visual + interpretation + business impact]

## Recommendations
| Priority | Action | Expected Impact | Effort |
|----------|--------|-----------------|--------|
| High | ... | ... | Low |

## Next Steps
[Concrete action items with owners]
```

### Executive Audience
```markdown
# [Title]

## Executive Summary
[Single paragraph with key message]

## Key Metrics
| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| ... | ... | ... | ... |

## Critical Findings
- [Finding 1 with business impact]
- [Finding 2 with business impact]
- [Finding 3 with business impact]

## Strategic Recommendations
1. [High-priority action]
2. [Medium-priority action]

## Required Decisions
[What needs to be decided and by when]
```

## Output Format

```markdown
## Analysis
[Report type and structure being generated]

## Code
[Python script that generates the report with all analyses]

## Report
[The complete report in requested format]

## Interpretation
[Notes on key messages and how to present]

## Next Steps
- Export options
- Presentation suggestions
- Follow-up analyses
```

## Format Options

### Markdown (md) - Default
- Clean, readable
- Version control friendly
- Easy to convert

### HTML
- Include interactive Plotly charts
- Professional styling
- Self-contained file

## Workflow

1. **Understand Context**
   - What analysis was performed?
   - What are the key findings?
   - Who is the audience?

2. **Structure Content**
   - Select appropriate template
   - Organize findings by importance
   - Create visualizations

3. **Generate Report**
   - Write in appropriate tone
   - Include relevant visuals
   - Add actionable recommendations

4. **Export**
   - Save to ./outputs/report_[date].md or .html
   - Offer PDF conversion if needed

## Language

Adapt language and terminology to audience:
- Technical: Use domain-specific terms
- Business: Use business metrics (ROI, conversion, etc.)
- Executive: Use strategic language (growth, competitive advantage, etc.)

Respond in the same language as the user.
