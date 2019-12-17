# Make sure that the correct virtual environment is active, in which Flask is installed (see the installation chapter).
# Create an empty folder inside python_stack/flask/flask_fundamentals/ called "hello_flask".
#       This will be our project folder and the root directory for all of the files that we use to create the project.
# Inside the "hello_flask" folder, create a file called hello.py
#       This will be our "SERVER" file where we will set up all of our routes to handle requests.
#       You'll want to create a new folder for each assignment moving forward. It will seem tedious at first, but as we add additional files to each project, we'll want to keep everything organized by assignment/project!
# Finally, put the following code inside of hello.py:

# SERVER FILE: hello.py

# Import Flask to allow us to create our app
from flask import Flask, render_template
print("Starting our hello flask SERVER file .... with name....")
print(__name__)             # All files have the propety called "name"
# Create a new instance of the Flask clas scalled "app"
app = Flask(__name__)

# ROOT
# The "@" decorator associates this route with th efunction immediate following (right under the "@app.route('/')" statement) . You must do this for every route that you want to add to our application.
@app.route('/')
def index():
    return render_template("index.html", phrase="hello", times=5)
# SUCCESS
@app.route('/success')
def success():
    return "success"

# HELLO/NAME
# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name


# for a route '/users/____/____', two parameters in the url get passed as username and id
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)

    return f"Wsername: {username}, id: {id}"


# LISTS
@app.route('/lists')
def render_list():
    # Entering data manually while we don't have a connection to a database
    # this is an array of dictionaries.
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)

if __name__ == "__main__":        # enrure this file is being run directly and not from a different module
    app.run(debug=True)     # Run the app in debug mode
