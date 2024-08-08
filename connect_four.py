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

while count<49:
    print_board(board)
    col = int(input("what column do you want to go in(1 - 7): "))
    col -= 1
    row = spot[col]
    spot[col]-=1
    board[row][col] = player
    if player == "[x]":
        player = "[o]"
    else:
        player = "[x]"