# Challenge 1 — Basic function
def calculate_area(length, width):
    return length*width
total_area = calculate_area(12,30)
total_area2 = calculate_area(7,90)
total_area3 = calculate_area(24,90)
print(total_area)
print(total_area2)
print(total_area3)

# Challenge 2 — Return vs print
def add_and_print(a, b):
    print(f"{a} + {b} = {a+b}")

total = add_and_print(20,40)
print(total) # None
def add_and_return(a, b):
    return a+b
total = add_and_return(20,40)
print(total) # 60

# Challenge 3 — Default arguments
def greet(name, greeting="Hello"):
    print(f"{greeting} {name}")
greet("Yuvraj")
greet("Yuvraj", "Welcome")

# Challenge 4 — Keyword arguments
def create_profile(name, age, role):
    return name, age, role
name, age, role = create_profile(name="Yuvraj", role="AI engineer", age= 23)
print(f"My name is {name}. I'm {age} years old and I'm an {role}.")

# Challenge 5 — *args
def calculate_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total
total1= calculate_sum(1, 2)
print(total1)
total2 = calculate_sum(1, 2, 3)
print(total2)
total3 = calculate_sum(10, 20, 30, 40, 50)
print(total3)

# Challenge 6 — **kwargs
def create_profile(**details):
    return details

profile1 = create_profile(
    name="Yuvraj",
    age=23,
    role="AI Engineer",
    learning="Python"
)
print(f"My name is {profile1['name']}. I'm {profile1['age']} years old and {profile1['role']} currently learning {profile1['learning']}.")

# Challenge 7 — Scope
name = "Yuvraj"
def detail():
    name = "Rahul"
    print(name) # Rahul
detail()
print(name) # Yuvraj

# Challenge 8 — Type hints
def calculate_sum(a: int, b: float) -> float:
    return a+b
total = calculate_sum(20,30)
print(total)

