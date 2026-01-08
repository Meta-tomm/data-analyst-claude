---
name: data-executing
description: This skill MUST be used after data-planning to execute the analysis plan. Generates appropriate outputs based on target (Python scripts, DAX/Excel formulas in .md for copy-paste, SQL files, reports).
---

# Data Executing

Executer le plan approuve et generer les livrables.

## Principe

Suivre le plan tache par tache. Le format de sortie depend du livrable cible.

## Execution par Type de Livrable

### Execution Python

1. Charger le plan
2. Pour chaque tache:
   - Ecrire le code
   - Executer et valider
   - Montrer le resultat
3. Assembler le script final
4. Sauvegarder dans `./scripts/`

**Format sortie:**
```python
#!/usr/bin/env python3
"""
[Nom analyse]
Generated: YYYY-MM-DD
"""

import pandas as pd
import numpy as np

# Tache 1: Chargement
df = pd.read_csv('./data/fichier.csv')

# Tache 2: Nettoyage
# ...

if __name__ == '__main__':
    main()
```

---

### Execution Power BI (DAX)

1. Charger le plan
2. Pour chaque mesure:
   - Ecrire la formule DAX
   - Expliquer la logique
   - Donner les instructions de copie
3. Sauvegarder dans `./outputs/dax-formulas.md`

**Format sortie (.md):**
```markdown
# Formules DAX - [Nom Analyse]

Generated: YYYY-MM-DD

---

## Mesure 1: Total Ventes

### Formule
```dax
Total Ventes = SUM(Sales[Amount])
```

### Instructions
1. Dans Power BI Desktop, aller dans **Modeling > New Measure**
2. Coller la formule ci-dessus
3. Renommer la mesure si necessaire
4. Format: Currency, 2 decimales

### Utilisation
- Cartes: afficher le total
- Graphiques: axe Y
- Filtres: peut etre utilise comme filtre

---

## Mesure 2: YoY Growth

### Formule
```dax
YoY Growth =
VAR CurrentYear = [Total Ventes]
VAR PreviousYear = CALCULATE(
    [Total Ventes],
    SAMEPERIODLASTYEAR('Date'[Date])
)
RETURN
DIVIDE(CurrentYear - PreviousYear, PreviousYear, BLANK())
```

### Instructions
1. **Prerequis**: Mesure "Total Ventes" doit exister
2. **Prerequis**: Table Date avec relation active
3. Coller dans New Measure
4. Format: Percentage, 1 decimale

### Utilisation
- Cartes: afficher la croissance
- Indicateurs conditionnels (vert si >0, rouge si <0)

---

[Autres mesures...]
```

---

### Execution Excel

1. Charger le plan
2. Pour chaque formule:
   - Ecrire la formule Excel
   - Donner les references exactes
   - Expliquer comment appliquer
3. Sauvegarder dans `./outputs/excel-formulas.md`

**Format sortie (.md):**
```markdown
# Formules Excel - [Nom Analyse]

Generated: YYYY-MM-DD

---

## Setup Initial

### Structure attendue
- **Onglet "Data"**: Donnees brutes
  - Colonne A: Date
  - Colonne B: Produit
  - Colonne C: Revenue
  - Colonne D: Categorie

- **Onglet "Analysis"**: Resultats

---

## Formule 1: Total par Categorie

### Formule
```excel
=SUMIFS(Data!$C:$C, Data!$D:$D, A2)
```

### Emplacement
- Onglet: **Analysis**
- Cellule: **B2**
- Tirer vers le bas pour chaque categorie

### Explication
- `Data!$C:$C`: Colonne des revenues (absolue)
- `Data!$D:$D`: Colonne des categories (absolue)
- `A2`: Categorie a filtrer (relative)

---

## Formule 2: Moyenne Mobile 7 Jours

### Formule
```excel
=IF(ROW()-1<7, "", AVERAGE(INDIRECT("C"&ROW()-6&":C"&ROW())))
```

### Emplacement
- Onglet: **Data**
- Colonne: **E** (a cote des donnees)
- Tirer de E2 jusqu'a la fin

### Alternative plus simple
```excel
=AVERAGE(C2:C8)
```
Puis tirer vers le bas (si donnees triees par date)

---

[Autres formules...]
```

---

### Execution SQL

1. Charger le plan
2. Pour chaque query:
   - Ecrire la requete SQL
   - Commenter chaque section
   - Adapter au dialecte
3. Sauvegarder dans `./scripts/queries.sql`

**Format sortie (.sql):**
```sql
-- ================================================
-- [Nom Analyse]
-- Generated: YYYY-MM-DD
-- Dialect: PostgreSQL
-- ================================================

-- Query 1: Aggregation mensuelle
-- But: Calculer le revenue par mois
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(amount) AS total_revenue,
    COUNT(*) AS order_count
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;

-- ------------------------------------------------

-- Query 2: Top 10 clients
-- But: Identifier les meilleurs clients
WITH customer_totals AS (
    SELECT
        c.customer_id,
        c.name,
        SUM(o.amount) AS total_spent
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.name
)
SELECT
    customer_id,
    name,
    total_spent,
    RANK() OVER (ORDER BY total_spent DESC) AS rank
FROM customer_totals
ORDER BY rank
LIMIT 10;

-- ================================================
-- End of queries
-- ================================================
```

---

### Execution Rapport

1. Charger le plan
2. Pour chaque section:
   - Rediger le contenu
   - Generer les visualisations si besoin
   - Adapter au niveau d'audience
3. Sauvegarder dans `./outputs/report.md`

## Workflow d'Execution

```
1. Afficher: "Execution du plan..."
2. Pour chaque tache:
   a. Marquer in_progress (TodoWrite)
   b. Executer
   c. Montrer resultat intermediaire
   d. Marquer completed
3. Assembler le livrable final
4. Afficher: "Execution terminee"
5. Proposer: "Sauvegarder dans [path]?"
```

## Gestion des Problemes

Si une tache echoue:
1. **Stop** - ne pas continuer
2. **Expliquer** le probleme
3. **Proposer** des solutions
4. **Attendre** la decision utilisateur

## Checkpoint Final

```markdown
## Execution Terminee

### Livrables generes

| Fichier | Type | Statut |
|---------|------|--------|
| ./outputs/dax-formulas.md | DAX | Pret a copier |
| ./scripts/analysis.py | Python | Executable |

### Resume
[Ce qui a ete fait]

### Prochaines etapes suggerees
- [Suggestion 1]
- [Suggestion 2]
```

## Langue

S'adapter a la langue de l'utilisateur.
