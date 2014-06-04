#class Post:
#	def __init__(self, title, author, content, date):
#		self.title = title
#		self.author = author
#		self.content = content
#		self.date = date

from app import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	firstname = db.Column(db.String(64))
	lastname = db.Column(db.String(64))
	username = db.Column(db.String(20), unique = True)
	#posts = db.relationship('Post', backref = 'author')

class Post(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(100))
	#author = db.Column(db.String(64))
	content = db.Column(db.Text)
	author = db.Column(db.Integer, db.ForeignKey('user.id'))





