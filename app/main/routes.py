from flask import render_tenplate
from . import main_bp

@main_bp.route("/")
def main_home():
    return()
    render_template("index.html")