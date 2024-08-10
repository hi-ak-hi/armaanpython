number=int(input("enter a number: "))
operation=input("enter a, s, m, d, sq, or e: \n a is addition, \n s is subtraction, \n m is multiplication, \n d is division, \n sq is square root, \n e is exponent: \n")
if operation=="sq" or operation=="SQ" or operation=="Square Root" or operation=="square root":
    answer=number**0.5
    print("the square root of",number,"is",answer)
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
answers=[]
while True:
    test=input("do you want to enter another opperation:")
    if test=="no":
        print("ok")
    if test=="yes" or test=="Yes":
        operation2=input("enter a, b, c, d, e, or f : \n a is addition, \n b is subtraction, \n c is multiplication, \n d is division, \n e is square root, \n f is exponent:\n ")
        number=int(input("enter a number:"))
        if operation2=="a" or operation2=="add" or operation2=="addition":
            newanswer=answer+number
            plus = "+"
            answers.append(answer, plus, number,"=",newanswer)
            print(answers[])
            answer=newanswer
        if operation2=="b" or operation2=="minus" or operation2=="subtraction":
            newanswer=answer-number
            answers.append(answer,"-",number,"=",newanswer)
            for answer in answers:
                print(answer)
            answer=newanswer
        if operation2=="c" or operation2=="times" or operation2=="multiplication":
            newanswer=answer*number
            answers.append(answer,"*",number,"=",newanswer)
            for answer in answers:
                print(answer)
            answer=newanswer
        if operation2=="d" or operation2=="divide" or operation2=="divided by":
            newanswer=answer/number
            answers.append(answer,"/",number,"=",newanswer)
            for answer in answers:
                print(answer)
            answer=newanswer
        if operation2=="f" or operation2=="exponent" or operation2=="to the power of":
            newanswer=answer**number
            answers.append(answer,"^",number,"=",newanswer)
            for answer in answers:
                print(answer)
            answer=newanswer