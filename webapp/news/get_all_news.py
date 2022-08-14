from webapp.news.parsers import habr
from webapp import create_app

app = create_app()
with app.app_context():
    habr.get_habr_snippets()