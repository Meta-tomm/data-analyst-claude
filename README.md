# Data Analyst Plugin

Assistant expert Data Analyst avec workflow structure pour Python, SQL, Power BI, Excel.

## Installation

```
/plugin marketplace add Meta-tomm/data-analyst-claude
```

---

## Toutes les Commandes

### Workflow Analyse (brainstorm → plan → execute)

| Commande | Quand l'utiliser |
|----------|------------------|
| `/data-analyst:brainstorm` | **Avant toute analyse.** Comprendre le besoin, explorer les donnees, choisir l'approche. |
| `/data-analyst:write-plan` | **Apres brainstorm.** Creer le plan detaille avec taches bite-sized. |
| `/data-analyst:execute-plan` | **Apres plan valide.** Executer tache par tache avec checkpoints. |

### Onboarding (nouveau dans une entreprise)

| Commande | Quand l'utiliser |
|----------|------------------|
| `/data-analyst:onboard` | **Premier jour.** Workflow structure 2-4 semaines pour prendre ses marques. |
| `/data-analyst:discover` | **Explorer un nouveau systeme.** Mapper schemas, tables, relations. |
| `/data-analyst:document` | **Documenter ses decouvertes.** Data dictionaries, guides domaine, glossaire. |
| `/data-analyst:lineage` | **Comprendre un flux.** Tracer d'ou vient une donnee, ou elle va. |

### Gestion de Session

| Commande | Quand l'utiliser |
|----------|------------------|
| `/data-analyst:config` | **Premiere utilisation.** Configurer environnement (SQL dialect, systemes, contacts). |
| `/data-analyst:resume` | **Debut de session.** Restaurer le contexte de la session precedente. |
| `/data-analyst:import` | **Doc existante.** Importer Confluence/Notion/Slack, Claude structure. |
| `/data-analyst:export` | **Travail offline.** Generer cheatsheets SQL, DAX, domaines. |
| `/data-analyst:describe` | **Donnees sensibles.** Decrire data sans exposer les vraies valeurs. |

### Commandes Directes

| Commande | Quand l'utiliser |
|----------|------------------|
| `/data-analyst:analyze` | Analyse exploratoire (declenche brainstorm si contexte manque) |
| `/data-analyst:clean` | Nettoyage de donnees |
| `/data-analyst:sql` | Generation/optimisation SQL |
| `/data-analyst:viz` | Visualisations |
| `/data-analyst:report` | Generation de rapports |
| `/data-analyst:transform` | Pipelines ETL |
| `/data-analyst:stats` | Tests statistiques |
| `/data-analyst:powerbi` | Formules DAX pour Power BI |
| `/data-analyst:quick` | Reference rapide (sans workflow) |
| `/data-analyst:init` | Initialiser structure projet |

---

## Workflows Recommandes

### Arrivee dans une nouvelle entreprise

```
Jour 1:
/data-analyst:config          ← Configurer SQL dialect, outils
/data-analyst:onboard         ← Demarrer workflow onboarding

Jour 2-10:
/data-analyst:discover        ← Explorer chaque systeme
/data-analyst:import          ← Importer doc existante (Confluence, etc.)

En continu:
/data-analyst:document        ← Documenter au fur et a mesure
/data-analyst:lineage         ← Quand besoin de tracer un flux

Entre sessions:
/data-analyst:resume          ← Reprendre ou on en etait
/data-analyst:export sql      ← Avoir une ref offline
```

### Projet d'analyse standard

```
/data-analyst:brainstorm      ← Comprendre le besoin
      ↓
/data-analyst:write-plan      ← Creer le plan
      ↓
/data-analyst:execute-plan    ← Executer avec checkpoints
```

### Question rapide (pas de workflow)

```
/data-analyst:quick "comment faire un SUMIFS avec plusieurs criteres"
```

---

## Comment les Skills se Chainent

```
                    ┌─────────────────────────────────────┐
                    │         ONBOARDING FLOW             │
                    └─────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ↓               ↓               ↓
               [config]       [discover]      [import]
                    │               │               │
                    └───────────────┼───────────────┘
                                    ↓
                             [document]
                                    │
                    ┌───────────────┼───────────────┐
                    ↓               ↓               ↓
              [lineage]       [export]        [resume]


                    ┌─────────────────────────────────────┐
                    │          ANALYSIS FLOW              │
                    └─────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    ↓               ↓               ↓
             [describe]     [brainstorm]     [config]
                                    │
                                    ↓
                            [write-plan]
                                    │
                                    ↓
                           [execute-plan]
                                    │
                                    ↓
                             [export]
```

---

## Livrables Supportes

### Python
- Scripts `.py` executables dans `./scripts/`

### Power BI (DAX)
- Fichiers `.md` avec formules a copier
- Instructions pour chaque mesure
- Dans `./outputs/dax-formulas.md`

### Excel
- Fichiers `.md` avec formules et placement
- Dans `./outputs/excel-formulas.md`

### SQL
- Fichiers `.sql` commentes
- Support PostgreSQL, MySQL, Snowflake, BigQuery, SQLite
- Dans `./scripts/queries.sql`

### Rapports
- Fichiers `.md` structures
- Adaptes a l'audience (tech/business/executive)
- Dans `./outputs/report.md`

---

## Structure des Fichiers Crees

```
projet/
├── data/                        # Donnees brutes
├── outputs/                     # Resultats, formules
├── scripts/                     # Python, SQL
├── exports/                     # Cheatsheets offline
├── docs/
│   ├── plans/                   # Plans d'analyse
│   ├── discovery/               # Schemas decouverts
│   ├── catalog/                 # Data dictionaries
│   │   ├── tables/
│   │   ├── domains/
│   │   ├── glossary.md
│   │   └── contacts.md
│   ├── lineage/                 # Flux documentes
│   ├── onboarding/              # Progression onboarding
│   └── data-descriptions/       # Descriptions anonymisees
└── .claude/
    ├── data-analyst.local.md    # Config environnement
    └── session-log.md           # Historique sessions
```

---

## Installation Alternative

```bash
git clone https://github.com/Meta-tomm/data-analyst-claude.git ~/.claude/plugins/data-analyst
```

**Mise a jour**: `cd ~/.claude/plugins/data-analyst && git pull`

**Desinstallation**: `/plugin uninstall data-analyst`

---

## MCP Server - Connexion Base de Donnees

Le plugin inclut un serveur MCP pour se connecter directement aux bases de donnees.

### Installation des dependances

```bash
# Dans le dossier du plugin
pip install -r mcp-server/requirements.txt

# Ou via le script
bash mcp-server/install.sh
```

### Configuration

**Option 1: DATABASE_URL (recommande)**

```bash
# PostgreSQL
export DATABASE_URL='postgresql://user:password@localhost:5432/mydb'

# MySQL
export DATABASE_URL='mysql://user:password@localhost:3306/mydb'
```

**Option 2: Variables separees**

```bash
export DB_TYPE=postgresql  # ou mysql
export DB_HOST=localhost
export DB_PORT=5432
export DB_NAME=mydb
export DB_USER=user
export DB_PASSWORD=password
```

### Outils MCP disponibles

| Outil | Description |
|-------|-------------|
| `db_connect` | Tester la connexion a la base |
| `db_tables` | Lister toutes les tables |
| `db_schema` | Schema d'une table (colonnes, types) |
| `db_query` | Executer une requete SELECT (read-only) |
| `db_profile` | Profiler une table (stats, nulls, distinct) |

### Utilisation

Une fois configure, Claude peut directement:
- Explorer vos schemas
- Executer des requetes SELECT
- Profiler vos tables
- Tout ca sans quitter la conversation

```
User: "Montre moi les tables de ma base"
Claude: [utilise db_tables automatiquement]
```

### Securite

- **Read-only**: Seules les requetes SELECT sont autorisees
- **Limite 100 rows**: Les resultats sont limites pour eviter les surcharges
- **Pas de credentials en dur**: Tout passe par variables d'environnement

---

## Bilingue

Le plugin detecte automatiquement la langue (francais/anglais) et s'adapte.
