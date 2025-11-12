from . import db

class Book(db.Model):
    __tablename__ = 'Books'
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    subtitle = db.Column(db.Text)
    description = db.Column(db.Text)
    total_copies = db.Column(db.Integer, default=5)
    available_copies = db.Column(db.Integer,default=5)
    author_id = db.Column(db.Integer, db.ForeignKey('Authors.author_id'), nullable=False)

    transactions = db.relationship('Transaction', backref='books', lazy='dynamic', cascade="all, delete-orphan")

    def to_dict(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'subtitle': self.subtitle,
            'description': self.description,
            'total_copies': self.total_copies,
            'available_copies': self.available_copies,
            'author_id': self.author_id,
        }
