from flask import Blueprint, request, render_template,  flash, redirect, url_for, session
import os
login_bp = Blueprint('login', __name__, url_prefix='')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('loginPage.html')
    name = request.form['name']
    password = request.form['password']
    if name and password:
        if os.getenv('ADMIN_USERNAME') == name and os.getenv('ADMIN_PASSWORD') == password:
            session['user'] = name
            return redirect(url_for('books.show_books'))
    flash("Invalid username or password", "error")
    return render_template('loginPage.html')

@login_bp.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login.login'))
