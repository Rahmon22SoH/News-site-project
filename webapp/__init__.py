<<<<<<< HEAD
from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user, logout_user

=======
from flask import Flask, render_template
from flask_login import login_manager

from webapp.weather import weather_by_city
>>>>>>> 98e414fd93215529cb5c8e5f6e0be32df4181513
from webapp.model import db, News, User
from webapp.forms import LoginForm
from webapp.weather import weather_by_city



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def loader_user(user_id):
        return User.query.get(user_id)

    @app.route("/")
    def index():
        title = "Новости Python"
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)

    @app.route("/login")
    def login():
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

<<<<<<< HEAD
    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы вошли на сайт')
                return redirect(url_for('index'))
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logaut():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect(url_for('index'))

=======
>>>>>>> 98e414fd93215529cb5c8e5f6e0be32df4181513
    return app

