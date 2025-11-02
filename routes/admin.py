from flask import Blueprint, render_template, request, flash, url_for, redirect
from models.author import Author
from models import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
def show_admin():
    return render_template('admin.html')

@admin_bp.route('/addauthor', methods=['POST'])
def add_author():
    if request.method == 'GET':
        return redirect(url_for('admin.show_admin'))
    name = request.form['authorname']
    about = request.form['aboutauthor']
    print(name, about)
    new_author = Author(author_name=name, about_author=about)
    db.session.add(new_author)
    db.session.commit()
    print(new_author)
    flash('Added the Author successfully.', 'info')
    return redirect(url_for('admin.show_admin'))