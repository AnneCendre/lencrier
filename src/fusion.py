import requests
import re
from operator import itemgetter, attrgetter

from models.article import Article
from utils.import_utils import lire_articles_from_lencrier_html
from utils.export_utils import write_html


EXPORT_PATH = "./exports/"

nom_fichier = EXPORT_PATH + "test_Cendre.html"
nom_lencrier = 'caillecendre'
articles = lire_articles_from_lencrier_html(nom_lencrier, nom_fichier)
nom_fichier = EXPORT_PATH + "test_Les amours de Cendre.html"
articles.extend(lire_articles_from_lencrier_html("cendre", nom_fichier))
nom_fichier = EXPORT_PATH + "test_Mes écrits manuscrits.html"
articles.extend(lire_articles_from_lencrier_html('manuscrits2caille', nom_fichier))

csv = open("./result/data.csv", "w")
csv.write('nomLencrier         ;  id       ; dateTime           ; dateLencrier              ; titre     ; length \n')
for article in sorted(articles, key=attrgetter('dateTime')):
    ligne =  '"' + article.nomLencrier + '" ; "' + article.idLencrier + '" ; "' + article.dateTime + '" ; "' + article.dateLencrier + '" ; "' + article.titre  + '" ; "' + str(len(article.content)) + '"'
    csv.write(ligne + '\n')
csv.close()

write_html(sorted(articles, key=attrgetter('dateTime')), "./result/template.html", "./result/journaux.html")


# inverser le tri :  , reverse = True

