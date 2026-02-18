from . import db

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    level = db.Column(db.String(15), nullable=False)
    title = db.Column(db.String(15), nullable=False)
    content = db.Column(db.String(250), nullable=False)
    finished = db.Column(db.Boolean, default=False)