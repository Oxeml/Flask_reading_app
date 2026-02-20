# Reading App

This is a practice Flask project for learning the modular architecture
using **Blueprints**.

What did I learn:
- Application factory pattern
- Blueprint structure for modular routes
- Minimal templates
- Prepared for database integration (models.py)
- Safe configuration via .env file

Purpose: learning scalable Flask architecture and keep code modular

## Setup
Create a virtual environment using Anaconda because VS Code and Windows don't want to cooperate
And because I like Anaconda and its Shell

```bash
conda create --name <name_for_env> python=<version_you_wanna_use>
conda activate <name_for_env>
```

This creates the environment and stores on the computer, the path is something like that:
```C:\Users\<User_name>\miniconda3\envs\```
It does not create a venv folder in your project directory
After the activation the name of the virtual env appears enclosed in the parentheses
infront of the path in the Shell

<img width="350" alt="image" src="https://github.com/user-attachments/assets/ec1087c0-6918-4402-b996-c86530ea3b92" />

## Using templates
- **Base template** - contains common structure for all lessons.
- **Child templates** - inherit from the base template and add their own content depending on the level
  
## Seeder

### Scope
All lessons are stored in a database. To populate the database with initial lessons' content, I created a seeder.
It reads from the .json file and inserts into the db automatocally. This makes filling the content in
somewhat automatically without any kind of admin UI or tools like Postman.

### Errors and debugging
- Module Resolution: Fixed ModuleNotFoundError by adding the project root directory 
  to sys.path. This allowed the seeder (located in /app) to "see" and import run.py and the app package.
- Flask Application Context: Resolved ```RuntimeError: Working outside of application context``` by 
  wrapping database operations within with ```app.app_context()```. This is required for Flask-SQLAlchemy 
  to access the database configuration outside of a live web request.
- File Path Handling: Fixed FileNotFoundError for lessons.json by using absolute paths (via os.path) or executing 
  the script from the root, ensuring the seeder could locate the data source regardless of the terminal's working directory.

### Running the seeder
1. activate the virtual environment
2. run ```python seeder.py```

### Virtual environment
- dependencies isolation, the project uses dependencies installed for the project, not globally on the machine
- need to activate each time the project or it's part (like seeder) is running
- to maintain the list of dependencies:
  ```pip freeze > requirements.txt```

### Templating
- Jinja2 Inheritance: implemented base-to-child architecture. Created base.html for shared structure and used {% block %} for level-specific content to be
injected dynamically.

- Dynamic Styling: Developed a multi-layered CSS strategy. In my base.html, which is a parent template for all lessons
  within the head section there's a place for styling extentions:
  ```{% block styles %}{% endblock %}```
  so that in child .html templates there will be a styling extention in the <head> section:
  ```{% block styles %}
        <link rel="stylesheet" href="{{ url_for('static', filename='<filename>.css') }}">
     {% endblock %} ```

- Data-driven Rendering: one route for all types of templates, developed by constructing a template name
  after fetching the lesson data from the database. Optional content is passed everytime a template is being rendered,
  and for now is managed by the fact that jinja2 ignores extra arguments gracefully :)

- Debugging: here was to put the closing qoutes for the stylesheet.
