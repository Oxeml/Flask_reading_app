from flask import render_template
from . import reading_bp

@reading_bp.route("/")
def reading_home():
    return
    render_template("reading_base.html")
