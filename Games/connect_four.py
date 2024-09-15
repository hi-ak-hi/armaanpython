board = []
for row in range(7):
    temp = []
    for spot in range(7):
        temp.append("[_]")
    board.append(temp)
player = "[x]"
count = 0
spot = [6,6,6,6,6,6,6]
def print_board(board):
    for x in range(7):
        for y in range(7):
            print(board[x][y], end="")
        print()
while count < 49:
    print_board(board)
    col = int(input("what column do you want to go in(1 - 7): "))
    col -= 1
    row = spot[col]
    if spot[row] == 0:
        print("you can't go there")    
    else:   
        spot[col]-= 1
        board[row][col] = player
        count += 1
    for x in range(7):
        for y in range(4):
            if board[y][x] == player and board[y+1][x] == player and board[y+2][x] == player and board[y+3][x] == player:
                if player == "[x]":
                    player = "x"
                else:
                    player = "o"
                print_board(board)
                print("player", player, "won")
                count = 50
                
    for x in range(7):
        for y in range(4):
            if board[x][y] == player and board[x][y+1]== player and board[x][y+2] == player and board[x][y+3] == player:
                if player == "[x]":
                    player = "x"
                else:
                    player = "o"
                print_board(board)
                print("player", player, "won")
                count = 50
    for x in range(4):
        for y in range(4):
            if board[x][y] == player and board[x+1][y+1] == player and board[x+2][y+2] == player and board[x+3][y+3] == player:
                if player == "[x]":
                    player = "x"
                else:
                    player = "o"
                print_board(board)
                print("player", player, "won")
                count = 50
    for x in range(3, 7):
        for y in range(4):
            if board[x][y] == player and board[x-1][y+1] == player and board[x-2][y+2] == player and board[x-3][y+3] == player:
                if player == "[x]":
                    player = "x"
                else:
                    player = "o"
                print_board(board)
                print("player", player, "won")
                count = 50
    if player == "[x]":
        player = "[o]"
    else:
        player = "[x]"