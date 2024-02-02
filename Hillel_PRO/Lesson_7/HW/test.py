# words = "Klark,22,13".split(",")

# *data, number = words

# print(number)


team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Kavin", "age": 31, "number": 12},
]


for player in team:
    print(f"[Player {player['number']}]: {player['name']}, {player['age']}")
