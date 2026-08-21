# # Challenge 1 - Expense Tracker
expenses = [
    {"name": "Rent", "amount": 3000, "category": "Housing"},
    {"name": "Lunch", "amount": 50*30, "category": "Food"},
    {"name": "Coffee", "amount": 5*30, "category": "Food"},
    {"name": "Rapido", "amount": 100*30, "category": "Transport"},
    {"name": "Eggs", "amount": 250*4, "category": "Food"},
]

# # Total expenses
# total_expense = 0
# for expense in expenses:
#     total_expense += expense["amount"]

# print(f"Total expenses: {total_expense}")

# # Highest expense
# highest_expense = 0
# for expense in expenses:
#     if expense["amount"] > highest_expense:
#         highest_expense = expense["amount"]
# print(f"Highest expense: {highest_expense}")

# # Lowest expense
# lowest_expense = float('inf')
# for expense in expenses:
#     if expense["amount"] < lowest_expense:
#         lowest_expense = expense["amount"]
# print(f"Lowest expense: {lowest_expense}")

# #Average expense
# average_expense = total_expense / len(expenses)
# print(f"Average expense: {average_expense}")


# Challenge - 2: Categorization

# # Categorize expenses

# # Food
# food_expense = 0
# for expense in expenses:
#     if expense.get("category") == "Food":
#         food_expense += expense["amount"]
# print(f"Total Food expenses: {food_expense}")

# # Transport
# transport_expense = 0
# for expense in expenses:
#     if expense.get("category") == "Transport":
#         transport_expense += expense["amount"]
# print(f"Total Transport expenses: {transport_expense}")

# # Housing
# housing_expense = 0
# for expense in expenses:
#     if expense.get("category") == "Housing":
#         housing_expense += expense["amount"]
# print(f"Total Housing expenses: {housing_expense}")

# Part - 3: Functions

def calculate_total(expenses):
    total_expense = 0
    for expense in expenses:
        total_expense += expense["amount"]
    return total_expense

total_expense = calculate_total(expenses)
print(f"Total expenses: {total_expense}")

def find_highest_expense(expenses):
    highest_expense = 0
    for expense in expenses:
        if expense["amount"] > highest_expense:
            highest_expense = expense["amount"]
    return highest_expense

highest_expense = find_highest_expense(expenses)
print(f"Highest expense: {highest_expense}")

def calculate_average(expenses):
    total_expense = calculate_total(expenses)
    average_expense = total_expense / len(expenses)
    return average_expense

average_expense = calculate_average(expenses)
print(f"Average expense: {average_expense}")