from getpass import getpass

username=input("enter a username: ")
password=getpass("enter a password: ")

while True:
    veiwing=input("do you want to see your password: ")
    if veiwing=="yes" or veiwing=="Yes":
        print(password)
        change=input("do you want to change it: ")
        if change=="yes" or change=="Yes":
            password=getpass("enter a password: ")
        
    if veiwing=="no" or veiwing=="No":
        break

print("ok, your all set,",username)

        