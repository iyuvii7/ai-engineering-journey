from pathlib import Path
import json

data_directory = Path(__file__).parent.parent / "data"
file_path = data_directory / "notes.txt"

# Challenge 5 — JSON
json_data_dir = Path(__file__).parent.parent/"data"
json_file_path = json_data_dir/"ai_engineer.json"
with open(json_file_path, "r") as file:
    user = json.load(file)
    
print(f"Name: {user['name']}")
print(f"Skills: {', '.join(user['skills'])}")
print(f"Goal: {user['goal']}")

# Challenge 6 — Modify JSON
json_data = {"current_focus": "Python Fundamentals"}
focus_file_path = data_directory / "focus.json"
with open(focus_file_path, "w") as file:
    json.dump(json_data, file, indent=4)