class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.category = category
        
        self._validate_amount(amount)
        self.amount = amount
    def _validate_amount(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Expense amount must be a number.")
        if amount < 0:
            raise ValueError("Expense amount cannot be negative.")
    def update_amount(self, new_amount):
        self._validate_amount(new_amount)
        self.amount = new_amount

    def display(self):
        print(
            f"{self.name} - ₹{self.amount} - {self.category}"
        ) 
coffee = Expense("Coffee", 150, "Food")

coffee.display()

coffee.update_amount(400)
coffee.update_amount(-500)