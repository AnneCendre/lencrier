import requests
import re
from bs4 import BeautifulSoup

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
nomLencrier = 'Cendre'
res = lireArticles(nomLencrier, nomFichier)

csv = open("./result/data.csv", "w")
csv.write('nomLencrier;  id     ; dateLencrier              ; titre     ; length \n')
for article in sorted(res, key=lambda art: art.idLencrier, reverse = True):
    ligne =  '"' + article.nomLencrier + '" ; "' + article.idLencrier + '" ; "' + article.dateLencrier + '" ; "' + article.titre  + '" ; "' + str(len(article.content)) + '"'
    csv.write(ligne + '\n')


csv.close()


