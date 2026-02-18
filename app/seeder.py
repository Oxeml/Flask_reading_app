import sys
import os
import json

# allows python find the path to the files seeder needs to import - app and run
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from run import app        # Get the app from run.py
from app import db         # Get the db from the app package
from app.models import Lesson

with app.app_context():
    db.session.query(Lesson).delete()

    # load lessons from json
    with open("app/lessons.json", "r", encoding="utf-8") as f:
        lessons = json.load(f)    

    # create Lessons objects and add them all at once
    lesson_objects = [Lesson(**data) for data in lessons]
    db.session.add_all(lesson_objects)
    db.session.commit()

    #Print summary
    print(f"Seeder finished! {len(lesson_objects)} lessons added:")
    for lesson in lesson_objects:
        print(f"- {lesson.title} ({len(lesson.content)} chars)")