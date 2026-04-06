from bs4 import BeautifulSoup
from models.article import Article
from utils.date_utils import date_fr_vers_iso

def lireArticlesFromLencrierHtml(nomLencrier, fichierSource):
    html = open(fichierSource)
    soup = BeautifulSoup(html.read(), 'html.parser')
    articlesTag = soup.find_all("div", class_="item")
    print (articlesTag[0].h2)
    articles = []
    for data in articlesTag:
        a = Article(nomLencrier, data.get('id'), data.h2.get_text(), data.h3.get_text(), data.div.get_text())
        a.dateTime = date_fr_vers_iso(a.dateLencrier)
        articles.append(a)
    print (articles.__len__())
    return articles