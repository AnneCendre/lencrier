import sqlite3

# Ouvrir la connexion à la base de données
conn = sqlite3.connect('articles.db')

# Créer un curseur pour effectuer des requêtes SQL
cur = conn.cursor()

# Exécuter une requête SQL pour récupérer le contenu de l'article avec l'ID spécifique
cur.execute('SELECT * FROM articles WHERE id_lencrier = ?', ('e125544',))

# Récupérer le résultat de la requête
article = cur.fetchone()

# Vérifier si l'article a été trouvé
if article:
    # Afficher le contenu de l'article dans la console
    print(article)
else:
    print('Article non trouvé')

# Fermer la connexion à la base de données
conn.close()