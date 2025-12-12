lines = open("2025/inputs/3.txt").read().splitlines()


def part_one(lines):

    batteries = []
    for line in lines:
        all_pairs = [int(line[i] + line[j]) for i in range(0, len(line)) for j in range(i+1, len(line))]
        batteries.append(max(all_pairs))
            
    print(sum(batteries))


def part_two(lines):
    batteries = []
    for line in lines:
        line = list(map(int, list(line)))
        battery = ""
        for i in range(11):
            max_battery = max(line[:i-11])
            battery += str(max_battery)
            line = line[line.index(max_battery)+1:]

        battery += str(max(line))
        batteries.append(int(battery))

    print(sum(batteries))

if __name__ == "__main__":

    print("Part One:")
    part_one(lines)

    print("Part Two:")
    part_two(lines)
