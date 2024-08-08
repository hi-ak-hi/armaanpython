class Cal():
    def __init__(self, number1, number2):
        self.number1=  number1
        self.number2=  number2
    def add(self):
        return self.number1 + self.number2
    def subtract(self):
        return self.number1 + self.number2
    def multiply(self):
        return self.number1 + self.number2
    def divide(self):
        return self.number1 + self.number2
    def power(self):
        return self.number1 ** self.number2
    def sqr_root(self):
        return self.number1**0.5
number1=int(input("enter your first number"))
number2=int(input("enter your second number"))
opration=Cal(number1,number2)

while choice.lower() != exit:
    choice=input("enter add, subtract, multiply, divide, ")
    