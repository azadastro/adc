lines = open("2015\inputs\\6.txt").read().splitlines()


def part_one():
    field = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        words = line.split()
        op = "toggle" if words[0] == "toggle" else words[1]
        start = list(map(int, words[-3].split(",")))
        end = list(map(int, words[-1].split(",")))
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if op == "toggle":
                    field[i][j] = 0 if field[i][j] == 1 else 1
                elif op == "on":
                    field[i][j] = 1
                elif op == "off":
                    field[i][j] = 0

    print(sum([sum(f) for f in field]))


def part_two():
    field = [[0 for _ in range(1000)] for _ in range(1000)]
    for line in lines:
        words = line.split()
        op = "toggle" if words[0] == "toggle" else words[1]
        start = list(map(int, words[-3].split(",")))
        end = list(map(int, words[-1].split(",")))
        for i in range(start[0], end[0] + 1):
            for j in range(start[1], end[1] + 1):
                if op == "toggle":
                    field[i][j] += 2
                elif op == "on":
                    field[i][j] += 1
                elif op == "off":
                    field[i][j] = max(0, field[i][j] - 1)

    print(sum([sum(f) for f in field]))


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
