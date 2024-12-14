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


def check_loop(grid):
    x, y = get_start_point()
    move = "^"
    visited = set()

    visited.add((x, y, "^"))
    while 0 <= x + moves[move][0] < len(grid) and 0 <= y + moves[move][1] < len(
        grid[0]
    ):

        next_x = x + moves[move][0]
        next_y = y + moves[move][1]

        if grid[next_x][next_y] == "#":
            move = moves[move][2]
        else:
            x = next_x
            y = next_y
            if (x, y, move) in visited:
                return True
            visited.add((x, y, move))

    return False


def part_two():

    loop_count = 0
    grid = "\n".join(lines)
    for i in range(len(grid)):
        if grid[i] == ".":
            new_grid = grid[:i] + "#" + grid[i + 1 :]
            if check_loop(new_grid.splitlines()):
                loop_count += 1

    print(loop_count)


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
