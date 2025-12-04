lines = open("2025/inputs/1.txt").read().splitlines()


def part_one(lines):

    initial_state = 50
    count_zeros = 0
    for line in lines:
        d = line[0]
        r = int(line[1:])
        if r > 100:
            r = r % 100
        # print(initial_state, d, r)
        if d == "L":
            initial_state -= r
            if initial_state < 0:
                initial_state = 100 + initial_state
        elif d == "R":
            initial_state += r
            if initial_state > 99:
                initial_state = initial_state - 100

        # print(f"Current state: {initial_state}")
        if initial_state == 0:
            count_zeros += 1

    print(f"Number of times pointing at zero: {count_zeros}")
    return


def part_two():

    pass


if __name__ == "__main__":

    print("Part One:")
    part_one(lines)

    print("\nPart Two:")
    part_two()
