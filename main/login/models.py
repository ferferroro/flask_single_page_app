from main import db
from flask_login import UserMixin

class User(UserMixin, db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))