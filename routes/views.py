from flask import Blueprint, render_template

from models import Author, Student, Transaction

views_bp = Blueprint('views', __name__)

@views_bp.route('/views')
def show_transactions():
    return render_template('viewsPage.html')

@views_bp.route('/views/authors-to-books')
def authors_to_books():
    return render_template('authorsToBooksPage.html', authors = Author.query.all())

@views_bp.route('/views/students-to-transactions')
def students_to_transactions():
    return render_template('studentsToTransactions.html', students = Student.query.all())

@views_bp.route('/views/active-transactions')
def active_transactions():
    return render_template('activeTransactions.html', transactions = Transaction.query.all())