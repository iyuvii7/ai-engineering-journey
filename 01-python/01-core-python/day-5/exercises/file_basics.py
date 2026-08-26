from pathlib import Path
import json
import csv

data_directory = Path(__file__).parent.parent / "data"
file_path = data_directory / "notes.txt"

# Challenge 1 — Create and write a file
with open(file_path, "w") as file:
    file.write("Python\n")
    file.write("Git\n")
    file.write("GitHub\n")
    file.write("AI Engineering\n")

print(f"Created: {file_path}")

# Challenge 2 — Read the file
with open(file_path, "r") as file:
    content = file.read()
print(content)

# # Challenge 3 — Append
with open(file_path, "a") as file:
    file.write("\nDocker")
    file.write("\nLinux")
with open(file_path, "r") as file:
    content = file.read()
print(content)

# Challenge 4 — Word counter
def count_words(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    return len(content.split())
words_count = count_words(file_path)
print(words_count)

# # Challenge 8 — pathlib
# # Define the path
data_dir = Path("data")
# Create a directory
data_dir.mkdir(parents=True, exist_ok=True)
print(f"Directory ready at: {data_dir.resolve()}")
    

