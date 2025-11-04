from . import db

class Student(db.Model):
    __tablename__ = 'Students'
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    branch = db.Column(db.Integer, db.ForeignKey('Branches.branch_id'), nullable=False)
    book_limit = db.Column(db.Integer, nullable=False)

    transactions = db.relationship('Transaction', backref='student', lazy='dynamic')

