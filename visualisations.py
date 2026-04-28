import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Connexion
conn = sqlite3.connect('ma_base.db')

# 1. Ventes par catégorie
print("📊 Création des visualisations...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Graph 1 : Ventes par catégorie (pie chart)
df_cat = pd.read_sql_query('''
    SELECT categorie, SUM(vente_totale) as total
    FROM ventes
    GROUP BY categorie
    ORDER BY total DESC
''', conn)

axes[0, 0].pie(df_cat['total'], labels=df_cat['categorie'], autopct='%1.1f%%', colors=['#FF6B6B', '#4ECDC4', '#45B7D1'])
axes[0, 0].set_title('Ventes par Catégorie', fontsize=12, fontweight='bold')

# Graph 2 : Top 5 clients (bar chart)
df_clients = pd.read_sql_query('''
    SELECT c.client_nom, SUM(v.vente_totale) as total
    FROM ventes v
    JOIN clients c ON v.client_id = c.client_id
    GROUP BY v.client_id
    ORDER BY total DESC
    LIMIT 5
''', conn)

axes[0, 1].barh(df_clients['client_nom'], df_clients['total'], color='#95E1D3')
axes[0, 1].set_xlabel('Ventes (€)')
axes[0, 1].set_title('Top 5 Clients', fontsize=12, fontweight='bold')
axes[0, 1].invert_yaxis()

# Graph 3 : Ventes par région (bar chart)
df_region = pd.read_sql_query('''
    SELECT c.region, SUM(v.vente_totale) as total
    FROM ventes v
    JOIN clients c ON v.client_id = c.client_id
    GROUP BY c.region
    ORDER BY total DESC
''', conn)

axes[1, 0].bar(df_region['region'], df_region['total'], color='#F38181')
axes[1, 0].set_ylabel('Ventes (€)')
axes[1, 0].set_title('Ventes par Région', fontsize=12, fontweight='bold')
axes[1, 0].tick_params(axis='x', rotation=45)

# Graph 4 : Evolution temporelle des ventes
df_temps = pd.read_sql_query('''
    SELECT date, SUM(vente_totale) as total
    FROM ventes
    GROUP BY date
    ORDER BY date
''', conn)

df_temps['date'] = pd.to_datetime(df_temps['date'])
axes[1, 1].plot(df_temps['date'], df_temps['total'], marker='o', linewidth=2, color='#AA96DA')
axes[1, 1].set_xlabel('Date')
axes[1, 1].set_ylabel('Ventes (€)')
axes[1, 1].set_title('Évolution des Ventes dans le Temps', fontsize=12, fontweight='bold')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('analyse_ventes.png', dpi=300, bbox_inches='tight')
print("✅ Graphique sauvegardé : analyse_ventes.png")

plt.show()

conn.close()
