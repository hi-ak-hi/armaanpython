def wrong():
    print('sorry, but you have not entered 1 or 2')
athmu=input('if you are a musicain, enter 1, and if you are a athalete enter 2 - ')
try:
    ans1 = int(athmu)
except:
    ans1=-1
if ans1 > 0:
    if int(athmu)==1:
        ints=input('ok, what instrement(s) do you play, if guitar enter 1,if other(s) enter 2 - ')
        try:
            ans2=int(ints)
        except:
            ans2=-1
        if ans2>0:
            if ans2==1:
                print('good job!!! ps-I personaly think it is the best instrement-shh!!!')
                print('bye')
                
            elif ans2==2:
                input('ok, then what instrement do you play? - ')
                print('wow, thats a cool instrement!!!')
                print('bye')
                
            else:
                wrong()
        else:
            wrong()
    elif int(athmu)==2:
        athl=input('are you a swimmer, if yes enter 1, if no enter 2 - ')
        try:
            ans3=int(athl)
        except:
            ans3=-1
        if ans3>0:
            if ans3==1:
                swim=input('what is your favorite stroke - ')
                print('wow, i love that stroke!!!')
                print('bye')
                
            elif ans3==2:
                input('ok, what sport(s) do you play - ')
                print('wow, that sport is fun!!!')
                print('bye')
                
            else:
                wrong()
        else:
            wrong()
    else:
        wrong()
else:
    wrong()
