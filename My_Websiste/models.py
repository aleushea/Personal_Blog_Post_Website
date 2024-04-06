from My_Websiste import db
from flask_sqlalchemy  import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))
    confirm_password = db.Column(db.String(100))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    feedback = db.Column(db.String(1000))
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    post = db.Column(db.Text)
    datetime = db.Column(db.DateTime)
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(100))
    date_commented = db.Column(db.DateTime(timezone=True), default=func.now())
    feedback = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))