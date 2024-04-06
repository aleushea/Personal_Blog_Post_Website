from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Blog
from werkzeug.security import generate_password_hash, check_password_hash
from My_Websiste import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True) 
                flash('Logged in successfully!', category='success')
                if user.username == "admin" and password == "admin":
                    return redirect(url_for('views.add_new_blog'))
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        if len(first_name) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif password1 != password2:
            flash('password don\'t match', category='error')
        elif len(password1) < 8:
            flash('password must be at least 8 characters.', category='error')
        else:
            #add user to database
            new_user = User(first_name=first_name, email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            try:
                db.session.commit()
                flash('Account created!', category='success')
                # to redirect the user to homepage  
                return redirect(url_for('auth.login'))
            except Exception:
                return redirect(url_for('views.home'))
    return render_template("sign up.html")

@auth.route('/.add_new_blog', methods=['GET', 'POST'])
@login_required
def add_blog():
    if request.method == 'POST':
        # Retrieve form data
        title = request.form.get('Blog')
        content = request.form.get('posted-text')
        
        # Validate form data
        if not title or not content:
            flash('Please fill in all fields.', category='error')
        else:
            # Create a new Blog object and save it to the database
            new_blog = Blog(title=title, content=content, user_id=current_user.id)
            db.session.add(new_blog)
            db.session.commit()
            flash('Blog added successfully!', category='success')
            return redirect(url_for('views.home'))
    
    return render_template('add_blog.html')

@auth.route('/edit_blog/<int:blog_id>', methods=['GET', 'POST'])
@login_required
def edit_blog(blog_id):
    # Retrieve the blog from the database
    blog = Blog.query.get_or_404(blog_id)
    
    if request.method == 'POST':
        # Retrieve form data
        title = request.form.get('Blog')
        content = request.form.get('posted-text')
        
        # Validate form data
        if not title or not content:
            flash('Please fill in all fields.', category='error')
        else:
            # Update the blog attributes and save changes
            blog.title = title
            blog.content = content
            db.session.commit()
            flash('Blog updated successfully!', category='success')
            return redirect(url_for('views.blog', blog_id=blog.id))
    
    return render_template('edit_blog.html', blog=blog)

@auth.route('/delete_blog/<int:blog_id>', methods=['POST'])
@login_required
def delete_blog(blog_id):
    # Retrieve the blog from the database
    blog = Blog.query.get_or_404(blog_id)
    
    # Delete the blog
    db.session.delete(blog)
    db.session.commit()
    flash('Blog deleted successfully!', category='success')
    return redirect(url_for('views.home'))