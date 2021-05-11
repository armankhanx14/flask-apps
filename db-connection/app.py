from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@94.6.145.219:3306/flask_exteral"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
    