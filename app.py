from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Config)

login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'you must login to acess this page'
login.login_message_category = 'info'