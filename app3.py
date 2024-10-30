"""4. Mini To-Do List
 Task: Create a basic to-do list web app where users can add tasks.
 Requirements: Implement a form to add tasks and display the tasks on the same
page.
 Hint: Use a list to store tasks temporarily and a POST method to add new tasks to the
list."""

from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tasks = []

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = {
            'id': len(tasks) + 1,  
            'content': task_content
        }
        tasks.append(new_task)
        return redirect('/')
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    global tasks
    tasks = [task for task in tasks if task['id'] != id]
    return redirect('/')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = next((task for task in tasks if task['id'] == id), None)

    if not task:
        return "Task not found"

    if request.method == 'POST':
        task['content'] = request.form['content']
        return redirect('/')

    return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)
