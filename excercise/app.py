
from flask import Flask

app = Flask(__name__)

@app.route('/')       ##same
@app.route('/home')   ##same
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/about/<number>')
def about_number(number):
    return 'This is the about page ' + str(number)


if __name__=='__main__':    ##at the end becuase you defined functions before it 
    app.run(debug=True)

