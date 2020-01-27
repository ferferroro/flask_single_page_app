# imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_sijax
import os

# instantiate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/flask_spa_db_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'seretolangto'
path = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax')
app.config['SIJAX_STATIC_PATH'] =  path
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'
# db
db = SQLAlchemy(app)
migrate = Migrate(app, db)
flask_sijax.Sijax(app)

from main.login.routes import login_route
app.register_blueprint(login_route)

from main.todo.routes import todo_route
app.register_blueprint(todo_route)