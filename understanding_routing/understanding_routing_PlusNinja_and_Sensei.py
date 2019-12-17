from flask import Flask 
print("Starting our hello flask SERVER file .... with name....")
print(__name__)             #

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')
def dojo():
    return 'dojo'  

@app.route('/say/<something>')
def say_something(something):
    return f' Hi {something} !'


@app.route('/repeat/<int:times>/<string:something>')
def say_something_manytimes(times=3, something="lightblue"):
    t = int(times)
    s = f"{something} "
    return s * t

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "Sorry! No response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.