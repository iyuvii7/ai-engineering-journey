# # Challenge 1 — Your first class
# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#     def print_information(self):
#         print(f"My name is {self.name}. I'm {self.age} years old and enrolled in {self.course} course.")

# student1 = Student("Yuvraj", 22, "BCA")
# student1.print_information()
# student2 = Student("Mahima", 21, "BA")
# student2.print_information()

# #Challenge 2 — Methods
# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
#     def introduce(self):
#         print(f"Hi, I'm {self.name}. I'm {self.age} and learning {self.course}.")
# student1 = Student("Yuvraj", 66, "Python")
# student1.introduce()

# Challenge 3 — Expense class
class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category
    # Challenge 4 — Expense method
    def display(self):
        print(f"{self.name} - ₹{self.amount} - {self.category}")
        
    # Challenge 5 — Update expense
    def update_amount(self, new_amount):
        self.amount = new_amount
    
    # Challenge 6 — Validation
    def validate_amount(self):
        if self.amount < 0:
            raise ValueError("Expense amount cannot be negative.")


coffee = Expense("Coffee", 150, "Food")
coffee.update_amount(400)
coffee.validate_amount()
coffee.display()
Housing = Expense("Housing", 3000, "Rent")
eggs = Expense("Eggs", 1000, "Food")

        