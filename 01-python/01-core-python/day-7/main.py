from expenses import calculations, validators


expenses = [
    {
        "name": "Rent",
        "amount": 3000,
        "category": "Housing",
    },
    {
        "name": "Lunch",
        "amount": 50 * 30,
        "category": "Food",
    },
    {
        "name": "Coffee",
        "amount": 5 * 30,
        "category": "Food",
    },
    {
        "name": "Rapido",
        "amount": 100 * 30,
        "category": "Transport",
    },
    {
        "name": "Eggs",
        "amount": 250 * 4,
        "category": "Food",
    },
]


for expense in expenses:
    validators.validate_expense(expense)


print(
    f"Total: {calculations.calculate_total(expenses)}"
)

print(
    f"Highest: {calculations.find_highest_expense(expenses)}"
)

print(
    f"Lowest: {calculations.find_lowest_expense(expenses)}"
)

print(
    f"Average: {calculations.calculate_average_expense(expenses)}"
)