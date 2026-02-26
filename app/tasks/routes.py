from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Task, Category
from app.forms import TaskForm, CategoryForm

tasks = Blueprint('tasks', __name__)

@tasks.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('tasks.list_tasks'))
    return render_template('index.html')

@tasks.route('/tasks')
@login_required
def list_tasks():
    user_tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.due_date.asc()).all()
    # Group tasks by status for the board view
    board = {
        'Pending': [t for t in user_tasks if t.status == 'Pending'],
        'In Progress': [t for t in user_tasks if t.status == 'In Progress'],
        'Completed': [t for t in user_tasks if t.status == 'Completed']
    }
    return render_template('tasks.html', board=board)

@tasks.route('/tasks/create', methods=['GET', 'POST'])
@login_required
def create_task():
    form = TaskForm()
    # Populate category choices
    categories = [(c.id, c.name) for c in current_user.categories]
    form.category_id.choices = [(0, 'No Category')] + categories
    
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            due_date=form.due_date.data,
            priority=form.priority.data,
            author=current_user,
            category_id=form.category_id.data if form.category_id.data != 0 else None
        )
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!', 'success')
        return redirect(url_for('tasks.list_tasks'))
    return render_template('create_task.html', form=form)

@tasks.route('/category/new', methods=['GET', 'POST'])
@login_required
def create_category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data, color=form.color.data, user=current_user)
        db.session.add(category)
        db.session.commit()
        flash('Category created!', 'success')
        return redirect(url_for('tasks.create_task'))
    return render_template('create_category.html', form=form)

@tasks.route('/tasks/<int:task_id>/toggle', methods=['POST'])
@login_required
def toggle_status(task_id):
    task = Task.query.get_or_404(task_id)
    if task.author != current_user:
        return "Unauthorized", 403
    
    # Simple toggle logic for demo
    if task.status == 'Pending':
        task.status = 'In Progress'
    elif task.status == 'In Progress':
        task.status = 'Completed'
    else:
        task.status = 'Pending'
        
    db.session.commit()
    return redirect(url_for('tasks.list_tasks'))

@tasks.route('/tasks/<int:task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.author != current_user:
        return "Unauthorized", 403
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted!', 'info')
    return redirect(url_for('tasks.list_tasks'))
