from Expense import Expense
from functools import reduce
from utils import print_expense_report
import datetime


def recent_expenses(expenses, days=7):
    cutoff = datetime.datetime.now() - datetime.timedelta(days=days)
    for expense in expenses:
        if expense.date >= cutoff:
            yield expense


def main():
    expenses = []

    while True:
        print("Welcome to expense tracker")
        print("Choose your input")
        print(" 1. Add Expense")
        print(" 2. View All Expenses")
        print(" 3. Filter Expense by category")
        print(" 4. Calculate Total Expense")
        print(" 5. Generate Custom Report")
        print(" 6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            category = ''
            while True:
                print("Select from these categories:")
                print("1. Food")
                print("2. Travel")
                print("3. House")
                print("4. Other")
                category_option = input("Enter the category number (1/2/3/4): ")

                if category_option == '1':
                    category = 'Food'
                    break
                elif category_option == '2':
                    category = 'Travel'
                    break
                elif category_option == '3':
                    category = 'House'
                    break
                elif category_option == '4':
                    category = 'Other'
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")

            description = input("Enter the description of the expense: ")
            try:
                amount = float(input("Enter the amount: $"))
            except ValueError:
                print("Invalid input! Please enter a valid number for the amount.")
                continue

            expense = Expense(amount, category, description)
            expenses.append(expense)
            print("Expense added successfully.")

        elif choice == '2':
            print("\nExpenses in the last 7 days:")
            found = False
            for i, exp in enumerate(recent_expenses(expenses), 1):
                print(f"{i}. {exp}")
                found = True
            if not found:
                print("No recent expenses found.")

        elif choice =='3':
            filter_category = ''
            
            while True:
                print("Select from these categories:")
                print("1. Food")
                print("2. Travel")
                print("3. House")
                print("4. Other")
                category_option = input("Enter the filter category number (1/2/3/4): ")

                if category_option == '1':
                    filter_category = 'Food'
                    break
                elif category_option == '2':
                    filter_category = 'Travel'
                    break
                elif category_option == '3':
                    filter_category = 'House'
                    break
                elif category_option == '4':
                    filter_category = 'Other'
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            
            filtered = filter(lambda exp : exp.category.lower() == filter_category.lower(),expenses)
            filtered_expenses = list(filtered)

            if not filtered_expenses:
                print("No expenses found in this category.")
            else:
                print(f"Expenses in category '{filter_category}':")
                for i, exp in enumerate(filtered_expenses, 1):
                    print(f"{i}. {exp}")

        elif choice == '4':
            if not expenses:
                print("No expense record")
            else:
                total = reduce(lambda acc,exp : acc + exp.amount ,expenses,0)
                print(f"\n Total Expense : ₹{total:.2f}")
            
        elif choice == '5':
            print("Choose report options:")
            print("1. Normal Report")
            print("2. Uppercase Report")
            print("3. Detailed Report with Total")
            option = input("Enter your choice: ")

            if option == '1':
                print_expense_report(*expenses)
            elif option == '2':
                print_expense_report(*expenses, uppercase=True)
            elif option == '3':
                print_expense_report(*expenses, detailed=True, show_total=True)
            else:
                print("Invalid option.")



        
        elif choice == '6':
            print("Exiting... Goodbye!")
            break

    
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()





            
            


