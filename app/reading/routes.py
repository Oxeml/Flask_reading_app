from flask import render_template, abort
from . import reading_bp
from ..models import Lesson

@reading_bp.route("/<int:lesson_id>")
def show_lesson(lesson_id):
    #return render_template("reading_base.html")
    #return render_template("base.html")
    
    #fetch the Lesson from the DB
    lesson = Lesson.query.get_or_404(lesson_id)
    
    #Add some sample data for levels medium and advanced
    vocab = [
        {"term": "Efficiency", "definition": "Doing things without waste."},
        {"term": "Ethical", "definition": "Relating to moral principles."}
    ]
    sample_question = "How do you think this topic affects your daily life?"


    #construct a template name by reading the lesson level from the db to avoid if elif
    template_name=f"reading_{lesson.level}.html"
    #construct title for the page
    page_title=f"Reading_{lesson.title}"

    #finally render a template, we are passing vocab and question in every rendering
    #jinja should ignore additional data
    return render_template(
            template_name,
            title=page_title,

            #data from the DB line, stored in var lesson
            Lesson_level=lesson.level,
            Lesson_title=lesson.title,
            Lesson_content=lesson.content,

            #optional data, vocab for advanced lessons, question for medium
            vocabularly=vocab,
            question=sample_question
    )
