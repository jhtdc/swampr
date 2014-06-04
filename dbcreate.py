# Go ahead and make my day
# creates  database based on the models we've defined in models.py

from config import SQLALCHEMY_DATABASE_URI
from app import db
db.create_all()
