expenses = [
    {"name": "Rent", "amount": 3000, "category": "Housing"},
    {"name": "Lunch", "amount": 50 * 30, "category": "Food"},
    {"name": "Coffee", "amount": 5 * 30, "category": "Food"},
    {"name": "Rapido", "amount": 100 * 30, "category": "Transport"},
    {"name": "Eggs", "amount": 250 * 4, "category": "Food"},
]


def calculate_total(expenses):
    total_expense = 0

    for expense in expenses:
        if expense["amount"] > 0:
            total_expense += expense["amount"]

    return total_expense


total_expense = calculate_total(expenses)
print(f"Total Expense: {total_expense}")


def find_highest_expense(expenses):
    highest_expense = None

    for expense in expenses:
        if highest_expense is None or expense["amount"] > highest_expense["amount"]:
            highest_expense = expense

    return highest_expense


highest_expense = find_highest_expense(expenses)
print(
    f"Highest Expense: "
    f"{highest_expense['name']} - "
    f"Amount: {highest_expense['amount']}"
)


def find_lowest_expense(expenses):
    lowest_expense = None

    for expense in expenses:
        if lowest_expense is None or expense["amount"] < lowest_expense["amount"]:
            lowest_expense = expense

    return lowest_expense


lowest_expense = find_lowest_expense(expenses)
print(
    f"Lowest Expense: "
    f"{lowest_expense['name']} - "
    f"Amount: {lowest_expense['amount']}"
)


def calculate_average_expense(expenses):
    total_expense = calculate_total(expenses)
    average_expense = total_expense / len(expenses)

    return average_expense


average_expense = calculate_average_expense(expenses)
print(f"Average Expense: {average_expense}")