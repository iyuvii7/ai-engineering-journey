# Challenge 1 — Lists
languages = ["Python", "Java", "C++", "JavaScript"]
# Add "Go"
languages.append("Go")
# Remove "Java"
languages.remove("Java")
# Insert "SQL" at index 1
languages.insert(1, "SQL")
# Print the final list
print(languages)
# Check whether "Python" exists
print("Python" in languages)

# Challenge 2 — Tuple unpacking
developer = ("Yuvraj", 23, "Python")
name, age, language = developer
print(name)
print(age)
print(language)

# Challenge 3 — Sets
backend_skills = {"Python", "SQL", "Git", "Docker"}
ai_skills = {"Python", "NumPy", "PyTorch", "Git"}
# All skills
all_skills = backend_skills | ai_skills
# Common skills
common_skills = backend_skills & ai_skills
# Skills only in backend_skills
skills_only_in_backend = backend_skills - ai_skills
# Skills only in ai_skills
skills_only_in_ai = ai_skills - backend_skills
print(all_skills)
print(common_skills)
print(skills_only_in_backend)
print(skills_only_in_ai)

# Challenge 4 — Dictionary
ai_engineer = {
    "name": "Yuvraj",
    "age": 23,
    "skills": ["Python", "Git"],
    "experience": 0,
    "is_learning": True
}
# Print the name
print(ai_engineer["name"])
# Print the skills
print(ai_engineer["skills"])
# Add "SQL" to the skills
ai_engineer["skills"].append("SQL")
print(ai_engineer["skills"])
# Add a "goal" key
ai_engineer["goal"] = "AI engineer"
print(ai_engineer)
# Print all key-value pairs using .items()
for key, value in ai_engineer.items():
    print(key, value)

# Challenge 5 — Nested data
students = [
    {
        "name": "Yuvraj",
        "skills": ["Python", "Git", "SQL"]
    },
    {
        "name": "Rahul",
        "skills": ["Java", "Spring", "SQL"]
    },
    {
        "name": "Aman",
        "skills": ["Python", "Docker", "Linux"]
    }
]
print(students[0]['name'])
print(students[0]['skills'][2])

# Challenge 6 — List comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [number **2 for number in numbers]
even_numbers = [number for number in numbers if number % 2==0]
numbers_greater_than_5 = [number for number in numbers if number > 5]
print(squares)
print(even_numbers)
print(numbers_greater_than_5)

# Challenge 7 — Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
multiple_numbers = {
    number: number*number for number in numbers
}
print(multiple_numbers)

