# from flask import Flask, render_template, request, redirect # added request
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def index():
    if 'totalvisits' in session:
        print('totalvisits key exists!')
        session['totalvisits'] += 1
    else:
        print("key 'totalvisits' does NOT exist")
        session['totalvisits'] = 1
    return render_template('index.html', totalvisits=session['totalvisits'])

@app.route('/add', methods=['POST'])
def add():
    print('trying to add more visits..........')
    x = request.form.get('increment', type=int)
    if 'totalvisits' in session:
        print(session['totalvisits'] + x )
        session['totalvisits'] += x
    else:
        print("key 'totalvisits' does NOT exist. Will set the value to 1.")
        session['totalvisits'] = 1

    return render_template('index.html', totalvisits=session['totalvisits'])



@app.route('/reset', methods=['POST'])
def delete():
    if 'totalvisits' in session:
        print('totalvisits key exists!')
        session.clear()
    #return render_template('index.html')
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
