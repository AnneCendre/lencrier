
# todo

créer le chatbot qui répond à des questions sur un article identifié par id.



# analyse par paragraphes

l'unité d'analyse est le paragraphe.
le texte du titre de l'article et éventuel sous-titre est ajouté dans la table comme texte de contexte pour chaque paragraphe.


il faut identifier des "sections" qui sont des groupes de paragraphes de même nature
par distance vectorielle ?

le titre 

# prompts

## analyse statistique d'un paraphe
- nombre de mots
- nombre de caractères



# idées



une base vectorielle pour les articles, avec des champs comme :
- nombre de paragraphes
- nombre de titres
- nombre de liens
- nombre d'images
- nombre de citations
- nombre de mots uniques
- nombre de phrases
- nombre de mots par phrase
- nombre de mots par paragraphe
- nombre de caractères par mot
- nombre de caractères par phrase
- nombre de caractères par paragraphe
- humeuur de l'article (positif, négatif, neutre)
- thème de l'article (politique, économie, culture, sport, etc.)
- date de publication
- auteur
- source (nom du journal)
- titre de l'article
- différentes sections de l'article : description, émotion, analyse, etc.
- différentes sections de l'article : pronoms (je, toi, nous, vous, neutre)
- différentes sections de l'article : temps (passé, présent, futur)
- différentes sections de l'article : voix (active, passive)
- différentes sections de l'article : modalité (indicatif, subjonctif, conditionnel, impératif)
- différentes sections de l'article : type de phrase (déclarative, interrogative, exclamative, impérative)
- différentes sections de l'article : type de discours (direct, indirect, narratif)
- différentes sections de l'article : type de texte (informatif, argumentatif, descriptif, narratif)



# document.embedding métadonnées

import sqlite3
from sentence_transformers import SentenceTransformer
import sqlite_vec
import json

2. Stockage séparé + filtrage hybride (post-traitement)
Générez l'embedding uniquement sur le texte, et stockez les métadonnées à part dans une base vectorielle (comme Chroma, Pinecone, ou Weaviate) :

# Stockage typique dans une base vectorielle
document = {
    "text": "Le temps est magnifique aujourd'hui.",
    "embedding": embedding.tolist(),
    "metadata": {
        "stats_basiques": stats_basiques,
        "analyse_sentiment": analyse_sentiment,
        "analyse_linguistique": analyse_linguistique
    }
}

Ensuite, lors de la recherche :

Faites une recherche sémantique avec l'embedding.
Filtrez ou réordonnez les résultats selon les métadonnées (ex: "seulement les textes positifs", "en temps présent", etc.). 
✅ Avantages : Plus flexible, permet des requêtes complexes. 
✅ Standard dans les systèmes RAG (Retrieval-Augmented Generation).
