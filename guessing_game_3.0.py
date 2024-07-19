def wrong():
     print("please enter a number between 0 and 100")
name=input ("what is your name - ")
print("hello, " + name)
print("today were playing a guessing game")

guess=input("this is the guesing game---please guess a number from 0 through 100 - ")

try:
    while int(guess)!=87:
        if int(guess)>=0:
            if int(guess)<=100:
                if int(guess)<20:
                    guess=input("you are very far, guess again - ")
                elif int(guess)<40:
                    guess=input("you are far, guess again - ")
                elif int(guess)<60:
                    guess=input("you are not close, but not far. guess again - ")
                elif int(guess)<80:
                    guess=input("you are close!!! guess again - ")
                else:
                    guess=input("you are soooo close, amlost there!!! guess again - ")
            else:
                wrong()
        else:
            wrong()
    print("good job, you guessed the number")
except:
    print("you didnt eneter a number")