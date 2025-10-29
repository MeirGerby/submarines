def create_board(board_size: int = 5):
    board = []
    # letters = ' ABCDEFGHIJKLMNOPQRSTYVWXYZ'
    # letters = letters[:board_size + 1]

    for i in range(board_size):  # create board with zeros
        for j in range(board_size):
            board.append(0)

