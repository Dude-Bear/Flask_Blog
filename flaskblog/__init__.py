from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# secret key to protect modefying cookies, ...
app.config['SECRET_KEY'] = '45abf140032ed87b92351aa9399b2751'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog import routes