# Advent of Code 2023
# Challenge 2 Part 2
# https://adventofcode.com/2023/day/2
# Aaron Sprouse

import re

INPUT_FILE = 'input.txt'

games = []
power_sum = 0

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
    red = 0
    green = 0
    blue = 0
    for pull in game:
        for color in pull:
            if (color == "red") and (pull[color] > red):
                red = pull[color]
            elif (color == "green") and (pull[color] > green):
                green = pull[color]
            elif (color == "blue") and (pull[color] > blue):
                blue = pull[color]
            
    game_power = red * green * blue

    power_sum += game_power

print(power_sum)