from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', render_kw={"placeholder": "Username"}, validators=[DataRequired()])
    password = StringField('Password', render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    submit_login = SubmitField('Login')