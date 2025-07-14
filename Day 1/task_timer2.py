print("Welcome to Task Timer ⏱️")

tasks = []

while True:
    print("\n[1] Add Task")
    print("[2] View Tasks")
    print("[3] Remove Task")
    print("[4] Exit Task")

    choice = input("Choose an option: ")

    if choice == "1":
        task_name = input("Task name: ")
        try:
            time_estimate = int(input("Time estimate (minutes): "))
        except ValueError:
            print("❌ Please input a valid number")
            continue

        tasks.append({
            "name": task_name,
            "time": time_estimate
        })
        print("✅ Task added.")

    elif choice == "2":
        if not tasks:
            print("🛑 You don't have any tasks yet.")
            continue

        print("\n📝 Tasks:")
        total_time = 0

        for task in tasks:
            name = task["name"]
            time = task["time"]
            print(f"- {name} — {time} mins")
            total_time += time

        total_tasks = len(tasks)
        print(f"\n⏳ Total time: {total_time} mins")
        print(f"📌 Total tasks: {total_tasks}")

    elif choice == "3":
        task_to_remove = input("Enter the name of the task to remove: ")

        found = False
        for task in tasks:
            if task["name"].lower() == task_to_remove.lower():
                tasks.remove(task)
                print(f"✅ Removed '{task_to_remove}' from your list.")
                found = True
                break

        if not found:
            print(f"❌ Could not find '{task_to_remove}' in your list.")

    elif choice == "4":
        print("👋 Goodbye — crush those tasks, Code Goddy!")
        break

    else:
        print("❌ Invalid option. Try again.")
