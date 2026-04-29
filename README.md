# E-Commerce Sales Analysis

## Description
Analyse complète des données de ventes d'une plateforme e-commerce. 
Projet de **data analyst** combinant **SQL** pour les requêtes complexes et **Python** pour l'analyse et la visualisation.

## Démo en ligne
[Clique ici pour voir le dashboard](https://app-ecommerce-dashboard-glcmes9z89beqpgyg9nkan.streamlit.app)

**Objectifs** :
- Identifier les tendances de ventes
- Analyser le comportement des clients
- Segmenter les ventes par catégorie et région
- Créer des visualisations pour le reporting

---

## Résultats clés

| Métrique | Valeur |
|---|---|
| **Ventes totales** | 8 020€ |
| **Nombre de clients** | 7 |
| **Nombre de transactions** | 50 |
| **Catégorie dominante** | Électronique (73.5%) |
| **Région dominante** | Europe (66.8%) |
| **Client VIP** | Alice Martin (3 590€) |
| **Panier moyen** | 160.4€ |

### Top Insights
- **Électronique** génère 73.5% du CA (produits haut de gamme)
- **Europe** est le marché principal avec 66.8% des ventes
- **Alice Martin** représente 44.8% des revenus totaux
- Les **chaussettes** sont le produit le plus vendu en quantité (10 unités)
- Le panier moyen varie beaucoup selon les clients (60€ à 299€)

---

## Technologies

- **Python 3** — Analyse et visualisation
- **SQL (SQLite)** — Requêtes complexes
- **pandas** — Manipulation de données
- **matplotlib & seaborn** — Visualisations
- **sqlite3** — Base de données

---

## Fichiers du projet---

## Installation & Utilisation

### Prérequis
```bash
pip install pandas matplotlib seaborn
```

### Importer les données
```bash
python3 importer_donnees.py
```

### Lancer les analyses
```bash
python3 analyse.py
```

### Générer les visualisations
```bash
python3 visualisations.py
```

---

## Analyses réalisées

### 1. Ventes par catégorie
- **Électronique** : 5 890€ (24 ventes)
- **Vêtements** : 1 590€ (16 ventes)
- **Livres** : 540€ (10 ventes)

### 2. Top 5 clients
1. Alice Martin : 3 590€
2. Charlie Chen : 1 120€
3. Eve Johnson : 990€
4. Diana Lee : 960€
5. Bob Smith : 780€

### 3. Ventes par région
- **Europe** : 5 360€ (28 ventes)
- **Amérique** : 1 540€ (14 ventes)
- **Asie** : 1 120€ (8 ventes)

### 4. Produits top
- Chaussettes : 10 unités
- Câbles : 8 unités
- T-Shirt : 6 unités

---

## Requêtes SQL clés

### Ventes totales
```sql
SELECT SUM(vente_totale) FROM ventes;
```

### Top clients avec JOIN
```sql
SELECT c.client_nom, SUM(v.vente_totale) as total
FROM ventes v
JOIN clients c ON v.client_id = c.client_id
GROUP BY v.client_id
ORDER BY total DESC;
```

### Segmentation par région
```sql
SELECT c.region, SUM(v.vente_totale) as total, COUNT(*) as nb_ventes
FROM ventes v
JOIN clients c ON v.client_id = c.client_id
GROUP BY c.region
ORDER BY total DESC;
```

---

## Insights & Recommandations

### Observations
- La catégorie **Électronique** est très lucrative (73.5% du CA)
- **Alice Martin** est cliente fidèle avec 12 achats
- Europe génère 2/3 des revenus, c'est la région clé
- Grosse variation de panier moyen par client (60€ à 299€)

### Recommandations
- **Fidéliser Alice Martin** : VIP, programme de loyauté
- **Développer l'Électronique** : meilleure marge
- **Élargir en Asie & Amérique** : potentiel de croissance
- **Crossselling** : proposer articles complémentaires

---

## Limitations

- Données limitées à 50 transactions (dataset de démonstration)
- Pas de données de coûts (impossible de calculer marges)
- Pas de segmentation par période saisonnière
- Données agrégées sans contexte externe

---

## Évolutions futures

- Ajouter prédictions ML (Random Forest)
- Création d'un dashboard interactif (Plotly/Dash)
- Analyse RFM (Recency, Frequency, Monetary)
- Détection d'anomalies
- Export en PDF pour reporting

---

## Auteure
**Ibtissem Lagha**
Data Analyst | Python | SQL
[LinkedIn](https://linkedin.com/in/ibtissem-lagha-741865336)

---

## Notes
Projet personnel pour développer compétences en **SQL**, **Python** et **data analysis**.
