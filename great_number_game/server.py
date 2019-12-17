from flask import Flask, render_template, request, redirect, session
import random
# FLASK VARIABLES
app = Flask(__name__)

# SESSION SECRET
# set a secret key for security purposes
app.secret_key = 'keep it secret, keep it safe'

# ROOT
@app.route('/')
def index():
    print("starting the game")
    reset()
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def guess():
    x = session['random']
    print("Random: " + str(x))
    guess_incoming = request.form.get('guess', type=int)
    print("Guess: " + str(guess_incoming))
    if guess_incoming == None:
        guess_incoming = 0

    if x > guess_incoming:
        print('too low')
        session['color'] = "red"
        session['succeeded'] = 0
        session['message'] = str(guess_incoming) + " Too low!!"
    elif x == guess_incoming:
        print("Same!!")
        session['color'] = "green"
        session['succeeded'] = 1
        session['message'] = str(session['random']) + " was the number!!"
    else:
        session['color'] = "red"
        session['succeeded'] = 0
        session['message'] = str(guess_incoming) + " Too high!!"
        print("too high")

    return render_template('index.html')


@app.route('/reset', methods=['POST'])
def reset():
    if 'random' in session:
        print('clearing random number')
        session.clear()
        session['random'] = random.randint(1, 100)
        session['succeeded'] = -1
        session['message'] = ""
        print(str(session['random']))
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
