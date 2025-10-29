def input_shots(num_shots: int = 6):
    """get shots allowed from the user or determine it to 6 shots by default"""
    user_inp = input("please enter the allowed shots \n"
                     "you want to play with this game\n"
                     "max shots you can choose is 10 shots\n"
                     "\n"
                     "if you will not choose you'll get \n"
                     "6 allowed shots before the game stops:\n ")
    user_input = int(user_inp)
    if user_input not in range(1,11):
        return input_shots()
    else:
        return user_input





