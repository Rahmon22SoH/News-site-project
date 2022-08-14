from bs4 import BeautifulSoup
from datetime import datetime
from webapp.news.parsers.utils import get_html, save_news


def get_habr_snippets():
    html = get_html("https://habr.com/ru/search/?target_type=posts&q=python&order")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('div', class_='tm-articles-list').findAll('article', class_='tm-articles-list__item')
        for news in all_news:
            title = news.find('a', class_='tm-article-snippet__title-link').text
            url = news.select('a',  class_='tm-article-snippet__title-link')['href']
            published = news.find('span', class_='tm-article-snippet__datetime-published').text
            print(title, url, published)
            # try:
            #     published = datetime.strptime(published, '%Y-%m-%d')
            # except ValueError:
            #     published = datetime.now()
            # save_news(title, url, published)