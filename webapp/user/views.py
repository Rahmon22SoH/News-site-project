from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user

from webapp.db import db
from webapp.user.forms import LoginForm, RegistrationForm
from webapp.user.model import User

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route("/login")
def login():
    if current_user.is_authenticated:
        return redirect(url_for("news.index"))
    title = 'Авторизация'
    login_form = LoginForm()
    return render_template('user/login.html', page_title=title, form=login_form)


@blueprint.route('/process-login', methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы вошли на сайт')
            return redirect(url_for('news.index'))

    flash('Неправильное имя пользователя или пароль')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logaut():
    logout_user()
    flash('Вы успешно разлогинились')
    return redirect(url_for('news.index'))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for("news.index"))
    title = 'Регистрация'
    form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form=form)


@blueprint.route('/process-reg', methods=['POST'])
def process_reg():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Вы успешно прошли регестрацию')
        return redirect(url_for('user.login'))
    flash('Пожалуйста исправьте ошибки в форме')
    return redirect(url_for('user/register'))


