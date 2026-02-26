from flask import Blueprint, render_template
from datetime import datetime
from flask_login import login_required, current_user
from app import db
from app.models import Task
from sqlalchemy import func

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/dashboard')
@login_required
def index():
    # Basic statistics
    total_tasks = Task.query.filter_by(user_id=current_user.id).count()
    completed_tasks = Task.query.filter_by(user_id=current_user.id, status='Completed').count()
    pending_tasks = total_tasks - completed_tasks
    
    # Task completion rate
    completion_rate = (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
    
    # Overdue tasks
    overdue_tasks = Task.query.filter(
        Task.user_id == current_user.id,
        Task.status != 'Completed',
        Task.due_date < datetime.utcnow()
    ).count()

    # Data for Chart.js (tasks by priority)
    priority_data = db.session.query(Task.priority, func.count(Task.id)).filter_by(user_id=current_user.id).group_by(Task.priority).all()
    priority_labels = [p[0] for p in priority_data]
    priority_counts = [p[1] for p in priority_data]

    stats = {
        'total': total_tasks,
        'completed': completed_tasks,
        'pending': pending_tasks,
        'rate': round(completion_rate, 1),
        'overdue': overdue_tasks,
        'priority_labels': priority_labels,
        'priority_counts': priority_counts
    }

    return render_template('dashboard.html', stats=stats)
