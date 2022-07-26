import os

basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = "Sochi,Russia"
WEATHER_API_KEY = "55d82c1a6ba2440eb58133738220506"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'sfjsjf515131351*(*&*(&*Y(Y(YJKK>mfksmdfkmUF(*&jswef'
