from bs4 import BeautifulSoup
from models.article import Article
from utils.database import save_in_db

def lire_articles_from_lencrier_html(nom_lencrier, fichierSource):
    html = open(fichierSource)
    soup = BeautifulSoup(html.read(), 'html.parser')
    articlesTag = soup.find_all("div", class_="item")
    print (articlesTag[0].h2)
    articles = []
    for data in articlesTag:
        a = Article(nom_lencrier, data.get('id'), data.h2.get_text(), data.h3.get_text(), data.div.decode_contents())
        articles.append(a)
    print (articles.__len__())
    save_in_db(articles)
    return articles
