Challenge 8 — Think like an engineer
Imagine your AI application eventually has:
main.py
containing:
5000 lines of code
Why would breaking it into modules and packages make the application easier to maintain?
Explain it in your own words.

Ans. Breaking into into modules will helps to improve the readebility of the application and if you have to fix the bug it is easier to fix the one module rather than fixing the entire one code file which consits all the codes of the project.

# 🧠 Day 7 Questions

Q1
What is a Python module?

Ans. Python module is a python file which consits of a lines of code for specific functionality which yu will use it in different place and it will help to improve the structure of an AI application.

Q2
What is a Python package??

Ans. Python package consits of differnt python modules for the project.

Q3
What's the difference between:
import math_utils
and:
from math_utils import add
?

Ans. Both are logically same but when we do "import math_utils" then in order to use the "add" function we have to write "math_utils.add()" and when we write "from math_utils import add" in order to use "add" function we can simply write "add()".

Q4
What does this mean?
if __name__ == "__main__":
Explain why we use it, not just what it does.

Ans. if __name__ == "__main__": makes a block run only when the Python file is executed directly. When the file is imported as a module, that block does not run. This lets a file provide reusable functions without automatically executing its test/demo code during import.

Q5
Why shouldn't we install every Python package globally?

Ans. Every module or the package have its own dependicies for the program and if we put it globaally it will eventually affects our project.

Q6
What problem does a virtual environment solve?

Ans. If both depend on different versions, a global installation can create conflicts.
A virtual environment gives each project its own package environment.

Q7
Why shouldn't .venv/ be committed to Git?

Ans. .venv contains the project's installed dependencies and environment-specific files. It can be recreated from dependency information, so committing it would unnecessarily add a large amount of machine-specific data to Git.

Q8
What is a circular import?

Ans. if two module are interdepended module a then module b and then use the module a this is called the circular import.

Q9
What's the difference between:
standard library
and:
third-party package
?

Ans. The standard library is the collection of modules that comes with Python itself, such as json, csv, pathlib, and os. Third-party packages are created and distributed separately by other developers or organizations, such as NumPy, FastAPI, and PyTorch.

Q10 — Engineering question
You have this:
main.py
with:
3000 lines
containing:
database code
API code
validation
calculations
file handling
business logic
Would you keep everything in main.py?
If not, how would you decide what goes into separate modules?

Ans. I would never keep eveything in one file it will refuce the readebility of the code also i will divide the code as per the logic 

keep validation, file handling, calculaion in one module. database code and api code different and business logic in different file.