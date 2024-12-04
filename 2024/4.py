lines = open("2024/inputs/4.txt").read().splitlines()


def build_new_grid(lines, n):
    new_grid = []
    len_line = len(lines[0]) + (n * 2)
    new_grid.extend(["." * len_line for i in range(n)])
    for line in lines:
        new_grid.append("." * n + line + "." * n)
    new_grid.extend(["." * len_line for i in range(n)])

    return new_grid


def count_xmas(i, j, g):
    strings = []
    # forward
    strings.append("".join([g[i][c] for c in range(j, j + 4)]))
    # backward
    strings.append("".join([g[i][c] for c in range(j, j - 4, -1)]))
    # upward
    strings.append("".join([g[c][j] for c in range(i, i - 4, -1)]))
    # downward
    strings.append("".join([g[c][j] for c in range(i, i + 4)]))

    # diag1
    strings.append("".join([g[c][k] for c, k in zip(range(i, i + 4), range(j, j + 4))]))
    # diag2
    strings.append(
        "".join([g[c][k] for c, k in zip(range(i, i + 4), range(j, j - 4, -1))])
    )
    # diag3
    strings.append(
        "".join([g[c][k] for c, k in zip(range(i, i - 4, -1), range(j, j - 4, -1))])
    )
    # diag4
    strings.append(
        "".join([g[c][k] for c, k in zip(range(i, i - 4, -1), range(j, j + 4))])
    )

    return strings.count("XMAS")


def part_one():

    new_grid = build_new_grid(lines, 3)

    total_count = 0
    for i, line in enumerate(new_grid[3:-3], 3):
        for j, ch in enumerate(line[3:-3], 3):
            if ch == "X":
                total_count += count_xmas(i, j, new_grid)

    print(total_count)


def count_x_mas(i, j, g):
    strings = []

    # diag1
    strings.append(
        "".join([g[c][k] for c, k in zip(range(i - 1, i + 2), range(j - 1, j + 2))])
    )
    # diag2
    strings.append(
        "".join([g[c][k] for c, k in zip(range(i - 1, i + 2), range(j + 1, j - 2, -1))])
    )

    if strings.count("MAS") + strings.count("SAM") == 2:
        return 1
    else:
        return 0


def part_two():
    total_count = 0
    for i, line in enumerate(lines[1:-1], 1):
        for j, ch in enumerate(line[1:-1], 1):
            if ch == "A":
                total_count += count_x_mas(i, j, lines)

    print(total_count)


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
