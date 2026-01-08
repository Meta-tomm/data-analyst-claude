---
name: execute-plan
description: Execute the approved analysis plan task by task
allowed-tools:
  - Read
  - Write
  - Bash
  - Glob
  - Grep
---

# Execute Plan Command

Executer le plan approuve tache par tache.

## Process

### 1. Verifier le Plan

Si pas de plan, suggerer `/write-plan` d'abord.

### 2. Charger dans TodoWrite

Convertir chaque tache du plan en todo.

### 3. Executer Tache par Tache

Pour chaque tache:
1. Marquer `in_progress`
2. Executer selon le livrable cible
3. Valider le resultat
4. Marquer `completed`

### 4. Format de Sortie par Livrable

#### Python
```python
#!/usr/bin/env python3
"""[Nom analyse] - Generated: YYYY-MM-DD"""

import pandas as pd
# ... code complet
```
→ Sauvegarder dans `./scripts/`

#### Power BI (DAX)
```markdown
# Formules DAX - [Nom]

## Mesure 1: [Nom]

### Formule
\`\`\`dax
[formule complete]
\`\`\`

### Instructions
1. Dans Power BI: Modeling > New Measure
2. Coller la formule
3. Format: [type]
```
→ Sauvegarder dans `./outputs/dax-formulas.md`

#### Excel
```markdown
# Formules Excel - [Nom]

## Formule 1: [Nom]

### Formule
\`\`\`excel
=SUMIFS(...)
\`\`\`

### Emplacement
- Onglet: [nom]
- Cellule: [ref]
- Tirer vers: [direction]
```
→ Sauvegarder dans `./outputs/excel-formulas.md`

#### SQL
```sql
-- [Nom] - Generated: YYYY-MM-DD
-- Dialect: [PostgreSQL/MySQL/SQLite]

-- Query 1: [description]
SELECT ...
```
→ Sauvegarder dans `./scripts/queries.sql`

### 5. Checkpoint Final

```markdown
## Execution Terminee

| Fichier | Type | Statut |
|---------|------|--------|
| [path] | [type] | Pret |

### Prochaines etapes
- [suggestions]
```

## Gestion des Erreurs

Si une tache echoue:
1. Stop
2. Expliquer le probleme
3. Proposer des solutions
4. Attendre decision

## Langue

S'adapter a la langue de l'utilisateur.
