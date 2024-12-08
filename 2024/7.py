lines = open("2024/inputs/7.txt").read().splitlines()


def part_one():

    total_calibration = 0
    for equation in lines:
        test_value, c = equation.split(":")
        test_value = int(test_value)
        configs = list(map(int, c.split()))

        cur_conf = [configs[0]]
        for i in range(1, len(configs)):
            temp_c = []
            for conf in cur_conf:
                temp_c.append(conf + configs[i])
                temp_c.append(conf * configs[i])

            cur_conf = temp_c

        if test_value in temp_c:
            total_calibration += test_value

    print(total_calibration)


def part_two():
    pass


if __name__ == "__main__":

    print("Part One:")
    part_one()

    print("Part Two:")
    part_two()
