import re
import numpy as np

with open("2023/inputs/2.txt", "r") as f:
    lines = f.readlines()


def part_one():
    max_cubes = {"red": 12, "green": 13, "blue": 14}

    possible_game_ids = []
    for line in lines:
        not_possible = False
        game_id, game_all_cubes = line.split(":")
        game_id = int(re.findall(r"\d+", game_id)[0])

        slpit_all_cubes = game_all_cubes.split(";")
        for play in slpit_all_cubes:
            colors = play.split(",")
            for color in colors:
                num_color, c = color.strip().split(" ")
                if int(num_color) > max_cubes[c]:
                    not_possible = True
                    break
            if not_possible:
                break

        if not not_possible:
            possible_game_ids.append(game_id)

    print(sum(possible_game_ids))


def part_two():
    power_set = []
    for line in lines:
        min_cubes = {"red": 1, "green": 1, "blue": 1}
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


if __name__ == "__main__":
    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
