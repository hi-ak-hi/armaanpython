from sys import exit
number=int(input("enter a number: "))
operation=input("enter a, s, m, d, sq, or e: \n a is addition, \n s is subtraction, \n m is multiplication, \n d is division, \n sq is square root, \n e is exponent: \n")
operation = operation.lower()
if operation=="sq" or operation=="square root":
    answer=number**0.5
    exit("the square root of",number,"is",answer)
elif operation=="a" or operation=="s" or operation=="m" or operation=="d" or operation=="e":
    number2=int(input("enter a number to add, subtract, multiply, or divide or make the exponent by the number you entered:")) 
    if operation=="a" or operation=="add" or operation=="addition":
        answer=number+number2
        print(number,"+",number2,"=",answer)
    if operation=="s" or operation=="minus" or operation=="subtraction":
        answer=number-number2
        print(number,"-",number2,"=",answer)
    if operation=="m" or operation=="times" or operation=="multiplication":
        answer=number*number2
        print(number,"*",number2,"=",answer)
    if operation=="d" or operation=="divide" or operation=="divided by":
        answer=number/number2
        print(number,"/",number2,"=",answer)
    if operation=="e" or operation=="exponent" or operation=="to the power of":
        answer=number**number2
        print(number,"^",number2,"=",answer)
while True:
    test=input("do you wanxt to enter another opperation:")
    test = test.lower()
    if test=="no":
        exit("ok")
    if test=="yes":
        operation2=input("enter a, b, c, d, or e: \n a is addition, \n b is subtraction, \n c is multiplication, \n d is division, e is exponent ")
        number=int(input("enter a number:"))
        if operation2=="a" or operation2=="add" or operation2=="addition":
            newanswer=answer+number
            print(answer, "+", number,"=",newanswer)
            answer=newanswer
        if operation2=="b" or operation2=="minus" or operation2=="subtraction":
            newanswer=answer-number
            print(answer,"-",number,"=",newanswer)
            answer=newanswer
        if operation2=="c" or operation2=="times" or operation2=="multiplication":
            newanswer=answer*number
            print(answer,"*",number,"=",newanswer)
            answer=newanswer
        if operation2=="d" or operation2=="divide" or operation2=="divided by":
            newanswer=answer/number
            print(answer,"/",number,"=",newanswer)
            answer=newanswer
        if operation2=="f" or operation2=="exponent" or operation2=="to the power of":
            newanswer=answer**number
            print(answer,"^",number,"=",newanswer)
            answer=newanswer

