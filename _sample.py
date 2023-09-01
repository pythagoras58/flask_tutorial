from flask import Flask
from flask import render_template
from forms import RegistrationForm, LoginForm
from flask import url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = 'f8d84fffc14df51ff6c5011166494244' # import secret, secret.token_hex(16)

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
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)