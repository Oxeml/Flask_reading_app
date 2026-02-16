from . import db

class Text(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable=False)