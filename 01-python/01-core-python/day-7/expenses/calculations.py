def calculate_total(expenses):
    total_expense = 0

    for expense in expenses:
        total_expense += expense["amount"]

    return total_expense


def find_highest_expense(expenses):
    highest_expense = None

    for expense in expenses:
        if (
            highest_expense is None
            or expense["amount"] > highest_expense["amount"]
        ):
            highest_expense = expense

    return highest_expense


def find_lowest_expense(expenses):
    lowest_expense = None

    for expense in expenses:
        if (
            lowest_expense is None
            or expense["amount"] < lowest_expense["amount"]
        ):
            lowest_expense = expense

    return lowest_expense


def calculate_average_expense(expenses):
    if not expenses:
        return 0

    total_expense = calculate_total(expenses)

    return total_expense / len(expenses)