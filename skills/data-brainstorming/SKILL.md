---
name: data-brainstorming
description: This skill MUST be used before any data analysis work. It collaborates with the data analyst to understand needs, explore data context, and define the analysis approach. Adapts to target outputs (Python, Power BI, Excel, SQL).
---

# Data Brainstorming

Phase collaborative pour comprendre les besoins avant toute analyse.

## Principe

Le data analyst sait ce qu'il veut obtenir. Claude aide a structurer et optimiser l'approche.

## Le Process

### Phase 1: Comprendre le Besoin (2-3 questions)

```markdown
## Brainstorming: [Sujet]

Quelques questions pour bien cadrer:

1. **Objectif**: Quelle question business cette analyse doit-elle repondre?

2. **Livrable attendu**:
   - [ ] Script Python executable
   - [ ] Formules DAX pour Power BI
   - [ ] Formules Excel
   - [ ] Requetes SQL
   - [ ] Rapport/Insights
   - [ ] Donnees nettoyees

3. **Contraintes**: Y a-t-il des contraintes specifiques? (perf, format, outils disponibles)
```

### Phase 2: Explorer les Donnees (si fournies)

Quick scan des donnees:
- Shape et types
- Colonnes cles identifiees
- Problemes evidents (nulls, formats)
- Patterns interessants

**Format compact:**
```markdown
### Apercu des donnees

| Metrique | Valeur |
|----------|--------|
| Lignes | 10,000 |
| Colonnes | 15 |
| Nulls | 3 colonnes concernees |
| Types | 8 num, 5 cat, 2 dates |

**Observations**:
- Colonne `revenue` a 5% de nulls
- `date` format mixte (YYYY-MM-DD et DD/MM/YYYY)
- `customer_id` semble etre la cle primaire
```

### Phase 3: Proposer des Approches

Adapter au livrable cible:

**Si Python:**
```markdown
### Approches possibles

**A) Analyse pandas classique** (Recommande)
- Script unique, reproductible
- Export CSV + visualisations PNG
- Temps: rapide

**B) Pipeline modulaire**
- Fonctions reutilisables
- Plus maintenable
- Temps: plus long

Preference?
```

**Si Power BI:**
```markdown
### Approches possibles

**A) Mesures DAX simples**
- Formules individuelles a copier
- Facile a maintenir
- Format: fichier .md avec formules

**B) Table calculee + Mesures**
- Pre-calcul dans une table
- Plus performant pour gros volumes
- Necessite import de la table

Preference?
```

**Si Excel:**
```markdown
### Approches possibles

**A) Formules dans les cellules**
- SUMIFS, VLOOKUP, etc.
- Pas de VBA requis
- Format: instructions + formules

**B) Tableau croise dynamique**
- Plus flexible
- Refresh automatique
- Format: guide etape par etape

Preference?
```

### Phase 4: Confirmer

```markdown
## Resume

**Objectif**: [1 phrase]
**Donnees**: [source]
**Livrable**: [format cible]
**Approche**: [choisie]

On passe a la planification?
```

## Adaptation au Contexte

### Si /init a ete fait
- Lire `./docs/project-config.md`
- Utiliser le contexte deja etabli
- Poser moins de questions

### Si pas de /init
- Poser les questions de contexte
- Suggerer `/init` pour les projets longs

## Ce que Brainstorming N'est PAS

- Pas d'ecriture de code
- Pas d'execution d'analyse
- Pas de generation de formules
- Juste: comprendre, explorer, proposer

## Apres Brainstorming

**REQUIS**: Passer au skill `data-analyst:data-planning`

## Langue

S'adapter a la langue de l'utilisateur.
