TEAM_TYPE = dict[int, dict]


# Database representation
_TEAM: TEAM_TYPE = {
    1: {"name": "John", "age": 20},
    3: {"name": "Mark", "age": 33},
    12: {"name": "Kavin", "age": 31},
}


def get_team() -> TEAM_TYPE:
    return _TEAM


def get(id_) -> dict | None:
    try:
        player = _TEAM[id_]
    except KeyError:
        return None
    else:
        return player


def update(id_: int, instance: dict, debug: bool = False):
    _TEAM[id_] = instance


def save(id_: int, instance: dict, debug: bool = False) -> bool:
    try:
        print(_TEAM[id_])
        if debug is True:
            print(f"Instance with id: {id_} already exists")
        return False
    except KeyError:
        _TEAM[id_] = instance
        return True


def delete(id_: int, debug: bool = False) -> bool:
    try:
        del _TEAM[id_]
    except KeyError:
        if debug is True:
            print(f"There is no instance with is {id_}")
        return False
    else:
        return True
