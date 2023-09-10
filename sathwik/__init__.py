from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask.config import Config
import os

app = Flask(__name__)
app.config['SECRET_KEY']='sath10hemu15prab17'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config.from_object(Config)
with app.app_context():
    db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

mail=Mail(app)
from sathwik.users.routes import users
from sathwik.posts.routes import posts
from sathwik.main.routes import main
from sathwik.errors.handlers import errors
app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)
app.register_blueprint(errors)