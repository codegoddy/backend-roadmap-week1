name = str(input("What is your name? "))
print(f"\nWelcome, {name}\n")

try:
    num_of_tasks = int(input("How many tasks do you want to track today? "))
except ValueError:
    print("Enter a valid number")
    exit()

tasks = []

for i in range (num_of_tasks):
    print(f"\nTask {i + 1}:")
    task = str(input("What did you work on? "))

    try:
        time = int(input("How many minutes? "))
    except ValueError:
        print("Please enter a valid number")
        continue

    tasks.append((task, time))

print(f"\nSummary for {name}:\n")

total = 0

for task, time in tasks:
    print(f"-{task}: {time} mins")
    total += time

print(f"\nTotal time spent: {total} minutes\n Great work! You crushed it today")