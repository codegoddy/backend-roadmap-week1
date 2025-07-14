name = input("What is your name? ")
print(f"\nWelcome, {name}!\n")

try:
    num_expenses = int(input("How many expenses do you want to recode today? "))
except ValueError:
    print("Please enter a valid number")
    exit()

expenses = []

for i in range(num_expenses):
    print(f"\nExpense {i + 1}:")
    item = input("What did you spend on? ")

    try:
        amount = float(input("How much did it cost? "))
    except ValueError:
        print("Invalid amount. Skipping this expense")
        continue

    expenses.append((item, amount))

print(f"\nSummary for {name}:")

total = 0

for item, amount in expenses:
    print(f"- {item}: {amount}")
    total += amount

print(f"\nTotal Spent: {total}")