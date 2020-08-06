from flask import Flask
app = Flask(__name__)

@app.route('/') 
def hello_world():
    return "Hello World"

@app.route('/Dojo')
def show_Dojo_stuff():
    return "Dojo"

@app.route('/say/<name>')
def show_hi_stuff(name):
    return f"Hi {name}"

@app.route('/repeat/<int:num>/<word>')
def repeatsomestuff(num, word):
    return word*num

if __name__ == "__main__":
    app.run(debug= True)