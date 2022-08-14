from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, \
    Length  # Клас помогает избежать ручных проверок, проверяет
# что пользователь вбил данные.
from webapp.user.model import User


# class CreateUserForm(FlaskForm):
#     username = StringField(label=('Username'),
#         validators=[DataRequired(),
#         Length(max=64, message='The username must contain no more than %(max 64)d characters.')])
#     email = StringField(label=('Email'),
#         validators=[DataRequired(),
#         Email(),
#         Length(max=120)])
#     password = PasswordField(label=('Password'),
#         validators=[DataRequired(),
#         Length(min=8, message='Password should be at least %(min)d characters long')])
#     confirm_password = PasswordField(
#         label=('Confirm Password'),
#         validators=[DataRequired(message='*Required'),
#         EqualTo('password', message='Both password fields must be equal!')])
#
#     receive_emails = BooleanField(label=('Receive merketting emails.'))
#
#     submit = SubmitField(label=('Submit'))
#

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(),], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    remember_me = BooleanField('Запомни меня', default=True, render_kw={"class": "form-check-input"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=5, max=64, message='Длина имени должна быть между %(mind и %(max) символов ')],render_kw={"class": "form-control"})
    email = StringField('Электронная почта', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

    def validate_username(self, username):
        user_count = User.query.filter_by(username=username.data).count()
        excluded_chars = "*?!'^+%&;/()=}][{$#"
        for char in self.username.data:
            if char in excluded_chars:
                raise ValidationError(
                    f"Символ {char} не допускается в имени пользователя.")
            if user_count > 0:
                raise ValidationError('Пользователь с таким именем уже зарегестрирован')

    def validate_email(self, email):
        user_count = User.query.filter_by(email=email.data).count()
        if user_count > 0:
            raise ValidationError('Пользователь с такой электронной почтой уже сушествует')

    def length(min=-1, max=-1, message=None):
        if not message:
            message = f'Must be between {min} and {max} characters long.'

        def _length(form, field):
            l = field.data and len(field.data) or 0
            if l < min or max != -1 and l > max:
                raise ValidationError(message)

        return _length



