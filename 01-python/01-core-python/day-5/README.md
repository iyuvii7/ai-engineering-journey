🧠 Day 5 Questions

Q1
Why is this:
with open("file.txt") as file:
generally better than:
file = open("file.txt")

Ans. This line of code file = open("file.txt") only save the file temprary once the code is quited it will not be saved and with open("file.txt") as file: it saved the code in the memory.

Q2
What's the difference between:
r
w
a
?

Ans. "r" is used to read the file, "w" is used to write the file and "a" This adds content to the end instead of replacing the existing content.

Q3
Why can "w" be dangerous if you're trying to preserve existing data?

Ans. "w" is ued to write the something in the file but if the data is already exists in the file whcih we are going to use for writing then it will erase or overwrite the content and add only the new content it means the existing content will get erased. And this is dangerous.

Q4
What's the difference between:
file.read()
and:
file.readlines()
?

Ans. read()- reads the entire file.
readlines()- reads the all the lines and gives you.

Q5
What is JSON and why is it important when working with APIs?

Ans. JSON is really important because it helps to communicate with API because API mainly uses python dictionary and with json we cna easily read, write the dictionary.

Q6
What's the difference between:
json.dump()
and:
json.load()
?

Ans. json.dump() helps to write python object into json format and json.load() used to reads the json data back to python object.

Q7
Why would you use pathlib instead of hardcoding file paths?

Ans. pathlib makes your code platform-independent, readable, and safer to maintain.


Q8 — Think like an engineer
Imagine your AI application generates a response:
response = "Python is a programming language..."
You want to save every response to a file without deleting previous responses.
Which file mode would you use?
Explain why.

Ans. You’d use the append mode ("a") when opening the file. Append mode adds new content to the end of the file without erasing existing data.