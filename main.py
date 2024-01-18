 
# main.py

# Import necessary libraries
from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    """
    Renders the main page of the application.
    """
    return render_template('index.html')

# Define the results route
@app.route('/results', methods=['POST'])
def results():
    """
    Processes the user's input and displays the results.
    """

    # Get the user's input
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    level = request.form.get('level')
    duration = request.form.get('duration')

    # Generate the results
    results = {
        'name': name,
        'email': email,
        'subject': subject,
        'level': level,
        'duration': duration
    }

    # Render the results page
    return render_template('results.html', results=results)

# Run the app
if __name__ == '__main__':
    app.run()
