from submarines import board, placement, game




def play():
    new_board = board.create_board()
    init_board = board.init_board(new_board)
    locate_submarines = placement.place_board(init_board)
    # print(locate_submarines)
    first_status = game.init_status()
    # print(first_status)







if __name__ == "__main__":
    play()
