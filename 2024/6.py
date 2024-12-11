lines = open("2024/inputs/6.txt").read().splitlines()


moves = {"^": (-1, 0, ">"), "<": (0, -1, "^"), ">": (0, 1, "v"), "v": (1, 0, "<")}


def get_start_point():
    for i, line in enumerate(lines):
        for j, ch in enumerate(line):
            if ch == "^":
                return i, j


def part_one():

    x, y = get_start_point()
    move = "^"
    visited = set()

    visited.add((x, y))
    while 0 <= x + moves[move][0] < len(lines) and 0 <= y + moves[move][1] < len(
        lines[0]
    ):

        next_x = x + moves[move][0]
        next_y = y + moves[move][1]

        if lines[next_x][next_y] == "#":
            move = moves[move][2]
        else:
            x = next_x
            y = next_y
            visited.add((x, y))

    print(len(visited))


def part_two():

    x, y = get_start_point()
    move = "^"
    visited = []
    loop = 0
    visited.append((x, y, move))
    while 0 <= x + moves[move][0] < len(lines) and 0 <= y + moves[move][1] < len(
        lines[0]
    ):

        next_x = x + moves[move][0]
        next_y = y + moves[move][1]

        if (next_x, next_y, moves[move][2]) in visited:
            loop += 1

        if lines[next_x][next_y] == "#":
            move = moves[move][2]
        else:
            x = next_x
            y = next_y
            visited.append((x, y, move))

    print(len(visited))


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
