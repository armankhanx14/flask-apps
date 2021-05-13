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
    all_todos = Todos.query.all()
    todos_string = ""
    for todo in all_todos:
        todos_string += "<br>" + str(todo.id) + todo.task + str(todo.complete)
    return "todo string"

@app.route("/add")
def add():
    new_todo = Todos(task="New Todo")
    db.session.add(new_todo)
    db.session.commit()
    return "added a new todo"

@app.route("/complete/<int:todo_id>")
def complete(todo_id):
    todo = Todos.query.get(todo_id)
    todo.complete = True
    db.session.commit()
    return "completed todos"

@app.route("/incomplete/<int:todo_id>")
def complete(todo_id):
    todo = Todos.query.get(todo_id)
    todo.complete = False
    db.session.commit()
    return "incompleted todos"

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todos.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')