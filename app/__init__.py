from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from app.auth.routes import auth
    from app.tasks.routes import tasks
    from app.dashboard import dashboard
    
    app.register_blueprint(auth)
    app.register_blueprint(tasks)
    app.register_blueprint(dashboard)

    return app
