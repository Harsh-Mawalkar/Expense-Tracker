import datetime

class Expense:
    def __init__(self, amount=0, category='', description=''):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.datetime.now()

    def __repr__(self):
        return f"Amount: ₹{self.amount}, Category: {self.category}, Description: {self.description}, Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
