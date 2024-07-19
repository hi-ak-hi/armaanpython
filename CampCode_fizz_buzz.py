#adding 1 to a so it starts at 1
'''for a in range(10):
  print(a+1)'''
#doing it from 1-11
#it does the first one but not the second one
'''for a in range(1,11):
  print(a)'''
#the same thing as the one aboze, but the third one shows how many it count by, for example  it does 1 3 5 etc.
'''for a in range(1,11,2):
  print(a)'''
#% sign prints the remandair of the number
'''x =10%3
print(x)

y=15%5
print(y)'''

for a in range(1,101):
  if a%3==0:
    print("fizz")
  if a%5==0:
    print("buzz")
  if a%3!=0 and a%5!=0:
      print(a)