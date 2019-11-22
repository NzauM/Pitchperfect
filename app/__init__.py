#pylint: skip-file
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config_options
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    # Create the app configurations
    app.config.from_object(Config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)
    db = SQLAlchemy()

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


