"""7. Image Gallery
 Task: Create a simple gallery page that displays three static images.
 Requirements: Display three images side by side on a page.
 Hint: Use HTML &lt;img&gt; tags in your HTML template and store the images in a
/static folder in the project."""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)
