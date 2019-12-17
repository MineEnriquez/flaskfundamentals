from flask import Flask, render_template, request, redirect, session
import random
import datetime
# FLASK VARIABLES
app = Flask(__name__)

# SESSION SECRET
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe'

# ROOT
@app.route('/')
def index():
    print("starting the game")
    session['activities'] = ""
    session['total_gold'] = 0
    reset()
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
    print("starting processing some money...") 

    now= datetime.datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')
    color = "green"
    min = request.form.get('min', type=int)
    max = request.form.get('max', type=int)
    x= random.randint(min, max)
    transaction = ""

    if x<0:
        color = "red"
        transaction = "Lost"
    else:
       color = "green"
       transaction = "Earned"

    message="<li style=\"color: "+ color +";\">" + transaction + " "+ str(x) +" golds for the farm ("+ now +")</li>" 
    print(message)
    session['total_gold'] = session['total_gold'] + x
    session['activities']  = message + session['activities']
    return render_template('index.html', message=session['activities'] )


@app.route('/reset')
def reset():
    if 'total_gold' in session:
        print('clearing random number')
        session.clear()
        session['total_gold'] = 0
        session['activities'] =""
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
