name=input("what's youre name: ")

file=open("CS50_name.txt","w")#w makes whatever you put in change the file
file.write(name)
file.close()