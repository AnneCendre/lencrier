
from operator import attrgetter

from models.article import Article
from utils import lire_articles_from_lencrier_html, write_html

## Lit les articles à partir des fichiers HTML exportés depuis Lencrier
## sauve les articles dans la base de données au fur et à mesure de leur lecture
## trie les articles par date 
## crée un fichier CSV avec les métadonnées des articles
## crée un fichier HTML de sortie avec les articles triés par date

nom_fichier = "./exports/test_Cendre.html"
nom_lencrier = "caillecendre"

articles: list[Article] = []
articles.extend(lire_articles_from_lencrier_html(nom_lencrier, nom_fichier))

nom_fichier = "./exports/test_Les amours de Cendre.html"
articles.extend(lire_articles_from_lencrier_html("cendre", nom_fichier))

nom_fichier = "./exports/test_Mes écrits manuscrits.html"
articles.extend(lire_articles_from_lencrier_html("manuscrits2caille", nom_fichier))

# print(articles.__len__())
# print(articles[0].content)


with open("./result/data.csv", "w") as csv_file:
    csv_file.write(
        "nomLencrier         ;  id       ; dateTime           ; dateLencrier              ; titre     ; length \n"
    )

    for article in sorted(articles, key=attrgetter("date_time")):
        ligne = (
            f'"{article.nom_lencrier}" ; '
            f'"{article.id_lencrier}" ; '
            f'"{article.date_time}" ; '
            f'"{article.date_lencrier}" ; '
            f'"{article.titre}" ; '
            f'"{str(len(article.content))}"'
        )
        csv_file.write(ligne + "\n")


articles_sorted = sorted(articles, key=attrgetter("date_time"))

write_html(
    articles_sorted,
    "./result/template.html",
    "./result/journaux.html"
)




# inverser le tri :  , reverse = True
