from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [
    {
        'author':'Pythagorasweb',
        'title': 'Love kills',
        'content': 'Be careful',
        'date_posted': 'May 12, 2023'
    },
    {
        'author':'Pythagorasweb',
        'title': 'Love is good',
        'content': 'Follow your heart',
        'date_posted': 'May 12, 2023'
    }
]

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)