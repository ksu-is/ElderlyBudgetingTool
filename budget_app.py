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
