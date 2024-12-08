lines = open("2024/inputs/8.txt").read().splitlines()


def part_one():

    antennas = {}
    max_i = len(lines)
    max_j = len(lines[0])
    for i, line in enumerate(lines):
        if len(line.replace(".", "")) == 0:
            continue
        for j, ch in enumerate(line):
            if ch != ".":
                if ch in antennas.keys():
                    antennas[ch].append((i, j))
                else:
                    antennas[ch] = []
                    antennas[ch].append((i, j))

    antinodes = 0
    for v in antennas.values():
        for ant1 in v:
            for ant2 in v:
                diff = (ant1[0] - ant2[0], ant1[1] - ant2[1])

    print(antennas)


def part_two():

    pass


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
