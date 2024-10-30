"""5. Random Quote Generator
 Task: Create an app that displays a random motivational quote from a predefined list
each time the page is refreshed.
 Requirements: Display one random quote from a list of quotes every time the user
visits the /quote page.
 Hint: Use Python’s random.choice() to select a quote from a list and display it
using HTML."""

from flask import Flask, render_template
import random

app = Flask(__name__)
quotes = [
    "Success usually comes to those who are too busy to be looking for it.",
    "Don’t watch the clock; do what it does. Keep going.",
    "If you’re going through hell, keep going.",
    "What seems to us as bitter trials are often blessings in disguise.",
    "The best revenge is massive success.",
    "The road to success and the road to failure are almost exactly the same.",
    "Don’t wait for the perfect moment; take the moment and make it perfect.",
    "Motivation is what gets you started. Habit is what keeps you going.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "The only way to achieve the impossible is to believe it is possible.",
    "What we fear of doing most is usually what we most need to do.",
    "The only limit to our realization of tomorrow is our doubts of today.",
    "Don’t wait for opportunity. Create it.",
    "Push yourself, because no one else is going to do it for you.",
    "Good things come to those who hustle.",
    "Success doesn’t just find you; you have to go out and get it.",
    "Keep going, your hardest times often lead to the greatest moments of your life.",
    "Dream it. Believe it. Build it.",
    "What defines us is how well we rise after falling.",
    "Believe you can and you’re halfway there.",
    "It’s not about perfect. It’s about effort.",
    "You don’t have to be perfect to be amazing.",
    "The only place where success comes before work is in the dictionary.",
    "Believe in yourself and all that you are.",
    "The future depends on what you do today.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "Sometimes later becomes never. Do it now.",
    "Success is not for the lazy.",
    "If it doesn’t challenge you, it won’t change you.",
    "Great things never come from comfort zones."
]


@app.route('/quote')
def quote():
    selected_quote = random.choice(quotes)
    return render_template('quote.html', quote=selected_quote)

if __name__ == '__main__':
    app.run(debug=True)
