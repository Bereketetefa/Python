from flask import Flask, render_template, session, redirect, request
import random


app = Flask(__name__)
app.secret_key = "bereket world"

@app.route('/')
def index():
    randomNumber = random.randint(1,100)
    if 'randomNum' not in session:
        session['randomNum'] = randomNumber
    if 'userguess' not in session:
        session['userguess'] = False
    
    return render_template("numbergame.html", randomnum = session 
    ['randomNum'], userguess = session['userguess'])

@app.route('/guess', methods = ['POST'])
def guess():
    print (request.form['userguess'])
    session ['userguess'] = int(request.form['userguess'])

    return redirect("/")

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)