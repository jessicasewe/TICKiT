from sqlalchemy import ForeignKey
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    tickets = db.relationship('Ticket')
    comments = db.relationship('Comment')


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.String(100))  
    item_id = db.Column(db.String(100))  
    product = db.Column(db.String(100))  
    currency = db.Column(db.String(10))   
    order_total = db.Column(db.Float)
    description = db.Column(db.String(255)) 
    checkout_url = db.Column(db.String(255))
    user_id = db.Column(db.Integer, ForeignKey('user.id'))

    # user = relationship('User', backref='tickets')