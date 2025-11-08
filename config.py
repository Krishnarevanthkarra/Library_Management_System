import secrets
from dotenv import load_dotenv
import os

load_dotenv()

dbusername = os.getenv('dbusername')
dbpassword = os.getenv('dbpassword')
dbhost = os.getenv('host')
dbname = os.getenv('dbname')

class Config:
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{dbusername}:{dbpassword}@{host}/{dbname}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/Images/book_covers'
