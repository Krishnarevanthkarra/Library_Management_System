from . import db

class Author(db.Model):
    __tablename__ = 'Authors'
    author_id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String)
    about_author = db.Column(db.String)