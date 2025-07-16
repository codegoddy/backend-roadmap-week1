try:
    number1 = int(input("Please input number1: "))
    number2 = int(input("Please input number2: "))

    result = number1 / number2

except ValueError:
    print("⚠️ Please input a valid number.")
    exit()

except ZeroDivisionError:
    print("⚠️ You can't divide by zero.")
    exit()

else:
    print(f"✅ Your answer is: {result}")
