def create_board(board_size: int = 3) -> list[list]:
    board = []
    for i in range(board_size):
        for j in range(board_size):
            board.append([])

    return board

# print(create_board())
# c = create_board()
def init_board(board: list[list]) -> list[list]:
    init = 0

    for i in board:
        i.append(init)


    return board
# print(init_board(c))

