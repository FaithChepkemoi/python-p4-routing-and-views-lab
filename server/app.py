#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Prints to console
    return param  # Displays in browser

@app.route('/count/<int:param>')
def count(param):
    numbers = [str(i) for i in range(param)]
    return '\n'.join(numbers) + '\n'  # Append a newline at the end

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Invalid number input", 400

    operations = {
        '+': num1 + num2,
        '-': num1 - num2,
        '*': num1 * num2,
        'div': num1 / num2 if num2 != 0 else "Error: Division by zero",
        '%': num1 % num2 if num2 != 0 else "Error: Modulo by zero"
    }

    result = operations.get(operation)
    if result is None:
        return "Invalid operation", 400
    
    # Convert to integer if result is a whole number, except for division
    if isinstance(result, float) and result.is_integer() and operation != 'div':
        result = int(result)
    
    return str(result)


if __name__ == '__main__':
    app.run(debug=True)
