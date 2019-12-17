# Import Flask to allow us to create our app
from flask import Flask, render_template
print("Starting our hello flask SERVER file .... with name....")
print(__name__)             # All files have the propety called "name"
# Create a new instance of the Flask clas scalled "app"
app = Flask(__name__)

# ROOT
# The "@" decorator associates this route with th efunction immediate following (right under the "@app.route('/')" statement) . You must do this for every route that you want to add to our application.
@app.route('/')
def render_list():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template("lists.html", users=users)

if __name__ == "__main__":        # enrure this file is being run directly and not from a different module
    app.run(debug=True)     # Run the app in debug mode
