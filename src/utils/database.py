from models.article import Article
import sqlite3

def save_in_db(articles):
    # Créer une connexion à la base de données
    conn = sqlite3.connect('articles.db')

    # Créer une instance de curseur
    cur = conn.cursor()

    # Créer une table "articles" si elle n'existe pas déjà
    cur.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            nom_lencrier TEXT,
            id_lencrier INTEGER,
            titre TEXT,
            date_lencrier TEXT,
            date_time TEXT,
            content TEXT,
            UNIQUE(id_lencrier)
        )
    ''')

    # Insérer chaque article dans la base de données
    for article in articles:
        cur.execute('''
            INSERT INTO articles (nom_lencrier, id_lencrier, titre, date_lencrier, content, date_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (article.nom_lencrier, article.id_lencrier, article.titre, article.date_lencrier, article.content, article.date_time))

    # Valider les modifications et fermer la connexion
    conn.commit()
    conn.close()
    
    