import random



def place_board(board):
    rand = random.randint
    for i in board:
            board[i] = rand(0,1)

    return board


