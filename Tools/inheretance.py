class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):#(mammal) means inheret all of mammal
    def bark(self):
        print("BARK!")
    


class Cat(Mammal):#(mammal) means inheret all of mammal
    def meow(self):
        print("MEOW!")


dog1=Dog()
dog1.walk
dog1.bark

cat1=Cat()
cat1.walk
cat1.meow