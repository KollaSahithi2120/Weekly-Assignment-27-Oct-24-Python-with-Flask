"""2. Personal Bio Page
 Task: Design a simple personal bio page.
 Requirements: Add a route (/bio) with basic information like name, age, and
hobbies displayed in HTML.
 Hint: Use Flask&#39;s render_template function and create a basic HTML file to display
personal details."""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/bio')
def bio():
    personal_info = {
        'name': 'Sahithi Kolla',
        'email': 'kollasahithi2120@gmail.com',
        'phone': '+91 8074951188',
        'linkedin': 'Kolla Sahithi',
        'github': 'KollaSahithi2120',
        'education': [
            {'degree': 'B.Tech in CSE (AIML)', 'institution': 'VNRVJIET', 'year': '2021-2025', 'cgpa': '8.9/10'},
            {'degree': 'Class XII', 'institution': 'Sri Chaitanya Junior College', 'year': '2019-2021', 'percentage': '98.2%'},
            {'degree': 'Class X', 'institution': 'Sri Chaitanya School', 'year': '2018-2019', 'percentage': '96.6%'}
        ],
        'technical_skills': {
            'languages': ['C', 'Python', 'Java', 'R'],
            'technologies': ['Artificial Intelligence', 'Machine Learning', 'HTML', 'CSS', 'React', 'JavaScript'],
            'concepts': ['Data Structures and Algorithms', 'Operating Systems', 'SQL', 'Computer Networks', 'Data Engineering'],
            'tools': ['MS Excel', 'Word', 'PowerPoint', 'StarUML', 'Canva']
        },
        'projects': [
            {'title': 'Sentiment Analysis on Twitter Data', 'description': 'Developed a sentiment analysis project using lemmatization and Random Forest for improved accuracy.'},
            {'title': 'Explainable Sexual Harassment Categorization', 'description': 'Built a model to categorize online sexual harassment using explainable AI techniques.'},
            {'title': 'Chronic Disease Management', 'description': 'Created a web app named WELLNEXA for managing chronic diseases, leveraging front-end and back-end development.'},
            {'title': 'Face Mask Detection', 'description': 'Developed a dataset and model for face mask detection using image processing and neural networks.'}
        ],
        'certifications': [
            'Machine Learning Specialization by Andrew Ng (Coursera)',
            'Python Proficiency Certificate (HackerRank)',
            'Web Development Certification',
            'Agile Methodology Virtual Experience Program (Cognizant)'
        ],
        'strengths': ['Articulate communicator', 'Leadership skills', 'Innovative', 'Attention to detail', 'Management skills', 'Community engagement'],
        'hobbies': ['Reading', 'Baking', 'Badminton'],
        'achievements': [
            'Top 10% academic performer within branch',
            'Panel discussion on “Transforming the mindset of engineering students: Preparing for a future shaped by AI”',
            'Organized Google Solution Challenge on the UN’s Sustainable Development Goals',
            'Member of CSI, KRITHOMEDH, and NSS'
        ]
    }
    return render_template('bio.html', info=personal_info)

if __name__ == '__main__':
    app.run(debug=True)
