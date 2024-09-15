from getpass import getpass

username=input("enter a username: ")
password=getpass("enter a password: ")

while True:
    veiwing=input("do you want to see your password: ").lower()
    if veiwing=="yes":
        print(password)
        change=input("do you want to change it: ").lower()
        if change=="yes":
            password=getpass("enter a password: ")
        
    if veiwing=="no":
        break

print("ok, your all set,",username)