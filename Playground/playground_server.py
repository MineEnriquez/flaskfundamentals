# imports
from flask import Flask, render_template

# global variables
app = Flask(__name__)

# start
print("Starting our playground application ..........")
print(__name__)

# ROOT
@app.route('/')
def index():
    return "Hello"

# Route: PLAY
@app.route('/play/<int:times>/<color>')
def render_play(times, color):
    return render_template("play.html", times=times, color=color)
# EOM render_play


# Stars the server
if __name__ == "__main__":
    app.run(debug=True)
# EOF
