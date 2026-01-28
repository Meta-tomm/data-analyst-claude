# Data Analyst Plugin v2.0

Assistant expert Data Analyst pour Python, SQL, Power BI, Excel et plus.

## Installation

```
/plugin marketplace add Meta-tomm/data-analyst-claude
```

Alternative:
```bash
git clone https://github.com/Meta-tomm/data-analyst-claude.git ~/.claude/plugins/data-analyst
```

---

## Commandes

### Workflow Analyse (brainstorm -> plan -> execute)

| Commande | Usage |
|----------|-------|
| `/data-analyst:brainstorm` | Comprendre le besoin, explorer les donnees, choisir l'approche |
| `/data-analyst:write-plan` | Creer le plan detaille avec taches et validations |
| `/data-analyst:execute-plan` | Executer tache par tache avec checkpoints |

### Langages & Outils

| Commande | Usage |
|----------|-------|
| `/data-analyst:python` | Scripts Python, pandas, numpy, visualisation |
| `/data-analyst:sql` | Generation/optimisation SQL multi-dialect |
| `/data-analyst:powerbi` | Formules DAX, modelisation Power BI |
| `/data-analyst:excel` | Formules Excel, Power Query, VBA |

### Qualite & Architecture

| Commande | Usage |
|----------|-------|
| `/data-analyst:code-review` | Review code : qualite, performance, securite |
| `/data-analyst:architecture` | Analyser pipelines ETL, architecture data |

---

## Skills

Le plugin inclut 11 skills activees automatiquement selon le contexte.

### Workflow

| Skill | Role |
|-------|------|
| `data-workflow` | Workflow 3 phases : brainstorm, plan, execute |
| `data-environment` | Onboarding, decouverte schemas, config, lineage |
| `data-docs` | Documentation, export offline, import docs externes |

### Langages

| Skill | Couverture |
|-------|------------|
| `lang-python` | pandas, numpy, scipy, matplotlib, seaborn, polars |
| `lang-sql` | PostgreSQL, MySQL, SQLite, T-SQL, Snowflake |
| `lang-powerbi` | DAX, star schema, time intelligence |
| `lang-excel` | Formules, Power Query M, VBA, pivot tables |
| `lang-typescript` | Types stricts, generics, Zod, async |
| `lang-javascript` | ES2024+, patterns fonctionnels |
| `lang-node` | Express/Fastify, streams, workers |
| `lang-react` | Hooks, state management, Server Components |

---

## Workflow Recommande

```
/data-analyst:brainstorm      <- Comprendre le besoin
      |
/data-analyst:write-plan      <- Planifier
      |
/data-analyst:execute-plan    <- Executer avec validation
```

Pour une question rapide, utiliser directement la commande appropriee :

```
/data-analyst:sql "optimise cette requete avec des CTEs"
/data-analyst:python "analyse exploratoire de ce CSV"
/data-analyst:powerbi "mesure YTD avec filtre region"
```

---

## Configuration (optionnel)

Creer `.claude/data-analyst.local.md` dans le projet pour persister la config :

```yaml
---
environment:
  name: "Mon projet"
  sql_dialect: "postgresql"
---
```

Le plugin charge automatiquement ce fichier au demarrage de session.

---

## Livrables Supportes

| Type | Format | Destination |
|------|--------|-------------|
| Python | `.py` | `./scripts/` |
| SQL | `.sql` | `./scripts/` |
| DAX | `.md` | `./outputs/` |
| Excel | `.md` | `./outputs/` |
| Rapports | `.md` | `./outputs/` |

---

## Bilingue

Le plugin detecte automatiquement la langue (francais/anglais) et s'adapte.

---

## Licence

MIT
