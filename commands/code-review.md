---
name: code-review
description: "Review code for quality, performance, security, and best practices"
argument-hint: "[file or directory to review]"
allowed-tools:
  - Read
  - Glob
  - Grep
---

# Code Review

Review code for quality, performance, security, and adherence to best practices.

## Process

1. **Read** the target code completely
2. **Analyze** against criteria below
3. **Report** findings with severity and suggestions

## Review Criteria

### Quality
- Code readability and clarity
- Naming conventions
- DRY principle adherence
- Function/file size limits
- Error handling completeness

### Performance
- Algorithm complexity (O notation)
- Database query efficiency (N+1, missing indexes)
- Memory usage patterns
- Unnecessary computations

### Security (OWASP Top 10)
- Input validation
- SQL injection risks
- XSS vulnerabilities
- Authentication/authorization issues
- Secrets in code

### Best Practices (language-specific)
- Invoke appropriate lang-* skill for language-specific checks
- Idiomatic patterns
- Anti-patterns detection

## Output Format

```markdown
## Code Review: [file/scope]

### Summary
[1-2 sentence overview]

### Critical Issues
- [Issue with line reference and fix]

### Warnings
- [Issue with suggestion]

### Suggestions
- [Nice-to-have improvements]

### Positive
- [What's done well]
```

## Language

Respond in the same language as the user.
