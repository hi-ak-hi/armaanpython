name=input ("what is your name - ")
print("hello, " + name)
print("hello,",name)
print("today were playing a guessing game")

guess=input("this is the guesing game---please guess a number from 1 through 10 - ")

try:
    while int(guess)!=4:
        guess=input("sorry guess again - ")
    print("Good job sigma")
except:
    print("YOU STPUID FALUIRE YOU DIDNT ENTER A NUMBER")
        
        
    
    
    
