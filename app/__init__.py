from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.auth.routes import auth
    from app.tasks.routes import tasks
    from app.dashboard import dashboard
    
    app.register_blueprint(auth)
    app.register_blueprint(tasks)
    app.register_blueprint(dashboard)

    return app
