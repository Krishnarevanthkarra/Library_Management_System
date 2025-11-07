from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify
from models import db, Book, Author, Student, Branch

admin_bp = Blueprint('admin', __name__)



# ADMIN PAGE
@admin_bp.route('/admin')
def show_admin():
    authors = Author.query.all()
    books = Book.query.all()
    branches = Branch.query.all()
    students = Student.query.all()
    return render_template('adminPage.html', authors=authors, books=books, branches=branches, students=students)



# TO ADD AN AUTHOR
@admin_bp.route('/admin/add-author', methods=['POST'])
def add_author():
    if request.method == 'GET':
        return redirect(url_for('admin.show_admin'))
    name = request.form['authorname']
    about = request.form['aboutauthor']
    new_author = Author(author_name=name, about_author=about)
    db.session.add(new_author)
    db.session.commit()
    flash('Added the Author successfully.', 'success')
    return redirect(url_for('admin.show_admin'))



# TO REMOVE AN AUTHOR
@admin_bp.route('/admin/remove-author', methods=['POST'])
def remove_author():
    author_id = request.form.get('author_id')
    if not author_id:
        flash("No author selected." 'error')
        return redirect(url_for('admin.show_admin'))

    author = Author.query.get(author_id)
    if author:
        db.session.delete(author)
        db.session.commit()
        flash(f"Removed author: {author.author_name}", 'success')
    else:
        flash("Author not found."'error')

    return redirect(url_for('admin.show_admin'))



# CHECKING AN AUTHOR IS FREE TO REMOVE (NO LINK TO ANY BOOK)
@admin_bp.route('/admin/is-author-free/<int:author_id>', methods=['GET'])
def is_author_free(author_id):
    if Book.query.filter_by(author_id=author_id).first():
        return jsonify({'free': False})
    else:
        return jsonify({'free': True})



# TO ADD A BOOK
@admin_bp.route('/admin/add-book', methods=['POST'])
def add_book():
    if request.method == 'GET':
        return redirect(url_for('admin.show_admin'))
    title = request.form['title']
    subTitle = request.form['subtitle']
    description = request.form['description']
    author_id = request.form.get('book_author_id')
    newBook = Book(title=title, subtitle=subTitle, description=description, author_id=author_id)
    db.session.add(newBook)
    db.session.commit()
    flash("Book added successfully.", 'success')
    return redirect(url_for('admin.show_admin'))



# TO REMOVE A BOOK
@admin_bp.route('/admin/remove-book',methods=['POST'])
def remove_book():
    if request.method == 'GET':
        return redirect(url_for('admin.show_admin'))
    book_id = request.form.get('book_id')
    if not book_id:
        flash("No book selected.", 'error')
        return redirect(url_for('admin.show_admin'))
    book = Book.query.get(book_id)
    if book:
        db.session.delete(book)
        db.session.commit()
        flash("Book removed successfully.", 'success')
    else:
        flash("Book not found.", 'error')
    return redirect(url_for('admin.show_admin'))



# CHECKING A BOOK IS FREE TO REMOVE (NO ONGOING TRANSACTIONS)
@admin_bp.route('/admin/is-book-free/<int:book_id>', methods=['GET'])
def is_book_free(book_id):
    book = Book.query.get(book_id)
    if book.total_copies == book.available_copies:
        return jsonify({'free': True})
    else:
        return jsonify({'free': False})



# TO GET THE BOOK DETAILS FOR BOOK DETAILS UPDATE
@admin_bp.route('admin/get-book/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return jsonify(book.to_dict())
    else:
        flash("Book not found.", 'error')
        return redirect(url_for('admin.show_admin'))



# TO UPDATE THE BOOK DETAILS
@admin_bp.route('/admin/update-book', methods=['POST'])
def update_book():
    if request.method == 'GET':
        return redirect(url_for('admin.show_admin'))
    book = Book.query.get(request.form.get('book_id_get'))
    book.title = request.form.get('title')
    book.subtitle = request.form.get('subtitle')
    book.description = request.form.get('description')
    copies = int(request.form.get('copies')) if request.form.get('copies') else 0
    book.total_copies += int(copies)
    book.available_copies += int(copies)
    book.author_id = request.form.get('author_id')
    db.session.commit()
    flash('Successfully updated the book.', 'success')
    return redirect(url_for('admin.show_admin'))



# TO ADD STUDENT
@admin_bp.route('/admin/addstudent', methods=['POST'])
def add_student():
    if request.method != 'POST':
        return redirect(url_for('admin.show_admin'))
    student_id = int(request.form.get('student-id'))
    student_name = request.form.get('student-name')
    branch = int(request.form.get('branch-id'))
    student = Student.query.get(student_id)
    if student:
        flash('Student already exists.', 'error')
        return redirect(url_for('admin.show_admin'))
    student = Student(student_id=student_id, name=student_name, branch=branch)
    db.session.add(student)
    db.session.commit()
    flash('Student added successfully.','success')
    return redirect(url_for('admin.show_admin'))

# TO REMOVE STUDENT
@admin_bp.route('/admin/remove-student', methods=['POST'])
def remove_student():
    if request.method == 'GET':
        return redirect(url_for('admin.show_admin'))
    student_id = request.form.get('student-id-to-remove')
    student = Student.query.get(student_id)
    if student:
        db.session.delete(student)
        db.session.commit()
        flash('Student removed successfully.', 'success')
        return redirect(url_for('admin.show_admin'))
    else:
        flash("Student not found.", 'error')
    return redirect(url_for('admin.show_admin'))

# TO CHECK STUDENT IS INVOLVED  IN ANY TRANSACTIONS
@admin_bp.route('/admin/is-student-free/<int:student_id>', methods=['GET'])
def is_student_free(student_id):
    student = Student.query.get(student_id)
    if student.book_limit == 2:
        return jsonify({'free': True})
    else:
        return jsonify({'free': False})
