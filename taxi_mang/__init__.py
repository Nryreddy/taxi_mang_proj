from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taxi_management_db.db'
db = SQLAlchemy(app)

from taxi_mang import routes
