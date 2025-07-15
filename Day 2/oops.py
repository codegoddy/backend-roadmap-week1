# file: dog_example.py

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says: Woof woof!")

    def info(self):
        print(f"{self.name} is a {self.breed}")


# Create a dog
my_dog = Dog("Bolt", "German Shepherd")
my_dog.bark()
my_dog.info()
