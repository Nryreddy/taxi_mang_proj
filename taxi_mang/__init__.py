from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:5500@localhost/taxi_management_db'
app.config['SECRET_KEY'] ='d3074feb89d17432bf49c34a'   # >>> import os    >>> os.urandom(12).hex()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager()

from taxi_mang import routes
