lines = open("2025/inputs/4.txt").read().splitlines()


def part_one(lines):
    grid = [['.'] * (len(lines[0])+2)]
    for line in lines:
        grid.append(["."] + list(line) + ["."])
    grid.append(['.'] * (len(lines[0])+2))

    valid = []
    for r in range(1, len(grid)):
        for c in range (1, len(grid[0])):
            if grid[r][c] == "@":
                neighbours = [grid[i][j] for i in range(r-1, r+2) for j in range(c-1, c+2)]
                if neighbours.count("@")-1 < 4:
                    valid.append((r, c))
    
    print(len(valid))


def part_two(lines):

    grid = [['.'] * (len(lines[0])+2)]
    for line in lines:
        grid.append(["."] + list(line) + ["."])
    grid.append(['.'] * (len(lines[0])+2))

    valids = []
    while True:
        valid = []
        for r in range(1, len(grid)):
            for c in range (1, len(grid[0])):
                if grid[r][c] == "@":
                    neighbours = [grid[i][j] for i in range(r-1, r+2) for j in range(c-1, c+2)]
                    if neighbours.count("@")-1 < 4:
                        valid.append((r, c))

        if len(valid) == 0:
            break
        valids.extend(valid)
        for r, c in valid:
            grid[r][c] = "."

    print(len(valids))


if __name__ == "__main__":

    print("Part One:")
    part_one(lines)

    print("Part Two:")
    part_two(lines)
