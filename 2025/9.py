tiles = [
    list(map(int, line.split(",")))
    for line in open("2025/inputs/9.txt").read().splitlines()
]


def calc_area(point1, point2):

    area = (abs(point1[0] - point2[0]) + 1) * (abs(point1[1] - point2[1]) + 1)
    return area


def part_one(tiles):
    max_area = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            area = calc_area(tiles[i], tiles[j])
            if area > max_area:
                max_area = area
                tiles_pair = (tiles[i], tiles[j])
    print(max_area)


def part_two():

    pass


if __name__ == "__main__":

    print("Part One:")
    part_one(tiles)

    print("Part Two:")
    part_two()
