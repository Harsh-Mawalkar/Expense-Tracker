def expense_logger(*args, **kwargs):
    print("\n📘 Expense Log:")

    for i, arg in enumerate(args, start=1):
        print(f"{i}. {arg}")

    print("🔧 Additional Info:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")



