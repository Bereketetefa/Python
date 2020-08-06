from flask import Flask, render_template
app = Flask(__name__)

@app.route("/play") 
def hello_world():
    return render_template('playground.html')

@app.route("/play/<number>/<color>")
def play(number, color):
    return render_template("playground.html", num=int(number), change=color)

if __name__ == "__main__":
    app.run(debug=True)