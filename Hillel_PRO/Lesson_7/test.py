# print(number)


team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Kavin", "age": 31, "number": 12},
]


# for player in team:
#     print(f"[Player {player['number']}]: {player['name']}, {player['age']}")


# words = "Klark,22,12".split(",")
# *data, number = words
# print(number)


# for check in team:
#     if check["number"] == int(number):
#         print("occupied")


number_list = [item["number"] for item in team]

print(number_list)
