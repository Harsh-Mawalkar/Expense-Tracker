import datetime

def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"\n[LOG] Function '{func.__name__}' called at {datetime.datetime.now()}")
        return func(*args, **kwargs)
    return wrapper
@log_action
def print_expense_report(*expenses, **options):
    print("\nExpense Report:\n" + "-"*30)

    if not expenses:
        print("No expenses to display.")
        return

    for expense in expenses:
        if options.get("uppercase", False):
            print(str(expense).upper())
        elif options.get("detailed", False):
            print(f"-> Category: {expense.category}, Amount: ₹{expense.amount}, Description: {expense.description}, Date: {expense.date}")
        else:
            print(expense)

    if options.get("show_total", False):
        from functools import reduce
        total = reduce(lambda acc, exp: acc + exp.amount, expenses, 0)
        print("-"*30)
        print(f"Total: ₹{total:.2f}")
