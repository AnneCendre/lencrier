from models.article import Article
from utils.database import create_metadata_table
import sqlite3  
from sentence_transformers import SentenceTransformer
import sqlite_vec
import json

# sur chaque article, on va faire un embedding de son contenu et le stocker dans la base de données

def article_factory(cursor, row):    
    return Article(*row)

create_metadata_table(drop=True)

conn = sqlite3.connect('articles.db')
conn.row_factory = article_factory
cur = conn.cursor()

cur.execute("SELECT * FROM articles")
articles = cur.fetchall()
for a in articles:
    # print(a.titre)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embedding = model.encode(a.content)
    embedding_json = json.dumps(embedding.tolist())
    cur.execute('INSERT INTO metadata (id_lencrier, embedding, nb_caracteres, nb_paragraphes) VALUES (?, ?, ?, ?)', (a.id_lencrier, embedding_json, len(a.content), a.content.count('<p>')))

conn.close()

