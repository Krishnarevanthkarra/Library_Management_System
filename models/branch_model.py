from . import db

class Branch(db.Model):
    __tablename__ = 'Branches'
    branch_id = db.Column(db.Integer, nullable=False, primary_key=True)
    branch_name = db.Column(db.String(20), nullable=False)