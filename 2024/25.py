l_ks = open("2024\inputs\\25.txt").read().split("\n\n")


def get_lock_keys():
    locks = []
    keys = []
    for lk in l_ks:
        lk_lines = lk.splitlines()

        pins = [0] * len(lk_lines[0])
        if all(p == "#" for p in lk_lines[0]):
            for lk_line in lk_lines:
                pins = [
                    a + b for a, b in zip(pins, [1 if p == "#" else 0 for p in lk_line])
                ]
            locks.append(pins)

        else:
            for lk_line in lk_lines:
                pins = [
                    a + b for a, b in zip(pins, [1 if p == "#" else 0 for p in lk_line])
                ]
            keys.append(pins)

    return locks, keys


def part_one():

    locks, keys = get_lock_keys()

    total_match = 0
    for key in keys:
        for lock in locks:
            if all(a + b <= 7 for a, b in zip(key, lock)):
                total_match += 1

    print(total_match)


def part_two():

    pass


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
