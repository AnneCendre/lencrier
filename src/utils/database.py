from models.article import Article
import sqlite3

# Fonction pour enregistrer les articles dans la base de données
def save_in_db(articles, drop=False):
    # Créer une connexion à la base de données
    conn = sqlite3.connect('articles.db')

    # Créer une instance de curseur
    cur = conn.cursor()

    # Supprimer la table "articles" si elle existe déjà et que drop est True
    if drop:
        cur.execute('DROP TABLE IF EXISTS articles')

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
            INSERT OR IGNORE INTO articles (nom_lencrier, id_lencrier, titre, date_lencrier, content, date_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (article.nom_lencrier, article.id_lencrier, article.titre, article.date_lencrier, article.content, article.date_time))

    # Valider les modifications et fermer la connexion
    conn.commit()
    conn.close()
    
# créer la table des metadata
def create_metadata_table(drop=False):
    conn = sqlite3.connect('articles.db')
    cur = conn.cursor()
    if drop:
        cur.execute('DROP TABLE IF EXISTS metadata')
        
    cur.execute('''
        CREATE TABLE IF NOT EXISTS metadata (
            id_lencrier INTEGER PRIMARY KEY,
            embedding TEXT,
            nb_caracteres INTEGER,
            nb_paragraphes INTEGER
        )
    ''')
    conn.commit()
    conn.close()



    id_lencrier: int
    embedding: str
    nb_caracteres: int
    nb_paragraphes: int