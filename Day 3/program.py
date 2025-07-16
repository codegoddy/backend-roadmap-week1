from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

try:
    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number2: "))

    result = number1/number2
except ValueError:
    print("Please input a valid number!")
    exit()
except ZeroDivisionError:
    print("A number can't be divided by zero!")
    exit()
with open("results.txt", "a") as file:
    file.write(f"[{timestamp}] {number1} ÷ {number2} = {result:.2f}\n")
print("\n Past Calculations:")
with open("results.txt", "r") as file:
    history = file.read()
    print(history)