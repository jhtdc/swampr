import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/swamprdb'

CSRF_ENABLED = True # this prevents csrf attacks
SECRET_KEY = 'big-secret'
