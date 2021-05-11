from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@35.223.241.119:3306/todos"

db = SQLAlchemy(app)

class Todos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(50), nullable=False)
    complete = db.Column(db.Boolean, default=False)

@app.route("/")
def index():
    return "This is a TODO App"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')