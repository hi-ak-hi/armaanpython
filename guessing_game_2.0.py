name=input ("what is your name - ")
print("hello, " + name)
print("today were playing a guessing game")

guess=input("this is the guesing game---please guess a number from 1 through 100 - ")

try:
    while int(guess)!=87:
        if int(guess)>60:
            if int(guess)<100:
                guess=input("your very close, but try aain - ")
        elif int(guess)<61:
            if int(guess)<100:
                guess=input("you are far from the number, please guess again - ")
    print("good job, you guessed the number")
except:
    print("you didnt eneter a number")