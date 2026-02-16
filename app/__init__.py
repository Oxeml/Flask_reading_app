# Creates the Flask app
# Loads config
# Initializes extensions
# Registers blueprints

# So it builds the main application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import DevelopmentConfig

db = SQLAlchemy()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    #Register blueprint for reading which I haven't coded yet
    from .reading import reading_bp
    # url prefix is for the browser, it will add "reading" infront of any reading url
    app.register_blueprint(reading_bp, url_prefix="/reading")

    # need to handle the main route here either view function or also
    # a blueprint for main
    # decided that I will for cleaningness
    from .main import main_bp
    app.register_blueprint(main_bp, url_prefix="/main")

    return app
