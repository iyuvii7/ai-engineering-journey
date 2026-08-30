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
        raise ValueError(
            "Expense name must be a non-empty string."
        )

    amount = expense["amount"]

    if not isinstance(amount, (int, float)):
        raise TypeError(
            "Expense amount must be a number."
        )

    if amount < 0:
        raise ValueError(
            "Expense amount cannot be negative."
        )

    category = expense["category"]

    if not isinstance(category, str) or not category.strip():
        raise ValueError(
            "Expense category must be a non-empty string."
        )

    return True