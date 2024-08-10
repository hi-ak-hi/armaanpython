import random
while True:
    roll=input("do you want to roll a die: ")
    if roll=="yes":
        die = random.randint(1,6)
        print(die)
    if roll == "no":
        break 