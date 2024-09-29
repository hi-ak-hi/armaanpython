from random import randrange

def print_board(board):
    print("abcdefghij")
    for x in range(10):
        print(x + 1, end="")
        for y in range(10):
            print(board[x][y], end="")
        print()

def make_board(board):
    for x in range(10):
        board.append([])
        for y in range(10):
            board[x].append("[ ]")

def check_xy(x, y, board):
    if x<0 or x>9:
        return False
    elif y<0 or y>9:
        return False
    else:
        return True

def check_pos(x, y, dir, board, ship_length):
    if dir == "up":
        for spot in range(ship_length):
            if check_xy(x, y-spot, board) and board[y][x] == "[ ]":
                pass
            else:
                return False
    elif dir == "down":
        for spot in range(ship_length):
            if check_xy(x, y+spot, board) and board[y][x] == "[ ]":
                pass
            else:
                return False
                
    elif dir == "right":
        for spot in range(ship_length):
            if check_xy(x+spot, y, board) and board[y][x] == "[ ]":
                pass
            else:
                return False
    elif dir == "left":
        for spot in range(ship_length):
            if check_xy(x-spot, y, board) and board[y][x] == "[ ]":
                pass
            else:
                return False
    return True

def place_ship(x, y, dir, board, ship_len):
    if dir == "up":
        for spot in range(ship_len):
            board[y-spot][x] = "[o]"
    if dir == "down":
        for spot in range(ship_len):
            board[y+spot][x] = "[o]"
    if dir == "left":
        for spot in range(ship_len):
            board[y][x-spot] = "[o]"
    if dir == "right":
        for spot in range(ship_len):
            board[y][x+spot] = "[o]"

def let_to_num(letter):
    if letter == "a":
        return 0
    elif letter == "b":
        return 1
    elif letter == "c":
        return 2
    elif letter == "d":
        return 3
    elif letter == "e":
        return 4
    elif letter == "f":
        return 5
    elif letter == "g":
        return 6
    elif letter == "h":
        return 7
    elif letter == "i":
        return 8
    elif letter == "j":
        return 9

def check_win(board):
    count = 0
    for x in range(10):
        for y in range(10):
            if board[x][y] == "[x]":
                count += 1
    if count == 17:
        return True
    else:
        return False

def make_move(master, veiw, x, y):
    if master[y][x] == "[o]":
        veiw[y][x] = "[x]"
    else:
        veiw[y][x] = "[#]"

player_board = []
computer_board = []
guessing_board = []

make_board(player_board)
make_board(computer_board)
make_board(guessing_board)