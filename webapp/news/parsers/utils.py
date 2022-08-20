import requests
from webapp.db import db
from webapp.news.model import News


def get_html(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:103.0) Gecko/20100101 Firefox/103.0"
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except(requests.RequestException, ValueError):
        print("Cетевая ошибка")
        return False


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    print(news_exists)
    if not news_exists:
        news_news = News(title=title, url=url, published=published)
        db.session.add(news_news)
        db.session.commit()