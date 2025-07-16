from datetime import datetime


class Calculator:
    def __init__(self):
        self.calc = []

    def addition(self):
        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
            result = num1 + num2
            self.calc.append(result)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("calc_history.txt", "a") as file:
                file.write(f"[{timestamp}] {num1} + {num2} = {result:.2f}\n")

        except ValueError:
            print("⚠️ Please enter a valid number.")

    def subtraction(self):
        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
            result = num1 - num2
            self.calc.append(result)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("calc_history.txt", "a") as file:
                file.write(f"[{timestamp}] {num1} - {num2} = {result:.2f}\n")

        except ValueError:
            print("⚠️ Please enter a valid number.")

    def multiplication(self):
        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
            result = num1 * num2
            self.calc.append(result)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("calc_history.txt", "a") as file:
                file.write(f"[{timestamp}] {num1} x {num2} = {result:.2f}\n")

        except ValueError:
            print("⚠️ Please enter a valid number.")

    def division(self):
        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
            result = num1 / num2
            self.calc.append(result)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("calc_history.txt", "a") as file:
                file.write(f"[{timestamp}] {num1} ÷ {num2} = {result:.2f}\n")

        except ValueError:
            print("⚠️ Please enter a valid number.")
        except ZeroDivisionError:
            print("🚫 A number cannot be divided by zero.")

    def history(self):
        print("\n📜 Past Calculations:")
        try:
            with open("calc_history.txt", "r") as file:
                history = file.read()
                print(history if history else "No history yet.")
        except FileNotFoundError:
            print("No history file found yet.")


# Run the calculator
calculator = Calculator()

while True:
    print("\n🔢 Welcome to your personal calculator\n")
    print("[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")
    print("[5] View History")
    print("[6] Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        calculator.addition()
    elif choice == "2":
        calculator.subtraction()
    elif choice == "3":
        calculator.multiplication()
    elif choice == "4":
        calculator.division()
    elif choice == "5":
        calculator.history()
    elif choice == "6":
        print("👋 Goodbye!")
        break
    else:
        print("⚠️ Please enter a valid option.")
