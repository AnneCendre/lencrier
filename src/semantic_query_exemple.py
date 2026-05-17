import torch   
import json
import numpy as np
from sentence_transformers import SentenceTransformer, util

# 1. Initialisation du modèle
# device = 'cuda' if torch.cuda.is_available() else 'cpu'
device = 'cpu'
model = SentenceTransformer('all-MiniLM-L6-v2').to(device)

# Encoder avec le bon device

# 2. Données d'exemple (Simulations d'articles)
articles = [
    {"id": 1, "content": "Le cours du Bitcoin a dépassé un nouveau record historique ce matin."},
    {"id": 2, "content": "La recette de la tarte aux pommes traditionnelle nécessite du beurre et des cannelles."},
    {"id": 3, "content": "Les nouvelles cartes graphiques Nvidia améliorent les performances en intelligence artificielle."}
]

# 3. Vectorisation et stockage (Simulation de la base de données existante)
# Note : Le format JSON est converti en liste Python pour le traitement
for a in articles:
    embedding = model.encode(a["content"])
    a["embedding_json"] = json.dumps(embedding.tolist())

# --- ÉTAPE D'EXTRACTION SÉMANTIQUE ---

# Texte de recherche (la requête)
query = "Le prix des crypto-monnaies s'envole"

# Vectorisation de la requête
query_embedding = model.encode(query, convert_to_tensor=True, device=device)


# Reconstruction de la matrice des embeddings des articles
# Conversion du JSON string -> Liste -> Tensor
corpus_embeddings = []
for a in articles:
    emb_list = json.loads(a["embedding_json"])
    corpus_embeddings.append(emb_list)

# corpus_embeddings = np.array(corpus_embeddings)
corpus_embeddings = torch.tensor(corpus_embeddings, dtype=torch.float32).to(device)

# Calcul des scores de similarité cosinus
# 'util.cos_sim' gère automatiquement les matrices de tenseurs/numpy
cosine_scores = util.cos_sim(query_embedding, corpus_embeddings)[0]

# Extraction de l'indice du meilleur score
best_match_idx = int(np.argmax(cosine_scores))
best_score = cosine_scores[best_match_idx].item()

# Affichage du résultat
print(f"Requête : {query}\n")
print(f"Article le plus proche (Score: {best_score:.4f}) :")
print(articles[best_match_idx]["content"])