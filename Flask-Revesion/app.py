from flask import Flask,request,render_template

obj = Flask(__name__)


@obj.route('/')
def welcome():
    return "Welcome to the Flask"

@obj.route('/cal', methods=["GET", "POST"])
def math_operator():
    operation = request.json["operation"] # written json cause we are going to request using postman
    number1 = request.json["number1"]
    number2 = request.json["number2"]

    if operation == "add":
        result = number1+number2
    elif operation == "sub":
        result = number1 - number2
    elif operation == "mul":
        result = number1*number2
    elif operation == "div":
        result = number1 / number2
    else:
        result = "Please select valide opeartion!"
    return result

print(__name__)

if __name__ == "__main__":
    obj.run(debug=False)