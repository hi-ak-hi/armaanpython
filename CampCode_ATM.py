balance=1000

try:
    while True:
        atm=input("\nclick a b c or d.\na is to check balance\nb is to deposit money\nc is to withdraw money\nd is to exit the atm\n")
        if atm=="a" or atm=="A":
            print("your balance is $",end="")
            print(balance)
        elif atm=="b" or atm=="B":
            add=int(input("how muchy money do you want to add: "))
            balance=balance+add
        elif atm=="c" or atm=="C":
            subtract=int(input("how much money do you want to withdraw: "))
            if subtract<=balance:
                balance=balance-subtract
            else:
                print("you are not allowed to take out that sum of money")
        elif atm=="d" or atm=="D":
            break
        else:
            print("you have to type a, b, c, or d")
except:
    print("enter a number please")