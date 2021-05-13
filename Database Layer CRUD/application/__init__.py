from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  ##create app object

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

from application import routes  ##goes at bottom because of the routes