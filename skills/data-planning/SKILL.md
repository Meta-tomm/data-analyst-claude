---
name: data-planning
description: This skill MUST be used after data-brainstorming to create a detailed analysis plan. Adapts plan structure to target output (Python scripts, DAX formulas, Excel formulas, SQL queries, reports).
---

# Data Planning

Creer un plan d'analyse adapte au livrable cible.

## Principe

Le plan definit QUOI faire, pas COMMENT le coder. Le format du plan depend du livrable.

## Plans par Type de Livrable

### Plan pour Python

```markdown
# [Nom Analyse] - Plan

**Livrable**: Script Python
**Fichier sortie**: `./scripts/[nom].py`

---

## Taches

### Tache 1: Chargement des donnees
**Input**: `./data/fichier.csv`
**Output**: DataFrame charge
**Validation**: Shape = (X, Y), pas d'erreur de parsing

### Tache 2: Nettoyage
**Actions**:
- Traiter nulls colonne `revenue` (imputation mediane)
- Convertir `date` en datetime
**Output**: DataFrame propre
**Validation**: 0 nulls, types corrects

### Tache 3: Analyse
**Actions**:
- Calculer stats descriptives
- Correlation matrix
**Output**: Resultats dans DataFrame
**Validation**: Valeurs plausibles

### Tache 4: Export
**Output**:
- `./outputs/results.csv`
- `./outputs/correlation.png`

---

**Approuve?** (oui/non)
```

### Plan pour Power BI (DAX)

```markdown
# [Nom Analyse] - Plan DAX

**Livrable**: Formules DAX (.md a copier)
**Fichier sortie**: `./outputs/dax-formulas.md`

---

## Mesures a creer

### Mesure 1: Total Ventes
**Objectif**: Somme des ventes
**Table source**: Sales
**Colonne**: Amount
**Format affichage**: Currency

### Mesure 2: YoY Growth
**Objectif**: Croissance annuelle
**Depend de**: Mesure 1, Table Date
**Format affichage**: Percentage

### Mesure 3: Top 10 Flag
**Objectif**: Identifier top 10 produits
**Depend de**: Mesure 1
**Type**: Colonne calculee ou mesure

---

## Ordre d'implementation
1. Mesure 1 (base)
2. Mesure 2 (depend de 1)
3. Mesure 3 (depend de 1)

---

**Approuve?** (oui/non)
```

### Plan pour Excel

```markdown
# [Nom Analyse] - Plan Excel

**Livrable**: Formules Excel (.md avec instructions)
**Fichier sortie**: `./outputs/excel-formulas.md`

---

## Structure du fichier Excel

### Onglet "Data"
- Donnees brutes importees
- Colonnes: A=Date, B=Product, C=Revenue, etc.

### Onglet "Analysis"
- Tableaux de synthese
- Formules a creer

## Formules a creer

### Formule 1: Total par categorie
**Cellule**: Analysis!B2
**Type**: SUMIFS
**References**: Data!C:C, Data!B:B

### Formule 2: Moyenne mobile 7j
**Cellule**: Data!E2 (a tirer)
**Type**: AVERAGE avec plage dynamique

### Formule 3: Variance vs budget
**Cellule**: Analysis!D2
**Depend de**: Formule 1

---

**Approuve?** (oui/non)
```

### Plan pour SQL

```markdown
# [Nom Analyse] - Plan SQL

**Livrable**: Requetes SQL (.sql)
**Fichier sortie**: `./scripts/queries.sql`
**Dialecte**: [PostgreSQL/MySQL/SQLite]

---

## Requetes a creer

### Query 1: Aggregation mensuelle
**Tables**: orders, customers
**Type**: SELECT avec GROUP BY
**Output**: Resultats agreges

### Query 2: Top clients
**Tables**: orders, customers
**Type**: Window function (RANK)
**Output**: Liste classee

### Query 3: Vue materialisee (optionnel)
**Depend de**: Query 1
**Type**: CREATE VIEW

---

## Ordre d'execution
1. Query 1 (standalone)
2. Query 2 (standalone)
3. Query 3 (depend de 1)

---

**Approuve?** (oui/non)
```

### Plan pour Rapport/Insights

```markdown
# [Nom Analyse] - Plan Rapport

**Livrable**: Rapport Markdown
**Fichier sortie**: `./outputs/report.md`
**Audience**: [Tech/Business/Executive]

---

## Sections du rapport

### Section 1: Resume executif
**Contenu**: 3-5 bullet points cles
**Longueur**: 100 mots max

### Section 2: Methodologie
**Contenu**: Sources, approche, limites
**Longueur**: Tech=detaille, Business=resume, Exec=skip

### Section 3: Resultats
**Contenu**: Findings principaux
**Visualisations**: 2-3 graphiques

### Section 4: Recommandations
**Contenu**: Actions suggerees
**Format**: Liste priorisee

---

**Approuve?** (oui/non)
```

## Regles

1. **Plan = QUOI, pas COMMENT** - Pas de code dans le plan
2. **Taches testables** - Chaque tache a une validation
3. **Dependencies claires** - Ordre logique
4. **Adapte au livrable** - Format different selon la cible
5. **Approbation explicite** - "oui" ou "approuve" requis

## Sauvegarder le Plan

Optionnel: sauvegarder dans `./docs/plans/YYYY-MM-DD-[nom].md`

## Apres Planning

**REQUIS**: Passer au skill `data-analyst:data-executing` une fois approuve.

## Langue

S'adapter a la langue de l'utilisateur.
