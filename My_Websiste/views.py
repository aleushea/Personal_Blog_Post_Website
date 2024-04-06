from flask import Blueprint, render_template
from flask_login import login_required

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about')
def about():
    return render_template("home.html")

@views.route('/blogs')
def blogs():
    return render_template("blogs.html")

@views.route('/service')
def service():
    return render_template("home.html")

@views.route('/contact')
def contact():
    return render_template("home.html")

# Restrict access to logged-in users
@views.route('/add_new_blog')
@login_required  
def add_new_blog():
    return render_template("add_New_Blog.html")
# Restrict access to logged-in users
@views.route('/blog')
@login_required 
def blog():
    return render_template("blog.html")
