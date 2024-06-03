# creating somple flask applicateion
from flask import Flask, render_template, request, redirect, url_for


# creating constructor
app = Flask(__name__)


# we will use decorators to cerate different pages in app
@app.route('/')
def home():
    return "<p>Hello, World!</p>"

@app.route('/welcome')
def welcome():
    return "<h1>Welcome to flask webapp!</h1>"

@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/success/<int:score>')
def success(score):
    return "The person is passed and score is " + str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person is failed and score is " + str(score)

@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == "GET":
        return render_template('calculate.html')
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])
        average_marks = (maths+science+history)/3

        result = ""
        if average_marks > 50:
            result='success'
        else:
            result='fail'
        # return redirect(url_for(result, score=average_marks)) # if want a link to show with use thi method
        return render_template('result.html', result=average_marks) # if we can same page and update it this is the way

@app.route('/calculatemarks')
def calculatemarks():
    return render_template('calculate.html')


# main entry point
if __name__ == "__main__":
    app.run(debug=True
            )

