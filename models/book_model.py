from . import db

class Book(db.Model):
    __tablename__ = 'Books'
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    subtitle = db.Column(db.String)
    description = db.Column(db.String)
    total_copies = db.Column(db.Integer, default=5)
    available_copies = db.Column(db.Integer,default=5)
    author_id = db.Column(db.Integer, db.ForeignKey('Authors.author_id'), nullable=False)