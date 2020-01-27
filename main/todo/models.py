from main import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo = db.Column(db.String(20))