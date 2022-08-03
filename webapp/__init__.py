from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.news.views import blueprint as news_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.user.model import User



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def loader_user(user_id):
        return User.query.get(user_id)

    return app


