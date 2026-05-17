from models.article import Article
from utils.database import create_metadata_table
import sqlite3  
from sentence_transformers import SentenceTransformer
import sqlite_vec
import json
import gc
import torch


def article_factory(cursor, row):    
    return Article(*row)


# sur chaque article, on va faire un embedding de son contenu et le stocker dans la base de données
create_metadata_table(drop=True)

# ouverture de la base de données
conn = sqlite3.connect('articles.db')
conn.row_factory = article_factory
cur = conn.cursor()

# Initialisation du modèle
# device = 'cuda' if torch.cuda.is_available() else 'cpu'
device = 'cpu'
# all-MiniLM-L6-v2 est un modèle léger pour être porté par une petite configuration.
model = SentenceTransformer('all-MiniLM-L6-v2').to(device)

cur.execute("SELECT * FROM articles")
articles = cur.fetchall()

for i in range(0, len(articles), 16):  # Batch de 16
    batch = [a.content for a in articles[i:i+16]]
    embeddings = model.encode(batch, convert_to_tensor=True)
    embeddings = embeddings.cpu()
    
    for j, emb in enumerate(embeddings):
        a = articles[i+j]
        print('## ', a.titre)
        embedding_json = json.dumps(emb.tolist())
        print(embedding_json.__len__())
        cur.execute('INSERT INTO metadata (id_lencrier, embedding, nb_caracteres, nb_paragraphes) VALUES (?, ?, ?, ?)', (a.id_lencrier, embedding_json, len(a.content), a.content.count('<p>')))


    # Sauvegarde des embeddings dans la base de données
#    cur.execute('INSERT INTO metadata (id_lencrier, embedding, nb_caracteres, nb_paragraphes) VALUES (?, ?, ?, ?)', (a.id_lencrier, embedding_json, len(a.content), a.content.count('<p>')))

    del embeddings
    torch.cuda.empty_cache()
    gc.collect()   


""" for a in articles:
    print('## ', a.titre)

    # encode un article et sauvegardé l'embedding
    embedding = model.encode(a.content, convert_to_tensor=True)
    embedding = embedding.cpu()  # Ramène le tenseur sur CPU
    embedding_json = json.dumps(embedding.tolist())
    cur.execute('INSERT INTO metadata (id_lencrier, embedding, nb_caracteres, nb_paragraphes) VALUES (?, ?, ?, ?)', (a.id_lencrier, embedding_json, len(a.content), a.content.count('<p>')))

    print(embedding_json.__len__())
    
    # Libère le tenseur GPU
    del embedding
    torch.cuda.empty_cache()  # Vide le cache CUDA
    gc.collect()  # Force le garbage collector    """

conn.close()

