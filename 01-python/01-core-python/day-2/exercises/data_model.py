# Challenge 1 — Identity
## == vs is

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2) # Checks if the values are equal
print(list1 is list2) # Checks if the two variable point to the same object in memory

# Challenge 2 - Shared references
a = [10,20,30]
b = a # points same object in memory
b.append(40)
print(a)
print(b)

# # Challenge 3 - Copy
a = [10,20,30]
b = a.copy() # Create new object in memory
b.append(40)
print(a)
print(b)

# # Challenge 4 - Slicing
numbers = [10, 20, 30, 40, 50, 60, 70]
print(numbers[1:4])
print(numbers[4:])
print(numbers[::2])
print(numbers[::-1])

# Challenge 5 — Mutable vs immutable
# List
list1 = [1, 2, 3]
list1[0]=10
print(list1) # list is mutable

# Dictionary
dict1 = {'a': 1, 'b': 2}
dict1['a'] = 10
print(dict1) # dictionary is mutable

# Set
set1 = {1, 2, 3}
set1.add(4)
print(set1) # set is mutable

# int
a = 10
a = 20
print(a) # int is immutable

# string
name = "John"
name[0] = "j" # This will raise an error because strings are immutable
# print(name)

# Tuple
tuple1 = (1, 2, 3)
tuple1[0] = 10 # This will raise an error because tuples are immutable
# print(tuple1)



