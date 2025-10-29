from submarines import board, placement, game, io
from submarines_project.submarines.io import how_to_play


def play():
    board_game = board.create_board()
    locate_submarines = placement.place_board(board_game)
    status = game.init_status()
    io.show_rules()                                            # show the rules to the screen
    limit_shots_inp = io.input_shots()                          # user input limit shots and board size
    size = io.input_size()
    limit_shots = game.shots_allowed(limit_shots_inp)           # determine the limit shots in the game
    update_limit = game.update_limit(limit_shots, status)         # update the status game
    update_size = game.update_size(status, size)
    location_update = game.update_location(status, locate_submarines)
    show_board = io.show_new_board(size)                        # user input size board


    how_play = how_to_play()
    display_status = io.show_status(limit_update)


    shot_place = io.shot(size)
    check_shot = game.update_shooting(board_game, shot_place)





    update_shot = game.update_shooting()




    # check if it was shot
    # if not send a message and ask input again
    # update the status
    # run this until win or lose








if __name__ == "__main__":
    play()
