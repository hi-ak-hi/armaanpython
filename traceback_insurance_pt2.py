number=input('enter a nuber')
#user mabey no enter number, so insurance
try:
    answr=int(number)
except:
    #means if not work
    answr=-1
if answr>0:
    print('nice work')
else:
    print('not a number')
