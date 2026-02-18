from flask import render_template
from . import main_bp

@main_bp.route("/")
def main_home():
    return render_template("index.html",
                            title="Reading App",
                            user_name="Oksana",
                            completed_lessons=[])
