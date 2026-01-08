---
name: write-plan
description: Create detailed analysis plan after brainstorming
allowed-tools:
  - Read
  - Write
  - Glob
---

# Write Plan Command

Creer un plan d'analyse detaille apres le brainstorming.

## Process

### 1. Verifier le Contexte

Si pas de brainstorming fait, suggerer `/brainstorm` d'abord.

### 2. Creer le Plan

Adapter au livrable cible:

#### Pour Python
```markdown
# [Nom] - Plan

**Livrable**: Script Python
**Fichier**: `./scripts/[nom].py`

## Taches

### Tache 1: Chargement
**Input**: fichier
**Output**: DataFrame
**Validation**: shape attendu

### Tache 2: Nettoyage
**Actions**: [liste]
**Validation**: 0 nulls
```

#### Pour Power BI (DAX)
```markdown
# [Nom] - Plan DAX

**Livrable**: Formules DAX (.md)
**Fichier**: `./outputs/dax-formulas.md`

## Mesures a creer

### Mesure 1: [Nom]
**Objectif**: [description]
**Depend de**: [autres mesures]
```

#### Pour Excel
```markdown
# [Nom] - Plan Excel

**Livrable**: Formules Excel (.md)
**Fichier**: `./outputs/excel-formulas.md`

## Formules a creer

### Formule 1: [Nom]
**Cellule**: [ref]
**Type**: SUMIFS/VLOOKUP/etc.
```

#### Pour SQL
```markdown
# [Nom] - Plan SQL

**Livrable**: Requetes SQL
**Fichier**: `./scripts/queries.sql`
**Dialecte**: [PostgreSQL/MySQL/SQLite]

## Requetes a creer

### Query 1: [Nom]
**Tables**: [liste]
**Type**: SELECT/JOIN/CTE
```

### 3. Demander Approbation

```markdown
**Approuve?** (oui/non)

Si oui → `/execute-plan`
```

## Sauvegarder le Plan

Optionnel: `./docs/plans/YYYY-MM-DD-[nom].md`

## Langue

S'adapter a la langue de l'utilisateur.
