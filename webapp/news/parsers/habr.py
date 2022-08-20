from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import locale
import platform
from webapp.news.parsers.utils import get_html, save_news
from webapp import db
from webapp.news.model import News
from requests_html import HTMLSession

if platform == 'Linux':
    locale.setlocale(locale.LC_ALL, 'rus_rus')
else:
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def parse_habr_date(date_str):
    while '  ' in date_str:
        date_str = date_str.replace('  ', ' ')
    if 'сегодня' in date_str:
        today = datetime.now()
        date_str = date_str.replace('сегодня', today.strftime('%d %B %Y'))
    elif 'вчера' in date_str:
        yesterday = datetime.now() - timedelta(days=1)
        date_str = date_str.replace('вчера', yesterday.strftime('%d %B %Y'))
    # elif '_' in date_str:
    #     date_str = date_str.replace('-', date_str.strftime('%d %B %Y'))
    try:
        return datetime.strptime(date_str, '%d %B %Y в %H:%M')
    except ValueError:
        return datetime.now()


def get_news_snippets():
    html = get_html("https://habr.com/ru/search/?q=python&target_type=posts&order=date")
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_news = soup.find('div', class_='tm-articles-list').findAll('article', class_='tm-articles-list__item')
        for news in all_news:
            title = news.find('a', class_='tm-article-snippet__title-link').text
            url = news.find('a', class_='tm-article-snippet__title-link')['href']
            url = f'https://habr.com{url}'
            published = news.find('span', class_='tm-article-snippet__datetime-published').text
            published = parse_habr_date(published)
            print(title, url, published)
            save_news(title, url, published)


def get_news_content():
    news_without_text = News.query.filter(News.text.is_(None))
    for news in news_without_text:
        html = get_html(news.url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            if soup.find('div', class_='tm-misprint-area__wrapper') is not None:
                article = soup.find('div', class_='tm-misprint-area__wrapper').decode_contents()
                print(article)
                if article:
                    news.text = article
                    db.session.add(news)
                    db.session.commit()

