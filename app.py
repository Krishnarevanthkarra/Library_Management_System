from flask import Flask, session, redirect, url_for, sessions
from config import Config
from routes import *
from models import db
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(login_bp, url_prefix='/')
app.register_blueprint(books_bp, url_prefix='/')
app.register_blueprint(transactions_bp, url_prefix='/')
app.register_blueprint(admin_bp, url_prefix='/')

db.init_app(app)

with app.app_context():
    db.create_all()
@app.route('/')
def index():
    return redirect(url_for('login.login'))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080",debug=True)