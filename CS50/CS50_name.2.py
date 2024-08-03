name=input("what's youre name: ")

file=open("CS50_name.2.txt","a")#a makes whatever you put in add/append to the file
file.write(f"{name}\n")# /n prints one new line in txt file( file.write(name) would not do that).
file.close()