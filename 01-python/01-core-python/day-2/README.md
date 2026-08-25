Q1
What is the difference between:
a = [1, 2, 3]
b = a
and:
a = [1, 2, 3]
b = a.copy()

Ans. The "b = a" just pointing the same object in the memory and "b = a.copy()" just create a new object.

Q2
What's the difference between:
==
and:
is

Ans. The "==" is checks that the values of the ojects are same and the "is" checks if the objects are pointing to the same memory.

Q3
Why can this happen?
a = [1, 2, 3]
b = a

b.append(4)

print(a)

Ans. This is because when "b = a" this line of code runs it simply create the same memory location for both ojects and eventually when "b.append(4)" this line of code works it just add the value to the same memory location and that change also added to "a".

Q4
What does:
numbers[1:5]
mean?

Ans. It is list slicing and it means Start at index 1 and stop before index 5.

Q5
What's the difference between a mutable and immutable object?

Ans. Mutable objects can be changed after they are created, while immutable objects cannot be changed after they are created.

Examples:
Mutable:
list
dict
set

Immutable:
int
float
str
tuple
bool
