# 🧠 Day 6 Questions

Q1
What is an exception?

Ans. Something happens which prevents the program from continuing the operation normally.

Q2
Why shouldn't we generally use:
except:
without specifying an exception?

Ans. It will get very broad and if some python bug occured in the program it we wil never know and not able to fix it.

Q3
What's the difference between:
ValueError
and:
TypeError
?

Ans. ValueError: When a functions gets a right value but the value itself is not right.
TypeError: When function run on a value of the wrong data type

Q4
What does else do in a try/except statement?

Ans. 'else' runs only when the try block completes successfully without raising an exception.

Q5
What is the purpose of finally?

Ans. It will always runs whether the try block runs or the except block runs.

Q6
Why would we use:
raise ValueError(...)
?

Ans. 'raise' allows us to deliberately create an exception when our program detects an invalid situation.

Q7
What's the difference between validation and exception handling?

Ans. Validation: We check the input is acceptable.
Exception: We handle the exception that occurs.

Q8
Why is this dangerous?
try:
important_operation()
except:
pass

Ans. could hide unexpected programming errors..

Q10 — Engineering question
Suppose your application is saving a user's important data.
Which is better?
A
try:
save_data()
except:
pass
B
try:
save_data()
except PermissionError:
print("You don't have permission to save this file.")
Explain why.

Ans. The answer is "B" blindly catching everything is dangerous.
