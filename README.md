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
