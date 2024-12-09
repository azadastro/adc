lines = open("2024/inputs/8.txt").read().splitlines()


def part_one():

    antennas = {}
    max_x = len(lines)
    max_y = len(lines[0])
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

    antinodes = set()
    for v in antennas.values():
        for ant1 in v:
            for ant2 in v:
                if ant1 == ant2:
                    continue
                diff = (ant1[0] - ant2[0], ant1[1] - ant2[1])
                x = ant1[0] + diff[0]
                y = ant1[1] + diff[1]
                if 0 <= x < max_x and 0 <= y < max_y:
                    antinodes.add((x, y))

    print(len(antinodes))


def part_two():

    antennas = {}
    max_x = len(lines)
    max_y = len(lines[0])
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

    antinodes = set()
    for v in antennas.values():
        for ant1 in v:
            antinodes.add(ant1)
            for ant2 in v:
                if ant1 == ant2:
                    continue
                diff = (ant1[0] - ant2[0], ant1[1] - ant2[1])

                step = 1
                x = ant1[0] + diff[0]
                y = ant1[1] + diff[1]
                while 0 <= x < max_x and 0 <= y < max_y:

                    antinodes.add((x, y))
                    step += 1
                    x = ant1[0] + step * diff[0]
                    y = ant1[1] + step * diff[1]

    print(len(antinodes))


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
