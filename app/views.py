# -*- coding: utf-8 -*-

from app import app
from flask import Flask, render_template, redirect
from models import Post, User
from forms import NewUserForm

'''@app.route('/')
def index():
	some_post = Post("What kinda day was it???","Ice Cube","Today was a good day", "1/1/2014")
	some_other_post = Post("What's good?", "Jason", "Everything is good!", "1/2/2014")
	return render_template("index.html", posts = [some_post,some_other_post])'''

@app.route('/') #this is the landing page
def index():
	all_users = User.query.all()
	posts = Post.query.all()
	return render_template("index.html", users = all_users, posts = posts)

@app.route('/add_user', methods = ['GET', 'POST']) #this is the landing page
def add_user():
	form = NewUserForm()
	if form.validate_on_submit():
		user = User()
		form.populate_obj(user)
		db.session.add(user)
		db.session.commit()
		return redirect('/')
	return render_template("add_user.html", form = form)