import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DB_SOURCE_FILE = "data.sqlite"
    SECRET_KEY = "Lol git rekt m8"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, DB_SOURCE_FILE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False