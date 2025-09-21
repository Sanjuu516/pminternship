# app.py

from flask import Flask, jsonify

# 1. Initialize the Flask application
app = Flask(__name__)

# 2. Define a route and its corresponding view function
@app.route('/')
def home():
    """This is the home endpoint."""
    return "Welcome to the Flask Backend!"

@app.route('/api/data')
def get_data():
    """This endpoint returns some sample JSON data."""
    sample_data = {
        'id': 1,
        'name': 'Sample Item',
        'description': 'This is a piece of sample data from the API.'
    }
    return jsonify(sample_data)

# 3. Run the application
if __name__ == '__main__':
    # The debug=True argument allows for auto-reloading when you save changes.
    # Do not use debug=True in a production environment.
    app.run(debug=True)