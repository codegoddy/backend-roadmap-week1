class Task:
    def __init__(self, name, time_estimate):
        self.name = name
        self.time_estimate = time_estimate
        self.is_completed = False

    def mark_complete(self):
        self.is_completed = True

    def display(self):
        checkbox = "✓" if self.is_completed else "✗"
        print(f"{checkbox} {self.name} - {self.time_estimate} mins")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, time_estimate):
        task = Task(name, time_estimate)
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return

        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. ", end="")
            task.display()

    def complete_task(self, index):
        actual_index = index - 1
        if 0 <= actual_index < len(self.tasks):
            task = self.tasks[actual_index]
            task.mark_complete()
            print(f"✓ Marked '{task.name}' as complete.")
        else:
            print("❌ Invalid task number.")

    def remove_task(self, index):
        actual_index = index - 1
        if 0 <= actual_index < len(self.tasks):
            removed = self.tasks.pop(actual_index)
            print(f"🗑️ Removed '{removed.name}' from your list.")
        else:
            print("❌ Invalid task number.")


# 🧠 CLI Loop — use the TaskManager here
manager = TaskManager()

while True:
    print("\n📋 Welcome to your Task Manager")
    print("[1] Add Task")
    print("[2] View Tasks")
    print("[3] Complete Task")
    print("[4] Remove Task")
    print("[5] Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task_name = input("Enter task name: ")
        try:
            time_estimate = int(input("Time estimate (minutes): "))
            manager.add_task(task_name, time_estimate)
            print("✅ Task added!")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    elif choice == "2":
        manager.view_tasks()

    elif choice == "3":
        try:
            task_number = int(input("Which task number to complete: "))
            manager.complete_task(task_number)
        except ValueError:
            print("⚠️ Please enter a valid number.")

    elif choice == "4":
        try:
            task_number = int(input("Which task number to remove: "))
            manager.remove_task(task_number)
        except ValueError:
            print("⚠️ Please enter a valid number.")

    elif choice == "5":
        print("👋 Goodbye!")


    else:
        print("❌ Invalid option. Try again.")
