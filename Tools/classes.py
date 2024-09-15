class Monster:
    #dunder methods
    def __init__(self, health, energy):
        print("The monster was created")
        self.health = health
        self.energy = energy
    
    def __len__(self):
        return self.health
    
    def __abs__(self):
        return self.energy
    
    def __call__(self):
        print("The monster was called")
    
    def __add__(self, other):
        print(self.health + other)

    def __str__(self):
        return f"A monster with {self.health} health and {self.energy} remaning energy"
    #methods
    def atack(self, damage):
        print("ATACK!!!")
        print(f"You took {damage} damage")
        self.energy -= 20
        print(f"You now have {self.energy} energy")
    
    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")
    
monster1 = Monster(10, 20)



#using dunder methods
'''
__init__
monster = Monster()
> actavated by calling the class

__len__
print(len(monster))
>actaveted by using len()

__abs__
print(abs(monster))
>actaveted by using abs()
>

__call__
monster()
>using the function of the object

__add__
print(monster +  10)
>in this case adds 10 to health

__str__
print(monster)
> prints the string
'''