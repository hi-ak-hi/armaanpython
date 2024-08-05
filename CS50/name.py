name=input("what's youre name: ")

file=open("name.2.txt","a")#a makes whatever you put in add/append to the file(w dosent)
file.write(f"\n{name}")# \n prints one new line in txt file( file.write(name) would not do that).
file.close()