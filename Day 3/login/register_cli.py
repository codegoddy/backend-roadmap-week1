class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display(self):
        print(f"{self.username},{self.password}")

class Register:
    def __init__(self):
        self.users = []

    def register(self):

        username = input("Username: ")
        password = input("Password: ")

        user = User(username,password)

        self.users.append(user)
        user.display()
        with open("users.txt", "a") as file:
            file.write(f"{username},{password}\n")

class Login:
    def __init__(self):
        pass

    def login(self):
        print("🔐 Login\n")

        # 1. Ask for username and password
        username = input("Username: ")
        password = input("Password: ")

        found = False

        with open("users.txt", "r") as file:
            for line in file:

                line = line.strip()

                saved_username, saved_password = line.split(",")

                if username == saved_username and password == saved_password:
                    found = True
                    break

        if found:
            print("Login successful!")
        else:
            print("Invalid username or password")




user_log = Login()
user_reg = Register()

while True:
    print("Welcome to our app\n")
    print("[1] Login: ")
    print("[2] Register: ")
    print("[3] Exit: ")

    choice = input("Choose an option: ")

    if choice == "1":
        validation = input(f"Do you have an account(yes/no): ").lower()
        if validation == "yes":
            user_log.login()
        else:
            user_reg.register()
            continue

    elif choice == "2":
        user_reg.register()

    elif choice == "3":
        print("Goodbye!")
        exit()
    else:
        print("Please enter a valid option")







