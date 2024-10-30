"""10. Temperature Converter
 Task: Create a simple temperature converter that converts Celsius to Fahrenheit.
 Requirements: Allow users to enter a Celsius value and display the converted
Fahrenheit value.
 Hint: Use forms for input, request.form to get the Celsius value, and simple
arithmetic in Python to calculate the Fahrenheit temperature."""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/convert', methods=['GET', 'POST'])
def convert_temperature():
    fahrenheit = None
    if request.method == 'POST':
        celsius = request.form.get('celsius')
        if celsius:
            fahrenheit = (float(celsius) * 9/5) + 32
    return render_template('temperature.html', fahrenheit=fahrenheit)

if __name__ == '__main__':
    app.run(debug=True)
