def print_board(board):
    print(f"""
        ---------
        | {board[0]} {board[1]} {board[2]} |
        | {board[3]} {board[4]} {board[5]} |
        | {board[6]} {board[7]} {board[8]} |
        ---------
        """)


def is_valid_position(position, board):
    return 1 <= position <= 9 and board[position - 1] == ' '

def is_board_full(board):
    return ' ' not in board

def new_board():
    return [' '] * 9

def check_symbol(simbol, board):
    for item in board:
        if board[0] + board[1] + board[2] == simbol or \
           board[2] + board[4] + board[6] == simbol or \
           board[0] + board[4] + board[8] == simbol or \
           board[2] + board[4] + board[6] == simbol or \
           board[6] + board[7] + board[8] == simbol or \
           board[0] + board[3] + board[6] == simbol or \
           board[1] + board[4] + board[7] == simbol or \
           board[2] + board[5] + board[8] == simbol:
            return True
        else:
            return False



def game_not_finish(board):
    return ' ' in board


def check_result(board):

    if check_symbol("XXX", board):
        print("X wins")
        return True
    elif check_symbol("OOO", board):
        print('O wins')
        return True
    elif is_board_full(board) == True and check_symbol("XXX", board) == False and  check_symbol("OOO", board) == False:
        print('Draw')
    return False


board = new_board()
print_board(board)
number = 0
while number < 9:
    try:
        input_str = input()
        row, col = map(int, input_str.split())
    except ValueError:
        print("You should enter numbers!")
        continue

    position = (row - 1) * 3 + col

    if is_valid_position(position, board):
        symbol = 'X' if number % 2 == 0 else 'O'
        board[position - 1] = symbol
        print_board(board)
        number += 1

        if check_result(board):
            break

    elif 1 <= position <= 9:
        print("This cell is occupied! Choose another one.")
    else:
        print("Coordinates should be from 1 to 3.")
