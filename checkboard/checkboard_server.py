# imports
from flask import Flask, render_template

# global variables
app = Flask(__name__)

# start
print("Starting our playground application ..........")
print(__name__)


# ROOT
#  Have the root route render a template with a checkerboard on it
@app.route('/')
def default():
    return render_template("default.html", rows=int(5), cols=int(5), color1="red", color2="black", squaresize=int(100))


#  Have the css in a separate stylesheet and link this to the template
#  Have another route accept a single parameter (i.e. "/<x>") and render a checkerboard with x many rows, with alternating colors

# #  NINJA BONUS: Have another route accept 2 parameters (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns, with alternating colors
# @app.route('/play/<int:rows>/<int:columns>')
@app.route('/customsize/<int:x>/<int:y>')
def customsize(x, y):
    return render_template("default.html", rows=x, cols=y, color1="purple", color2="black", squaresize=int(1000/y))

# def render_play(rows, columns):
#     return render_template("xxxx.html", rows=rows, columns=columns)
# # EOM render_play
# #  SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2
@app.route('/customfull/<int:x>/<int:y>/<color1>/<color2>')
def customfull(x, y, color1, color2):
    return render_template("default.html", rows=x, cols=y, color1=color1, color2=color2, squaresize=int(1000/y))



# Stars the server
if __name__ == "__main__":
    app.run(debug=True)
# EOF

