line = open("2015/inputs/1.txt").read()


def part_one():
    floor = 0
    for ch in line:
        if ch == "(":
            floor += 1
        else:
            floor -= 1

    print(floor)


def part_two():
    floor = 0
    for c, ch in enumerate(line, 1):
        if ch == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            print(c)
            break


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
