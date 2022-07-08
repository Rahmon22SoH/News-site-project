from getpass import getpass
<<<<<<< HEAD
import sys
=======
import  sys
>>>>>>> 98e414fd93215529cb5c8e5f6e0be32df4181513

from webapp import create_app
from webapp.model import db, User

app = create_app()

with app.app_context():
<<<<<<< HEAD
    username = input('Введите имя пользователя:')
=======
    username = input('Введите имя:')
>>>>>>> 98e414fd93215529cb5c8e5f6e0be32df4181513

    if User.query.filter(User.username == username).count():
        print("Пользователь с таким именем уже есть")
        sys.exit(0)

    password1 = getpass('Введите пароль')
    password2 = getpass('Подтвердите пароль')

<<<<<<< HEAD
    if not password1 == password2:
=======
    if not  password1 == password2:
>>>>>>> 98e414fd93215529cb5c8e5f6e0be32df4181513
        print('Пароли не одинаковые')
        sys.exit(0)

    new_user = User(username=username, role='admin')
<<<<<<< HEAD
    new_user.set_password(password1)
=======
    new_user.set_password((password1))


>>>>>>> 98e414fd93215529cb5c8e5f6e0be32df4181513

    db.session.add(new_user)
    db.session.commit()
    print('Создан пользователь с id={}'.format(new_user.id))
