from flask import Blueprint, render_template, jsonify, request, flash, redirect, url_for
from models import Book, Author, Branch, Student, Transaction, db
from datetime import date

books_bp = Blueprint('books', __name__)

@books_bp.route('/books')
def show_books():
    return render_template('booksPage.html', books=Book.query.all(), authors=Author, students= Student.query.all(), transactions=Transaction.query.all())

@books_bp.route('/books/student-free/<int:student_id>', methods=['GET'])
def is_student_free(student_id):
    student = Student.query.get(student_id)
    message = {'free': True, 'student_name': student.name, 'student_branch': student.branches.branch_name}
    if student.book_limit > 0:
        return jsonify(message)
    else:
        message['free'] = False
        return jsonify(message)

@books_bp.route('/books/add-transaction', methods=['POST'])
def add_book_transaction():
    student_id = request.form.get('student-id')
    book_id = request.form.get('book-id')
    book = Book.query.get(book_id)
    book.available_copies -= 1
    student = Student.query.get(student_id)
    student.book_limit -= 1
    transaction = Transaction(student_id=student_id, book_id=book_id, issued_date=date.today())
    db.session.add(transaction)
    db.session.commit()
    flash('Transaction has been added.', 'success')
    return redirect(url_for('books.show_books'))

@books_bp.route('/books/close-transaction', methods=['POST'])
def close_transaction():
    transaction_id = request.form.get('transaction-id')
    transaction = Transaction.query.get(transaction_id)
    book = Book.query.get(transaction.book_id)
    book.available_copies += 1
    student = Student.query.get(transaction.student_id)
    student.book_limit += 1
    transaction.return_date = date.today()
    transaction.status = 'Returned'
    db.session.commit()
    flash('Transaction has been closed.', 'success')
    return redirect(url_for('books.show_books'))