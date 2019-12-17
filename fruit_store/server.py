from flask import Flask, render_template, request, redirect  # added request
import datetime
app = Flask(__name__)

# ROOT
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# END OF ROUTE

# USERS- the form requesting this page should be sending the information listed below.
# REQUEST - handles the information from the ORIGINATOR
@app.route('/checkout', methods=['POST'])
def checkout():
    print("Got Post Info")
    print(request.form)
    dic = {'01':'st','21':'st','31':'st', '02':'nd','22':'nd','03':'rd','23':'rd'}

    strawberry_qty_incoming = request.form['strawberry_qty']
    raspberry_qty_incoming = request.form['raspberry_qty']
    apple_qty_incoming = request.form['apple_qty']
    name_incoming = request.form['name']
    studentid_incoming = request.form['studentid']
    transaction_time = datetime.datetime.now().strftime('%B %d')
    transaction_time =  transaction_time + dic.get(transaction_time[-2:],'th')
    transaction_time =  transaction_time + datetime.datetime.now().strftime(' %Y %I:%M:%S %p')
    total_items = int(strawberry_qty_incoming) + int(raspberry_qty_incoming) + int(apple_qty_incoming)
    return render_template("checkout.html", strawberry_qty=strawberry_qty_incoming, raspberry_qty=raspberry_qty_incoming, apple_qty=apple_qty_incoming, name=name_incoming, studentid=studentid_incoming, transaction_time=transaction_time , total_items=total_items)

if __name__ == "__main__":
    app.run(debug=True)
