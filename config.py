import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback_secret')
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:krishna%402004@localhost/library"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'static/Images/book_covers'