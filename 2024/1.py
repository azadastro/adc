import re

with open("2024/inputs/1.txt", "r") as f:
    lines = f.readlines()


def read_lists():

    left_list = []
    right_list = []
    for line in lines:
        numbers = re.findall(r"\d+", line)
        left_list.append(int(numbers[0]))
        right_list.append(int(numbers[1]))

    return left_list, right_list


def part_one(left_list, right_list):

    print(sum([abs(l - r) for l, r in zip(sorted(left_list), sorted(right_list))]))


def part_two(left_list, right_list):

    print(sum([l * right_list.count(l) for l in left_list]))


if __name__ == "__main__":

    left_list, right_list = read_lists()

    print("Part One:")
    part_one(left_list, right_list)

    print("Part Two:")
    part_two(left_list, right_list)
