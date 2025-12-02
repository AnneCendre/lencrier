import requests
import re
import copy
from bs4 import BeautifulSoup
from operator import itemgetter, attrgetter
from datetime import datetime

class Article:
    def __init__ (self, nomLencrier, idLencrier, titre, dateLencrier, content):
        self.nomLencrier = nomLencrier
        self.idLencrier = idLencrier
        self.titre = titre
        self.dateLencrier = dateLencrier
        self.content = content
        
    def __str__ (self):
        return f"{self.idLencrier}({self.titre})"

    def __lt__ (self, other):
        # le tri par idLencrier est un pis aller : certains articles retro-publiés n'apparaissent pas dans l'ordre
        # TODO : la surcharge de l'opérateur "<" ne semble pas fonctionner, j'ai du utiliser sorted(articles, key=attrgetter('idLencrier'))
        self.idLencrier < other.idLencrier

def lireArticles(nomLencrier, fichierSource):
    html = open(fichierSource)
    soup = BeautifulSoup(html.read(), 'html.parser')
    articlesTag = soup.find_all("div", class_="item")
    print (articlesTag[0].h2)
    articles = []
    for data in articlesTag:
        a = Article(nomLencrier, data.get('id'), data.h2.get_text(), data.h3.get_text(), data.div.get_text())
        a.dateTime = date_fr_vers_iso(a.dateLencrier)
        articles.append(a)
    return articles

mois_fr = {
    "janvier": 1, "février": 2, "mars": 3, "avril": 4,
    "mai": 5, "juin": 6, "juillet": 7, "août": 8,
    "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12
}

def date_fr_vers_iso(date_str):
    # Exemple d'entrée : "27 août 2023 à 8h37"
    date_part, time_part = date_str.split(" à ")

    # --- Partie date ---
    jour, mois_str, annee = date_part.split(" ")
    mois = mois_fr[mois_str]

    # --- Partie heure ---
    heure = int(time_part.split("h")[0])
    minute = int(time_part.split("h")[1])

    # Construire l'objet datetime
    dt = datetime(int(annee), mois, int(jour), heure, minute)

    # Retour ISO 8601
    return dt.isoformat(timespec="minutes")



def writeHtml(articles, template, output):
    soup = BeautifulSoup(open(template),"html.parser")
    section = soup.find('section')
    articleTagTemplate = section.article
    for article in articles:
        articleTag = copy.copy(articleTagTemplate)
        articleTag["class"] = article.nomLencrier
        articleTag.h2.string = article.titre
        articleTag.time.string = article.dateTime
        articleTag.div.string = article.content
        section.append(articleTag)
    with open(output, "w", encoding = 'utf-8') as file:
        file.write(str(soup.prettify()))




nomFichier = "./exports/2025-11-24_Cendre.html"
nomLencrier = 'caillecendre'
articles = lireArticles(nomLencrier, nomFichier)
nomFichier = "./exports/2025-11-24_Les amours de Cendre.html"
articles.extend(lireArticles("cendre", nomFichier))
nomFichier = "./exports/2025-11-24_Mes écrits manuscrits.html"
articles.extend(lireArticles('manuscrits2caille', nomFichier))

csv = open("./result/data.csv", "w")
csv.write('nomLencrier         ;  id       ; dateTime           ; dateLencrier              ; titre     ; length \n')
for article in sorted(articles, key=attrgetter('dateTime')):
    ligne =  '"' + article.nomLencrier + '" ; "' + article.idLencrier + '" ; "' + article.dateTime + '" ; "' + article.dateLencrier + '" ; "' + article.titre  + '" ; "' + str(len(article.content)) + '"'
    csv.write(ligne + '\n')
csv.close()

writeHtml(articles, "./result/template.html", "./result/journaux.html")


# inverser le tri :  , reverse = True

