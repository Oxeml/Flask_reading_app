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

    #Database part
    db.init_app(app)
    from .models import Lesson
    with app.app_context():
        db.create_all()

    #..Register blueprint for reading which I haven't coded yet
    #..ok I prepared all my reading templates
    from .reading import reading_bp
    # url prefix is for the browser, it will add "reading" infront of any reading url
    # so that whoever opens pages in the browser won't get confused where exactly they are :)
    app.register_blueprint(reading_bp, url_prefix="/reading")

    # need to handle the main route here either view function or also
    # .. so I decided to have a blueprint for main
    # for cleaningness
    from .main import main_bp
    app.register_blueprint(main_bp)

    return app
