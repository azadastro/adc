with open("2024/inputs/2.txt", "r") as f:
    lines = f.readlines()


def is_safe(line_list):

    for num1, num2 in zip(line_list, line_list[1:]):
        d = num1 - num2
        if d < 1 or d > 3:
            return False

    return True


def part_one():

    count = 0
    for line in lines:
        line_list = [int(ch) for ch in line.split()]
        if line_list[0] - line_list[1] < 0:
            line_list = line_list[::-1]

        if is_safe(line_list):
            count += 1

    print(count)


def part_two():
    count = 0
    for line in lines:
        line_list = [int(ch) for ch in line.split()]
        if line_list[0] - line_list[1] < 0:
            line_list = line_list[::-1]
            print(line_list)

        if is_safe(line_list):
            count += 1
        else:
            dist = [n1 - n2 for n1, n2 in zip(line_list, line_list[1:])]
            for i, d in enumerate(dist):
                if d < 1 or d > 3:
                    line_list.remove(line_list[i])
                    break
            if is_safe(line_list):
                count += 1

    print(count)


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
