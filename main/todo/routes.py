from flask import Flask, Blueprint, render_template, g, redirect, url_for, flash
from main.todo.models import Todo
from main.todo.forms import TodoForm
import flask_sijax
from flask_login import login_required
from main import db

todo_route = Blueprint('todo', __name__)

@flask_sijax.route(todo_route, '/todo')
@login_required
def todo():

    def sijax_todo_add_function(obj_response, todo_form):
        form = TodoForm(data=todo_form)
        form.validate()

        if form.todo.errors:
            obj_response.html('#todo_error', ','.join(form.todo.errors))
        else:
            # instantiate new model class
            new_todo = Todo()
            # copy yung matching attributes from 'form' to model
            form.populate_obj(new_todo)
            # save to db
            db.session.add(new_todo)
            db.session.commit()
            # update the component
            flash('Okay na add mo na!')
            data = Todo.query.all()
            html_string = render_template('todo/todo_list.html', data=data)
            obj_response.html('#todo_list', html_string)

    if g.sijax.is_sijax_request:
        g.sijax.register_callback('sijax_todo_add', sijax_todo_add_function)
        return g.sijax.process_request()
    else:
        form = TodoForm()
        data = Todo.query.all()
        return render_template('todo/todo.html', form=form, data=data)
