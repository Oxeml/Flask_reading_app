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
  
### Seeder
All lessons are stored in a database. To populate the database with initial lessons' content, I created a seeder.
It reads from the .json file and inserts into the db automatocally. This makes filling the content in
somewhat automatically without any kind of admin UI or tools like Postman.