import datetime

def expense_logger(*args, **kwargs):
    print("\n📘 Expense Log:")
    for i, arg in enumerate(args, start=1):
        print(f"{i}. {arg}")

    print("🔧 Additional Info:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def expense_stream(expense_list):
    for expense in expense_list:
        yield expense

class Expense:
    def __init__(self, amount=0, category='', description=''):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.datetime.now()

    def __repr__(self):
        return f"Amount: ₹{self.amount}, Category: {self.category}, Description: {self.description}, Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}"