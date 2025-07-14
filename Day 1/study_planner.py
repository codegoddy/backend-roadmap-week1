def motivate(name: str, goal: str, hours: int) -> str:
    if hours >=6:
        return f"{name}, you're grinding hard towards '{goal}' - unstoppable energy"
    elif hours >=3:
        return f"{name}, solid focus on '{goal}'. Keep going!"
    else:
        return f"{name}, even smal steps matter towards '{goal}'. stay focused!"


def main():
    print("Welcome to your study Planner!\n")

    name = str(input("Enter your name: "))
    goal = str(input("Enter your goal: "))

    try:
        hours = int(input("How many hours will you study today? "))
    except ValueError:
        print("Please enter a valid number of hours.")
        return

    message = motivate(name,goal,hours)
    print("\n" + message)

if __name__ == "__main__":
    main()