""" 1. Hello Flask Website
 Task: Create a simple &quot;Hello, World!&quot; Flask application.
 Requirements: Make a single route (/) that displays “Hello, Flask!” on a web page.
 Hint: Start by setting up a basic Flask app with a single route. Use app.route() to
set the URL path."""

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_flask():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
