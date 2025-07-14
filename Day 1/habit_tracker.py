name = str(input("What is your name? "))
print(f"\nWelcome, {name}!\n")

try:
    num_of_habit = int(input("How many habits are you tracking today? "))
except ValueError:
    print("Please input a valid number!")
    exit()

habits = []  # lowercase by convention

for i in range(num_of_habit):
    print(f"\nHabit {i + 1}:\n")

    habit = input("Name of habit: ")
    completed = input("Did you complete it? (yes/no): ").lower()

    # Validate input
    if completed not in ["yes", "no"]:
        print("❌ Invalid input — skipping this habit.")
        continue

    habits.append((habit, completed))

print(f"\nHabit summary for {name}\n")

completed_count = 0

for habit_name, done in habits:
    checkbox = "✓" if done == "yes" else "✗"
    print(f"{checkbox} {habit_name}")

    if done == "yes":
        completed_count += 1

total_habits = len(habits)
if total_habits == 0:
    print("\nNo valid habits recorded.")
    exit()

percent = (completed_count / total_habits) * 100
print(f"\n You have completed {completed_count}/{total_habits} habits({int(percent)}%)")