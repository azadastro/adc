lines = open("2015\inputs\\2.txt").read().splitlines()


def part_one():

    total_area = 0
    for line in lines:
        l, w, h = map(int, line.split("x"))
        sides = [l * w, w * h, l * h]
        total_area += sum([2 * s for s in sides]) + min(sides)

    print(total_area)


def part_two():

    total_ribbon = 0
    for line in lines:
        sides = sorted(map(int, line.split("x")))
        total_ribbon += sum([2 * s for s in sides[:2]]) + (
            sides[0] * sides[1] * sides[2]
        )

    print(total_ribbon)


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
