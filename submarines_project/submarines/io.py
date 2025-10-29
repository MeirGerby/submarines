def input_shots(num_shots: int = 6):
    """get shots allowed from the user or determine it to 6 shots by default"""
    user_inp = input("please enter the allowed shots \n"
                     "you want to play with this game\n"
                     "max shots you can choose is 10 shots\n"
                     "\n"
                     "if you will not choose you'll get \n"
                     "6 allowed shots before the game stops \n "
                     ":")
    user_input = int(user_inp)
    if user_input not in range(1,11):
        return input_shots()
    else:
        return user_input


def show_new_board(board_size: int):
    """show the first board on the screen"""

    for i in range(board_size + 1): # show the indexes to the board
        if i == 0:
            print(end="\t")
        else:
            print(i, end="\t")

    letters = ' ABCDEFGHIJKLMNOPQRSTYVWXYZ'
    letters = letters[:board_size + 1]
    for i in range(board_size + 1):  # show board with zeros
        for j in range(board_size + 1):
            if j == 0:
                print(letters[i], end="\t")
            elif i != 0:
                print(0, end='\t')
        print()
    return letters






def input_size(size: int = 5):
    size = int(input(""
          "input the size board you want to create\n"
          "if you will input the size \n"
          "it will be defaulted by 5 \n"
          "the limit size is 10 \n"
          ":"))

    while size not in range(1, 11):
        size = int(input(""
                     "input the size board you want to create\n"
                     "if you will input the size \n"
                     "it will be defaulted by 5 \n"
                     "the limit size is 10 \n"
                     ":"))
    return size


def show_rules():
    print(""
          "This game a board with zeros.\n"
          "under each zero may has a submarine.\n "
          "the program will place submarines in a random place.\n"
          "the submarines will be hidden \n"
          "\n"
          "you need to find out where the submarines are. \n"
          "you have limits shot to disappear them. \n"
          "\n"
          "try to win the game by hunting the whole submarines. \n"
          "if you pass your limit shoots the game will be over. \n"
          "\n"
          "be smart! \n "
          "we are trusting you!\n"
          " \n"
          "have fun")

def how_to_play():
    """show how to play the game"""

    print(""
          "if you wants to hit place \n"
          "use the letters and numbers shown at the screen")

def show_status(status: dict):
    """display the status game on the screen"""

    print(f''',
       limit shots :{status['limit shots']}\t
        "shots fired":{status["shots fired"]}\t
        "empty squares fired":{status["empty squares fired"]}\t
        "Submarine exposed":{status["Submarine exposed"]}\t''')


def shot(board_size: int):

    letters = "ABCDEFGHIJKLMNOPQRSTYVWXYZ"
    user_input = input("Enter the place you want to hit")
    flag = user_input not in range(board_size) and user_input not in letters

    while flag:
        user_input = input("Enter the place you want to hit")

    return user_input


s = shot(5,"ABCDEFG")
print(s)
