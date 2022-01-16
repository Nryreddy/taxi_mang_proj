from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:5500@localhost/taxi_management_db'
app.config['SECRET_KEY'] = 'd3074feb89d17432bf49c34a'  # >>> import os    >>> os.urandom(12).hex()
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'owner_login_page'
login_manager.login_view = 'customer_login_page'
login_manager.login_message_category = 'info'

from taxi_mang import routes
