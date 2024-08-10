board=[]
for x in range(3):
    temp=[]
    for a in range(3):
        temp.append(" ")
    board.append(temp)
player = ("x")
swap = True
count = 0
def printboard(board):
    print("  1  2  3  ")
    print("1", board[0][0] + " |" + board[0][1] + " |" + board[0][2])
    print("  ---------")
    print("2", board[1][0] + " |" + board[1][1] + " |" + board[1][2])
    print("  ---------")
    print("3", board[2][0] + " |" + board[2][1] + " |" + board[2][2])
while count < 9:
    printboard(board)
    row = int(input("player "+player+" what row do you want to move in (1-3): "))
    col = int(input("player "+player+" what column do you want to move in: (1-3): "))
    if board[row-1][col-1] == " ":
        count += 1
        board[row-1][col-1] = player
    else:
        swap = False
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        printboard(board)
        print("player ", player, " won")
        count = 10
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        printboard(board)
        print("player ", player, " won")
        count = 10
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        printboard(board)
        print("player ", player, " won")
        count = 10
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        printboard(board)
        print("player ", player, " won")
        count = 10
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        printboard(board)
        print("player ", player, " won")
        count = 10
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        printboard(board)
        print("player ", player, " won")
        count = 10
    elif board[0][0] == player and board[1][0] == player and board[2][0]== player:
        printboard(board)
        print("player ", player, " won")
        count = 10
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        printboard(board)
        print("player ", player, " won")
        count = 10
    if player == "x" and swap == True:
        player = "o"
    elif player == "o" and swap == True:
        player = "x"
    else:
        print("sorry, you cant go there")
if count == 9:
    print("tie")