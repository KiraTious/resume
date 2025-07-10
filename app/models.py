from .extensions import db

class Contact (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(50), unique=True, nullable=False)
    telegram = db.Column(db.String(50), unique=True, nullable=False)