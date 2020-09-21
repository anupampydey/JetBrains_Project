def print_row(idx):
    print('|', end=' ')
    for val in val_str[idx:idx + 3]:
        if val == '_':
            val = ' '
            print(val, end=' ')
        else:
            print(val, end=' ')
    print('|')


def display_game(game_str):
    if set(game_str).issubset({'X', '_', 'O'}):
        print("---------")
        for idx in range(0, 8, 3):
            print_row(idx)  # print three rows
        print("---------")

def chk_coordinates(i, j, move):
    global val_str, val_lst
    game_index = [[6, 3, 0], [7, 4, 1], [8, 5, 2]]
    if {i, j}.issubset({'1', '2', '3'}):
        i = int(i)
        j = int(j)
        index = game_index[i - 1][j - 1]
        if val_lst[index] == '_':
            val_lst[index] = move
            val_str = "".join(val_lst)
            display_game(val_str)
            return True
        else:
            print('This cell is occupied! Choose another one!')
            return False
    else:
        print('Coordinates should be from 1 to 3!')
        return False


def row_count(player):
    for idx in range(0, 8, 3):
        count = val_lst[idx:idx + 3].count(player)
        if count == 3:
            return count


def col_count(player):
    for idx in range(3):
        count = val_lst[idx:7+idx:3].count(player)
        if count == 3:
            return count


def diag_count(player):
    if val_lst[:9:4].count(player) == 3:
        return 3
    if val_lst[2:7:2].count(player) == 3:
        return 3

def game_status():
    x = val_lst.count('X')
    o = val_lst.count('O')
    nil = val_lst.count('_')
    X_row = row_count('X')
    O_row = row_count('O')
    X_col = col_count('X')
    O_col = col_count('O')

    if abs(x - o) >= 2 or X_row == O_row == 3 or X_col == O_col == 3:
        return 'Impossible'
    elif X_row == 3 or X_col == 3:
        return 'X wins'
    elif O_row == 3 or O_col == 3:
        return 'O wins'

    if diag_count('X') == 3:
        return 'X wins'
    elif diag_count('O') == 3:
        return 'O wins'
    elif nil >= 1:
        return False
    else:
        return 'Draw'


val_str = "_________"
display_game(val_str)
val_lst = list(val_str)
status = False
check = False
turn = 'X'
while not status:
    while not check:
        posn = input('Enter the coordinates: > ').split()
        if posn[0].isdigit() and posn[1].isdigit():
            check = chk_coordinates(posn[0], posn[1], turn)
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
        else:
            print('You should enter numbers!')
    status = game_status()
    if status:
        print(status)
    else:
        check = False
