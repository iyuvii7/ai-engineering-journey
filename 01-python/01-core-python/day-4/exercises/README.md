🧠 Day 4 Questions

Q1
What's the difference between a parameter and an argument?

Ans.
def add(a,b):
    return a+b
total = add(10,20)
Here a,b is parameter and 10,20 the values passed to the functions in the argument.

Q2
What's the difference between print() and return?

Ans.When "print()" is used in a function is simply print the value without returning any value from the function.
While "return" returns the value based on the specific function and then later we can use those value for the other operations.

Q3
What does *args store inside a function?

Ans. "*args" It store multiple positional argument and we can use those positional arguments for operation. Also, it store the values in a tuple.

Q4
What does **kwargs store inside a function?

Ans."**kwargs" It store multiple keyword argument and we can use those keyword arguments for operation. Also, it store the values in a dictionary.

Q5
What's the difference between a local and global variable?

Ans. "global" variable can use used anywhere in the code and the "local" variable can only be used within that function in which he was created.

Q6
Why are type hints useful?

Ans. "type hints" are used in python functions to describe the datatype of the paramater for better readability of the code.
e.g. def add(a:int, b:int) -> int:
        return a+b
Here a: int means parameter a is integer and same for b.
Also "-> int" means the value which return will also be an integer.

Q7
Why is this generally better?
def calculate_total(expenses):
    return total
than:
def calculate_total():
    # uses a global expenses variable

Ans. It makes functions easier to test and reuse.

Q8 — Think like an engineer
What's wrong with this function?
def process_user(user):
    print(user["name"])
    save_user_to_database(user)
    send_email(user)
    generate_report(user)
    calculate_score(user)

Ans. Each function has one clear responsibility.

