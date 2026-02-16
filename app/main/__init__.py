#Creates a blueprint object for the main route
#the view functions are in the routes.py

from flask import Blueprint

main_bp = Blueprint("main", __name__, template_folder="../templates")

from . import routes