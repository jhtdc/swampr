# -*- coding: utf-8 -*-

from app import app
from flask import render_template
from models import Post

@app.route('/')
def index():
	some_post = Post("What kinda day was it???","Ice Cube","Today was a good day", "1/1/2014")
	some_other_post = Post("What's good?", "Jason", "Everything is good!", "1/2/2014")
	return render_template("index.html", posts = [some_post,some_other_post])

