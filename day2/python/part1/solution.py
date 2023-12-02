# Advent of Code 2023
# Challenge 2
# https://adventofcode.com/2023/day/2
# Aaron Sprouse

import re

INPUT_FILE = 'input.txt'
POSSIBLE_GAMES = {
    "red":12,
    "green":13,
    "blue":14,
}

games = []
id_sum = 0

with open(INPUT_FILE, "r") as file:
    for game in file:
        game = re.sub("^(.+?): ", "" ,game) # Strip the game ID
        game = re.split("; ", game) # Split on "; " to form idividual pulls
        game = [re.split(", ", play) for play in game]
        
        result = []

        for sublist in game:
            sublist_dict = {}
            for item in sublist:
                parts = item.split()
                sublist_dict[parts[1]] = int(parts[0])
            result.append(sublist_dict)
        games.append(result)

for game in games:
    game_valid = True
    for pull in game:
        for color in pull:
            if POSSIBLE_GAMES[color] < pull[color]:
                game_valid = False
                break
            else:
                continue

    print(f"Is game {(games.index(game) + 1)} valid? {game_valid}")
    if game_valid:
        id_sum += (games.index(game) + 1)
    else:
        continue

print(id_sum)

# [{'red': 12, 'green': 9}, {'red': 12}, {'red': 9, 'green': 3}, {'red': 8, 'blue': 4, 'green': 4}, {'blue': 8, 'red': 11, 'green': 2}, True]