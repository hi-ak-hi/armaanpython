try:
    length=int(input("How much stuff do you want:\n"))
    SL=[]
    unchecked=[]
    checked=[]
    for x in range(length):
        food=input("what food do you want:\n")
        check=input("do you want to check this item off;type yes or no:\n")
        if check=="yes" or check=="YES" or check=="Yes" or check=="yEs" or check=="yeS" or check=="YeS" or check=="YEs" or check=="yES":
            SL.append("✔️  "+food)
            checked.append("✔️  "+food)
        elif check=="no" or check=="NO" or check=="No" or check=="nO":
            SL.append("⭕  "+food)
            unchecked.append(food)
    for x in range(len(unchecked)):
        check2=input("do you want to check the item " + unchecked[x] + ":\n")
        if check2 == "yes" or check2 == "YES" or check2 == "Yes" or check2 == "yEs" or check2 == "yeS" or check2 == "YeS" or check2 == "YEs" or check2 == "yES":
            unchecked[x]="✔️  "+unchecked[x]
        elif check2 == "no" or check2 == "NO" or check2 == "No" or check2 == "nO":
            unchecked[x]="⭕  " + unchecked[x]
    def printlist(list,list2):
        for x in range(len(list)):
            print(list[x])
        for y in range(len(list2)):
            print(list2[y])
    printlist(unchecked, checked)
except:
    print("stop trynna break my code")