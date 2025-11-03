from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .book_model import Book
from .author_model import Author
from .student_model import Student
from .transaction_model import Transaction