import requests
import re
from bs4 import BeautifulSoup
from operator import itemgetter, attrgetter

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
        # TODO : la surcharge de l'opérateur "<" ne semble pas fonctionner, j'ai du utiliser sorted(res, key=attrgetter('idLencrier'))
        self.idLencrier < other.idLencrier

def lireArticles(nomLencrier, fichierSource):
    html = open(fichierSource)
    soup = BeautifulSoup(html.read(), 'html.parser')
    articles = soup.find_all("div", class_="item")
    print (articles[0].h2)
    res = []
    for data in articles:
        a = Article(nomLencrier, data.get('id'), data.h2.get_text(), data.h3.get_text(), data.div.get_text())
        res.append(a)
    return res
    

nomFichier = "./exports/2024-08-08_Cendre.html"
nomLencrier = 'caillecendre'
res = lireArticles(nomLencrier, nomFichier)
nomFichier = "./exports/2024-08-08_Les amours de Cendre.html"
res.extend(lireArticles("cendre", nomFichier))
nomFichier = "./exports/2024-08-08_Mes écrits manuscrits.html"
res.extend(lireArticles('manuscrits2caille', nomFichier))

csv = open("./result/data.csv", "w")
csv.write('nomLencrier;  id     ; dateLencrier              ; titre     ; length \n')
for article in sorted(res, key=attrgetter('idLencrier')):
    ligne =  '"' + article.nomLencrier + '" ; "' + article.idLencrier + '" ; "' + article.dateLencrier + '" ; "' + article.titre  + '" ; "' + str(len(article.content)) + '"'
    csv.write(ligne + '\n')


csv.close()


# inverser le tri :  , reverse = True

