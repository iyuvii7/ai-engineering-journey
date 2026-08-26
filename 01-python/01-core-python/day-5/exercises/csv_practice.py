from pathlib import Path
import csv

data_directory = Path(__file__).parent.parent / "data"
csv_file_path = data_directory / "students.csv"
# Challenge 7 — CSV
with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['name']} age {row['age']} skill {row['skill']}")