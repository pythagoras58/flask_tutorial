from flask import Flask
from flask import render_template, flash, redirect
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


@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account Created For {form.username.data}', 'success')
        return redirect(url_for('index'))

    return render_template('register.html', title='Sign Up', form=form)


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)