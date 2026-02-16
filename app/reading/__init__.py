# Creates a blueprint object
#This object can be plugged into the main app
#the view functions are in the ./routes.py file

from flask import Blueprint

reading_bp = Blueprint("reading", __name__, template_folder="../templates")

from . import routes