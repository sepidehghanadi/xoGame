

def main():
    board = [["_" for _ in range(3)] for _ in range(3)]
    is_x = True
    game_over = False
    while not game_over:
        print_board(board)
        try:
            selection = convert(validate_square())
            place_piece(selection, is_x, board)
        except ValueError:
            print("Sorry, please select an empty square number 1-9")
            continue
        game_over = is_win(board) or is_draw(board)
        is_x = not is_x


def is_draw(board):
    for row in board:
        for values in row:
            if values == "_":
                return False
    print("DRAW!")
    return True


def is_win(board):
    winner = None
    for i in range(3):
        # horizontal
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            winner = board[i][0]
            break
        # vertical
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            winner = board[0][i]
            break
    # diagonal
    if board[1][1] != "_":
        if (board[0][0] == board[1][1] == board[2][2]
                or board[0][2] == board[1][1] == board[2][0]):
            winner = board[1][1]
    if winner is not None:
        print_board(board)
        print(f"{winner} is the winner!")
        return True
    return False


'''
this function stack the rows on top of each other
'''


def print_board(board):
    for row in board:
        print(row)


'''
this function will make sure user is gonna choose a square from 1 to 9
'''


def validate_square():
    selection = int(input("Select a square: "))
    if not 1 <= selection <= 9:
        raise ValueError
    return selection


'''print_board(board)'''

''' this returns the (i,j) as a tuple'''


def convert(selection):
    selection -= 1
    return (selection // 3, selection % 3)


'''updates the board'''


def place_piece(selection, is_x, board):
    '''This line will prevent users from rewriting the filled squares'''
    if board[selection[0]][selection[1]] == "_":
        board[selection[0]][selection[1]] = "X" if is_x else "O"
    else:
        raise ValueError


if __name__ == "__main__":
    main()
