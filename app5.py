"""6. Simple Login Page
 Task: Build a basic login form with username and password fields.
 Requirements: Display a welcome message if the username is “user” and the
password is “password.”

 Hint: Use POST requests and if statements to check login credentials."""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'user' and password == 'password':
            return redirect(url_for('welcome'))
        else:
            return render_template('login.html', error="Invalid username or password.")
    
    return render_template('login.html')

@app.route('/welcome')
def welcome():
    return "<h1>Welcome!</h1>"

if __name__ == '__main__':
    app.run(debug=True)
