def init_status() -> dict:
    """create a dict that will contain the status of the game"""
    status = {
        "Submarine location": None,
        "number of shots allowed": None,
        "shots fired": None,
        "empty squares fired": None,
        "squares exposed": None
    }
    return status

# print(init_status())


