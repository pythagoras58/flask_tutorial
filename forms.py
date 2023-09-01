from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

# form for registration
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Sign Up')



# form for login
class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired(), Length(min=5)])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Sign In')
