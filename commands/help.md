---
name: help
description: Display available commands and usage guide
allowed-tools: []
---

# Help Command

Display comprehensive help for the Data Analyst plugin.

## Response

Generate help in the user's language (French or English).

### English Version

```markdown
# Data Analyst Plugin - Help

## Available Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `/analyze` | Exploratory data analysis | `/analyze data.csv` |
| `/clean` | Data cleaning and preprocessing | `/clean data.csv --strategy conservative` |
| `/sql` | SQL query generation and optimization | `/sql "find top customers"` |
| `/viz` | Create visualizations | `/viz data.csv --type bar` |
| `/report` | Generate analysis reports | `/report --audience business` |
| `/transform` | Build transformation pipelines | `/transform "aggregate by month"` |
| `/stats` | Statistical tests | `/stats --test ttest` |
| `/powerbi` | DAX measures and Power BI help | `/powerbi "YoY growth measure"` |
| `/quick` | Quick syntax reference | `/quick "how to pivot"` |
| `/help` | This help message | `/help` |
| `/examples` | Usage examples | `/examples` |
| `/config` | Configuration options | `/config` |

## Quick Start

1. **Analyze a dataset**: `/analyze mydata.csv`
2. **Clean the data**: `/clean mydata.csv`
3. **Create visualization**: `/viz mydata.csv --type auto`
4. **Generate report**: `/report --audience executive`

## Output Format

All commands follow this structure:
- **Analysis**: Summary of approach/findings
- **Code**: Reproducible Python/SQL script
- **Interpretation**: Plain language explanation
- **Next Steps**: Suggested follow-up actions

## File Locations

- Scripts: `./scripts/`
- Outputs: `./outputs/`

## Tips

- Commands adapt to your language (French/English)
- Use `--type auto` in `/viz` for automatic chart selection
- Use `/quick` for fast syntax lookups
- Scripts are displayed first, then you're asked to save
```

### French Version

```markdown
# Plugin Data Analyst - Aide

## Commandes disponibles

| Commande | Description | Usage |
|----------|-------------|-------|
| `/analyze` | Analyse exploratoire | `/analyze data.csv` |
| `/clean` | Nettoyage de donnees | `/clean data.csv --strategy conservative` |
| `/sql` | Generation/optimisation SQL | `/sql "trouver les meilleurs clients"` |
| `/viz` | Creer des visualisations | `/viz data.csv --type bar` |
| `/report` | Generer des rapports | `/report --audience business` |
| `/transform` | Pipelines de transformation | `/transform "agreger par mois"` |
| `/stats` | Tests statistiques | `/stats --test ttest` |
| `/powerbi` | Mesures DAX et aide Power BI | `/powerbi "mesure croissance YoY"` |
| `/quick` | Reference syntaxe rapide | `/quick "comment pivoter"` |
| `/help` | Ce message d'aide | `/help` |
| `/examples` | Exemples d'utilisation | `/examples` |
| `/config` | Options de configuration | `/config` |

## Demarrage rapide

1. **Analyser un dataset**: `/analyze donnees.csv`
2. **Nettoyer les donnees**: `/clean donnees.csv`
3. **Creer une visualisation**: `/viz donnees.csv --type auto`
4. **Generer un rapport**: `/report --audience executive`

## Format de sortie

Toutes les commandes suivent cette structure:
- **Analyse**: Resume de l'approche/resultats
- **Code**: Script Python/SQL reproductible
- **Interpretation**: Explication en langage clair
- **Prochaines etapes**: Actions suggerees

## Emplacements des fichiers

- Scripts: `./scripts/`
- Sorties: `./outputs/`

## Astuces

- Les commandes s'adaptent a votre langue
- Utilisez `--type auto` dans `/viz` pour selection automatique
- Utilisez `/quick` pour des recherches syntaxe rapides
- Les scripts sont affiches d'abord, puis sauvegarde proposee
```

Detect user's language and display appropriate version.
