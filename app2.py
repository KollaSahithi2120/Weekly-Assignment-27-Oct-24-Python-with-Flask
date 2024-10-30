"""3. Calculator App
 Task: Build a simple calculator that can add two numbers.
 Requirements: Create a form where users enter two numbers. Display the result on
submission.
 Hint: Use HTML forms and handle data in Flask using the request.form method to
get the inputs."""

from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            result = num1 + num2
        except ValueError:
            result = "Invalid input. Please enter numbers only."

    return render_template('calculator.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
