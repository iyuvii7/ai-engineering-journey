🧠 Day 3 Questions
Q1
When would you use a list instead of a set?

Ans. When we need duplicates values, ordered values and wants to change the values.

Q2
Why would you use a tuple instead of a list?

Ans. When we need fixed and immmutable grouped values.

Q3
What's the difference between:
user["name"]
and:
user.get("name")

Ans. Both used to get the value of name but the difference is when "name" doesn't exits in the lists the "user["name"]" throws an error while "user.get("name")" simply return None without error.

Q4
Explain what this means:
[x ** 2 for x in numbers if x % 2 == 0]

Ans.This line of code "for x in numbers" iterate each number in the numbers lit.
"if x % 2 == 0" This line of code provides only the even number from the list.
x ** 2 This line of code makes the sqaured of each number.
So, in short it returns the sqaures of even number.

Q5
What is dictionary unpacking/iteration using:
for key, value in user.items():

Ans. Its giving "key" as each key from the dictionary and "value" as each value with respect to the corresponding key.

Q6
Given:
a = [1, 2, 3]
b = [1, 2, 3]
Why would you use a set if your goal is to efficiently check whether a value exists in a large collection?

Ans. When we care about unique values and frequently need to check whether a value exits we use a set.