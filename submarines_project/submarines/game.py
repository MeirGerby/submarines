def init_status() -> dict:
    """create a dict that will contain the status of the game"""
    status = {
        "Submarine location": [],
        "limit shots": None,
        "shots fired": 0,
        "empty squares fired": None,
        "Submarine exposed": None
    }
    return status

# print(init_status())
def shots_allowed(num: int):
    return num

def update_limit(limit_shots: int, status: dict):
    """update the status game the limit shots"""
    status["limit shots"] = limit_shots
    return status


def update_shooting(status: dict, shot: int):
    status["shots fired"] += 1
    if shot == status["submarine location"]:
        status["submarine exposed"] = shot
    else:
        status["empty squares fired"] = status["submarine location"]


def update_size(status, size):



    # {
    #         "size": 0
    #     "Submarine location": [],
    #     "limit shots": None,
    #     "shots fired": 0,
    #     "empty squares fired": None,
    #     "Submarine exposed": None
    # }
    pass

def update_location(status, location):
    # {
    #     "Submarine location": [],
    #     "limit shots": None,
    #     "shots fired": 0,
    #     "empty squares fired": None,
    #     "Submarine exposed": None
    # }
    pass