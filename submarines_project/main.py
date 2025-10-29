from submarines import board, placement, game, io
from submarines_project.submarines.io import how_to_play


def play():
    new_board = board.create_board()
    board_game = board.init_board(new_board)
    locate_submarines = placement.place_board(board_game)
    first_status = game.init_status()

    # game start
    io.show_rules()                                             # show the rules to the screen
    limit_shots_inp = io.input_shots()                          # user input limit shots
    limit_shots = game.shots_allowed(limit_shots_inp)           # determine the limit shots in the game
    limit_update = game.update_limit(limit_shots, first_status) # update the status game
    size = io.input_size()                                      # user input size board
    show_board = io.show_new_board(size)                        # show the first board on the screen
    how_play = how_to_play()                                    # show how to play the game
    display_status = io.show_status(limit_update)               # display the status game on the screen
    shot_place = io.shot(size)                                  #
    # check if it was shot
    # if not send a massage and ask input again
    # update the status
    # run this until win or lose








if __name__ == "__main__":
    play()
