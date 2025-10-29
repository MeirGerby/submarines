def init_status() -> dict:
    """create a dict that will contain the status of the game"""
    status = {
        "Submarine location": None,
        "limit shots": None,
        "shots fired": None,
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


