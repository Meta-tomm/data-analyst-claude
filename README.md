# Data Analyst Plugin

Assistant expert Data Analyst avec workflow structure: **brainstorm → plan → execute**.

## Workflow

Chaque analyse suit un processus en 3 phases:

```
1. BRAINSTORMING
   - Comprendre le besoin
   - Explorer les donnees
   - Choisir l'approche

2. PLANNING
   - Definir les taches
   - Specifier les livrables
   - Obtenir approbation

3. EXECUTING
   - Executer tache par tache
   - Valider chaque etape
   - Generer les livrables
```

## Installation

### Via Marketplace (recommande)

Dans Claude Code, executez:

```
/plugin marketplace add Meta-tomm/data-analyst-claude
/plugin install data-analyst
```

C'est tout. Les commandes `/analyze`, `/init`, etc. sont disponibles.

### Via Git (alternative)

```bash
git clone https://github.com/Meta-tomm/data-analyst-claude.git ~/.claude/plugins/data-analyst
```

### Mise a jour

```
/plugin update data-analyst
```

Ou manuellement:
```bash
cd ~/.claude/plugins/data-analyst && git pull
```

### Desinstallation

```
/plugin uninstall data-analyst
```

## Commandes

| Commande | Description |
|----------|-------------|
| `/init` | **Nouveau** - Initialiser un projet d'analyse |
| `/analyze` | Analyse exploratoire |
| `/clean` | Nettoyage de donnees |
| `/sql` | Generation/optimisation SQL |
| `/viz` | Visualisations |
| `/report` | Generation de rapports |
| `/transform` | Pipelines ETL |
| `/stats` | Tests statistiques |
| `/powerbi` | Formules DAX |
| `/quick` | Reference rapide (sans workflow) |
| `/help` | Aide |
| `/examples` | Exemples d'utilisation |
| `/config` | Configuration |

## Livrables Supportes

Le plugin s'adapte au type de livrable:

### Python
- Scripts `.py` executables
- Sauvegarde dans `./scripts/`

### Power BI (DAX)
- Fichiers `.md` avec formules a copier
- Instructions detaillees pour chaque mesure
- Sauvegarde dans `./outputs/dax-formulas.md`

### Excel
- Fichiers `.md` avec formules a copier
- References cellules et instructions
- Sauvegarde dans `./outputs/excel-formulas.md`

### SQL
- Fichiers `.sql` avec requetes commentees
- Support MySQL, PostgreSQL, SQLite
- Sauvegarde dans `./scripts/queries.sql`

### Rapports
- Fichiers `.md` structures
- Adaptes a l'audience (tech/business/executive)
- Sauvegarde dans `./outputs/report.md`

## Structure Projet (apres /init)

```
mon-analyse/
├── data/           # Donnees brutes
├── outputs/        # Resultats (CSV, charts, formules)
├── scripts/        # Scripts Python/SQL
└── docs/
    ├── project-config.md   # Configuration projet
    └── plans/              # Plans d'analyse
```

## Exemple d'Utilisation

```bash
# 1. Initialiser le projet
/init ./analyse-ventes-q4

# 2. Analyser les donnees (workflow complet)
/analyze

# 3. Creer des mesures Power BI
/powerbi "mesures pour dashboard ventes"

# 4. Reference rapide (pas de workflow)
/quick "comment faire un SUMIFS"
```

## Skills Internes

| Skill | Description |
|-------|-------------|
| `data-brainstorming` | Phase de decouverte |
| `data-planning` | Creation du plan |
| `data-executing` | Execution du plan |
| `data-analyst-core` | Connaissances partagees |
| `using-data-analyst` | Regles d'utilisation |

## Bilingue

Le plugin detecte automatiquement la langue (francais/anglais) et s'adapte.

## Differences avec Superpowers

Ce plugin est inspire de superpowers mais adapte au metier de Data Analyst:
- Focus sur les donnees, pas le code
- Livrables adaptes (DAX, Excel, pas que Python)
- Workflow collaboratif avec le data analyst
- Commande `/init` pour setup projet
- `/quick` pour reponses immediates sans workflow
