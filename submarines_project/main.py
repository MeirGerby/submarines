from submarines import board, placement, game, io




def play():
    new_board = board.create_board()
    board_game = board.init_board(new_board)
    locate_submarines = placement.place_board(board_game)
    first_status = game.init_status()
    limit_shots_inp = io.input_shots()
    limit_shots = game.shots_allowed(limit_shots_inp)
    limit_update = game.update_limit(limit_shots, first_status)
    # print(limit_update)







if __name__ == "__main__":
    play()
