# Database representation
team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Kavin", "age": 31, "number": 12},
]


# Application source code
def repr_players(players):
    for player in players:
        print(
            f"\t[Player {player['number']}]: {player['name']}, {player['age']}"
        )


def player_add(name: str, age: int, number: int) -> dict:
    player: dict = {"name": name, "age": age, "number": number}
    for person in team:
        if person["number"] == number:
            print("This number is occupied, choose another one")
            return player
    else:
        team.append(player)
        return player


def player_delete(number: int) -> None:
    for player in team:
        if player["number"] == number:
            del player


def player_update(name: str, age: int, number: int) -> dict:
    for person in team:
        if person["number"] == number:
            person["name"] = name
            person["age"] = age


def main():
    operations = ("add", "upd", "repr", "del", "exit")
    while True:
        operation = input("Please enter the operation: ")
        if operation not in operations:
            print(f"Operation: {operation} is not available\n")
            continue

        if operation == "exit":
            print("Bye")
            break
        elif operation == "repr":
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
        elif operation == "upd":
            number_to_update = input(
                "Enter the player's number whose data you want to update: "
            )
            name_and_age_to_update = input(
                "Enter new player information [name, age] :"
            ).split(",")
            new_name, new_age = name_and_age_to_update
            try:
                player_update(new_name, int(new_age), int(number_to_update))
            except ValueError:
                print("Age and player's number must be integers\n\n")
                continue
        else:
            raise NotImplementedError


main()
