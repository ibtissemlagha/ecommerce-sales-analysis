import sqlite3
import pandas as pd

# Connexion
conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()

print("=" * 60)
print("📊 ANALYSE E-COMMERCE")
print("=" * 60)

# 1. Ventes totales
print("\n1️⃣ VENTES TOTALES")
cursor.execute('SELECT SUM(vente_totale) FROM ventes')
total = cursor.fetchone()[0]
print(f"   Total : {total:.2f}€")

# 2. Ventes par catégorie
print("\n2️⃣ VENTES PAR CATÉGORIE")
cursor.execute('''
    SELECT categorie, SUM(vente_totale) as total, COUNT(*) as nb_ventes
    FROM ventes
    GROUP BY categorie
    ORDER BY total DESC
''')
for row in cursor.fetchall():
    print(f"   {row[0]:15} : {row[1]:8.2f}€ ({row[2]} ventes)")

# 3. Top 5 clients
print("\n3️⃣ TOP 5 CLIENTS")
cursor.execute('''
    SELECT c.client_nom, SUM(v.vente_totale) as total
    FROM ventes v
    JOIN clients c ON v.client_id = c.client_id
    GROUP BY v.client_id
    ORDER BY total DESC
    LIMIT 5
''')
for row in cursor.fetchall():
    print(f"   {row[0]:20} : {row[1]:8.2f}€")

# 4. Ventes par région
print("\n4️⃣ VENTES PAR RÉGION")
cursor.execute('''
    SELECT c.region, SUM(v.vente_totale) as total, COUNT(*) as nb_ventes
    FROM ventes v
    JOIN clients c ON v.client_id = c.client_id
    GROUP BY c.region
    ORDER BY total DESC
''')
for row in cursor.fetchall():
    print(f"   {row[0]:15} : {row[1]:8.2f}€ ({row[2]} ventes)")

# 5. Produits les plus vendus
print("\n5️⃣ PRODUITS LES PLUS VENDUS (par quantité)")
cursor.execute('''
    SELECT produit, SUM(quantite) as total_quantite, SUM(vente_totale) as total_revenu
    FROM ventes
    GROUP BY produit
    ORDER BY total_quantite DESC
    LIMIT 5
''')
for row in cursor.fetchall():
    print(f"   {row[0]:25} : {row[1]} unités ({row[2]:.2f}€)")

# 6. Panier moyen par client
print("\n6️⃣ PANIER MOYEN PAR CLIENT")
cursor.execute('''
    SELECT c.client_nom, AVG(v.vente_totale) as panier_moyen, COUNT(*) as nb_achats
    FROM ventes v
    JOIN clients c ON v.client_id = c.client_id
    GROUP BY v.client_id
    ORDER BY panier_moyen DESC
''')
for row in cursor.fetchall():
    print(f"   {row[0]:20} : {row[1]:8.2f}€/achat ({row[2]} achats)")

print("\n" + "=" * 60)

conn.close()
