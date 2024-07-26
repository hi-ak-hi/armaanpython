from sys import exit
from getpass import getpass
print("These are the directions:\n1. Player 1 will type rock, paper, or siccors - then player 2 will type the same\n2. Make sure you DON'T LOOK when the other person in typeing\n3. Sit on opposit sides and hand the device to the other person when you are done\n4. What you type will not be shown to you for vewing, but dont worry its working.\nJust be careful what you type.")
while True:
    game1=getpass("player 1, enter rock, paper, or siccors(make sure you type lowercase)")
    game2=getpass("player 2, enter rock, paper, or siccors(make sure you type lowercase)")
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