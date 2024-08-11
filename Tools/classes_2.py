class Person:
    def __init__(self, age, height, weight, first_name, last_name):
        self.age = age
        self.height = height
        self.weight = weight
        self.first_name = first_name
        self.last_name = last_name
    def walk(self):
        print("walking...")
    def running(self):
        print("running...")

age=input("how old are you: ")
height=input("how tall are you: ")
weight=input("how much do you weigh: ")
first_name=input("whats you first name: ")
last_name=input("whats your last name: ")

user=Person(age, height, weight, first_name, last_name)
print("This is", user.first_name.title, user.last_name.title + ", and he's/she's", user.age + ". ", end="")
print("He/she whiegh's", user.wieght + ", and is", user.height, "tall.")