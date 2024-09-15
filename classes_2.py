'''def add(a, b):
    return a + b

class Test:
    def __init__(self, add_function):
        self.add_function = add_function

test = Test(add_function = add)k
print(test.add_function(6, 4))'''

class Monster:
    def __init__(self, func):
        self.func = func

class Atacks:
    def bite(self):
        print("bite")
    def strike(self):
         print("strike")
    def slash(self):
        print("slash")
    def kick(self):
        print("kick")

atacks = Atacks()
monster = Monster(func = atacks.bite)
monster.func()