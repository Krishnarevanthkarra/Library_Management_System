from flask import Flask, session, redirect, url_for, sessions
from config import Config
from routes.login import login_bp
app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(login_bp, url_prefix='/')
@app.route('/')
def index():
    #if 'user' in session:
    #    return redirect(url_for('home'))
    return redirect(url_for('login.login'))

if __name__ == '__main__':
    app.run(debug=True)
