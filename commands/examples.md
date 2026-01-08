---
name: examples
description: Show usage examples for all commands
allowed-tools: []
---

# Examples Command

Display detailed usage examples for all Data Analyst commands.

## Response

Generate examples in the user's language (French or English).

### English Version

```markdown
# Data Analyst Plugin - Examples

## /analyze - Exploratory Analysis

```bash
# Basic analysis
/analyze sales_data.csv

# Analyze Excel file
/analyze report.xlsx

# Without file (paste data after)
/analyze
```

**Example output**:
- Dataset overview (shape, types, memory)
- Missing values analysis
- Descriptive statistics
- Correlation matrix
- Key findings summary

---

## /clean - Data Cleaning

```bash
# Conservative cleaning (default - preserves data)
/clean customers.csv

# Aggressive cleaning (removes nulls, outliers)
/clean customers.csv --strategy aggressive

# Specify output
/clean raw_data.csv --output cleaned_data.csv
```

**Strategies**:
- `conservative`: Impute missing, flag outliers
- `aggressive`: Remove missing rows, remove outliers

---

## /sql - SQL Generation

```bash
# Natural language to SQL
/sql "find customers who ordered more than 3 times this month"

# Specific dialect
/sql "top 10 products by revenue" --dialect mysql

# Optimize existing query
/sql "optimize: SELECT * FROM orders WHERE YEAR(date) = 2024"

# Explain complex query
/sql "explain: [paste your query here]"
```

**Supported dialects**: mysql, postgres, sqlite

---

## /viz - Visualizations

```bash
# Auto-select best chart type
/viz sales.csv --type auto

# Specific chart types
/viz revenue.csv --type line
/viz categories.csv --type bar
/viz metrics.csv --type scatter
/viz correlation.csv --type heatmap
/viz distribution.csv --type hist
/viz groups.csv --type box

# With specific columns
/viz data.csv --x date --y revenue --color region
```

**Available types**: auto, bar, line, scatter, heatmap, box, hist, pie

---

## /report - Report Generation

```bash
# Technical audience (detailed methodology)
/report --audience tech

# Business audience (actionable insights)
/report --audience business

# Executive summary (1-page highlights)
/report --audience executive

# HTML format with interactive charts
/report --audience business --format html
```

---

## /transform - Data Pipelines

```bash
# Aggregation
/transform "aggregate sales by month and region"

# Multiple transformations
/transform "filter 2024, group by customer, calculate total and average order value"

# Pivot
/transform "pivot table with months as columns and products as rows"

# Join datasets
/transform "join orders with customers on customer_id"
```

---

## /stats - Statistical Tests

```bash
# Compare two groups
/stats --test ttest

# Compare multiple groups
/stats --test anova

# Test correlation
/stats --test correlation

# Check normality
/stats --test normality

# Categorical association
/stats --test chi2
```

**Each test includes**: assumptions check, test results, effect size, plain language interpretation.

---

## /powerbi - DAX & Power BI

```bash
# Create measures
/powerbi "create a YoY growth percentage measure"
/powerbi "running total of sales"
/powerbi "rank products by revenue within category"

# Debug DAX
/powerbi "debug: CALCULATE(SUM(Sales[Amount]), FILTER(...))"

# Model optimization
/powerbi "how to optimize my star schema model"
```

---

## /quick - Quick Reference

```bash
# Pandas syntax
/quick "how to pivot a dataframe"
/quick "rolling average pandas"
/quick "merge two dataframes"

# SQL syntax
/quick "window function rank SQL"
/quick "date difference PostgreSQL"

# DAX syntax
/quick "CALCULATE with multiple filters"
/quick "time intelligence DAX"
```

---

## Workflow Example

A complete analysis workflow:

```bash
# 1. Explore the data
/analyze sales_2024.csv

# 2. Clean issues found
/clean sales_2024.csv --strategy conservative

# 3. Create visualizations
/viz sales_2024_clean.csv --type line

# 4. Run statistical test
/stats --test correlation

# 5. Generate report
/report --audience executive
```
```

### French Version

```markdown
# Plugin Data Analyst - Exemples

## /analyze - Analyse exploratoire

```bash
# Analyse basique
/analyze ventes.csv

# Analyser fichier Excel
/analyze rapport.xlsx

# Sans fichier (coller donnees apres)
/analyze
```

**Sortie type**:
- Vue d'ensemble (dimensions, types, memoire)
- Analyse des valeurs manquantes
- Statistiques descriptives
- Matrice de correlation
- Resume des decouvertes

---

## /clean - Nettoyage de donnees

```bash
# Nettoyage conservateur (defaut - preserve les donnees)
/clean clients.csv

# Nettoyage agressif (supprime nulls, outliers)
/clean clients.csv --strategy aggressive
```

**Strategies**:
- `conservative`: Impute manquants, signale outliers
- `aggressive`: Supprime lignes avec manquants et outliers

---

## /sql - Generation SQL

```bash
# Langage naturel vers SQL
/sql "trouver les clients qui ont commande plus de 3 fois ce mois"

# Dialecte specifique
/sql "top 10 produits par CA" --dialect mysql

# Optimiser requete existante
/sql "optimize: SELECT * FROM orders WHERE YEAR(date) = 2024"
```

---

## /viz - Visualisations

```bash
# Selection automatique du type
/viz ventes.csv --type auto

# Types specifiques
/viz revenue.csv --type line
/viz categories.csv --type bar
/viz metrics.csv --type scatter
/viz correlation.csv --type heatmap
```

---

## /report - Generation de rapports

```bash
# Audience technique
/report --audience tech

# Audience business
/report --audience business

# Resume executif
/report --audience executive
```

---

## /transform - Pipelines de donnees

```bash
# Agregation
/transform "agreger les ventes par mois et region"

# Transformations multiples
/transform "filtrer 2024, grouper par client, calculer total et panier moyen"

# Pivot
/transform "tableau croise avec mois en colonnes et produits en lignes"
```

---

## /stats - Tests statistiques

```bash
/stats --test ttest        # Comparer 2 groupes
/stats --test anova        # Comparer 3+ groupes
/stats --test correlation  # Tester correlation
/stats --test normality    # Verifier normalite
/stats --test chi2         # Association categorielle
```

---

## /powerbi - DAX & Power BI

```bash
/powerbi "creer une mesure de croissance YoY"
/powerbi "total cumule des ventes"
/powerbi "debug: CALCULATE(SUM(Sales[Amount]), ...)"
```

---

## /quick - Reference rapide

```bash
/quick "comment pivoter un dataframe"
/quick "moyenne mobile pandas"
/quick "fusionner deux dataframes"
```

---

## Exemple de workflow complet

```bash
# 1. Explorer les donnees
/analyze ventes_2024.csv

# 2. Nettoyer les problemes trouves
/clean ventes_2024.csv

# 3. Creer visualisations
/viz ventes_2024_clean.csv --type line

# 4. Test statistique
/stats --test correlation

# 5. Generer rapport
/report --audience executive
```
```

Detect user's language and display appropriate version.
