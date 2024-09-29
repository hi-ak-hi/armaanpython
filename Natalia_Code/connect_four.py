import os
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"
board = []
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
for row in range(7):
    temp = []
    for spot in range(7):
        temp.append("[_]")
    board.append(temp)
player = "[" + RED + "o" + RESET + "]"
player2 =  RED + "o" + RESET
count = 0 
spot = [6,6,6,6,6,6,6]
def print_board(board):
    for x in range(7):
        for y in range(7):
            print(board[x][y], end="")
        print()
win = False
clear1 = False
while count < 49:
    if not clear1:
        clear_screen()
        clear1 = True
    print_board(board)
    col = int(input(player2 + " what column do you want to go in(1 - 7): "))
    col -= 1
    row = spot[col]
    if spot[row] == -1:
        print("you can't go there")    
    else:   
        spot[col]-= 1
        board[row][col] = player
        count += 1
    for x in range(7):
        for y in range(4):
            if board[y][x] == player and board[y+1][x] == player and board[y+2][x] == player and board[y+3][x] == player:
                print_board(board)
                print("player", player2, "won")
                win = True
                count = 50
                
    for x in range(7):
        for y in range(4):
            if board[x][y] == player and board[x][y+1]== player and board[x][y+2] == player and board[x][y+3] == player:
                print_board(board)
                print("player", player2, "won")
                win = True
                count = 50
    for x in range(4):
        for y in range(4):
            if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
                print_board(board)
                print("player", player2, "won")
                win = True
                count = 50
    for x in range(3, 7):
        for y in range(4):
            if board[x][y] == player and board[x-1][y+1] == player and board[x-2][y+2] == player and board[x-3][y+3] == player:
                print_board(board)
                print("player", player2, "won")
                win = True
                count = 50
    if player == "[" + RED + "o" + RESET + "]":
        player = "[" + YELLOW + "o" + RESET + "]"
        player2 = YELLOW + "o" + RESET
    else:
        player = "[" + RED + "o" + RESET + "]"
        player2 = RED + "o" + RESET
    if not win:
        clear_screen()
if count == 49:
    print_board()
    print("it was a tie")