# Challenge 1 — Basic exception

try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))

    result = number1 / number2
    print(f"Result: {result}")

except ValueError:
    print("Please enter valid numbers.")

except ZeroDivisionError:
    print("Number cannot be divided by zero.")


# Challenge 2 — Safe integer function

def get_integer():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number

        except ValueError:
            print("Please enter a valid integer.")


number = get_integer()
print(f"You entered: {number}")


# Challenge 3 — File error

def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()

    except FileNotFoundError:
        print("File not found.")
        return None


file_content = read_file("notes.txt")
print(file_content)


# Challenge 4 — Validate expense

def validate_expense(expense):
    if not isinstance(expense, dict):
        raise TypeError("Expense must be a dictionary.")

    if "name" not in expense:
        raise KeyError("Expense is missing the 'name' key.")

    if "amount" not in expense:
        raise KeyError("Expense is missing the 'amount' key.")

    if "category" not in expense:
        raise KeyError("Expense is missing the 'category' key.")

    name = expense["name"]

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Expense name must be a non-empty string.")

    amount = expense["amount"]

    if not isinstance(amount, (int, float)):
        raise TypeError("Expense amount must be a number.")

    if amount < 0:
        raise ValueError("Expense amount cannot be negative.")

    category = expense["category"]

    if not isinstance(category, str) or not category.strip():
        raise ValueError("Expense category must be a non-empty string.")


# Challenge 5 — Safe expense addition

def add_expense(expenses, expense):
    validate_expense(expense)
    expenses.append(expense)
    return expenses


valid_expense = {
    "name": "Coffee",
    "amount": 50,
    "category": "Food"
}

expenses = []

updated_list = add_expense(expenses, valid_expense)

print(updated_list)


# Challenge 6 — try / except / else / finally

try:
    number = int(input("Enter another number: "))

except ValueError:
    print("You did not enter a valid number.")

else:
    print(f"You entered: {number}")

finally:
    print("This block always runs.")


# Challenge 7 — Custom exception

class InvalidExpenseError(Exception):
    pass

def validate_expense_amount(amount):
    if amount < 0:
        raise InvalidExpenseError(
            "Expense amount cannot be negative."
        )

try:
    validate_expense_amount(-50)

except InvalidExpenseError as error:
    print(f"Invalid expense: {error}")