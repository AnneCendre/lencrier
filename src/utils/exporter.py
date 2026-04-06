from bs4 import BeautifulSoup
from models.article import Article
import copy

def write_html(articles, template, output):
    soup = BeautifulSoup(open(template),"html.parser")
    section = soup.find('section')
    articleTagTemplate = section.article
    for article in articles:
        articleTag = copy.copy(articleTagTemplate)
        articleTag["class"] = article.nom_lencrier
        articleTag.h2.string = article.titre
        articleTag.time.string = article.date_time
        articleTag.div.string = article.content
        section.append(articleTag)
    with open(output, "w", encoding = 'utf-8') as file:
        file.write(str(soup.prettify()))
