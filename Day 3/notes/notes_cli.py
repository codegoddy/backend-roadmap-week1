from datetime import datetime

class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display(self):
        print(f"{self.title} - {self.content}")

class NoteApp:
    def __init__(self):
        self.notes = []

    def add_note(self):
        title = input("Title: ")
        content = input("Content: ")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = Note(title, content)

        self.notes.append(note)
        print("Note added successfully")
        with open("notes.txt", "a") as file:
            file.write(f"{timestamp} - {title} - {content}")

    def view_notes(self):
        try:
            with open("notes.txt", "r") as file:
                notes = file.readlines()
                if not notes:
                    print("no notes yet.")
                    return
                print("\nYour Notes: ")
                for i, line in enumerate(notes, 1):
                    print(f"{i}. {line.strip()}")
        except FileNotFoundError:
            print("No notes file found yet.")


    def update_note(self):
        self.view_notes()
        try:
            index = int(input("Which note number do you want to update? ")) -1
            with open("notes.txt", "r") as file:
                notes = file.readlines()

            if 0 <= index < len(notes):
                new_title = input("New title: ")
                new_content = input("New content: ")
                notes[index] = f"{new_title} - {new_content}\n"

                with open("notes.txt", "w") as file:
                    file.writelines(notes)

                print("Note updated successfully.")
            else:
                print("Invalid note number.")

        except(ValueError, FileNotFoundError):
            print("Error updating note. Please try again.")

    def delete_note(self):
        self.view_notes()
        try:
            index = int(input("Which note number do you want to delete? ")) - 1
            with open("notes.txt", "r") as file:
                notes = file.readlines()

            if 0 <= index < len(notes):
                deleted = notes.pop(index)

                with open("notes.txt", "w") as file:
                    file.writelines(notes)

                print(f"Deleted note: {deleted.strip()}")
            else:
                print("Invalid note number.")
        except (ValueError, FileNotFoundError):
            print("Error deleting note. Please try again.")


notes = NoteApp()

while True:
    print("\n📒 Welcome to NoteApp")
    print("[1] Add Note")
    print("[2] View Notes")
    print("[3] Update Note")
    print("[4] Delete Note")
    print("[5] Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        notes.add_note()
    elif choice == "2":
        notes.view_notes()
    elif choice == "3":
        notes.update_note()
    elif choice == "4":
        notes.delete_note()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")






