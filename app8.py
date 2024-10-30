"""9. Basic Data Table with Jinja
 Task: Display a table of users and their details (name, age, city).
 Requirements: Use a predefined list of dictionaries and render it in an HTML table.
 Hint: Use Jinja templating with for loops to iterate over the list and display the data
in a table format."""

from flask import Flask, render_template

app = Flask(__name__)
users = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 22, "city": "Chicago"},
    {"name": "Diana", "age": 27, "city": "Houston"},
    {"name": "Elijah", "age": 32, "city": "New Orleans"},
    {"name": "Freya", "age": 28, "city": "Mystic Falls"},
    {"name": "Gina", "age": 36, "city": "Brooklyn"},
    {"name": "Harry", "age": 47, "city": "Paradise Valley"},
    {"name": "Inadu", "age": 37, "city": "Washington"},
]

@app.route('/users')
def user_table():
    return render_template('table.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)
