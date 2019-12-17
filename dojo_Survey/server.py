from flask import Flask, render_template, request, redirect  # added request
app = Flask(__name__)

# ROOT
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# END OF ROUTE

# USERS- the form requesting this page should be sending the information listed below.
# REQUEST - handles the information from the ORIGINATOR
@app.route('/result', methods=['POST'])
def submit_survey():
    print("Got Post Info")
    print(request.form)
    name_incoming = request.form['name']
    dojo_location_incoming = request.form['dojo_location']
    favorite_language_incoming = request.form['favorite_language']
    favorite_stack_incoming_list = request.form.getlist('stack')
    favorite_stack_incoming = ', '.join(favorite_stack_incoming_list)
    program_incoming = request.form['program']
    comments_incoming = request.form['comments']
    return render_template("show.html", name=name_incoming, dojo_location=dojo_location_incoming, favorite_language=favorite_language_incoming, favorite_stack=favorite_stack_incoming, comments=comments_incoming, program=program_incoming)


if __name__ == "__main__":
    app.run(debug=True)
