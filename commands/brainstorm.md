---
name: brainstorm
description: Start brainstorming phase - understand needs, explore data, choose approach
allowed-tools:
  - Read
  - Glob
  - Grep
---

# Brainstorm Command

Phase collaborative pour comprendre les besoins avant toute analyse.

## Process

### 1. Comprendre le Besoin

Poser 2-3 questions:

```markdown
## Brainstorming

1. **Objectif**: Quelle question business cette analyse doit-elle repondre?

2. **Livrable attendu**:
   - [ ] Script Python executable
   - [ ] Formules DAX pour Power BI
   - [ ] Formules Excel
   - [ ] Requetes SQL
   - [ ] Rapport/Insights

3. **Contraintes**: Y a-t-il des contraintes specifiques?
```

### 2. Explorer les Donnees (si fournies)

Quick scan:
- Shape et types
- Colonnes cles
- Problemes evidents

### 3. Proposer des Approches

2-3 options avec tradeoffs selon le livrable cible.

### 4. Confirmer

```markdown
## Resume

**Objectif**: [1 phrase]
**Donnees**: [source]
**Livrable**: [format cible]
**Approche**: [choisie]

On passe a la planification? → `/write-plan`
```

## Langue

S'adapter a la langue de l'utilisateur.
