class Habit:
    def __init__(self, name):
        self.name = name
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def display(self):
        checkbox = "✓" if self.is_done else "✗"
        print(f"{checkbox} {self.name}")

class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, name):
        habit_name = Habit(name)
        self.habits.append(habit_name)
    def view_habits(self):
        if not self.habits:
            print("No habits recorded yet")
            return
        for i, habit in enumerate(self.habits, start=1):
            print(f"{i}. ", end="")
            habit.display()
    def mark_done(self, index):
        actual_index = index - 1
        if 0 <= actual_index < len(self.habits):
            habit = self.habits[actual_index]
            habit.mark_done()
            print(f"✓ Marked '{habit.name}' as complete.")
        else:
            print("❌ Invalid task number.")

    def summary(self):
        total_habits = len(self.habits)
        total_complete = 0

        for habit in self.habits:
            if habit.is_done:
                total_complete += 1

        if total_habits == 0:
            print("No habits tracked yet.")
            return

        percent = (total_complete / total_habits) * 100

        print("\n📋 Daily Habit Summary\n------------------------")
        print(f"🧮 Total Habits: {total_habits}")
        print(f"✅ Completed: {total_complete}")
        print(f"📊 Progress: {percent:.1f}%")
        print(f"\nGreat job! Keep going 💪")


habits = HabitTracker()

while True:
    print("\nWelcome to your habit tracker\n")

    print("[1] ➕ Add Habit")
    print("[2] 📋 View Habits")
    print("[3] ✅ Mark Habit as Done")
    print("[4] 📊 Summary")
    print("[5] ❌ Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        habit_name = input("Habit: ")
        if habit_name.strip() == "":
            print("Please enter a valid habit name.")
            continue
        habits.add_habit(habit_name)
        print("Habit added successfully!")
    elif choice == "2":
        habits.view_habits()
    elif choice == "3":
        try:
            habit_number = int(input("Which task number to complete: "))
            habits.mark_done(habit_number)
        except ValueError:
            print("⚠️ Please enter a valid number.")
    elif choice == "4":
        habits.summary()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please enter a valid option")



