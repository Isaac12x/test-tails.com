import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    PORT = int(os.environ.get("PORT", 5000))
    FLASK_APP = os.environ.get("FLASK_APP") or "main.main:app"
    FLASK_ENV = os.environ.get("FLASK_ENV") or "development"
    DEBUG = os.environ.get("DEBUG") or "True"
