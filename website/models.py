from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id = db.Column(db.Integer , primary_key = True)
    email = db.Column(db.String(150), unique = True) 
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    blogs = db.relationship('Blogs')


class Blogs(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    data = db.Column(db.__dict__)
    date = db.Column(db.DateTime(timezone = True),default = func.now())
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))