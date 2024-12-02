with open("2024/inputs/2.txt", "r") as f:
    lines = f.readlines()


def is_safe(line_list):
    dist = [n1 - n2 for n1, n2 in zip(line_list, line_list[1:])]
    return all(1 <= d <= 3 for d in dist) or all(-3 <= d <= -1 for d in dist)


def part_one():

    count = 0
    for line in lines:
        line_list = [int(ch) for ch in line.split()]

        if is_safe(line_list):
            count += 1

    print(count)


def part_two():
    count = 0
    for line in lines:
        line_list = [int(ch) for ch in line.split()]

        if is_safe(line_list):
            count += 1
        else:
            for i in range(len(line_list)):
                if is_safe(line_list[:i] + line_list[i + 1 :]):
                    count += 1
                    break

    print(count)


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
