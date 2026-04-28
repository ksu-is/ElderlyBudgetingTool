print("Simple Budgeting App for Elderly Users")

income = float(input("Enter your monthly income: $"))

expenses = []

while True:
    expense = input("Enter an expense amount or type done to finish: ")

    if expense.lower() == "done":
        break

    expenses.append(float(expense))

total_expenses = sum(expenses)
remaining_balance = income - total_expenses

print("\nBudget Summary")
print("Monthly Income: $", income)
print("Total Expenses: $", total_expenses)
print("Remaining Balance: $", remaining_balance)

# budget_app.py

print("Welcome to the Simple Budgeting App")
print("This program helps users track income, expenses, and remaining money.")

income = float(input("Enter your monthly income: $"))

expenses = []

while True:
    expense = input("Enter an expense amount or type done to finish: ")

    if expense.lower() == "done":
        break

    expenses.append(float(expense))

total_expenses = sum(expenses)
remaining_balance = income - total_expenses

print("\nCalculating your budget...")

print("\nBudget Summary")
print("----------------------")
print(f"Monthly Income: ${income:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")

if remaining_balance < 0:
    print("Warning: Your expenses are higher than your income.")
else:
    print("Good job. You are staying within your budget.")
