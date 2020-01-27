from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    todo = StringField('Todo', render_kw={"placeholder": "Todo"}, validators=[DataRequired()])
    submit_todo = SubmitField('Add Todo')