# Day 1 — Python Fundamentals

## Objective

The goal of Day 1 was to assess and strengthen my existing Python fundamentals.

I focused on:

- Variables and data types
- Arithmetic operators
- Floor division
- Lists
- List indexing
- List mutation
- Tuples
- Sets
- Dictionaries
- Loops
- Functions
- Basic problem solving

---

## Python Assessment

### 1. Assignment vs Equality

`=` is used for assignment.

```python
age = 25
== is used to check whether two values are equal.
5 == 5
2. Python Data Structures
List
A list is an ordered and mutable collection.
numbers = [10, 20, 30]
Tuple
A tuple is an ordered and immutable collection.
coordinates = (10, 20)
Set
A set is a collection of unique values.
skills = {"Python", "SQL", "Docker"}
Duplicate values are automatically removed.
Dictionary
A dictionary stores data as key-value pairs.
user = {
    "name": "Yuvraj",
    "age": 23
}
3. Why Use Functions?
Functions help with:
Code reuse
Organization
Readability
Maintainability
Testing
Instead of repeating the same logic, the logic can be placed inside a function and reused.
4. IndexError
Trying to access an index that doesn't exist causes an IndexError.
numbers = [1, 2, 3]

print(numbers[10])
This produces:
IndexError: list index out of range
5. For vs While
Both are loops.
A for loop is generally used to iterate over a collection or sequence.
for number in numbers:
    print(number)
A while loop continues executing while a condition remains true.
while condition:
    ...