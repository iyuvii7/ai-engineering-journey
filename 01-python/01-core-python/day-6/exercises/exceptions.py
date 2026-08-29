# Challenge 1 — Basic exception
# Write a program that asks the user for two numbers and divides them.
# Handle:
# ValueError
# ZeroDivisionError
# Don't use a broad except.
try:
    number1 = int(input("Enter the first number: "))
    number2= int(input("Enter the second number: "))
    result = number1/number2
    print(result)
except ValueError:
    print("Enter the correct number.")
except ZeroDivisionError:
    print("Number cannot divide by 0.")

# Challenge 2 — Safe integer function
# Create:
# def get_integer():
#     ...
# It should ask the user for an integer.
# If they enter:
# abc
# it should not crash.
# Keep asking until they provide a valid integer.
def get_integer():
    while True:
        try:
            number = int(input("Enter a number."))
            return number
        except ValueError:
            print("Please enter a valid number! ")
number = get_integer()

# Challenge 6 — try/except/else/finally
try: 
    number = int(input("Enter a number "))
except ValueError:
    print("You have not enterd the valid number")
else:
    print(f"Here is your Entered number {number}")
finally:
    print("Have a nice day!")

# Challenge 8 — Think like an engineer
# Imagine:
# def load_config():
#     try:
#         ...
#     except:
#         return None
# Why could this be dangerous?
# Think about what happens if the configuration contains a programming bug rather than simply being missing.

# Ans. Can hide an unexpected programming bug..

