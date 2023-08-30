from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html')


@app.route("/save")
def saveTheDate():
    return "Babe"

if __name__ == '__main__':
    app.run(debug=True)