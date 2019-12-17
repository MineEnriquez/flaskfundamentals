# from flask import Flask, render_template, request, redirect # added request
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


# ROOT
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
#END OF ROUTE

# USERS- the form requesting this page should be sending the information listed below.
# REQUEST - handles the information from the ORIGINATOR 
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    # name_from_form = request.form['name']
    # email_from_form = request.form['email']
    # return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)   # changed this line!

    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

# adding this method after the redirect has happened
@app.route("/show")
def show_user():
    print("Redirected here...")
    print("Showing the User Info From the Form")
    print(request.form)
    # return render_template("show.html")
    return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])

if __name__ == "__main__":
    app.run(debug=True)
