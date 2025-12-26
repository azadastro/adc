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


def get_all_xs(tiles):
    all_xs = {}
    for (x1, y1), (x2, y2) in zip(tiles, tiles[1:]+tiles[:1]):
        all_xs.setdefault(y1, set()).add(x1)
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        if x1 == x2:
            for y in range(y1+1, y2):
                all_xs.setdefault(y, set()).add(x1)
        
        if y1 == y2:
            for x in range(x1+1, x2):
                all_xs.setdefault(y1, set()).add(x)

    for k, v in all_xs.items():
        all_xs[k] = (min(v), max(v))
        
    return all_xs


def valid_area(all_xs, tile1, tile2):
    min_x, max_x = sorted([tile1[0], tile2[0]])
    min_y, max_y = sorted([tile1[1], tile2[1]])
    for y in range(min_y, max_y+1):
        x_min, x_max = all_xs[y]
        if min_x < x_min or max_x > x_max:
            return False
    return True


def part_two(tiles):
    
    all_xs = get_all_xs(tiles)

    max_area = 0
    for i in range(len(tiles)):
        for j in range(i + 1, len(tiles)):
            area = calc_area(tiles[i], tiles[j])
            if area > max_area and valid_area(all_xs, tiles[i], tiles[j]):
                max_area = area
                tiles_pair = (tiles[i], tiles[j])
    print(max_area)


if __name__ == "__main__":

    print("Part One:")
    part_one(tiles)

    print("Part Two:")
    part_two(tiles)
