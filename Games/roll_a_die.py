import random
count = 0   
rolls = []
roll = "yes"
while roll.lower() == "yes":
    roll=input("do you want to roll a die: ")
    if roll == "no":
        break
    if count == 0:
        die = random.randint(1,6)
        rolls.append(die)
        print(die)
        count += 1
    elif count > 0:
        die = random.randint(1,6)
        rolls.append(die)
        print(rolls[-2] + rolls[-1])
        count += 1
    else:
        print("ERROR")
print("Done")