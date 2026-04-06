import sqlite3

# non utilisé car la table est créée dans exporter.py

# Créer une connexion à la base de données
conn = sqlite3.connect('articles.db')

# Créer une instance de curseur
cur = conn.cursor()

# Créer la table "articles"
cur.execute('''
    CREATE TABLE articles (

    )
''')

# Fermer la connexion lorsque vous avez terminé
conn.close()