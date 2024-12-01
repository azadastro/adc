import re
import numpy as np

with open("2024/inputs/1.txt", "r") as f:
    lines = f.readlines()


def part_one():
    left_list = []
    right_list = []
    for line in lines:
        numbers = re.findall(r"\d+", line)
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

    s_left = sorted(left_list)
    s_rght = sorted(right_list)
    print(sum([abs(l - r) for l, r in zip(s_left, s_rght)]))


def part_two():
    left_list = []
    right_list = []
    for line in lines:
        numbers = re.findall(r"\d+", line)
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

    print(sum([l * right_list.count(l) for l in left_list]))


if __name__ == "__main__":
    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
