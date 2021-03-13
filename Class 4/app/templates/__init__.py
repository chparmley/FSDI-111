from flask import Flask
from flask_sqlalchemy import flask_sqlalchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)
Bootstrap(app)

from app import routes
from app.database import *