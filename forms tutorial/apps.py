from flask import Flask, render_template, request, render_template
from flask_wtf import FlaskForm
from wtforms import  SubmitField, StringField, DateField, IntegerField, DecimalField, SelectField

app = Flask(__name__)

app.config["SECRET_KEY"] = "arman"

class BasicForm(FlaskForm):
    first_name = StringField("First Name")
    last_name = StringField("Last Name")
    date_of_birth = DateField("DOB", format="%d/%m/%Y")
    age = IntegerField("Age")
    salary = DecimalField("Salary", places=2)
    fave_food = SelectField("Favourite Food", choices=[("Indian","Indian"),("Fish and Chips", "Fish and Chips"),("Pizza, Pizza")])
    submit = SubmitField("Add Name")

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def register():
    error = ""
    form = BasicForm()

    if request.method == "POST":
        first_name = form.first_name.data
        last_name = form.last_name.data

    if len(first_name) == 0 or len(last_name) == 0:
        error = "Please supply both first and last name"
    else:
        return "thank you"

    return render_template("home.html", form=form, message=error)    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")