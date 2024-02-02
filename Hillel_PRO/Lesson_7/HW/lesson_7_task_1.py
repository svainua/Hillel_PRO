# Database representation
team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Kavin", "age": 31, "number": 12},
]


# Application source code
def repr_players(players: list[dict]):
    pass


def player_add(name: str, age: int, number: int) -> dict:
    player: dict = {"name": name, "age": age, "number": number}
    team.append(player)
    return player


def player_delete(number: int) -> None:
    for player in team:
        if player["number"] == number:
            del player


def main():
    operations = ("add", "del", "repr")
    while True:
        operation = input("Please enter the operation: ")
        if operation not in operations:
            print(f"Operation: {operation} is not available\n")
            continue

        if operation == "repr":
            repr_players(team)
        elif operation == "add":
            user_data = input(
                "Enter new player information [name, age, number]: "
            ).split(",")
            name, age, number = user_data
            try:
                player_add(name, int(age), int(number))
            except ValueError:
                print("Age and player's number must be integers\n\n")
                continue
        elif operation == "del":
            player_delete()


if __main__ == "__main__":
    main()
