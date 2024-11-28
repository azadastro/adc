import re
import numpy as np


with open("2.txt", "r") as f:
    lines = f.readlines()

power_set = []
for line in lines:
    min_cubes = {
        "red": 1,
        "green": 1,
        "blue": 1
    }
    game_id, game_all_cubes = line.split(":")

    slpit_all_cubes = game_all_cubes.split(";")
    for play in slpit_all_cubes:
        colors = play.split(",")
        for color in colors:
            num_color, c = color.strip().split(" ")
            if int(num_color) > min_cubes[c]:
                min_cubes[c] = int(num_color)

    power_set.append(np.prod(list(min_cubes.values())))

print(sum(power_set))