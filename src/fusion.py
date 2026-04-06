import requests
import re
from operator import itemgetter, attrgetter

from models.article import Article
import utils.import_utils
import utils.export_utils
from utils.export_utils import writeHtml

lireArticlesFromLencrierHtml = utils.import_utils.lireArticlesFromLencrierHtml

EXPORT_PATH = "./exports/"

nomFichier = EXPORT_PATH + "test_Cendre.html"
nomLencrier = 'caillecendre'
articles = lireArticlesFromLencrierHtml(nomLencrier, nomFichier)
nomFichier = EXPORT_PATH + "test_Les amours de Cendre.html"
articles.extend(lireArticlesFromLencrierHtml("cendre", nomFichier))
nomFichier = EXPORT_PATH + "test_Mes écrits manuscrits.html"
articles.extend(lireArticlesFromLencrierHtml('manuscrits2caille', nomFichier))

csv = open("./result/data.csv", "w")
csv.write('nomLencrier         ;  id       ; dateTime           ; dateLencrier              ; titre     ; length \n')
for article in sorted(articles, key=attrgetter('dateTime')):
    ligne =  '"' + article.nomLencrier + '" ; "' + article.idLencrier + '" ; "' + article.dateTime + '" ; "' + article.dateLencrier + '" ; "' + article.titre  + '" ; "' + str(len(article.content)) + '"'
    csv.write(ligne + '\n')
csv.close()

writeHtml(sorted(articles, key=attrgetter('dateTime')), "./result/template.html", "./result/journaux.html")


# inverser le tri :  , reverse = True

