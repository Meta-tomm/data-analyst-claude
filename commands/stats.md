---
name: stats
description: Perform statistical tests with clear interpretations
argument-hint: "[--test ttest|anova|correlation|normality|chi2]"
allowed-tools:
  - Read
  - Write
  - Bash
---

# Statistical Tests Command

Perform statistical tests and provide clear, actionable interpretations.

## Available Tests

### Comparison Tests
- **t-test (independent)**: Compare means of 2 independent groups
- **t-test (paired)**: Compare means of same group at 2 times
- **ANOVA**: Compare means of 3+ groups
- **Mann-Whitney U**: Non-parametric alternative to t-test

### Association Tests
- **Pearson correlation**: Linear relationship (continuous vars)
- **Spearman correlation**: Monotonic relationship (ordinal/non-normal)
- **Chi-square**: Association between categorical variables

### Distribution Tests
- **Shapiro-Wilk**: Test normality (n < 5000)
- **Kolmogorov-Smirnov**: Test normality (large n)
- **Levene**: Test homogeneity of variances

## Workflow

1. **Understand the Question**
   - What is being compared/tested?
   - What type of data?
   - What assumptions to check?

2. **Check Assumptions**
   - Normality (for parametric tests)
   - Equal variances (for t-test/ANOVA)
   - Sample size requirements

3. **Perform Test**
   - Calculate test statistic
   - Compute p-value
   - Calculate effect size

4. **Interpret Results**
   - Plain language explanation
   - Practical significance
   - Limitations

## Output Format

```markdown
## Analysis
[What test and why it's appropriate]

## Assumptions Check
| Assumption | Test | Result | Met? |
|------------|------|--------|------|
| Normality | Shapiro-Wilk | p=0.23 | Yes |
| Equal variance | Levene | p=0.45 | Yes |

## Code
```python
from scipy import stats
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('data.csv')

# Check normality
shapiro_stat, shapiro_p = stats.shapiro(df['group_a'])
print(f"Shapiro-Wilk: W={shapiro_stat:.4f}, p={shapiro_p:.4f}")

# Perform t-test
t_stat, p_value = stats.ttest_ind(df['group_a'], df['group_b'])

# Effect size (Cohen's d)
def cohens_d(g1, g2):
    n1, n2 = len(g1), len(g2)
    var1, var2 = g1.var(), g2.var()
    pooled_std = np.sqrt(((n1-1)*var1 + (n2-1)*var2) / (n1+n2-2))
    return (g1.mean() - g2.mean()) / pooled_std

d = cohens_d(df['group_a'], df['group_b'])

print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Cohen's d: {d:.4f}")
```

## Results
| Metric | Value |
|--------|-------|
| t-statistic | 2.45 |
| p-value | 0.018 |
| Cohen's d | 0.52 |

## Interpretation
**Statistical Result**: The difference between groups is statistically significant (p < 0.05).

**Practical Meaning**: [Plain language explanation of what this means in context]

**Effect Size**: Medium effect (d = 0.52), meaning [practical interpretation].

**Confidence**: [Level of confidence in results, caveats]

## Next Steps
- Follow-up analyses
- Additional tests to consider
- Recommendations
```

## Test Selection Guide

| Question | Test | Requirements |
|----------|------|--------------|
| Are 2 group means different? | Independent t-test | Normal, equal var |
| Are 2 paired means different? | Paired t-test | Normal differences |
| Are 3+ group means different? | One-way ANOVA | Normal, equal var |
| Are 2 group medians different? | Mann-Whitney U | Ordinal+ |
| Is there linear correlation? | Pearson r | Both continuous |
| Is there monotonic correlation? | Spearman rho | Ordinal+ |
| Are categories associated? | Chi-square | Categorical |
| Is data normally distributed? | Shapiro-Wilk | n < 5000 |

## Effect Size Interpretation

### Cohen's d (t-test)
- Small: d = 0.2
- Medium: d = 0.5
- Large: d = 0.8

### Correlation (r)
- Small: r = 0.1
- Medium: r = 0.3
- Large: r = 0.5

### Eta-squared (ANOVA)
- Small: eta2 = 0.01
- Medium: eta2 = 0.06
- Large: eta2 = 0.14

## P-value Guidelines

- p < 0.001: Very strong evidence against H0
- p < 0.01: Strong evidence
- p < 0.05: Moderate evidence (conventional threshold)
- p >= 0.05: Insufficient evidence to reject H0

Always report:
1. The actual p-value (not just "p < 0.05")
2. Effect size
3. Confidence intervals when available
4. Sample sizes

## Language

Respond in the same language as the user. Adapt statistical explanations to audience (technical vs non-technical).
