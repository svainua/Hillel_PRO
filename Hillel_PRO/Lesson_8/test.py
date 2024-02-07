import database

for number, player in database._TEAM.items():
    print(f"\t[Player {number}]: {player['name']}, {player['age']}")
