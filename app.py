from flask import Flask, session, redirect, url_for, sessions, request, render_template, flash
from config import Config
from routes import *
from models import *
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(login_bp, url_prefix='/')
app.register_blueprint(books_bp, url_prefix='/')
app.register_blueprint(views_bp, url_prefix='/')
app.register_blueprint(admin_bp, url_prefix='/')

db.init_app(app)

with app.app_context():
    db.create_all()
    branches = ['Computer Science', 'Information Technology',
            'Data Science', 'AIML', 'Mechanical', 'Civil']
    for branch in branches:
        db.session.add(models.Branch(branch_name=branch))
        db.session.commit()

@app.before_request
def check_login():
    allowed_routes = ['login.login', 'static']  # Add more if needed
    endpoint = request.endpoint
    if 'user' not in session and endpoint not in allowed_routes:
        return redirect(url_for('login.login'))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080",debug=True)
