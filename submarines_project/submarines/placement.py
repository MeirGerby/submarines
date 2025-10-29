import random
import builtins


def place_board(board: list[list]) -> list[list]:
    rand = random.randint
    for i in board:
        for j in i:
            i[j] = rand(0,1)

    return board

# print(place_board([[0],[0],[0],[0],[0],[0],[0],[0],[0]], 3))
