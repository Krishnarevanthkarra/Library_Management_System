from flask import Blueprint, request, render_template, session, redirect, url_for, flash
import os
login_bp = Blueprint('login', __name__, url_prefix='')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    print('Hello, this is login')
    #if 'user' in session:
    #   return redirect(url_for('home'))
    if request.method == 'GET':
        return render_template('login.html')
    name = request.form['name']
    password = request.form['password']
    if name and password:
        if os.getenv('ADMIN_USERNAME') == name and os.getenv('ADMIN_PASSWORD') == password:
            session['user'] = name
            return render_template('books.html')
    flash("Invalid username or password", "error")
    return render_template('login.html')

