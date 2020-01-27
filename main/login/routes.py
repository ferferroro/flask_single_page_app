from flask import Blueprint, render_template, g, redirect, url_for
from main.login.models import User
from main.login.forms import LoginForm
import flask_sijax
from main import app
from flask_login import LoginManager, login_user

# instantiate
login_manager = LoginManager()
login_manager.init_app(app)

# user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

login_route = Blueprint('login_route', __name__)

@flask_sijax.route(login_route, '/')
def login():

    def sijax_login_function(obj_response, login_form):

        form = LoginForm(data=login_form)
        form.validate()

        # check if error 
        if form.username.errors:
            obj_response.html('#username_error', ','.join(form.username.errors))
        if form.password.errors:
            obj_response.html('#password_error', ','.join(form.password.errors))

        # chekc if valid user
        existing_user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

        if existing_user:
            login_user(existing_user)
            obj_response.redirect(url_for('todo.todo'))
        else:
            obj_response.html('#submit_login_error', 'Sorry! invalid account!')

    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_login', sijax_login_function)
        return g.sijax.process_request()
    else:
        form = LoginForm()
        return render_template('login/login.html', form=form)