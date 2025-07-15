class Developer:
    def __init__(self, name, language, level):
        self.name = name
        self.language = language
        self.level = level.lower()

    def introduce(self):
        print(f"My name is {self.name},I am currently focusing on {self.language} as my language, and my current level in programming is {self.level}")

    def code(self):
        print("Writing code...")

    def promote(self):
        if self.level == "junior":
            self.level = "mid"
        elif self.level == "mid":
            self.level = "senior"
        else:
            print(f"{self.name} you are already a senior developer")

developer_info = Developer("Godwin", "Python", "mid")

developer_info.introduce()
developer_info.code()
developer_info.promote()