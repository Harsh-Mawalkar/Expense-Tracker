from flask import Flask, render_template, request, redirect, url_for, jsonify
from Expense import Expense, expense_logger, expense_stream
from decorator import log_function_call
import datetime

app = Flask(__name__)
expenses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
@log_function_call
def add_expense():
    category = request.form['category']
    description = request.form['description']
    amount = float(request.form['amount'])

    expense = Expense(amount, category, description)
    expenses.append(expense)
    return redirect(url_for('view_expenses'))

@app.route('/high')
def high_expenses():
    high = [e for e in expenses if e.amount > 1000]
    return render_template('view.html', expenses=high)

@app.route('/view')
@log_function_call
def view_expenses():
    if not expenses:
        return jsonify({"message": "No expenses recorded yet."}), 200

    stream = expense_stream(expenses)
    streamed_data = [str(exp) for exp in stream]

    return render_template('view.html', expenses=expenses)

@app.route('/summary')
def summary():
    # Group expenses by category
    from collections import defaultdict

    category_summary = defaultdict(lambda: {'total': 0, 'expenses': []})

    for expense in expenses:
        category_summary[expense.category]['total'] += expense.amount
        category_summary[expense.category]['expenses'].append(expense)

    return render_template('summary.html', category_summary=category_summary)

@app.route('/log')
def log_summary():
    sample_notes = ["Groceries", "Fuel", "Snacks"]
    extra_info = {
        "date": datetime.datetime.now().strftime("%d-%m-%Y %H:%M"),
        "count": len(expenses),
        "user": "Test User"
    }
    expense_logger(*sample_notes, **extra_info)
    return "Logged expense summary! Check your console."

if __name__ == '__main__':
    app.run(debug=True)