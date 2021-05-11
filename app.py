'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return "Hello Internet!"

@app.route('/')
@app.route('/home')
def home():
    return 'this is home page'


if __name__=='__main__':
    app.run(debug=True)

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)