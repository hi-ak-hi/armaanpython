from getpass import getpass
from time import sleep
print("These are the directions:")
sleep(2)
print("1. Player 1 will type rock, paper, or siccors - then player 2 will type the same")
sleep(3)
print("2. Make sure you DON'T LOOK when the other person in typing")
sleep(3)
print("3. Sit on opposite sides and hand the device to the other person when you are done")
sleep(3)
print("4. What you type will not be shown to you for vewing, but don't worry its working.")
sleep(3)
print("5. Be careful what you type, because if you make a typo it'll crash.")

print("the game is starting...")
sleep(1)
print("5")
sleep(1)
print("4")
sleep(1)
print("3")
sleep(1)
print("2")
sleep(1)
print("1 \n\n")
sleep(1)
while True:
    game1=getpass("player 1, enter rock, paper, or siccors: ")
    game2=getpass("player 2, enter rock, paper, or siccors: ")
    game1 = game1.lower()
    game2 = game2.lower()
    if game1=="rock" and game2=="siccors":
        exit("player 1 won")
    if game1=="rock" and game2=="paper":
        exit("player 2 won")
    if game1=="siccors" and game2=="paper":
        exit("player 1 won")
    if game2=="rock" and game1=="siccors":
        exit("player 2 won")
    if game2=="rock" and game1=="paper":
        exit("player 1 won")
    if game2=="siccors" and game1=="paper":
        exit("player 2 won")
    if game1=="rock" and game2=="rock":
        print("you guys both entered rock")
    if game1=="paper" and game2=="paper":
        print("you guys both entered paper")
    if game1=="siccors" and game2=="siccors":
        print("you guys both entered siccors")
    else:
        print("ERROR")