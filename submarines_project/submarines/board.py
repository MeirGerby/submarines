def create_board(board_size: int = 5):
    """create board for manage the game"""

    board = []

    for i in range(board_size):  # create board with zeros
        for j in range(board_size):
            board.append(0)

    return board

