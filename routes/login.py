from flask import Blueprint, request, render_template, session, flash, redirect, url_for
import os
login_bp = Blueprint('login', __name__, url_prefix='')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    print('Hello, this is login')
    #if 'user' in session:
    #   return redirect(url_for('home'))
    if request.method == 'GET':
        return render_template('loginPage.html')
    name = request.form['name']
    password = request.form['password']
    if name and password:
        if os.getenv('ADMIN_USERNAME') == name and os.getenv('ADMIN_PASSWORD') == password:
            print('Authentication successful')
            session['user'] = name
            return redirect(url_for('books.show_books'))
    flash("Invalid username or password", "error")
    return render_template('loginPage.html')

