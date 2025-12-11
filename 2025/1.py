lines = open("2025/inputs/1.txt").read().splitlines()


def part_one(lines):

    state = 50
    count_zeros = 0
    for line in lines:
        turn = int(line.replace("L", "-").replace("R", "+"))

        state = (state + turn) % 100

        if state == 0:
            count_zeros += 1

    print(f"Number of times pointing at zero: {count_zeros}")
    return


def part_two():

    state = 50
    count_zeros_cross = 0
    for line in lines:

        d = line[0]
        r = int(line[1:])
        count_zeros_cross += r // 100
        r = r % 100
        if d == "L":
            if state != 0 and state - r <= 0:
                count_zeros_cross += 1
            state = (state - r) % 100
        elif d == "R":
            if state + r >= 100:
                count_zeros_cross += 1
            state = (state + r) % 100
            
    print(f"Number of times pointing at zero: {count_zeros_cross}")
    return


if __name__ == "__main__":

    print("Part One:")
    part_one(lines)

    print("\nPart Two:")
    part_two()
