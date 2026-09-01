Challenge 8 — Think like an engineer
You previously had:
expenses = [
    {"name": "Coffee", "amount": 50, "category": "Food"},
    {"name": "Rent", "amount": 3000, "category": "Housing"}
]
and functions such as:
calculate_total(expenses)
Now you have:
class Expense:
    ...
Question:
What advantages could an Expense object provide over using a dictionary?

Ans. Now we can use the Expense object to create multiple objects and it helps in program readebility, it usebility. We dont have no longer to store the expense in a dictionary we can simply use the object pass the value and thats it.

Q1
What is a class?

Ans. A class is a blueprint that defines the data and behavior that objects created from it can have..

Q2
What is an object?

Ans. Obejcts are the instance of the class you can create numbers of objects from the class.

Q3
What's the difference between a class and an object?

Ans. Class is the actual blueprint and the object is instance created from the class.

Q4
What does __init__() do?

Ans. It is a special method python calls automatically when you create the object. It is commonly used to set the initial attributes.

Q5
What does self represent?

Ans. 'self' refers to the current object.

Q6
What's the difference between an attribute and a method?

Ans. Attribute is the data that a class is containing further a Method is the functionallity or the behaviour a class can perform.

Q7
What's the difference between an instance attribute and a class attribute?

Ans. Each objects gets it own copy value which we called instance attribute and Class attributes can be shared by all the objects.

Q8
Why might an Expense class be better than a dictionary for a larger application?

Ans. An Expense class keeps expense-related data and behavior together. It gives every expense a consistent structure and allows us to add behavior such as validation, updating the amount, and displaying the expense. This makes a larger application easier to organize and maintain..

Q9
Why is putting related data and behavior together useful?

Ans. Putting related data and behavior together makes a class represent one logical concept. This makes the code easier to understand, maintain, reuse, and extend.

Q10 — Engineering question
Imagine you're building an AI application and you have:
User
Document
Conversation
Message
Model
VectorStore
Why might classes be useful  for representing these things?

Ans. Classes can represent things such as Users, Documents, Conversations, Messages, Models, and VectorStores. Each object can keep its related data and behavior together, which makes a larger AI application easier to organize, maintain, and extend.