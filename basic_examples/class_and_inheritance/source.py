# imports
from dataclasses import dataclass
# ===============================================================
# global variables and constants
fruit_list = []

# ===============================================================
# classes

class Animal:
    """Base class"""
    def __init__(self, name, age):
        self.name = name
        self._age = age  # protected attribute

    def speak(self):
        return f"{self.name} makes a sound."

    def info(self):
        return f"{self.name}, {self._age} years old"

class Dog(Animal):
    """Dog inherits from Animal"""
    def speak(self):  # method overriding
        return f"{self.name} says Woof!"

# ===============================================================
# Dataclass example

@dataclass
class Fruit:
    """Simple data container, like a C struct"""
    name: str
    color: str
    origin: str
    weight: str

# ===============================================================
# Helper functions

def show_animal(animal):
    print("Animal info:", animal.info())
    print("Speak:", animal.speak())
    print("")

def show_fruit():
    if len(fruit_list) == 0:
        print("fruit list is empty")
        return
    c = 0
    for fruit in fruit_list:
        c = c + 1
        print(f"{c}. {fruit}")

def add_fruit():
    f = Fruit(
        name = input("fruit name? "),
        color = input("fruit color? "),
        origin = input("fruit origin? "),
        weight = input("fruit weight? ")
    )

    fruit_list.append(f)

# ===============================================================
# Main interactive routine

def main():
    print("this examples illustartes basic concepts of classes\n")

    while True:
        print(" 1. Show generic Animal")
        print(" 2. Show Dog")
        print(" 3. Show Fruit (dataclass)")
        print(" 4. Add a fruit")
        print(" 5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            a = Animal("Generic", 5)
            show_animal(a)
        elif choice == '2':
            d = Dog("Buddy", 3)
            show_animal(d)
        elif choice == '3':
            show_fruit()
        elif choice == '4':
            add_fruit()
        elif choice == '5':
            print("Exiting...")
            return
        else:
            print("[Error] Invalid choice.\n")


if __name__ == "__main__":
    main()