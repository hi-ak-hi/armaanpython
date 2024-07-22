guess = input("guess a number between 1 and 10. you have one chance")
#one way of doing it
'''if guess<=10 and guess>7 or guess>=0 and guess<7: 
    print("sorry, you didnt guess it")
else:
    print("you got it")'''
#beter way
if int(guess)<=10 and int(guess)>7 or int(guess)>=0 and int(guess)<7: 
    exit("sorry, you didnt guess it")

print("you got it")