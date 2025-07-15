class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

    def display(self):
        print(f"{self.description} - KSH.{self.amount}")


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        description = input("What did you spend on? ")
        try:
            amount = float(input("How much? "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            return
        expense = Expense(description, amount)
        self.expenses.append(expense)
        print("✅ Expense added!")

    def view_expense(self):
        if not self.expenses:
            print("No expenses add yet!")
            return
        for i, expense in enumerate(self.expenses, start=1):
            print(f"{i}. ", end="")
            expense.display()

    def summary(self):
        total_expense = len(self.expenses)
        total_spent = 0
        max_expense = None

        for expense in self.expenses:
            total_spent += expense.amount
            if not max_expense or expense.amount > max_expense.amount:
                max_expense = expense

        if total_expense == 0:
            print("No Expenses tracked yet.")
            return

        print("\nSummary:")
        print(f"Total expenses: {total_expense}")
        print(f"Total spent: {total_spent}")
        print(f"Highest expense: {max_expense}")


expense_track = ExpenseTracker()

while True:
    print("\nWelcome to your expense tracker\n")
    print("[1] Add Expense")
    print("[2] View Expense")
    print("[3] Summary")
    print("[4] Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        expense_track.add_expense()
    elif choice == "2":
        expense_track.view_expense()
    elif choice == "3":
        expense_track.summary()
    elif choice =="4":
        print("Goodbye!")
        break
    else:
        print("please choose a valid option")


