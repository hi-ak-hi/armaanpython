from random import randint
SecNum=randint(1,100)

guess=int(input("please guess a number from 1 to 100: "))

while guess!=SecNum:
    if guess>=1 and guess<=100:
        if SecNum > guess:
            print("guess higher")   
        if SecNum < guess:
            print("guess lower")
        guess=int(input("guess a new number: "))
    else:
        print("you guess was not between 1 and 100")
        guess = int(input("guess a new number: "))
print("good job, you guessed the number")
