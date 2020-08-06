
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key='Bereketsworld'
    if 'key_name' in session:
    print('key exists!')
    else:
    print("key 'key_name' does NOT exist")

@app.route('/')
def index():
    return render_template("Dojosurvey.html")


@app.route('/destroy_session', methods =['POST'])
def user_result():
    name = request.form['your_name']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    print (name, location, language, comment)
    return render_template("submittedinfo.html", name=request.form['your_name'], location=request.form['location'], language = request.form['language'], comment = request.form['comment'])

if __name__ == "__main__":
    app.run(debug=True)