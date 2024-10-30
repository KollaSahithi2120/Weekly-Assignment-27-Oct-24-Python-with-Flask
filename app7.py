""""8. Feedback Form
 Task: Make a feedback form that saves users&#39; names and feedback temporarily.
 Requirements: Save the submitted feedback to a list and display the list on the same
page.
 Hint: Use Python lists or dictionaries to store each feedback entry, and display
feedback history at the bottom of the page."""

from flask import Flask, render_template, request

app = Flask(__name__)
feedback_list = []

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        branch = request.form.get('branch')
        roll_number = request.form.get('roll_number')
        liked = request.form.get('liked')
        improvements = request.form.get('improvements')
        next_sessions = request.form.get('next_sessions')
        drawback = request.form.get('drawback')
        
        feedback_list.append({
            'name': name,
            'branch': branch,
            'roll_number': roll_number,
            'liked': liked,
            'improvements': improvements,
            'next_sessions': next_sessions,
            'drawback': drawback
        })
    
    return render_template('feedback.html', feedback_list=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)
