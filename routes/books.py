from flask import Blueprint, render_template

from models import Book, Author

books_bp = Blueprint('books', __name__)

@books_bp.route('/books')
def show_books():
    return render_template('booksPage.html', books=Book.query.all(), authors=Author)
