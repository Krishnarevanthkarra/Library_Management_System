from flask import Blueprint, render_template

books_bp = Blueprint('books', __name__)

@books_bp.route('/books')
def show_books():
    return render_template('booksPage.html')
