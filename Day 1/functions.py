def format_sum(total: int) -> str:
    return f"The sum is {total}"

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

total = n1 + n2
print(format_sum(total))

if n1 % 2 == 0 and n2 % 2 == 0:
    print("Even Sum!")          # stretch‑goal message
elif total % 2 == 0:
    print(f"Even num, {total}")
else:
    print(f"Odd num, {total}")
