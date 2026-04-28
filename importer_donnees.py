import sqlite3
import csv
import pandas as pd

# Connexion à la base
conn = sqlite3.connect('ma_base.db')
cursor = conn.cursor()

# Créer les tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        client_id TEXT PRIMARY KEY,
        client_nom TEXT,
        region TEXT,
        pays TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventes (
        id INTEGER PRIMARY KEY,
        date TEXT,
        client_id TEXT,
        categorie TEXT,
        produit TEXT,
        quantite INTEGER,
        prix_unitaire REAL,
        vente_totale REAL,
        FOREIGN KEY (client_id) REFERENCES clients(client_id)
    )
''')

# Lire le CSV
df = pd.read_csv('ventes.csv')

# Insérer clients uniques
clients_uniques = df[['client_id', 'client_nom', 'region', 'pays']].drop_duplicates()
for _, row in clients_uniques.iterrows():
    cursor.execute('''
        INSERT OR IGNORE INTO clients (client_id, client_nom, region, pays)
        VALUES (?, ?, ?, ?)
    ''', (row['client_id'], row['client_nom'], row['region'], row['pays']))

# Insérer ventes
for _, row in df.iterrows():
    cursor.execute('''
        INSERT INTO ventes (date, client_id, categorie, produit, quantite, prix_unitaire, vente_totale)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (row['date'], row['client_id'], row['categorie'], row['produit'], 
          row['quantite'], row['prix_unitaire'], row['vente_totale']))

conn.commit()

# Vérifier
cursor.execute('SELECT COUNT(*) FROM ventes')
nb_ventes = cursor.fetchone()[0]

cursor.execute('SELECT COUNT(*) FROM clients')
nb_clients = cursor.fetchone()[0]

print(f"✅ Données importées !")
print(f"   - {nb_ventes} ventes")
print(f"   - {nb_clients} clients")

conn.close()
