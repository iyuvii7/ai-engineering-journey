# Challenge 1 - Expense Tracker

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


# 1. Floor division

floor_div = 10 // 3
print(f"Floor division of 10 by 3: {floor_div}")


# 2. List indexing

numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[2])
print(numbers[4])


# 3. List mutation

numbers = [10, 20, 30]

numbers.append(40)
numbers.append(50)
numbers.pop(1)

print(numbers)


# 4. Set

my_set = {
    "Python",
    "SQL",
    "Python",
    "Docker",
    "SQL",
    "Git",
}

print(my_set)


# 5. Dictionary

ai_engineer = {
    "name": "Yuvraj",
    "skills": ["Python", "SQL", "Docker", "Git"],
    "experience": 1,
    "learning": "Python",
}

print(ai_engineer)


# 6. Function

def calculate_numbers_total(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


list_of_numbers1 = [1, 2, 3, 4, 5]
list_of_numbers2 = [10, 20, 30, 40, 50]

total1 = calculate_numbers_total(list_of_numbers1)
total2 = calculate_numbers_total(list_of_numbers2)

print(f"Total of list_of_numbers1: {total1}")
print(f"Total of list_of_numbers2: {total2}")