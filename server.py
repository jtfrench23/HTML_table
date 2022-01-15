# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def html_table():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi', 'full_name': 'Michael Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin', 'full_name': 'John Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen', 'full_name': 'Mark Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel', 'full_name': 'KB Tonel'}
    ]

    return render_template('index.html', table=users)


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
